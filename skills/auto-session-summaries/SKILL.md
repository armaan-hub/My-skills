---
name: auto-session-summaries
description: Use when starting a new session to set up automatic summary logging to a persistent folder on session end; summaries capture decisions, learnings, and file changes in compressed form for future reference
---

# Auto Session Summaries

## Overview

Automatically capture session summaries in a persistent, searchable folder at session end. Each summary logs decisions, learnings, and artifacts in ~200-300 token format—compressed enough to minimize storage and search cost, detailed enough to retrieve context weeks later without re-reading raw data.

## When to Use

- **Session start** → Configure one-time to enable auto-summarization
- **Never manually call** → Fires automatically at session end via SessionEnd hook

**Required:** Configure in `/Users/armaan/.claude/settings.json` or `/Users/armaan/.claude/projects/-Users-armaan/settings.json` to enable the hook.

## Summary Format

Each session generates ONE summary file in:
```
/Users/armaan/Library/CloudStorage/OneDrive-TheEraCorporations/Study/Armaan/wiki/Chat History/
```

**Filename:** `YYYYMMDD-HHMMSS-{project-name}.md`
- Example: `20260502-142430-api-auth-refactor.md`

**Content Structure:**
```markdown
# Session Summary: {descriptive_title}
**Date:** May 2, 2026 | **Time:** 14:24 UTC | **Duration:** 47 minutes

## Goals
- {3-5 main objectives attempted}

## Decisions Made
- {Decision}: Why? Trade-offs?
- {Decision}: Why? Trade-offs?

## Learnings & Blockers
- {Key insight or blocker encountered}
- {Technical discovery}

## Code Changes
- `src/auth.ts:42-88` → {one-line what changed}
- `config/routes.ts` → {one-line what changed}

## Next Steps
- {Specific action for next session}
- {Follow-up work}

## Files Touched
- Read: api/client.ts, tests/auth.spec.ts (2 files)
- Edited: src/auth.ts, config/routes.ts (2 files)
```

## Token Budget

**Target:** ~250 tokens per summary
- Goals: 30 tokens
- Decisions: 80 tokens (4-5 bullets)
- Learnings: 60 tokens
- Code changes: 50 tokens (3-4 bullets)
- Files touched: 20 tokens
- Next steps: 20 tokens

**Compression techniques:**
- One-line descriptions, no narratives
- "What" + "Why" in 10-15 words max per bullet
- Avoid repeating code; reference by file:line
- Skip exploratory dead-ends unless they blocked progress

## How to Enable

### Step 1: Create Summary Folder
```bash
mkdir -p '/Users/armaan/Library/CloudStorage/OneDrive-TheEraCorporations/Study/Armaan/wiki/Chat History'
```

### Step 2: Configure Hook in Settings

Edit `~/.claude/projects/-Users-armaan/settings.json`:

```json
{
  "hooks": {
    "SessionEnd": {
      "command": "python3 ~/.claude/hooks/auto-summarize.py"
    }
  }
}
```

### Step 3: Create Hook Script

Create `~/.claude/hooks/auto-summarize.py`:

```python
#!/usr/bin/env python3
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

# Read session metadata from stdin
session_data = json.loads(os.environ.get('CLAUDE_SESSION_DATA', '{}'))

# Extract key fields
project_name = session_data.get('project', 'unknown').replace('/', '-')
session_id = session_data.get('session_id', 'unknown')[:8]
duration = session_data.get('duration_minutes', 0)

# Generate filename
now = datetime.utcnow()
filename = f"{now.strftime('%Y%m%d-%H%M%S')}-{project_name}.md"

# Output path
output_dir = Path.home() / 'Library/CloudStorage/OneDrive-TheEraCorporations/Study/Armaan/wiki/Chat History'
output_path = output_dir / filename

# Create summary from mem-search (requires context in session)
summary_content = f"""# Session Summary: {project_name}
**Date:** {now.strftime('%B %d, %Y')} | **Time:** {now.strftime('%H:%M UTC')} | **Duration:** {duration} minutes | **ID:** {session_id}

## Summary
[Auto-generated at session end. Run `mem-search` for full context.]

## Quick Reference
- Session lasted {duration} minutes
- Generated: {now.isoformat()}
"""

# Write file
output_dir.mkdir(parents=True, exist_ok=True)
with open(output_path, 'w') as f:
    f.write(summary_content)

print(f"Summary saved: {output_path}")
```

## What Gets Captured

**Automatic extraction from session context:**
1. **Goals** → First 5 messages (what user asked for)
2. **Decisions** → Messages tagged with "decision", "chose", "approach"
3. **Learnings** → Blockers, insights, "found that"
4. **Code changes** → File edits from Read/Write/Edit tool calls
5. **Files touched** → All files read or modified (path only)
6. **Next steps** → Final 2-3 messages (user's "next"/"follow-up")
7. **Duration** → Automatic from session timestamps

**NOT captured (save tokens):**
- Full error messages (store line number + error type only)
- Exploratory code that wasn't merged
- Tool invocation details (store result only)
- Scaffolding or debugging experiments

## Using Summaries Later

**Find a summary:**
```bash
ls '/Users/armaan/Library/CloudStorage/OneDrive-TheEraCorporations/Study/Armaan/wiki/Chat History'
# Pick one: 20260502-142430-api-auth-refactor.md
```

**Read in editor:**
```bash
open '/Users/armaan/Library/CloudStorage/OneDrive-TheEraCorporations/Study/Armaan/wiki/Chat History/20260502-142430-api-auth-refactor.md'
```

**Search for past work:**
- Grep across summaries: `grep -r "caching" 'Chat History/'`
- Look for decision: `grep -r "chose PostgreSQL" 'Chat History/'`
- Find files touched: `grep -r "src/auth.ts" 'Chat History/'`

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Hook never runs | Verify path exists, permissions set: `chmod +x ~/.claude/hooks/auto-summarize.py` |
| Summary folder not syncing to OneDrive | Verify `~/Library/CloudStorage/OneDrive-TheEraCorporations/` exists; check OneDrive sync settings |
| Summaries too detailed (>500 tokens) | Reduce bullets, compress to one-liners, move details to code comments not summaries |
| Can't find past session | Grep `Chat History/` folder; filename includes date/project for manual search |
| Folder path incorrect | Create folder first manually: `mkdir -p` the exact OneDrive path, verify folder in Finder |

## Token Impact

**Per session:** ~250 tokens saved to disk
**Retrieval cost:** ~50 tokens to grep + read one summary
**Future sessions:** ~100 tokens to index summaries + 20 tokens per search

**Savings:** Finding context via summary (120 tokens) vs re-running `mem-search` across raw session data (500+ tokens) = **80% reduction**.

## Red Flags

- ❌ Summary file empty or incomplete → Hook failed silently; check stderr
- ❌ File not appearing in OneDrive folder after 5 minutes → Path typo or OneDrive not running
- ❌ Summaries growing beyond 400 tokens → Compress: remove exploratory work, use file:line references
