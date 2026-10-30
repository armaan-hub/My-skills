# My Skills

Claude skills for Claude Code (`skills/`), and claude.ai / Claude Desktop / Excel uploads (`claude-chat-zips/`, `chat-edition/`).

## Claude Code
Copy a folder from `skills/` into `~/.claude/skills/` (the folders are already in that layout).

| Skill | Folder | Notes |
|---|---|---|
| `ai-council-orchestration` | skills/ai-council-orchestration | Multi-model autonomous loop through Think→Plan→Create→Review→Verify — uses the best model per stage from ALL connected providers. Live auto- |
| `ai-relay-handoff` | skills/ai-relay-handoff | Auto-detects AI tool context handoff from OpenCode/Copilot to Claude Code and continues work seamlessly across all projects. |
| `auto-session-summaries` | skills/auto-session-summaries | Use when starting a new session to set up automatic summary logging to a persistent folder on session end; summaries capture decisions, lear |
| `council-orchestration` | skills/council-orchestration | Fully self-contained autonomous autoresearch loop with dynamic domain-aware agent teams — Boot→Think→Plan→Create→Review→Verify. Scans projec |
| `Financial-Agents` | skills/Financial-Agents | Autonomous 6-Subagent Financial Audit Council & Data Analysis Engine for UAE Statutory Comparative Mainland Audit Reports, Trial Balance aud |
| `graphify` | skills/graphify | "any input (code, docs, papers, images, videos) to knowledge graph. Use when user asks any question about a codebase, documents, or project  |
| `loop` | skills/loop | Cross-platform recurrent task runner — run any command on an interval (fixed or self-paced). Portable across Claude Code, Gemini CLI, Copilo |
| `notebooklm` | skills/notebooklm | Complete API for Google NotebookLM - full programmatic access including features not in the web UI. Create notebooks, add sources, generate  |
| `ponytail-audit` | skills/ponytail-audit | > |
| `ponytail-debt` | skills/ponytail-debt | > |
| `ponytail-gain` | skills/ponytail-gain | > |
| `ponytail-help` | skills/ponytail-help | > |
| `ponytail-review` | skills/ponytail-review | > |
| `ponytail` | skills/ponytail | > |
| `powerbi-agents` | skills/powerbi-agents | 5-Expert Specialized Power BI & Analytics Council (Instructor, Helper, Business Analyst, Strategist, Report Designer) to collaboratively gui |
| `reconciliation-excel-lambda-expert` | skills/reconciliation-excel-lambda-expert | Excel modeling architect for reconciliation workbooks. Use when building or reviewing reconciliation Excel workbooks with formulas, LAMBDA/L |
| `reconciliation-external-auditor` | skills/reconciliation-external-auditor | Independent external audit partner. Use when challenging reconciliation results against source rows and IFRS/GAAP, evaluating substantive te |
| `reconciliation-internal-auditor` | skills/reconciliation-internal-auditor | Senior internal auditor and operational risk lead. Use when testing reconciliation controls and segregation of duties, investigating root ca |
| `reconciliation-manager-coordinator` | skills/reconciliation-manager-coordinator | Financial controller and reconciliation project manager. Use when planning or running an end-to-end bank, GL or subledger reconciliation, ro |
| `reconciliation-reconciler` | skills/reconciliation-reconciler | Senior forensic reconciliation accountant. Use when matching bank statements, payment-gateway payouts, AP/AR subledgers or GL accounts line  |
| `reverse-engineer-anything` | skills/reverse-engineer-anything | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. Use shipped-artifact or requested r |
| `switch-model` | skills/switch-model | Switch between OpenCode AI models (free tier) |
| `twc-auditor` | skills/twc-auditor | — |
| `uae-law` | skills/uae-law | Use when answering questions about UAE laws, Federal Tax Authority regulations, VAT, Corporate Tax, Excise Tax, or legal requirements for bu |
| `video-vision` | skills/video-vision | Director-level vision interrogation for AI video generation. Chains brainstorming, writing-skills, council-orchestration, code-review, and p |
| `visiting-card-designer` | skills/visiting-card-designer | Use when asked to design, create, or generate a visiting card, business card, or name card — whether SVG, PDF, printable, or digital. Covers |

## claude.ai, Claude Desktop, Excel
Upload one zip per skill under Customize > Skills: see `claude-chat-zips/`. `chat-edition/council-orchestration/` is the chat-ready council (split into reference files).

## Secrets
API keys are not stored in this repo. `Financial-Agents/audit_council_local/llm.py` reads `OPENCODE_API_KEY` from the environment.
