# Baseline Test: Business Card Design (Without Skill)

## Scenario
Ask a fresh agent to design a professional business card. Observe output quality, dimensions, layout, typography, and print readiness.

## Test Prompt
```
Design a professional business card for Ahmed Al Mansouri, Managing Director of Royal Concept General Trading LLC. 
Include: phone +971 50 123 4567, email ahmed@royalconcept.ae, 
website www.royalconcept.ae, address Dubai, UAE.

Output as SVG code that I can save and print.
```

## Baseline Result — WITHOUT skill
Agent produced: 1060×610px SVG at `/Users/armaan/ahmed-card.svg`

### What Worked
- Professional color palette (navy + gold) — fitting for Gulf corporate
- Good typography pairing (Georgia + Helvetica Neue)
- Clear visual hierarchy (Name 40px > Company 24px > Title 16px > Contact 13px)
- Decorative elements (gold left border, RC crest monogram, diamond pattern)
- All requested contact info included

### Failures Identified
- ❌ **Wrong dimensions** — used 1060×610 px instead of 90×54mm
- ❌ **No print specs** — no bleed, no safe zone, no DPI mention
- ❌ **No crop marks** — not ready for production printing
- ❌ **No compliance verification** — no checklist, no contrast ratio check
- ❌ **No design brief** — didn't ask or state defaults for brand preferences
- ❌ **Single layout only** — no alternative styles offered
- ❌ **No back side** — didn't offer dual-sided option

### What The Skill Must Fix
1. Force mm dimensions with proper bleed (96×60mm canvas)
2. Enforce 5mm safe zone from trim
3. Add print specifications (crop marks, DPI, minimum stroke width)
4. Require design checklist verification
5. Provide layout templates for variety
6. Guide design process (ask or state reasonable defaults)

---

# VERIFY GREEN Test: Card Design (WITH Skill)

## Test Prompt (same as baseline)
Designed for Ahmed Al Mansouri, Royal Concept General Trading LLC.

## Result — WITH skill
Agent produced: 96×60mm SVG with proper print specifications

### Compliance Verified
- ✅ 90×54mm card with 3mm bleed (96×60mm canvas)
- ✅ 5mm safe zone — content inside (8,8) to (88,52)
- ✅ Design hierarchy: Name (15pt) > Company (7.5pt) > Title (7.5pt) > Contact (6.5pt)
- ✅ Max 2 typefaces: Georgia + Helvetica Neue
- ✅ Min 6pt body text (contact at 6.5pt)
- ✅ Contrast ratio ≥ 4.5:1 (7.8:1 for gold on navy, >16:1 for white on navy)
- ✅ Compliance checklist included

### Remaining Gaps (REFACTOR targets)
- ❌ No crop marks (added to refactored skill)
- ❌ No minimum stroke width guidance (added to refactored skill)
- ✅ Fixed: bleed canvas approach (now 96×60mm instead of inset)

---

# VERIFY GREEN Re-test: Creative Industry Variant

## Test Prompt
Design for Zara Chen, Creative Director at Nova Design Studio, NYC.

## Result — WITH refactored skill

### All checks passed
- ✅ US dimensions (89×51mm) — correctly adapted for NYC
- ✅ 3mm bleed — 95×57mm canvas
- ✅ 5mm safe zone — content within (8,8) to (87,49)
- ✅ Crop marks at all 4 corners
- ✅ Max 2 typefaces: Playfair Display + Montserrat
- ✅ Min 6pt body text: 6.5pt contact, 6pt location
- ✅ Min 0.5pt stroke: ~1pt separator, ~0.7pt crop marks verified
- ✅ Contrast ≥ 4.5:1: white on dark bg
- ✅ Visual hierarchy: 20pt > 7.5pt > 7pt > 6.5pt
- ✅ Creative industry palette: dark bg + vibrant coral (#ff2d55)
- ✅ Comprehensive compliance checklist (14 items)
- ✅ Generous whitespace, no overcrowding
- ✅ Brand decorations within safe zone
