---
name: visiting-card-designer
description: Use when asked to design, create, or generate a visiting card, business card, or name card — whether SVG, PDF, printable, or digital. Covers print-ready dimensions, typography, layout hierarchy, and color principles for professional card design.
---

# Visiting Card Designer

## Overview

Professional visiting cards follow a tight set of constraints: fixed dimensions, limited space, and print production requirements. This skill gives you the dimensions, layout rules, and design patterns to produce cards that look professional on paper — not just on screen.

## Standard Dimensions

| Standard | Size | Notes |
|----------|------|-------|
| **ISO 7810 ID-1 (Worldwide)** | 90mm × 54mm | Most common; use as default |
| **US/Canada** | 3.5in × 2in (89×51mm) | Slightly smaller; preferred in North America |
| **Japan** | 91mm × 55mm | Slightly larger |

**ALWAYS use mm (millimeters) for print cards.** Pixels are for screen mockups only.

## SVG Template — Print-Ready (With Bleed)

For professional printing, the SVG canvas must be LARGER than the card to allow for bleed:

```svg
<svg xmlns="http://www.w3.org/2000/svg"
     width="96mm" height="60mm" viewBox="0 0 96 60">
  <!-- Canvas = 90+3+3 = 96mm wide, 54+3+3 = 60mm tall
       TRIM (where card is cut):  x=3, y=3, w=90, h=54
       SAFE ZONE (keep content inside): x=8, y=8, w=80, h=44
       BLEED (bg extends to canvas edge so no white after trim)
  -->
  <rect x="0" y="0" width="96" height="60" fill="BACKGROUND_COLOR"/>
  
  <!-- All content stays within safe zone -->
  <g transform="translate(8, 8)">
    <!-- card content here -->
  </g>
</svg>
```

Key points:
- **Canvas is 96×60mm** (= card + 3mm bleed on each side)
- **Trim line** is at `x=3, y=3` (the 90×54mm card area)
- **Safe zone** 5mm from trim = `x=8, y=8, width=80, height=44`
- Background fills the entire canvas so no white edges after trimming
- For US cards: canvas = `95×57mm` (= 89+3+3 × 51+3+3)

## Print Specifications

| Parameter | Value | Why |
|-----------|-------|-----|
| Bleed | 3mm outside trim on all sides (canvas = card + 6mm) | Prevents white edges after trimming |
| Safe zone | Content stays 5mm inside trim line | Content won't be cut by ±1mm trim tolerance |
| DPI reference | 300dpi (1 mm ≈ 11.8 px at 300dpi) | Standard print resolution |
| Color | Use SVG hex for digital; note CMYK for professional print if known |

**Crop / trim marks** (for production printers):

Add at canvas corners to show where to cut:

```svg
<g stroke="#000" stroke-width="0.25" fill="none">
  <!-- Top-left -->
  <line x1="3" y1="0" x2="3" y2="5"/>
  <line x1="0" y1="3" x2="5" y2="3"/>
  <!-- Top-right -->
  <line x1="93" y1="0" x2="93" y2="5"/>
  <line x1="91" y1="3" x2="96" y2="3"/>
  <!-- Bottom-left -->
  <line x1="3" y1="55" x2="3" y2="60"/>
  <line x1="0" y1="57" x2="5" y2="57"/>
  <!-- Bottom-right -->
  <line x1="93" y1="55" x2="93" y2="60"/>
  <line x1="91" y1="57" x2="96" y2="57"/>
</g>
```

**Minimum stroke width:** 0.5pt (0.18mm) for any decorative line. Thinner strokes (0.15, 0.2) often fail to reproduce in print.

## Design Hierarchy (What Goes Where)

```
TOP THIRD        → Company name / Logo (biggest visual weight)
MIDDLE THIRD     → Person's name + Title (largest text)
BOTTOM THIRD     → Contact details (phone, email, website, address)
```

**Hierarchy rules (by font size, use `pt` for consistency):**
1. **Person's name** — largest (14-18pt) — bold, prominent
2. **Company name** — next (8-10pt) or visually weighted via color/bold
3. **Job title** — smaller than name (7-9pt), often uppercase or muted color
4. **Contact info** — smallest but still readable (6-7pt minimum)

**Visual weight formula:**
- Name > Company > Title > Contact
- Use color, weight (bold/medium/light), letter-spacing, and caps to differentiate levels — not just size

## Typography Rules

| Rule | Why |
|------|-----|
| **Max 2 typefaces** | More looks unprofessional |
| **Prefer serif + sans-serif pairing** (e.g., Georgia + Helvetica, Playfair + Lato) | Contrast creates readability |
| **Body text ≥ 6pt for print** | Below 6pt becomes unreadable when printed |
| **Avoid font-weight thinner than 300** | Thin strokes disappear in print |
| **Use `font-family` fallback stacks** | SVG has no font embedding — ensure fallbacks |

