name: ai-relay-handoff
description: Auto-detects AI tool context handoff from OpenCode/Copilot to Claude Code and continues work seamlessly across all projects.
version: 1.0
author: Armaan
---

# AI Relay Handoff

This skill enables seamless context handoff between AI CLI tools (OpenCode/Copilot, Claude Code, Gemini CLI, etc.) using a universal relay system at `~/.ai-relay/`.

## How It Works

1. When switching from OpenCode/Copilot → Claude Code:
   - Run `ai-relay capture opencode` in OpenCode before switching
   - In Claude Code, the context auto-loads when entering the project directory

2. When switching from Claude Code → Gemini CLI:
   - Run `ai-relay handoff gemini` in Claude Code
   - In Gemini CLI, context is ready to read

## Quick Commands (after sourcing integration)

| Command | Description |
|---------|-------------|
| `ar` | AI Relay main command |
| `arc <tool>` | Capture current session |
| `arh <tool>` | Hand off to another AI tool |
| `arcx` | Get context for current project |
| `cap <tool>` | Quick capture (alias) |
| `relay <tool>` | Quick handoff (alias) |

## Usage Flow

### OpenCode → Claude Code
```
# In OpenCode/Copilot (before switching)
$ ai-relay capture opencode
✓ Context captured for myproject

# In Claude Code
$ cd ~/myproject
$ ai-relay context
📋 Handoff Detected!
From: opencode
[Context summary loads]
```

### Claude Code → Gemini
```
# In Claude Code
$ ai-relay handoff gemini
🔄 Handoff prepared for gemini

# In Gemini CLI
$ cd ~/myproject
$ ai-relay context
📋 Context ready to continue
```

## Token Optimization

The relay system captures:
- **Git diff summary** (not full diffs) - minimal tokens
- **Recent file modifications** - only files changed in last hour
- **Source file list** - tree, not content
- **Context summary** - AI-generated markdown overview

This ensures the receiving AI gets:
1. What changed (git status)
2. Why it changed (recent commits)
3. Where to look (file list)
4. Summary of intent (markdown)

## Setup

Add to your shell profile:
```bash
source ~/.ai-relay/bin/ai-relay-integration.sh
```

## Cross-Platform

This relay works with ANY AI CLI that can:
1. Execute shell commands
2. Read/write files
3. Access `~/.ai-relay/`

Supported tools:
- OpenCode (GitHub Copilot proxy)
- Claude Code
- Gemini CLI
- OpenAI Codex
- Ollama CLI
- Any other terminal AI tool