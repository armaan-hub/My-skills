# AI-Live Model — Production Bible v1.0

## Core Philosophy: The Invisible Camera

**Every video in this project follows ONE rule above all others:**

> The subject does not know she is being filmed.
> The camera is invisible. She exists in her own private space.
> No performance. No posing. No acting.

This is not a suggestion. This is the default for every generation unless explicitly overridden by the user.

---

## Part 1: The Three Permanent Standards

### 1.1 Natural State (No Over-Acting)

| ✅ DO | ❌ DO NOT |
|-------|-----------|
| Lost in thought, introspective | Looking at camera |
| Eyes closed, gazing unfocused | Making eye contact with lens |
| Neutral/blank expression | Smiling, grinning, happy |
| Natural micro-movements (breathing, shifting position, adjusting arm) | Choreographed "sexy" moves |
| Organic body language | Posed/staged body positions |
| Calm, slow breathing | Exaggerated expressions |
| She exists in her space | She performs for an audience |
| Documentary/candid feel | Fashion shoot / music video feel |

**Keyword blacklist for ALL prompts:**
`seductive, sensual, smoldering gaze, looking at camera, eye contact, performing, acting, posing, photoshoot, modeling, fashion, confident smile, flirting`

### 1.2 Clothing Standards (95-99% Reveal)

| Level | Description | When to Use |
|-------|-------------|-------------|
| **Default** | 95-99% body visible. Bare minimum covering — a thin strap of fabric, tiny triangle, or thread covering only the groin area. Breasts fully or mostly visible. Hips and legs fully visible. | ALL generations unless told otherwise |
| **Moderate** | Partial covering — small top + bottom. Bikini-equivalent. | Only if user specifies |
| **Fully nude** | 100% visible, no covering. | **NEVER by default.** Only if user explicitly says "fully nude" or "completely nude" |

**Rule:** Default is ALWAYS 95-99% covered (bare minimum). The model generates "nearly nude" by default. But I NEVER output explicit full nudity (genitalia fully visible, no covering at all) unless the user explicitly requests it.

**Prompt language for default:**
- "wearing only a tiny strap of fabric barely covering her"
- "barely-there covering showing almost all of her body"
- "minimum covering, 95% of her body bare and visible"

### 1.3 Dramatic Lighting Standard

| Element | Default |
|---------|---------|
| **Light source** | Single, warm, dim — candle glow, firelight, single window, one lamp |
| **Mood** | Dark, moody, atmospheric, cinematic chiaroscuro |
| **Darkness level** | 60-80% dark. Shadows dominate. Body partially lit by rim/edge light |
| **Reveal** | Light reveals fragments — a shoulder, hip curve, spine, leg — not the whole body at once |
| **Color temperature** | Warm amber (candle/fire ~1850K) or cool moonlight (~4100K) depending on scene |

**Rule:** Never use bright, flat, studio, or multi-point lighting. A single source creates realism and intimacy.

---

## Part 2: Prompt Architecture (Universal Template)

Every prompt must follow this structure. This is the **default template** for ALL video generations.

```
[CHARACTER — simple, natural description]
  beautiful young woman in her early 20s, porcelain skin,
  hourglass figure, long messy dark brown hair

[CLOTHING — default: bare minimum]
  wearing only a small strap of fabric barely covering her

[SCENE — dark, single light source]
  she lies on her side on a [chair/sofa/floor] in a pitch dark room,
  single [candle glow / window light] casting warm light on her body,
  dramatic shadows, rim light on her skin

[STATE OF MIND — CRITICAL: she doesn't know]
  she doesn't know she is being watched,
  her face is calm, expressionless, lost in thought,
  eyes half-closed, gazing into the darkness,
  she breathes slowly, shifts slightly, a natural movement

[ANTI-PERFORMANCE MARKER — must be present]
  no performance, no posing, just existing in her own space

[QUALITY]
  cinematic, natural skin texture, photorealistic,
  shallow depth of field, film grain
```

---

## Part 3: Default Negative Prompt (Every Generation)

Every generation script MUST include this negative prompt as a minimum:

```
smiling, grinning, laughing, happy, cheerful, excited,
posed, modeling, photoshoot, fashion, looking at camera, eye contact,
seductive, sensual, flirting, performing, acting,
bikini, swimsuit, lingerie, high heels,
standing, walking, dancing,
bright, well-lit, sunny, daylight, studio lighting,
cartoon, deformed, blurry, ugly, multiple girls, distorted
```

---

## Part 4: Pre-Generation Checklist

Before writing ANY generation script, verify:

- [ ] **/video-vision check:** Has /video-vision been invoked for this scene? Is VISION_BRIEF.md complete?
- [ ] **Philosophy check:** Does the prompt describe a person existing, or a model performing?
- [ ] **Eye contact check:** Does she look at the camera? If yes, reject.
- [ ] **Smile check:** Is she smiling? If yes, reject.
- [ ] **Clothing check:** Is it default 95-99% bare minimum? If more covered, was it specified?
- [ ] **Nudity check:** Is she fully nude? If yes, was the user's explicit instruction given?
- [ ] **Lighting check:** Single source? Dramatic shadows? Not bright?
- [ ] **Movement check:** Natural/organic, not choreographed?

---

## Part 5: Generation Technical Defaults

| Parameter | Default Value | Notes |
|-----------|---------------|-------|
| Model | Wan2.1 T2V-14B (8-bit quantized) | Best quality for 48GB |
| Frames | 81 (max) | ~5s raw + interpolation |
| Steps | 20 | Quality/time balance |
| Guidance | 5.0 | Standard |
| Teacache | 0.05 | ~2x speedup |
| Resolution | 832×480 | Model native |
| Post-production | 2x frame interpolation → ~10s | Slow-mo enhances candid feel |

---

## Part 6: Enforcement Protocol

### 6.1 Script Writing Phase
Every generation script MUST:
1. Import this production bible as header comment
2. Include the standard negative prompt
3. Include the anti-performance marker in the prompt
4. Be audited against Part 4 checklist

### 6.2 Critic Review Phase
The Critic agent MUST reject any generation that:
- Has the subject smiling
- Has the subject looking at camera
- Has the subject performing/posing
- Has bright/studio lighting
- Has clothing that's "modeling-style" (swimsuits, lingerie poses)
- Shows full nudity without explicit instruction

### 6.3 Prompt Audit
Every prompt must pass the "natural language" test:
> Read the prompt aloud. Does it describe a person in a private moment?
> Or does it describe a model shooting content?
> If the latter, rewrite.

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-08 | Council Agents | Created. Codifies "In Her Own Zone" philosophy, clothing standards, prompt template, enforcement protocol. |

---

*This Production Bible overrides any previous prompt-writing habits. All agents must adhere to it.*
