# NAD+ IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product nad`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to NAD+.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops:**
- Claims: only ✅ pre-screen lines; ⚠ lines ("boost(s)", "reduces fatigue", "DNA repair", celebrity/CEO/athlete authority) only with
  the user's explicit OK + flagged for Jeremy. Weak lines: avoid.
- **Lead with the choice:** sublingual tablet or injection (one per ad, or both side by side). "Injection" may be named; **no needles,
  syringes, pens, injecting or "needle free"** in words or pictures ("easy sublingual delivery").
- **The tablet is the hero** in sublingual ads: larger than the bottle in frame. Never a strength in copy.
- Offers: the form's own ("Save up to 56% on sublingual tablets" / "Save up to 62% on injections"), "Starting at $119/month", the
  30-day money-back guarantee. Never mix a tablet offer onto an injection ad.
- No disease words, no age-reversal promises, no "Are you/Do you…?" questions, no first person, no named competitors.
- "NAD+" big in every ad; never "by Everlife" on images. Proof exact; disclaimer verbatim (the footer handles both).

**Headline tiers:** Tier A = a ✅ bible headline or benefit · ⚠ lines: explicit OK per line · Tier B (max 2): PROPOSED, Jeremy.

## 1. Product facts for the prompt
- **Product:** NAD+ (`nad`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `nad_bottle.png`, pill: `nad_tablet.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Forms (one per ad; the image question asks which):** **sublingual** = sublingual tablet (bottle `nad_bottle.png`, pill `nad_tablet.png`); **injection** = injection (bottle `nad_vial.png`)
- **Hero:** the NAD+ tablet (sublingual ads) or the NAD+ vial (injection ads), large and in front; the bottle secondary; min width 0.35 of canvas; never: needles, syringes, pens or injecting; 'needle free'; the nasal spray; celebrity look-alikes; another product's bottle, tablet or vial.
- **Cast & mood:** active adults 30–65, bright real rooms; no body-composition or targeted fat-loss claims, no before/after.
- **World translation family for the dealer:** `metabolic` (each world card's `translate.metabolic` line, else `translate.generic`).

## 2. This product's references
| File | Read for |
|---|---|
| `references/product-bible.md` | every claim, headline, CTA, offer |
| `references/winners/winners.md` | reference level 1: our own winners, open first |
| `references/personas.md` | the critique pass per ad |
| `references/lessons.md` | paid-for mistakes; read before writing |
| `references/reviews.md` | any review world (verbatim ✅ reviews only) |
| `assets/RENDERS.md` | what each render is |

Shared: the World Deck `core/references/world-deck/WORLDS.md`, batch-2 contact sheets
`~/Everlife-Creative/references/restora-z-2nd-batch-2026-10-29/_sheets/`, layout zones `core/references/prompt-layout-zones.md`.

## 3. Finishing
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product nad --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/NAD+/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/nad-copy-log.md`;
`deal_worlds.py --product nad --n <N> --log` once approved.
