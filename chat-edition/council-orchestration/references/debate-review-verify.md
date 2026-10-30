# Debate, Review, Debugging, and Verification

## Team Debate Protocol (3 rounds)

Use whenever a team must solve a problem together. Write each round under its own heading, with each persona speaking in turn.

**Round 1 — Independent proposals.** Each agent writes their approach without reading the others': "My proposed approach: …"

**Round 2 — Cross-critique.** Each agent reads the other's proposal and names its flaws, risks, and gaps: "What is wrong with B's approach: …"

**Round 3 — Convergence.** Each agent revises their position in light of the critiques: "Given the critique of mine and my critique of B, my revised position is …"
- Agreement → consensus.
- Still diverging → the Head decides: "The correct path is X, because Y."

### Consensus record

```
# Team Consensus — <stage> — <topic>
Team: <Thinking | Execution>
Agents: <A title> + <B title>

Round 1: <A summary> | <B summary>
Round 2: <A on B> | <B on A>
Round 3: <final consensus>
Key decision: <most important choice>
Rejected alternatives: <what was ruled out and why>
```

The Head reads the consensus and either accepts it (proceed) or rejects it with the missing point (run a new round with the Head's note added). Tester errors always trigger a new debate round with the error report included.

---

## Domain-aware review

- The Critic reviews the work as an outside expert. The question is: "Would a <Critic title> approve this for real use?"
- The Tester runs every check and reports every failure, with exact output.
- Both run on the same work. Neither one's report replaces the other's.

---

## Systematic debugging

Use for any error, failed check, or unexpected result. Do not propose a fix before finishing phase 1.

**Phase 1 — Root cause (before any fix):**
1. Read the full error message: the exact cell, line, or clause that failed.
2. Reproduce it: same input, same result, every time?
3. Check what changed: the last edit, the last input, the last version.
4. Trace the data: where does the bad value first appear?

**Phase 2 — Pattern:**
1. Find a similar part that works.
2. Compare it to the broken one, completely.
3. List every difference.

**Phase 3 — Hypothesis:**
1. State one hypothesis: "I think X is the cause, because Y."
2. Test it with the smallest change, one variable at a time.
3. Worked → fix. Did not work → new hypothesis.

**Phase 4 — Fix:**
1. Write a test or check that reproduces the failure.
2. Apply one fix that addresses the cause.
3. Re-run the check and the full set. Confirm no regressions.
4. If three fixes have failed, stop and question the design, not the details.

**Iron law:** No fix without a root cause.

---

## Verification gate

**Iron law:** No completion claim without fresh evidence from this iteration.

For each claim:
1. Name the check that proves it.
2. Run the complete check.
3. Read the full output. Count the failures. Note any warnings.
4. If the output does not confirm the claim, say so with the actual result. If it does, state the claim with the evidence.

**Red flags** (stop and run the check): "should work", "probably", "looks right", "seems fine", reporting success before a result is shown, or trusting a claim from an earlier iteration.

---

## Feedback handling

1. Read all feedback before responding.
2. Restate what is being asked, or ask one clarifying question.
3. Check the claim against the actual work.
4. Decide: is it correct for this work?
5. Respond: accept with a note of what changes, or push back with a reason.
6. Implement one item at a time, and re-check after each.

Never agree without checking. Never apply a batch of changes without re-checking.
