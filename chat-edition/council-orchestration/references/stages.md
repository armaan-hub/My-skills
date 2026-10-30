# Stages

Work through the stages in order. A stage ends with a Head decision: ADVANCE, KEEP, or LOOPBACK (send back to a named stage with a reason). Update the State Tracker after each decision.

Use the Team Debate Protocol (`debate-review-verify.md`) wherever a team must decide something.

---

## Stage 1 — THINK

**Who:** Thinking Team (debate), Critic, Head.

1. **Explore context.** The Head asks the Thinking Team to read the project material and list what exists, what is missing, and what constraints apply.
2. **Debate the approach.** Topic: "Best approach for: <objective>". Cover: structure of the deliverable, data or input flow, error and edge cases, how this domain would check the result. Apply the Ponytail ladder.
3. **Head stress test.** The Head asks:
   - Which domain assumptions could be false?
   - Which regulatory, legal, or operational rules are non-negotiable?
   - What is most likely to fail in real use?
4. **Thought report.** Write `THOUGHT REPORT`: interpretations, constraints, risks, at least three approaches compared (pros and cons), and the recommended approach with domain justification.
5. **Critic review.** The Critic writes `CRITIQUE`: assume the approach is wrong, list the assumptions that could be false and the risks that were missed. If there are none, the Critic must write exactly: **"No concerns — approach is sound."**
6. **Decide.**
   - Critic has concerns → LOOPBACK to THINK with the concerns added to the debate.
   - No concerns → Head approves → ADVANCE to PLAN.

**Light mode:** Creator gives one proposal. Head approves. Advance to CREATE.

---

## Stage 2 — PLAN

**Who:** Thinking Team (structure), Execution Team (feasibility), Critic, Head.

1. **Map the structure.** The Thinking Team proposes the parts of the deliverable: sections, files, sheets, modules, or documents. Each part has one clear purpose. Include only what is needed.
2. **Feasibility check.** Executor A: "Can this be built this way with the tools we have? Are the tasks realistic?" Executor B: "Is documentation and any secondary output covered?"
3. **Break into tasks.** Each task is one action. Format:
   ```
   Task N: <name>
   Owner: Executor A | Executor B
   Input: <what is needed>
   Action: <exact steps, including formulas, code, or wording to produce>
   Expected output: <what done looks like>
   Check: <how the Tester will verify it>
   ```
4. **Write the plan.** Sections: Goal (one sentence), Approach (2–3 sentences), Domain rationale, Tools, Tasks.
5. **Self-review.** Confirm:
   - Every requirement maps to a task.
   - No placeholders such as "TBD" or "later".
   - Names and definitions match across tasks.
   - Every step has the concrete content, not a description of it.
   - Every file, sheet, or dependency is essential. Cut anything that is not.
6. **Critic review.** Ask: are any tasks under-specified? Are the dependencies right? Are the Stage 1 risks covered? Would a real <Critic title> approve this plan?
7. **Decide.** Concerns → LOOPBACK to PLAN. Clear → Head approves → ADVANCE to CREATE.

---

## Stage 3 — CREATE

**Who:** Execution Team (builds), Tester (gate), Head (routing).

1. **Set the success metric before building.** Choose one measurable criterion, for example:
   - Test pass rate (higher is better)
   - Number of formula or data errors (lower is better)
   - Requirements met out of total (higher is better)
   - Word count or time within a limit (within range)
   If nothing measurable exists, use: "Does the output satisfy every completion criterion?"
2. **Build task by task.** For each task, the owning Executor produces the output, then self-checks it against the task's Check line.
3. **Two-stage review per task.**
   - Spec check: does it match the plan, with nothing missing and nothing extra?
   - Domain quality check: would a <Executor title> accept this as professional-grade work?
   Both must pass before the next task.
