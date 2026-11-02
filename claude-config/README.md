# Claude Code global config backup

Backup of `~/.claude` settings, hooks and global instructions.

| File | Restores to | Purpose |
|------|-------------|---------|
| `settings.json` | `~/.claude/settings.json` | All settings, including hooks |
| `CLAUDE.md` | `~/.claude/CLAUDE.md` | Global instructions (model routing rule, agent rule) |
| `hooks/model-routing.sh` | `~/.claude/hooks/` | SessionStart hook: Opus plans, Haiku codes, Sonnet fixes, Haiku overviews |
| `hooks/token-guard.py` | `~/.claude/hooks/` | PreToolUse token-saving guard |
| `jarvis-auto-sync.py` | `~/.claude/` | Jarvis auto-sync hook script |

## Restore

```sh
git clone https://github.com/armaan-hub/My-skills.git
cd My-skills/claude-config
./restore.sh
```

Then restart Claude Code and open `/hooks` to confirm. Existing files are backed up as `*.bak-<timestamp>` before being replaced.

Note: `settings.json` references MCP servers in `~/.jarvis` and `~/.claude/mcp-daemon`, which are not part of this backup.
