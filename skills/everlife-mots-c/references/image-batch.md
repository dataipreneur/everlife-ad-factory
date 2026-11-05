# MOTS-c IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product mots-c`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to MOTS-c.

## 0. Copy rules (product-specific; kept from the original skill)
**✅ Disclaimer now in the bible (sync 1793728650-5a0d, 2026-11-03):** the bible's MOTS-c page carries the standard ad disclaimer, word for word the text already in product.json (`bible_sync.py --check` ✅). The old "provisional disclaimer: Jeremy to confirm" flag is retired; Jeremy's usual sign-off before anything goes live still applies.

**Hard stops:**
- Claims: only the ✅ lines of the pre-screen (`product-bible.md`, APPROVED UPDATE); ⚠ lines (the glucose lines, "Supports Energy
  Balance", the "upgrade / activated / optimized" headlines) only with the user's explicit OK + flagged for Jeremy; ❌ never.
- MOTS-c is METABOLIC support for energy and endurance. **No weight, fat, body-composition, appetite or "fat and skinny" words or
  images; no body areas; no melt / burn / ripped / shred; no before/after.** No disease words (diabetes, blood sugar control,
  insulin). "Supports", never "boosts / burns / builds". No timing promises, no guarantees.
- **No needles, syringes, pens, injecting or "needle-free"** in words or pictures. The vial is a still object.
- One product image: the Rx vial. Never a strength, dose, mL or count in copy.
- People: active adults 30–55, men and women, in motion or just after; never a physique shot (`direction.md`).
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically" for the product.
- **Offer: "Save up to 40%"** (Creative Messaging doc), exact string; never the lander's "Start MOTS-C — 40% Off", never a $ price.
- "MOTS-C" big in every ad; never "by Everlife" on images. Proof exact; disclaimer verbatim (the footer handles both).

**Headline tiers:** Tier A = the Creative Messaging doc's ✅ headlines, verbatim (prefer the top of its ranking) or an ✅ benefit · ⚠ lines: explicit OK per line, Jeremy · Tier B (max 2): PROPOSED, Jeremy.

## 1. Product facts for the prompt
- **Product:** MOTS-c (`mots-c`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `mots-c_bottle.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Hero:** the MOTS-c vial (a still object, label to camera); min width 0.35 of canvas; never: needles, syringes, pens or injecting; capsules or pills; scales, tape measures, waistlines, bellies or any body-composition cue; before/after or body comparison; another product's vial.
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
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product mots-c --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/MOTS-c/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/mots-c-copy-log.md`;
`deal_worlds.py --product mots-c --n <N> --log` once approved.
