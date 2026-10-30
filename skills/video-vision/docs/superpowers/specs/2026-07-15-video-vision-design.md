# /video-vision — Custom Skill Design Spec

## Overview

A custom Claude Code skill that chains multiple superpowers to produce a comprehensive, director-level vision brief for AI video generation. The skill ensures every video concept is fully interrogated across 25 categories before any generation script is written, preventing the quality issues seen in previous generations (face quality, era inconsistency, body part merging, object generation from thin air, cross-segment continuity failures).

## Location

`~/.claude/skills/video-vision/SKILL.md`

## Invocation

```
/video-vision "Describe the scene you want to create"
```

The user types `/video-vision` followed by their initial concept. The skill takes over from there.

---

## The 6-Phase Pipeline

### Phase 1: VISION

**Tool:** `/superpowers:brainstorming`

**Purpose:** Iterative interrogation across 25 categories until every aspect of the vision is crystal clear.

**Process:**
- The brainstorming skill drives the Q&A, asking one question at a time
- Each category is explored until the answer is complete and unambiguous
- The 25 categories are used as the question framework:

| # | Category | What It Covers |
|---|----------|---------------|
| 1 | **Character** | Face shape, features, expression, skin texture, hair, ethnicity |
| 2 | **Scene & Era** | Time period, architecture style, props, furniture |
| 3 | **Lighting & Mood** | Light source, shadows, contrast, color temperature |
| 4 | **Clothing** | What's worn, coverage %, fabric type, transparency |
| 5 | **Pose & Movement** | Exact body position, limb placement, weight distribution |
| 6 | **Camera** | Angle, distance, height, movement, lens type |
| 7 | **Continuity (BEFORE)** | What happened in the previous segment |
| 8 | **Continuity (AFTER)** | What happens in the next segment |
| 9 | **Physical Constraints** | What should NOT appear, merge, or stretch |
| 10 | **Negative Space** | What must be absent from the frame |
| 11 | **Anatomy Rules** | Specific body part instructions (neck, hands, fingers, lips) |
| 12 | **Era Consistency** | Architecture, furniture, props matching the time period |
| 13 | **Blocking** | Character's path of movement through the space |
| 14 | **Depth Staging** | Foreground / midground / background layers |
| 15 | **Frame Composition** | Rule of thirds, leading lines, framing |
| 16 | **Character's Internal State** | What is she thinking, feeling, mood |
| 17 | **Breathing & Rhythm** | Pace of breath, micro-movements, stillness vs motion |
| 18 | **Time of Day** | Specific hour, how light changes through the scene |
| 19 | **Atmosphere** | Weather outside window, season, air quality |
| 20 | **Film Stock Reference** | Specific film type, grain pattern, lens characteristics |
| 21 | **Texture & Material** | Skin texture, fabric weave, building material feel |
| 22 | **Color Palette** | Specific tones (silver, deep black, warm amber) |
| 23 | **Motion Dynamics** | Speed of movement, stillness vs motion, breathing |
| 24 | **Segment Dependencies** | What the model MUST know about adjacent segments |
| 25 | **Previous Failure Log** | What went wrong in past attempts, what to avoid |

**Output:** `VISION_BRIEF.md` (draft) — a document with all 25 categories answered clearly.

---

### Phase 2: PROMPT CRAFT

**Tool:** `/superpowers:writing-skills`

**Purpose:** Transform the VISION_BRIEF.md into a structured, Production Bible-compliant prompt.

**Process:**
1. Read VISION_BRIEF.md
2. Use writing-skills to craft the prompt following the Production Bible template:
   - `[CHARACTER]` section from categories 1, 16
   - `[CLOTHING]` section from category 4
   - `[SCENE]` section from categories 2, 3, 12, 14, 18, 19, 22
   - `[STATE OF MIND]` section from categories 16, 17
   - `[POSE]` section from categories 5, 6, 13, 15
   - `[ANTI-PERFORMANCE MARKER]` — always present
   - `[QUALITY]` section from categories 20, 21, 22, 23
3. Apply anti-performance markers
4. Include era-consistent details from categories 2, 12, 20
5. Include anatomy/physical constraints from categories 9, 10, 11
6. Include continuity notes from categories 7, 8, 24
7. Include failure prevention notes from category 25
8. Output: **draft prompt** ready for council debate

---

### Phase 3: COUNCIL DEBATE

**Tool:** `/council-orchestration`

**Purpose:** Full 7-agent council debate on the draft prompt. Iterates until Critic and Council are fully satisfied.

