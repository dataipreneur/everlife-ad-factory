# Ultra premium, product only (every product skill)

Mitansh's standing rule (2026-10-29, extended to every product 2026-11-02): **every product skill offers "✨ Ultra premium,
product only" in its image setup.** Picked, it applies to every slot in the batch. This file is the one definition; each skill's
SKILL.md / image-batch.md only adds the option and points here.

## What it is
The Hims / Ro codes in `core/references/static-refs/13_Premium_DTC/README.md`, on every slot:
- ONE sentence-case headline on two short lines, the second line in a tonal variant; at most one small line (or three quiet lines).
  No bullets, icons, tiles, badges, ALL CAPS, italic accent words. Copy still comes only from the product's approved lines.
- The product as an OBJECT on real material (stone, walnut, linen, paper, painted plaster, brushed metal), one hard directional
  light, one long real shadow, confident crop. Never floating, never a mockup, never flat colour (texture and depth always).
- Monochrome harmony: the product's own colour family becomes the field (see "Per product" below). About 60% empty field.
- **Product only, no people.** It overrides the skill's People and Copy density answers (mix headline + small line / +1 line / +3 quiet lines).
- GPT Image 2.5 by default (the skill's image-model rules still apply).

## Staging references (look at ONE per slot; staging only, never the words)
| Product form | Reference |
|---|---|
| Rx vial (BPC-157, GLP-1, NAD+ injection, MOTS-c, Spartan, Wolverine) | `skills/everlife-bpc-157/references/vial-refs/` (V31 monochrome hero, V20 black luxury, V40 / V37 pale editorial; `OVERVIEW.jpg`) or a Hims tile. Read that README's "Compliance traps" list. Its "one vial, always" and slate palette are BPC-157's; GLP-1 may show both vials side by side, each product uses its own colours. |
| Tablet / capsule + bottle (Restora-Z, Sermorelin, Sermorelin GHK, Spark, Lovara, Titan-rx, PT-141 sublingual, NAD+ sublingual) | the Hims tiles: `hims_enjoy-sex_charcoal-pills.png` (pills on a dark field, top-down), `hims_new-hairline_tan-on-walnut.png`, `hims_grid_1/2.jpg` |
| Spray / tube (PT-141 nasal spray) | `hims_testosterone_amber-tube.png` (product colour on product colour) + the grids |

Log the reference used per slot in `prompts.md` and SESSION.md.

## The gates still win (never relaxed by "premium")
- **Tablet products: the tablet is the hero, not the bottle** (gates §3). Tablet large and sharp; a bottle, if shown, large,
  foreground and legible. Tablet prompts use the attached render with the gate wording ("use the attached tablet reference exactly;
  do not invent, alter, or substitute a different pill") and never describe its shape, colour or markings.
- **The product name runs big** and is identifiable in under 2 s: in the headline, or as the second large text. The quiet look
  never makes the name small.
- **Legible for 50+ at story size:** the small line is still ≥ the skill's minimum body size; tonal second lines keep contrast.
- **Women's creative:** GHK-Cu Cream and Glow Stack use pinks, tans and beige (no oranges or greens); other women's runs follow
  the bible's guidance (pinks, tans, warm neutrals, white and teal), and a product's own colour may lead the field when it serves
  the overall look (e.g. NAD+ green, tirzepatide green; Mitansh 2026-11-02).
- Intimate wellness (PT-141, Spark, Lovara, Titan-rx): no bed, bedroom, lingerie; product-led is already the rule.
- No needles, syringes, pens or droppers next to any vial. One form per ad unless the skill allows side by side.
- The footer still adds the Everlife logo, the social proof (Trustpilot rated 4.9 Excellent / 100,000+), the verbatim disclaimer and
  the AI disclosure: the canvas itself stays clean (no logo, stars or badges in the generated image).

## Per product (field colours; women's runs per the women's rule above)
| Product | Monochrome field |
|---|---|
| BPC-157 | slate / charcoal / chalk, or black + slate blue |
| GLP-1 | navy on navy (compounded semaglutide), deep green on green (compounded tirzepatide), or both on pale stone |
| NAD+ | the product's green, or charcoal with the green as the one colour |
| MOTS-c, Spartan, Wolverine | the vial label's colour family, or charcoal / concrete with the label as the one colour |
| Restora-Z | navy, lavender, pale sky, cream |
| Sermorelin / Sermorelin GHK | warm stone, chalk, linen; the label's colour as the one accent |
| PT-141 | cyan on cyan, glass-and-white on white, or charcoal with the cyan label as the only colour |
| Spark | black + rose-gold, warm brass on dark stone |
| Lovara | blush, travertine, cream |
| Titan-rx | black on black (matte black stone, gunmetal, brushed steel) with the label's red chevron as the one colour; or chrome capsule on charcoal |

## QA additions (on top of the skill's QA)
60% empty field; one headline, no bullets or badges; the product name big; the hero form correct (tablet hero for tablet
products); real material and one shadow, never floating; women's rule above held. Fail → one automatic re-roll naming the fix.
