---
name: switch-model
description: Switch between OpenCode AI models (free tier)
user_invocable: true
---

# switch-model - Switch between OpenCode AI models

## Available Free Models (Verified Working)

| Model | ID | Provider | Status |
|-------|-----|----------|--------|
| MiniMax | minimax-m2.5-free | MiniMax | ✅ Active |
| Ring 2.6 | ring-2.6-1t-free | Novita | ✅ Active |
| Nemotron | nemotron-3-super-free | NVIDIA | ✅ Active |

## Usage

```
switch-model              # Show model list
switch-model minimax      # Switch to MiniMax (default)
switch-model ring         # Switch to Ring 2.6
switch-model nemotron     # Switch to Nemotron
```

## How to Switch

Type `/model minimax-m2.5-free` or use the model selector in the UI.

## Notes

- These are **FREE tier models** — no cost to use
- Start a new session after switching
- More models available with OpenCode Go plan

## Current Model

Check: `cat ~/.claude/settings.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('model'))"`