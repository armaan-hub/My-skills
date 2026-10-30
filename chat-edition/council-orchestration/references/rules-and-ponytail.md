# Standing Rules and the Ponytail Ladder

## Standing rules

| # | Rule |
|---|---|
| 1 | **Keep going.** Do not stop to ask permission for each step. Resolve blockers yourself and note what you assumed. |
| 2 | **Boot first.** No stage starts before the team is written. |
| 3 | **Personas on every output.** Every stage speaks in the team's personas. |
| 4 | **Teams debate before reporting.** Thinking and Execution teams use the 3-round protocol. |
| 5 | **The Tester is the gate.** Failures stop the cycle. |
| 6 | **The Head routes.** The Head accepts or rejects team output and sends errors back. |
| 7 | **Build from a failing check.** Write the check that defines "done" before building each part. If the part was built first, rebuild it against the check. |
| 8 | **Verify before claiming.** Show the result, then the claim. |
| 9 | **Find the cause before fixing.** |
| 10 | **Never silence the Critic.** The Critic reports at THINK, PLAN, CREATE, and REVIEW, with an explicit "no concerns" if there are none. |
| 11 | **Each task is its own unit.** One behavior per check. |
| 12 | **Keep the record.** The state tracker, consensus records, and experiment log are the truth. Re-read the team when the conversation gets long. |
| 13 | **Deliver only after sign-off.** VERIFY sign-off and a delivery check both pass. |
| 14 | **Log every keep and discard.** |
| 15 | **Stop at 5 iterations.** Report the state and ask the user whether to continue. |
| 16 | **Ponytail on everything.** |

## Context length

Long sessions lose the personas. When the conversation is getting long:
1. Restate the State Tracker.
2. Restate the Council Agents section (the team).
3. Restate the last Experiment Log rows and the open gaps.
4. Continue from the stated stage.

## The Ponytail ladder

Apply in order at every stage. Stop at the first step that solves the problem.

1. **YAGNI** — Is this part, feature, abstraction, or dependency needed now? If not, remove it.
2. **Standard library** — Does the tool's standard function or library already do this?
3. **Built-in platform feature** — Does the platform already do this (a spreadsheet function, a built-in table, a native feature)?
4. **One line** — Can it be done in one line or one formula?
5. **Minimum** — Write the smallest thing that works.

Mark any deliberate shortcut in the work with a note: `Simplification: <limit>, <what to do if it grows>`.

### Ponytail review tags

When reviewing work, tag each finding:
- **delete** — dead content or unneeded flexibility
- **stdlib** — something rebuilt that a standard feature already does
- **native** — something a dependency does that the platform does already
- **yagni** — an abstraction with only one use
- **shrink** — same result, fewer steps

For each: location, what to cut, what replaces it, and the net amount removable.
