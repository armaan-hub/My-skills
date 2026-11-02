# Financial-Agents
- **Financial-Agents** (`~/.claude/skills/Financial-Agents/SKILL.md`) - 6-Subagent Financial Audit Council & Data Analysis Engine for UAE Statutory Comparative Mainland Audit Reports, Trial Balance auditing, P&L mapping, corporate legal context integration, and mathematical verification. Trigger: `/Financial-Agents` or `/financial-agents`
When the user types `/Financial-Agents` or `/financial-agents`, invoke the Skill tool with `skill: "Financial-Agents"` before doing anything else.

# Power BI Agents
- **powerbi-agents** (`~/.claude/skills/powerbi-agents/SKILL.md`) - 5-Expert Specialized Power BI & Analytics Council (Instructor, Helper, Business Analyst, Strategist, Report Designer) to collaboratively guide, build, transform, model, and design executive-grade Power BI reports for any dataset.
Trigger: `/powerbi-agents` or `@instructor`, `@helper`, `@analyst`, `@strategist`, `@designer`.
When the user asks for Power BI help or uses any of these triggers, invoke the Skill tool with `skill: "powerbi-agents"` before doing anything else.

# graphify
- **graphify** (`~/.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, invoke the Skill tool with `skill: "graphify"` before doing anything else.

## Model Selection & Claude Code Modes

### Official Claude (Anthropic Account)
```bash
claude                                    # Default model (Sonnet 4.5)
claude --dangerously-skip-permission     # Skip permission prompts
claude --model claude-opus-4-7           # Specific model
```
**Models:** Claude Haiku 4.5, Sonnet 4.5/4.6, Opus 4.7
**Cost:** From Claude PRO subscription

### Proxy Mode (OpenCode + All Providers)
```bash
run-claude-opencode                      # Interactive model picker (all 21+ models)
run-claude-opencode gpt-4o               # Start with gpt-4o
run-claude-opencode -m minimax-m2.7      # Start with minimax
```
**Models:** 21+ (minimax, kimi, glm, deepseek, qwen, etc.)
**Dashboard:** http://127.0.0.1:4001
**Cost:** Depends on provider (OpenCode, GitHub, Google, etc.)

### How to Change Models
**In either mode:**
- Click the **model name at bottom of Claude Code window**
- Arrow keys ↑↓ to browse, Enter to select
- Works immediately in this session

### Command Reference

| Task | Official | Proxy |
|------|----------|-------|
| Start + pick model | `claude --dangerously-skip-permission` | `run-claude-opencode` |
| Start with default | `claude` | `run-claude-opencode gpt-4o` |
| Specific model | `claude --model opus-4-7` | `run-claude-opencode minimax-m2.7` |
| View all models | (click status bar model) | http://127.0.0.1:4001 |

## Provider Status
- `/providers` — shows connected providers
- `/connect-provider <name>` — connect new provider

## Proxy Dashboard
**URL:** http://127.0.0.1:4001
**Shows:**
- Available models from all providers
- API key management
- Usage statistics
- Provider status

# Agent rule (all projects, set by the user 2026-10-23)
- Run subagents strictly one at a time. Start the next agent only after the previous one has finished and its work is verified and merged. Never run agents in parallel, even if a skill (e.g. council-orchestration "parallel dispatch") says to.

# Model routing rule (all projects, set by the user 2026-11-02)
- **Opus (main session) plans**: writes the spec/plan, splits work into tasks, verifies and merges results. It does not write feature code unless the user explicitly says so for that task.
- **Haiku writes the code**: dispatch an Agent subagent with `model: "haiku"` for each coding task.
- **Sonnet fixes errors**: failing tests, bugs and broken builds go to an Agent subagent with `model: "sonnet"`.
- **Haiku watches / overviews**: a read-only Agent subagent with `model: "haiku"` reviews finished work and reports.
- Subagents run one at a time (see Agent rule). At the start of any new project, copy this rule into the project's CLAUDE.md and keep a `HANDOFF.md` status board.
