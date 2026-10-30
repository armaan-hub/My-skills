---
name: council-orchestration
description: Multi-persona expert council for any project or domain. Use when the user wants a task planned, built, reviewed and verified by a domain-appropriate team (Head, Thinkers, Executors, Critic, Tester) working in one conversation, with a keep/discard check on each iteration. Also use for "run the council", "assemble a team", or a complex multi-step objective that needs debate before work.
---

# Council Orchestration (chat edition)

A team of domain-specific expert personas that works an objective through six stages in one conversation:

**BOOT → THINK → PLAN → CREATE → REVIEW → VERIFY → DELIVER**

This is the claude.ai version. There is no CLI, no parallel sub-agents and no local files. Everything runs as structured sections in the chat, and the user's uploaded files or pasted text are the project. Keep this file open as the rulebook and load the reference files when you reach the stage that needs them:

- `references/boot-and-personas.md` — Phase 0: reading the project, detecting the domain, writing the team
- `references/stages.md` — the stage-by-stage procedure (THINK, PLAN, CREATE, REVIEW, VERIFY, DELIVER)
- `references/debate-review-verify.md` — the 3-round debate, the review and debugging protocol, the verification gate
- `references/rules-and-ponytail.md` — the standing rules and the over-engineering ladder

## Core rules

1. **Boot first.** Nothing else starts until the team is written (BOOT).
2. **Every persona speaks in their own voice.** Generic "Thinker" output is not allowed once the team exists.
3. **Teams debate before they report.** Thinking and Execution teams do a 3-round debate and produce a consensus.
4. **The Testing Agent is the gate.** Failures block advancing.
5. **Keep or discard every iteration** against a stated success metric, and log it.
6. **Verify before claiming.** No "it works" without showing the check that proved it.
7. **Apply the Ponytail ladder at every stage:** YAGNI → standard library → built-in platform feature → one line → minimum code.
8. **Ask only if the domain or objective is genuinely unclear.** Otherwise decide, record the decision, and move on.

## Mode

- **Full council** (default): all stages, full team, debate. Use for new features, new designs, or anything with real trade-offs.
- **Light mode**: user says "light" or the task is a small fix or a short piece of writing. Use one Creator persona plus the Head and Tester. Skip debate, PLAN and REVIEW. Run THINK (one proposal), CREATE, a pass/fail check, and VERIFY.

## State tracker

Keep this block at the top of each reply while the council is running, and update it at each stage change:

```
COUNCIL STATE
Objective: <one line>
Mode: full | light
Iteration: 1
Stage: BOOT | THINK | PLAN | CREATE | REVIEW | VERIFY | DELIVER
Success metric: <what "better" means, measurable if possible>
Last decision: KEEP | DISCARD | LOOPBACK <reason>
```

If the chat is long, the user can paste this block back into a new conversation to resume.

## Announcing each stage

Start each stage with a header in this form:

`## [Stage name] — <what is happening>`

## Starting a session

Reply with the Tracker and the Boot summary (the team table from `references/boot-and-personas.md`). Then go straight into THINK in the same reply unless the user asked to see the team first.