4. **Tester checkpoint.** After each batch, the Tester runs every check in the plan and reports every failure, with the exact output. Failures go back to the Execution Team with the error list. Repeat until the Tester reports zero failures.
5. **Missing capability.** If a reusable pattern is needed and missing, write a short definition (what it is, when to use it, core pattern) and use it. Do not improvise undocumented logic.
6. **Head council check.** All components done? Tester has zero failures? All Critic concerns resolved? If yes → KEEP/DISCARD. If no → LOOPBACK to CREATE.

### KEEP / DISCARD

Measure the success metric against the previous iteration (or against zero, on the first pass).

- **Improved or unchanged and acceptable → KEEP.** Log it. Advance to REVIEW.
- **Worse, or unacceptable → DISCARD.** State what failed and why. Undo the changes in this iteration (say what is being reverted, and rebuild from the last kept version). Loop back to THINK with the reason added as a learning: "Approach X was tried and discarded because Y. Next, try Z."

### Experiment log

Keep this table in the conversation and update it on every KEEP or DISCARD:

| # | Iter | Action | Metric | Changes | Learning |
|---|---|---|---|---|---|

---

## Stage 4 — REVIEW

**Who:** Critic, Tester, Head, Execution Team (fixes).

1. **Brief.** State what was built and what it should do.
2. **Critic review.** Look for logic errors, domain-specific correctness, edge cases, gaps, anti-patterns, and maintainability. Then run the Ponytail review: name what to delete, what to replace with a standard feature, and what to simplify, with the location and the expected effect. Report the approximate amount of unnecessary content removable.
3. **Tester review.** Run every check. Report every failure with its full output. Suppress nothing.
4. **Issues report.** Write `REVIEW ISSUES`, grouped as Critical (fix now), Important (fix before proceeding), Minor (note for later).
5. **Route fixes.** The Head sends each Critical and Important item to the Execution Team with its error. The Execution Team debates the root cause and fix, then the Executor applies it. Use the debugging protocol in `debate-review-verify.md`.
6. **Evaluate feedback.** Read all feedback before reacting. Check each item against the actual work. Accept what is correct. Push back, with reasons, on anything that breaks existing work or adds scope without need. Fix one item at a time and re-check after each.
7. **Loop until clear.** Zero unresolved Critical and Important issues, and the Tester reports zero failures → ADVANCE to VERIFY. Otherwise LOOPBACK to REVIEW.

---

## Stage 5 — VERIFY

**Who:** Tester (final gate), Head (sign-off).

1. **Verification gate.** For every claim you will make, do the following and show the result:
   - Identify the check that proves it.
   - Run it (for a spreadsheet, recalculate and read the values; for code, run the tests; for a document, check each requirement against the text).
   - Read the full result.
   - Confirm or state the actual status.
2. **Full integration check.** Run the complete set of checks, not a sample. Check every link between parts (formulas across sheets, references between documents, imports between modules).
3. **Completeness sign-off.** Tester checks every criterion from the original objective and writes `VERIFICATION SIGN-OFF`:
   - "VERIFIED — ready to deliver", or
   - each unmet criterion, listed explicitly.
4. **Head decision.** VERIFIED → ADVANCE to DELIVER. Gaps → LOOPBACK to the stage that owns the gap.

---

## Stage 6 — DELIVER

1. Check the output against the original objective and the completion criteria again.
2. Write `ANALYSIS REPORT`:
   - Iterations run
   - Experiments: kept, discarded, keep rate
   - What changed each time and what was learned
   - Recommendations for next time
3. Present the final output.

**If fully satisfied:**

```
## 📦 [DELIVERY] Objective satisfied
🎯 Objective: <objective>
✅ Iterations: N
📊 Experiments: Y kept, Z discarded (K% keep rate)
📄 Output: <what the user should take away, or the attached file>
```
Stop.

**If not fully satisfied:** list the unmet gaps, start Iteration N+1 with all accumulated learnings, and go to THINK. Stop after 5 iterations and report to the user. Ask whether to continue.
