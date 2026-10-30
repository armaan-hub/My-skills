# /video-vision — Director-Level Video Vision Skill

A custom Claude Code skill that chains multiple superpowers to produce a comprehensive, director-level vision brief for AI video generation.

## What It Does

`/video-vision` runs a **6-phase pipeline** that interrogates your video concept across 25 director-level categories before any generation script is written:

1. **VISION** — Iterative Q&A across 25 categories until every detail is clear
2. **PROMPT CRAFT** — Transforms the vision into a structured prompt
3. **COUNCIL DEBATE** — Full 7-agent council debate with Critic loopback
4. **CODE REVIEW** — Reviews the generation script for correctness
5. **PONYTAL** — Prevents over-engineering
6. **OUTPUT** — Generates VISION_BRIEF.md

## Problems It Solves

- ❌ Face/lips quality issues
- ❌ Era inconsistency (modern building in vintage scene)
- ❌ Body part merging (hand, thong, finger merging)
- ❌ Objects generating from thin air
- ❌ Neck/limb stretching unnaturally
- ❌ Cross-segment continuity failures
- ❌ Flat/unrealistic backgrounds

## Quick Start

```bash
# Install
git clone https://github.com/armaan-hub/video-vision.git ~/.claude/skills/video-vision

# Use in any Claude Code session
/video-vision "A woman standing by a window in a 1950s apartment"
```

## Repository Structure

```
video-vision/
├── SKILL.md                              # Main skill file (6-phase pipeline)
├── README.md                             # Documentation
├── LICENSE                               # MIT license
├── .gitignore
├── agents/
│   ├── COUNCIL_AGENTS.md                 # Film Production Studio (7 agents)
│   └── COUNCIL_AGENTS_WAN.md             # Technical AI Generation (7 agents)
├── skills/
│   ├── council-orchestration/            # Full council orchestration
│   │   ├── SKILL.md
│   │   ├── program.md
│   │   └── orchestrator.py
│   ├── ai-council-orchestration/         # Multi-model council orchestration
│   │   └── SKILL.md
│   ├── ponytail/                         # Base ponytail (lazy senior dev)
│   │   └── SKILL.md
│   ├── ponytail-debt/                    # Over-engineering debt tracker
│   │   └── SKILL.md
│   ├── ponytail-review/                  # Over-engineering review
│   │   └── SKILL.md
│   ├── ponytail-gain/                    # Ponytail impact scoreboard
│   │   └── SKILL.md
│   └── ponytail-audit/                   # Whole-repo over-engineering audit
│       └── SKILL.md
├── docs/
│   ├── PRODUCTION_BIBLE.md               # Production standards & philosophy
│   ├── STANDARD_SETTINGS.md              # Core generation parameters
│   ├── CAMERA_MOTION_TEMPLATES.md        # Camera motion reference
│   └── superpowers/specs/
│       └── 2026-07-15-video-vision-design.md
└── scripts/
    ├── validate_prompt.sh                 # Pre-generation prompt validation
    └── update_journal.py                  # Project journal updater
```

## Dependencies

| Skill | Purpose |
|-------|---------|
| `/superpowers:brainstorming` | Drives the iterative VISION Q&A |
| `/superpowers:writing-skills` | Crafts the structured prompt |
| `/council-orchestration` | Full 7-agent council debate |
| `/code-review:code-review` | Reviews generation script |
| `/ponytail-debt` | Checks for unnecessary complexity |
| `/ponytail-review` | Reviews for YAGNI violations |
| `/ponytail-gain` | Confirms minimal focused script |

## What's Included

### Agents
- **COUNCIL_AGENTS.md** — Creative Film Production Studio personas (Executive Producer, Cinematography Director, Character Design Director, etc.)
- **COUNCIL_AGENTS_WAN.md** — Technical Wan2.1 AI Generation personas (AI Video Production Director, Cinematography & Prompt Strategy Lead, AI Video Pipeline Analyst, etc.)

### Skills
- **council-orchestration/** — Full autonomous autoresearch loop with 7-agent debate, Keep/Discard protocol, experiment logging
- **ai-council-orchestration/** — Multi-model variant using best model per stage
- **ponytail/** — Lazy senior dev: simplest, shortest, most minimal solutions
- **ponytail-debt/** — Collect deliberate shortcuts into a debt ledger
- **ponytail-review/** — Diff-based over-engineering review
- **ponytail-gain/** — Ponytail impact scoreboard
- **ponytail-audit/** — Whole-repo over-engineering audit

### Documentation
- **PRODUCTION_BIBLE.md** — Core philosophy (Invisible Camera), clothing standards, lighting standards, prompt template, enforcement protocol
- **STANDARD_SETTINGS.md** — Core generation parameters (61 frames, 20 steps, teacache 0.05, etc.)
- **CAMERA_MOTION_TEMPLATES.md** — Camera movement reference (body scan pan, etc.)
- **2026-07-15-video-vision-design.md** — Full design spec for this skill

### Scripts
- **validate_prompt.sh** — Pre-generation prompt validation hook
- **update_journal.py** — Project journal auto-update

## License

MIT