**Process:**
1. Load COUNCIL_AGENTS.md (all 7 agents with their domain personas)
2. Run the 3-round debate protocol:
   - **Round 1:** Independent proposals from Thinker A & B
   - **Round 2:** Cross-critique between agents
   - **Round 3:** Convergence to consensus
3. Critic Agent reviews the prompt for:
   - Era consistency (architecture, furniture, props match time period)
   - Anatomy correctness (no stretching, no merging, natural proportions)
   - Continuity logic (transitions between segments make sense)
   - Physics realism (objects don't appear from thin air)
   - Anti-performance compliance (no posing, no acting)
4. **Loopback:** If Critic is not satisfied → revise prompt → re-debate → repeat until Critic says "Approved"
5. Testing Agent validates against known failure modes from Previous Failure Log
6. **Output:** `TEAM_CONSENSUS.md` with the approved prompt

### Phase 5: PONYTAL

**Tool:** `/ponytail-debt` → `/ponytail-review` → `/ponytail-gain`

**Purpose:** Prevent over-engineering and ensure the script is minimal and focused.

**Process:**
1. **ponytail-debt** — Check if the script has unnecessary complexity, speculative features, or bloat
2. **ponytail-review** — Review for YAGNI violations, unnecessary abstractions
3. **ponytail-gain** — Confirm the script is minimal and focused
4. If any check fails → loop back to simplify the script

---

### Phase 6: OUTPUT

**Purpose:** Produce the final deliverable.

**Output:**
- **`VISION_BRIEF.md`** — The complete prompt brief document containing:
  - All 25 categories answered clearly
  - The final approved prompt
  - Council consensus notes
  - Code review results
  - Ponytal audit results
- Saved to `docs/superpowers/specs/YYYY-MM-DD-<scene-name>-vision-brief.md`
- Ready for manual script creation

---

## Skill File Structure

The skill file at `~/.claude/skills/video-vision/SKILL.md` will contain:

```markdown
---
name: video-vision
description: Director-level vision interrogation for AI video generation. Chains brainstorming, writing-skills, council-orchestration, code-review, and ponytail to produce a comprehensive VISION_BRIEF.md.
---

# /video-vision — Director-Level Video Vision Skill

## When to use
Before creating ANY video generation script. Invoke this skill to get a thorough, director-level vision brief that prevents common quality issues.

## How to invoke
```
/video-vision "Describe the scene you want to create"
```

## Pipeline

### Phase 1: VISION
Invoke /superpowers:brainstorming with the 25-category framework.
Iterative Q&A until all categories are clear.
Output: VISION_BRIEF.md

### Phase 2: PROMPT CRAFT
Invoke /superpowers:writing-skills to transform VISION_BRIEF.md into a structured prompt.
Follow the Production Bible template.
Apply anti-performance markers, era details, anatomy constraints.

### Phase 3: COUNCIL DEBATE
Invoke /council-orchestration with the draft prompt.
Run 3-round debate protocol.
Critic reviews: era, anatomy, continuity, physics.
LOOP until Critic says "Approved".
Output: TEAM_CONSENSUS.md

### Phase 4: CODE REVIEW
Invoke /code-review:code-review on the generation script.
Check model loading, parameters, post-processing, error handling.
LOOP until clean.

### Phase 5: PONYTAL
Run ponytail-debt → ponytail-review → ponytail-gain.
LOOP until all pass.

### Phase 6: OUTPUT
Generate VISION_BRIEF.md with all findings.
Save to docs/superpowers/specs/YYYY-MM-DD-<scene-name>-vision-brief.md.
Ready for manual script creation.
```

---

## Integration with Existing Project Files

### CLAUDE.md Update
Add a rule to the project's CLAUDE.md:
```
## /video-vision Skill
Before creating ANY video generation script, invoke /video-vision to produce a vision brief.
The vision brief must be complete before any generation script is written.
```

### Production Bible Update
Add a reference to the /video-vision skill in the Pre-Generation Checklist:
- [ ] Has /video-vision been invoked for this scene?
- [ ] Is VISION_BRIEF.md complete with all 25 categories?

---

## Success Criteria

The skill is successful when:
1. Every video generation is preceded by a complete VISION_BRIEF.md
2. No more "objects from thin air" — physical constraints are explicit
3. No more body part merging — anatomy rules are clear
4. No more era inconsistency — era details are specified
5. Cross-segment transitions are smooth — continuity is planned
6. Face/lips quality is improved — character details are specific
7. The Critic catches issues before generation, not after

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-15 | Council Agents | Created. Full 6-phase pipeline design. |
