# Pressure Test: Quick Card Request (With Skill)

## Scenario
User is in a hurry and provides minimal info. Tests whether the agent makes reasonable defaults while still following professional standards.

## Test Prompt
```
Quick — I need a business card. Name: Sarah. Company: TechVista. 
She's a UX Designer. Just give me the SVG.
```

## What to Watch For
- [ ] Uses mm dimensions (not px)
- [ ] Respects 5mm safe zone
- [ ] Follows hierarchy (Name > Title > Company)
- [ ] Max 2 typefaces
- [ ] Makes reasonable design choices for tech industry
- [ ] Doesn't ask unnecessary questions but uses sensible defaults
- [ ] Still provides print-ready output

---

# Pressure Test: Different Industry (Creative Agency)

## Scenario
Creative industry card — tests if agent adapts to industry-appropriate design.

## Test Prompt
```
Design a business card for Zara, Creative Director at "Nova Design Studio" in New York.
Make it look creative and modern.
```

## What to Watch For
- [ ] Appropriate creative-industry palette (dark + vibrant accent)
- [ ] Modern/minimalist layout option offered
- [ ] Still respects mm dimensions and print specs
- [ ] Still follows hierarchy rules
- [ ] Appropriate typography for creative field

---

# Pressure Test: US Dimensions

## Scenario
US-based company — tests if agent correctly uses US card dimensions.

## Test Prompt
```
I need a business card for an American company. 
Name: James Miller, CEO of "Boston Capital Partners."
Boston, MA. Can you make it?
```

## What to Watch For
- [ ] Uses US dimensions (3.5×2in / 89×51mm)
- [ ] Appropriate corporate/finance palette
- [ ] Proper typography for financial industry
- [ ] Respects print specs