**Good pairings:**
- `Georgia, 'Times New Roman', serif` + `'Helvetica Neue', Arial, sans-serif`
- `'Playfair Display', Georgia, serif` + `'Open Sans', Arial, sans-serif`
- `'Montserrat', Arial, sans-serif` (single typeface, weight contrast only)

## Color Principles

| Principle | Guideline |
|-----------|-----------|
| Contrast | Dark text on light background (or light text on dark) — at least 4.5:1 ratio |
| Brand colors | Use company colors if known; otherwise choose an industry-appropriate palette |
| Max colors | 2-3 main colors + 1 accent. More = amateur |
| Accent sparingly | Use accent (gold, bright color) for highlights only — name, logo, separator lines |

**Industry palette suggestions:**

| Industry | Palette | Mood |
|----------|---------|------|
| Corporate/Finance | Navy + White + Gold accent | Trust, stability |
| Creative/Design | Dark bg + vibrant accent + white text | Modern, bold |
| Legal/Consulting | Dark blue/maroon + cream/ivory | Tradition, authority |
| Tech/Startup | White + dark gray + one brand color | Clean, modern |
| Trades/Construction | Dark + high-vis accent + white | Strength, reliability |

## Layout Templates

### Classic (Default)
```
┌──────────────────────────────┐
│  [Logo]     COMPANY NAME     │
│             Job Title        │
│                              │
│  NAME (largest element)      │
│                              │
│  ─── separator ───           │
│  📞 +971 XX XXX XXXX        │
│  ✉ email@company.ae          │
│  🌐 www.company.ae           │
│                              │
│  EST. 2018 · DUBAI · UAE     │
└──────────────────────────────┘
```

### Modern — Minimalist
```
┌──────────────────────────────┐
│                              │
│         NAME                 │
│         Title                │
│                              │
│   COMPANY                    │
│                              │
│   📞 +971 XX XXX XXXX        │
│   ✉ email@company.ae         │
│                              │
└──────────────────────────────┘
```

### Vertical / Portrait
```
┌──────────┐
│  LOGO    │
│          │
│  NAME    │
│  Title   │
│          │
│ COMPANY  │
│          │
│ 📞       │
│ ✉        │
│          │
└──────────┘
```

**Note:** Horizontal layouts are standard for 90% of visiting cards. Use vertical only when the brand identity demands it or for creative industries.

## Back Side Design (Optional)

When asked for a dual-sided card:
- **Front:** Person's info (name, title, company, contact)
- **Back:** Company info (services, map, QR code, social media, or a clean brand pattern)

Keep the back side less dense than the front. A logo + tagline + clean pattern is often enough.

## Design Process (What to Ask Before Designing)

When a user says "design a business card," ask (or make reasonable defaults for):

1. **Dimensions:** 90×54mm (default) or US 3.5×2in?
2. **Industry:** Corporate, creative, trades, tech, legal, other?
3. **Brand colors:** Known or infer from industry
4. **Logo:** Provided or need monogram/initials
5. **Layout:** Classic, modern minimalist, or vertical
6. **Front/back:** Single or dual sided?
7. **Company established year?** (optional, for footer)

If the user provides minimal info (e.g., just name + company), use defaults and note your decisions.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using `px` instead of `mm` in SVG | Use canvas 96×60mm with `mm` units |
| Putting content too close to edges | Stay within 5mm safe zone from each edge |
| Font too small to print | Body text ≥ 6pt |
| Too many fonts | Max 2 typefaces |
| Low contrast text | Check contrast ratio ≥ 4.5:1 |
| No visual hierarchy | Follow TOP → MIDDLE → BOTTOM layout |
| Forgetting contact details | Always include phone + email — these are essential |
| Overcrowding | Less is more — whitespace is professional |
| No bleed margin | Use canvas = card + 6mm (3mm per side) |
| Using device-dependent colors for print | Use safe hex colors or note CMYK conversion |
| Strokes too thin to print | Decorative stroke minimum: **0.5pt (0.18mm)** |
| No crop marks for production | Add corner trim marks at canvas edges |

## Quick Reference Checklist

Before calling a card design complete:
- [ ] Dimensions in **mm** (not px) — canvas is card + 3mm bleed per side
- [ ] Content within **5mm safe zone** from trim line
- [ ] **3mm bleed** — background extends to canvas edge
- [ ] **Crop marks** included for production printing
- [ ] **Max 2 typefaces** used
- [ ] **Minimum 6pt** text size for body
- [ ] **Minimum 0.5pt** stroke width for decorative lines
- [ ] **Contrast ratio ≥ 4.5:1** between text and background
- [ ] **Visual hierarchy** clear (Name > Company > Title > Contact)
- [ ] **All contact info** included and readable
- [ ] File output as SVG (preferred for vector/print) or HTML/CSS (for digital mockup)
