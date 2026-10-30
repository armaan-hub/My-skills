#!/usr/bin/env python3 -u
"""
Auto-Journal Updater for PROJECT_JOURNAL.md
Usage:
    python3 scripts/hooks/update_journal.py --event <type> --<args>

Types: completion, decision, iteration, issue, script, council, production_bible, skill, video_batch, summary, failed_attempt
"""

import argparse, os, re, sys
from datetime import datetime, timezone

JOURNAL = "/Users/armaan/AI-Live Model/PROJECT_JOURNAL.md"
TZ = "+04:00"

def now(): return datetime.now(timezone.utc).strftime(f"%Y-%m-%d %H:%M GMT{TZ}")

def prepend(content, entry):
    """Insert entry at TOP of Recent Activity table."""
    marker = "## Recent Activity\n"
    if marker not in content:
        return content, False
    lines = content.split("\n")
    out = []
    inserted = False
    for line in lines:
        out.append(line)
        if line.startswith("|------") and not inserted:
            out.append(f"| {now()} | {entry}")
            inserted = True
    if not inserted:
        # Fallback: insert before the next ## heading
        out2 = []
        for line in lines:
            if line.startswith("## ") and not inserted:
                out2.append(f"| {now()} | {entry}")
                inserted = True
            out2.append(line)
        return "\n".join(out2), True
    return "\n".join(out), True

# ── Event handlers ──────────────────────────────────────────────────────────

def h_completion(video, script=None, log=None, params=None):
    e = f"**Completed:** `{os.path.basename(video)}`"
    if script: e += f" Script: `{script}`"
    if log and os.path.exists(log): e += f" Log: `{os.path.basename(log)}`"
    if params: e += f" Params: {params}"
    return e

def h_decision(title, detail=None):
    e = f"**Decision:** {title}"
    if detail: e += f" — {detail}"
    return e

def h_iteration(name, summary):
    return f"**New Iteration:** {name} — {summary}"

def h_issue(title, status=None, detail=None):
    icon = "✅" if status == "fixed" else "🔴"
    e = f"{icon} **Issue:** {title}"
    if status: e += f" [{status.upper()}]"
    if detail: e += f" — {detail}"
    return e

def h_script(name, path=None, purpose=None):
    e = f"**New Script:** `{name}`"
    if purpose: e += f" — {purpose}"
    if path: e += f" at `{path}`"
    return e

def h_council(round=None, topic=None, outcome=None):
    e = f"🏛️ **Council"
    if round: e += f" Round {round}"
    if topic: e += f": {topic}"
    if outcome: e += f" → {outcome}"
    return e

def h_production_bible(change=None):
    return f"📖 **Production Bible:** {change}"

def h_skill(name, file=None, purpose=None):
    e = f"⚡ **New Skill:** `{name}`"
    if purpose: e += f" — {purpose}"
    if file: e += f" at `{file}`"
    return e

def h_video_batch(count=None, scene=None):
    e = f"🎬 **Batch:"
    if count: e += f" {count} videos"
    if scene: e += f" — {scene}"
    return e

def h_summary(text):
    return f"📝 **Update:** {text}"

def h_failed(script, reason=None, log=None):
    e = f"❌ **Failed:** `{script}`"
    if reason: e += f" — {reason}"
    if log and os.path.exists(log): e += f" Log: `{os.path.basename(log)}`"
    return e

HANDLERS = {
    "completion": h_completion,
    "decision": h_decision,
    "iteration": h_iteration,
    "issue": h_issue,
    "script": h_script,
    "council": h_council,
    "production_bible": h_production_bible,
    "skill": h_skill,
    "video_batch": h_video_batch,
    "summary": h_summary,
    "failed_attempt": h_failed,
}

# ── CLI ──────────────────────────────────────────────────────────────────

P = argparse.ArgumentParser()
P.add_argument("--event", required=True, choices=list(HANDLERS.keys()))
P.add_argument("--video", "--path")
P.add_argument("--script")
P.add_argument("--log")
P.add_argument("--params")
P.add_argument("--title")
P.add_argument("--detail")
P.add_argument("--summary")
P.add_argument("--status")
P.add_argument("--name")
P.add_argument("--purpose")
P.add_argument("--round")
P.add_argument("--topic")
P.add_argument("--outcome")
P.add_argument("--change")
P.add_argument("--count")
P.add_argument("--scene")
P.add_argument("--text")
P.add_argument("--reason")

if __name__ == "__main__":
    a = P.parse_args()
    if not os.path.exists(JOURNAL):
        print(f"❌ Journal not found: {JOURNAL}")
        sys.exit(1)
    handler = HANDLERS[a.event]
    kw = {k: getattr(a, k) for k in dir(a) if not k.startswith("_") and getattr(a, k) is not None}
    kw = {k: v for k, v in kw.items() if v not in (None, False)}
    kw.pop("event", None)
    entry = handler(**kw)
    with open(JOURNAL) as f: c = f.read()
    c, ok = prepend(c, entry)
    # Update timestamp
    c = re.sub(r"\*\*Last Updated:\*\* .+", f"**Updated:** {now()}", c, count=1)
    with open(JOURNAL, "w") as f: f.write(c)
    print(f"✅ Journal updated [{a.event}]")
    print(f"   {entry[:120]}")
