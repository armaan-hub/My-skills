#!/usr/bin/env python3
"""Universal token guard: a .claudeignore for Claude Code (PreToolUse hook).

- Read/Grep/Glob: blocks noisy paths (deps, caches, build output, lockfiles,
  minified/map files, binaries) and unbounded reads of huge files.
- Agent: prepends a short token-saving preamble to every subagent prompt.
Extra patterns (gitignore-style globs, one per line) go in:
  ~/.claude/claudeignore   (all projects)   and   ./.claudeignore  (this project)
Lines starting with '!' un-block a path. Disable: TOKEN_GUARD_OFF=1.
"""
import fnmatch, json, os, sys

MAX_BYTES = 200_000          # unbounded Read above this is refused
BINARY_OK = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".ipynb"}  # Read handles these natively

DIRS = {"node_modules", ".git", ".venv", "venv", "__pycache__", ".pytest_cache",
        ".mypy_cache", ".ruff_cache", ".tox", ".next", ".nuxt", "dist", "build",
        "target", "coverage", ".gradle", "Pods", "DerivedData", ".idea",
        ".cache", "site-packages", ".parcel-cache", ".turbo", "graphify-out/cache"}
NAMES = ["package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock", "Cargo.lock",
         "Pipfile.lock", "composer.lock", "Gemfile.lock", "uv.lock", ".DS_Store"]
GLOBS = ["*.min.js", "*.min.css", "*.map", "*.pyc", "*.pyo", "*.so", "*.dylib", "*.dll",
         "*.exe", "*.o", "*.a", "*.class", "*.jar", "*.zip", "*.tar", "*.gz", "*.tgz",
         "*.7z", "*.dmg", "*.pkg", "*.sqlite", "*.db", "*.parquet", "*.npa.bak",
         "*.woff", "*.woff2", "*.ttf", "*.mp4", "*.mov", "*.mp3", "*.wasm", "*.log"]

def extra_patterns(cwd):
    pats = []
    for p in (os.path.expanduser("~/.claude/claudeignore"), os.path.join(cwd, ".claudeignore")):
        try:
            pats += [l.strip() for l in open(p) if l.strip() and not l.startswith("#")]
        except OSError:
            pass
    return pats

def blocked_reason(path, cwd, extra):
    rel = path.replace("\\", "/")
    parts = rel.split("/")
    base = parts[-1]
    allow = [p[1:] for p in extra if p.startswith("!")]
    deny = [p for p in extra if not p.startswith("!")]
    if any(fnmatch.fnmatch(rel, "*" + a) or fnmatch.fnmatch(base, a) for a in allow):
        return None
    for d in DIRS:
        if "/" in d:
            if "/" + d + "/" in "/" + rel: return d + "/"
        elif d in parts[:-1] or (d == base and False):
            return d + "/"
    if base in NAMES: return base
    for g in GLOBS:
        if fnmatch.fnmatch(base, g): return g
    for g in deny:
        g2 = g.rstrip("/")
        if fnmatch.fnmatch(base, g2) or fnmatch.fnmatch(rel, "*" + g2 + "*") or g2 in parts:
            return g
    return None

def deny(msg):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
          "permissionDecision": "deny", "permissionDecisionReason": msg}}))
    sys.exit(0)

PREAMBLE = ("[token-saving rules] Be economical: do not read files under node_modules, .git, venv, "
            "caches, build/dist, lockfiles, minified/map/binary files. Use Grep/Glob to locate before "
            "Read; read with offset/limit, never whole large files. Do not re-read files already in "
            "your prompt. Return a concise conclusion (<300 words), not file dumps.\n\n")

def main():
    if os.environ.get("TOKEN_GUARD_OFF") == "1":
        return
    d = json.load(sys.stdin)
    tool, ti = d.get("tool_name", ""), d.get("tool_input", {}) or {}
    cwd = d.get("cwd") or os.getcwd()

    if tool in ("Agent", "Task"):
        p = ti.get("prompt", "")
        if p and not p.startswith("[token-saving rules]"):
            ti["prompt"] = PREAMBLE + p
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                  "permissionDecision": "allow", "updatedInput": ti}}))
        return

    extra = extra_patterns(cwd)
    if tool == "Read":
        path = ti.get("file_path", "")
        r = blocked_reason(path, cwd, extra)
        if r:
            deny(f"token-guard: '{r}' is on the ignore list (noisy/low-value). Use Grep for a specific "
                 f"symbol, or add '!{os.path.basename(path)}' to .claudeignore, or set TOKEN_GUARD_OFF=1.")
        ext = os.path.splitext(path)[1].lower()
        if ext not in BINARY_OK and not ti.get("offset") and not ti.get("limit") and not ti.get("allow_large"):
            try:
                if os.path.getsize(path) > MAX_BYTES:
                    deny(f"token-guard: {os.path.getsize(path)//1000} KB file. Use Grep to find the "
                         f"section, then Read with offset/limit.")
            except OSError:
                pass
    elif tool in ("Grep", "Glob"):
        path = ti.get("path", "") or ""
        r = blocked_reason(path + "/x", cwd, extra) if path else None
        pat = ti.get("pattern", "") + " " + (ti.get("glob", "") or "")
        if not r:
            for dname in DIRS:
                if "/" not in dname and dname + "/" in pat:
                    r = dname + "/"
        if r:
            deny(f"token-guard: searching '{r}' is blocked (noisy). Narrow to your source directories.")

try:
    main()
except SystemExit:
    raise
except Exception:
    pass  # never break the session
