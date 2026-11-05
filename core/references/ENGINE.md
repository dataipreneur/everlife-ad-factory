# The Everlife Ad Engine: what is global, what is per product, what is a variation (2026-11-05)

Mitansh, 2026-11-05: "make everything global and in core … with some exceptional variations like shirtless mode in bodybuilding
products and ultra premium for vials … every other rule should be global! The skills should only load up the product briefs."

```
core/  (GLOBAL: read by every product, edited in one place)
├── claude/everlife-gates.md ........ compliance + standards gates (loaded into every session)
├── references/global-rules.md ...... bible global rules, verbatim extract
├── references/image-flow.md ........ THE image flow: one question → deal worlds → write → both sizes → finish → QA
├── references/world-deck/ .......... 132 worlds (the diversity engine) + WORLDS.md
├── references/prompt-layout-zones.md  STRICT LAYOUT blocks (9:16, 4:5)
├── references/variations/ .......... named exceptions a product opts into (below)
├── scripts/deal_worlds.py .......... the dealer (mix + variety, reads the product's variations)
├── scripts/build_product_briefs.py . regenerates every skill's product-brief.md
├── scripts/skill_lint.py ........... proves every skill has the same shape
└── tools/ .......................... finish_batch.py, safezones.py, standard_footer.py … (rules as code)

skills/everlife-<product>/  (PER PRODUCT: a brief, not a rulebook)
├── product.json .................... facts the tools read: name, renders, forms, hero, disclaimer, variations
├── references/product-brief.md ..... GENERATED: who it's for, creative direction, hard stops, facts, its references
├── references/product-bible.md ..... the bible page extract (claims, headlines, CTAs, offers, Hard NOs, disclaimer)
├── assets/ ......................... renders
├── references/winners|team-refs|lessons|personas ... this product's own learning
└── SKILL.md ........................ thin: route to the engine for images; the video flow (untouched for now)
```

## Variations (`product.json` → `"variations": [...]`)
A variation is a short rule module in `core/references/variations/` (or an existing core file) that changes the default for a
product. Nothing else may override the global flow. Current set:

| id | file | products | what changes |
|---|---|---|---|
| `hardcore-men` | `core/references/hardcore-men.md` | sermorelin, sermorelin-ghk, bpc-157, wolverine, spartan | men's slots lean shirtless / stringer; the dealer tags up to 30% of men's slots HARDCORE (bible 2026-11-04 cap, `hardcore-men.json`); "💪 Hardcore" offered first |
| `vial-product` | `variations/vial-product.md` | bpc-157, wolverine, spartan, mots-c, epithalon, glp-1 | the vial is never thrown / smashed; no needles; **ultra-premium material worlds favoured** |
| `ultra-premium` | `core/references/ultra-premium.md` | every product, as an option; default-on bias for `vial-product` | Hims/Ro object-on-material codes |
| `intimacy-tasteful` | `variations/intimacy-tasteful.md` | pt-141, lovara, spark, titan-rx | no beds / bedrooms / body shots; clothed, shoulder-up; the dealer filters those worlds out |
| `womens-palette` | `variations/womens-palette.md` | ghk-cream, lovara (+ women's slots everywhere) | pinks, tans, beige; no orange, no green |
| `peptide-stack` | `variations/peptide-stack.md` | wolverine, spartan | every peptide named legibly in every ad |
| `two-forms` | `variations/two-forms.md` | pt-141, nad, glp-1 | one form per ad; the image question asks which |
| `compounded-glp1` | `variations/compounded-glp1.md` | glp-1 | "compounded" with every drug name; the price line |

Adding a variation = one file in `variations/` + its id in the products' `product.json` + a row here. Never a banner in a skill.

## How a new bible rule is routed (never into a skill)
- a number (size, zone, split, px) → the tools / `rules` constants; - a claim, CTA, banned word → `global-rules.md` or the
  product's bible extract; - a product-only exception → a variation; - a judgement call → one line in `image-flow.md` §7.
`skill_lint.py` fails when a skill carries a rule banner, a stale number or an expired route.

## What stays per product, on purpose
The brief (who / direction / hard stops), the bible extract, the renders, the product's own winners, team refs, lessons and
personas. These are the references that make the ads good; the engine makes them consistent.
