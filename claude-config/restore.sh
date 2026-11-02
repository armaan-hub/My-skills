#!/bin/sh
# Restore Claude Code global config (settings, hooks, CLAUDE.md) into ~/.claude.
# Existing files are backed up with a .bak-<timestamp> suffix first.
set -e
SRC="$(cd "$(dirname "$0")" && pwd)"
TS=$(date +%Y%m%d%H%M%S)
mkdir -p ~/.claude/hooks
for f in settings.json CLAUDE.md jarvis-auto-sync.py; do
  [ -f "$SRC/$f" ] || continue
  [ -f ~/.claude/$f ] && cp ~/.claude/$f ~/.claude/$f.bak-$TS
  cp "$SRC/$f" ~/.claude/$f
done
for f in "$SRC"/hooks/*; do
  n=$(basename "$f")
  [ -f ~/.claude/hooks/$n ] && cp ~/.claude/hooks/$n ~/.claude/hooks/$n.bak-$TS
  cp "$f" ~/.claude/hooks/$n
done
chmod +x ~/.claude/hooks/*.sh 2>/dev/null || true
echo "Restored Claude config into ~/.claude (backups: *.bak-$TS). Restart Claude Code."
