---
name: video-vision
description: Director-level vision interrogation for AI video generation. Chains brainstorming, writing-skills, council-orchestration, code-review, and ponytail to produce a comprehensive VISION_BRIEF.md.
---

# /video-vision — Director-Level Video Vision Skill

A custom Claude Code skill that chains multiple superpowers to produce a comprehensive, director-level vision brief for AI video generation. The skill ensures every video concept is fully interrogated across 25 categories before any generation script is written.

## When to Use

Before creating ANY video generation script. Invoke this skill to get a thorough, director-level vision brief that prevents common quality issues:

- ❌ Face/lips quality issues
- ❌ Era inconsistency (modern building in vintage scene)
- ❌ Body part merging (hand, thong, finger merging)
- ❌ Objects generating from thin air
- ❌ Neck/limb stretching unnaturally
- ❌ Cross-segment continuity failures
- ❌ Flat/unrealistic backgrounds

## How to Invoke

```
/video-vision "Describe the scene you want to create"
```

The user types `/video-vision` followed by their initial concept. The skill takes over from there.

---

## The 6-Phase Pipeline

```
PHASE 1: VISION ──────────────────────────────────────
  Uses /superpowers:brainstorming
  Iterative Q&A across 25 categories until clear
  Output: VISION_BRIEF.md (draft)

PHASE 2: PROMPT CRAFT ────────────────────────────────
  Uses /superpowers:writing-skills
  Transforms VISION_BRIEF.md into structured prompt
  Follows Production Bible template

PHASE 3: COUNCIL DEBATE ──────────────────────────────
  Loads COUNCIL_AGENTS.md (all 7 agents)
  3-round debate protocol
  Critic reviews: era, anatomy, continuity, physics
  ❌ Not satisfied → LOOP BACK to revise
  ✅ Only proceeds when ALL pass

PHASE 4: CODE REVIEW ─────────────────────────────────
  Uses /code-review:code-review
  Checks script correctness, parameters, error handling
  ❌ Issues found → loop back to fix

PHASE 5: PONYTAL ────────────────────────────────────
  ponytail-debt → ponytail-review → ponytail-gain
  ❌ Over-engineering found → simplify

PHASE 6: OUTPUT ──────────────────────────────────────
  Generates VISION_BRIEF.md
  Saved to docs/superpowers/specs/
  Ready for manual script creation
```

## The 25 Vision Categories

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

---

## Installation

### Prerequisites
- Claude Code CLI
- Superpowers plugin installed (`superpowers@claude-plugins-official`)
- The following skills available:
  - `/superpowers:brainstorming`
  - `/superpowers:writing-skills`
  - `/code-review:code-review`
  - `/council-orchestration`
  - `/ponytail-debt`
  - `/ponytail-review`
  - `/ponytail-gain`

### Install

```bash
# Clone the skill
git clone https://github.com/armaan-hub/video-vision.git ~/.claude/skills/video-vision
```

### Verify Installation

```bash
ls -la ~/.claude/skills/video-vision/
# Should show: SKILL.md README.md LICENSE docs/
```

Then in any Claude Code session, type:
```
/video-vision "A woman standing by a window in a 1950s apartment"
```

---

## Project Integration

### Add to your project's CLAUDE.md

```markdown
## /video-vision Skill
Before creating ANY video generation script, invoke /video-vision to produce a vision brief.
The vision brief must be complete before any generation script is written.
```

### Add to Production Bible Pre-Generation Checklist

- [ ] Has /video-vision been invoked for this scene?
- [ ] Is VISION_BRIEF.md complete with all 25 categories?

---

## Dependencies

This skill chains the following Claude Code skills (all must be installed):

| Skill | Purpose |
|-------|---------|
| `/superpowers:brainstorming` | Drives the iterative VISION Q&A |
| `/superpowers:writing-skills` | Crafts the structured prompt |
| `/council-orchestration` | Full 7-agent council debate |
| `/code-review:code-review` | Reviews generation script |
| `/ponytail-debt` | Checks for unnecessary complexity |
| `/ponytail-review` | Reviews for YAGNI violations |
| `/ponytail-gain` | Confirms minimal focused script |

---

## License

MIT
