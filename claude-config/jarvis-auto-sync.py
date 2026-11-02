#!/usr/bin/env python3
"""GitHub auto-sync hook for Jarvis project.
Detects changes to ~/.jarvis files, appends to PROJECT_JOURNAL.md,
and auto-commits/pushes to GitHub when Claude Code runs tools on jarvis files.
"""
import sys
import json
import subprocess
import os
from datetime import datetime

sys.path.insert(0, "/Users/armaan/.jarvis")

try:
    import agent_coordinator
except Exception:
    agent_coordinator = None

try:
    import terminal_cache
except Exception:
    terminal_cache = None

JARVIS_HOME = os.path.expanduser("~/.jarvis")
JOURNAL_FILE = os.path.join(JARVIS_HOME, "PROJECT_JOURNAL.md")
REPO_DIR = JARVIS_HOME


def get_github_remote(repo_dir: str) -> str | None:
    """Get the GitHub remote URL for the repo."""
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=repo_dir, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def append_journal_entry(entry: str) -> None:
    """Append a timestamped entry to PROJECT_JOURNAL.md."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(JOURNAL_FILE, "a") as f:
        f.write(f"\n[{now}] {entry}\n")


def git_commit_push(repo_dir: str, message: str) -> bool:
    """Git add all, commit, and push to origin master."""
    try:
        subprocess.run(["git", "add", "-A"], cwd=repo_dir, capture_output=True, timeout=30)
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=repo_dir, capture_output=True, text=True, timeout=10
        )
        if not result.stdout.strip():
            return True  # No changes to commit

        commit_msg = "[Auto-commit] {} ({})".format(
            message, datetime.now().strftime("%Y-%m-%d %H:%M")
        )
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=repo_dir, capture_output=True, timeout=30
        )
        push_result = subprocess.run(
            ["git", "push", "origin", "master"],
            cwd=repo_dir, capture_output=True, timeout=60
        )
        return push_result.returncode == 0
    except Exception as e:
        print("Git hook error: {}".format(e), file=sys.stderr)
        return False


def extract_jarvis_file(command: str) -> str:
    """Extract ~/.jarvis file paths from a bash command."""
    if JARVIS_HOME in command:
        idx = command.find(JARVIS_HOME)
        rest = command[idx:]
        for i, c in enumerate(rest):
            if c in " \n\t'\"|;&$":
                return rest[:i]
        return rest
    return ""


def is_jarvis_command(command: str) -> bool:
    """Check if a bash command operates on the jarvis project."""
    command_lower = command.lower()
    return (
        JARVIS_HOME in command
        or "jarvis" in command_lower
        or "cd ~/.jarvis" in command
    )


def _stringify_tool_input(tool_input) -> str:
    if isinstance(tool_input, str):
        return tool_input
    try:
        return json.dumps(tool_input, ensure_ascii=False)
    except Exception:
        return str(tool_input)


def is_jarvis_activity(cwd: str, tool_input) -> bool:
    """Detect whether the hook payload is related to Jarvis work."""
    cwd_value = cwd or ""
    if ".jarvis" in cwd_value:
        return True

    tool_input_text = _stringify_tool_input(tool_input)
    tool_input_lower = tool_input_text.lower()
    return (
        JARVIS_HOME in tool_input_text
        or "/.jarvis/" in tool_input_text
        or " ~/.jarvis" in tool_input_text
        or "jarvis/" in tool_input_lower
    )


def _compact_preview(value, limit: int = 500) -> str:
    text = _stringify_tool_input(value)
    if len(text) <= limit:
        return text
    return text[:limit] + "...(truncated)"


def _build_advisory_prompt(data: dict, workstation_context: dict) -> str:
    return (
        "Provide a brief proactive advisory for this Jarvis hook event.\n"
        "What Claude just did:\n"
        f"- tool_name: {data.get('tool_name', '')}\n"
        f"- cwd: {data.get('cwd', '')}\n"
        f"- session_id: {data.get('session_id', '')}\n"
        f"- tool_input: {_compact_preview(data.get('tool_input', {}), 700)}\n"
        f"- tool_response: {_compact_preview(data.get('tool_response', {}), 700)}\n"
        "Current workstation snapshot:\n"
        f"{_compact_preview(workstation_context, 1200)}\n\n"
        "In <=3 bullets, flag concerns/risks or explicitly say 'No concerns.'"
    )


def _is_advisory_error(text: str) -> bool:
    lower = text.lower().strip()
    return (
        not lower
        or lower.startswith("advisory unavailable")
        or lower.startswith("[agent")
    )


def maybe_dispatch_advisory(data: dict) -> None:
    """Dispatch bounded proactive advisory for Jarvis-scoped payloads."""
    if not agent_coordinator or not terminal_cache:
        return

    if not is_jarvis_activity(data.get("cwd", ""), data.get("tool_input", {})):
        return

    try:
        workstation_context = terminal_cache.get_cached()
    except Exception:
        workstation_context = {}

    prompt = _build_advisory_prompt(data, workstation_context)
    try:
        advisory = agent_coordinator.dispatch_advisory(prompt, timeout=15)
    except Exception:
        return

    if isinstance(advisory, str) and not _is_advisory_error(advisory):
        print(advisory, file=sys.stderr)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    try:
        maybe_dispatch_advisory(data)
    except Exception:
        pass

    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    is_jarvis = False
    entry = ""

    if tool_name in ("Write", "Edit"):
        file_path = tool_input.get("file_path", "")
        if file_path.startswith(JARVIS_HOME):
            is_jarvis = True
            if tool_name == "Write":
                entry = "Write: {}".format(file_path)
            else:
                entry = "Edit: {}".format(file_path)

    elif tool_name == "Bash":
        command = tool_input.get("command", "")
        if is_jarvis_command(command):
            is_jarvis = True
            entry = "Bash: {}".format(command[:200])

    if not is_jarvis:
        sys.exit(0)

    append_journal_entry(entry)

    remote = get_github_remote(REPO_DIR)
    if remote:
        git_commit_push(REPO_DIR, entry)


if __name__ == "__main__":
    main()
