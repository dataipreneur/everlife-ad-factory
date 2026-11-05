# Spartan Stack IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product spartan`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to Spartan Stack.

## 0. Copy rules (product-specific; kept from the original skill)
**✅ Bible fixed (2026-11-02):** Justin un-swapped the Spartan / Wolverine pages; the bible now matches the vial label (Spartan Stack = BPC-157 / KPV / TB-500). This skill uses its own page (`references/product-bible.md`): benefits and CTAs ✅, headlines ⏳ (only with the user's OK, flagged for Jeremy), no offer yet.

**Hard stops:**
- Claims: only the ✅ quick-hit benefits in `product-bible.md` (pre-screen). ❌/⛔ lines never; ⏳ headlines and ⚠ lines only with the
  user's explicit OK + flagged for Jeremy.
- Spartan Stack is RECOVERY support. No "heal", "repairs", "regenerate", "injury", "pain", "inflammation", "torn", "cure", "treat", "boost",
  "fast"/"faster" as an outcome, no timing promises, no guarantees. "Supports", never "builds". "Supports Connective Tissue Repair"
  only exactly as the bible writes it (where the pre-screen allows it).
- **No needles, syringes, pens, injecting or "needle-free"** in words or pictures. The vial stands or lies on a surface; a hand may hold it.
- One product image: the Rx vial. Copy never states a strength, dose, mL or count; ingredients only together as on the label (BPC-157 + KPV + TB-500 (three peptides)).
- People: active men 25–55, rugged, strong, unmistakably masculine (`mens-direction.md`); fighting imagery fine **without blood or gore,
  no animal death**; no before/after, no body comparison, no body-composition words in copy.
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically" for the product.
- **Offer:** none: the sources disagree (39% / 46% / XX%); Ronnel to confirm. No F6, no "% off".
- "Spartan Stack" big in every ad and **"BPC-157 / TB-500 / KPV" on every design** (bible 2026-11-03, mandatory: supporting copy, a subheadline or an ingredient callout; legible; never overwhelming the headline or vial; 4:5 and 9:16). An ad without the peptide list fails QA. Never "by Everlife" on images.
- Proof wording exact; disclaimer verbatim (the footer handles both).

**Headline tiers:**
- **Tier A (default):** an ✅ quick-hit benefit used as the headline, verbatim or lightly trimmed.
- **⏳ bible headlines:** all four are Pending approval: each needs the user's explicit OK for that exact line, flagged for Jeremy.
- **Tier B (max 2 per batch):** fresh wording whose every claim maps to an ✅ benefit. Mark it **PROPOSED**; explicit OK; Jeremy.
- Never repeat a headline in the copy log. The pool is small: when it runs low, say so and ask for approved headlines.

## 1. Product facts for the prompt
- **Product:** Spartan Stack (`spartan`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `spartan_bottle.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Hero:** the Spartan Stack vial (a still object, label to camera); min width 0.35 of canvas; never: needles, syringes, pens or injecting; capsules or pills; blood, gore or animal death; before/after or body comparison; another product's vial.
- **Cast & mood:** men's slots follow `core/references/hardcore-men.md` (the dealer tags 40% HARDCORE); women's slots pinks, tans, beige. Copy never ties the body to the product.
- **World translation family for the dealer:** `men` (each world card's `translate.men` line, else `translate.generic`).

## 2. This product's references
| File | Read for |
|---|---|
| `references/product-bible.md` | every claim, headline, CTA, offer |
| `references/winners/winners.md` | reference level 1: our own winners, open first |
| `references/personas.md` | the critique pass per ad |
| `references/mens-direction.md` | men's ads |
| `references/lessons.md` | paid-for mistakes; read before writing |
| `references/reviews.md` | any review world (verbatim ✅ reviews only) |
| `assets/RENDERS.md` | what each render is |

Shared: the World Deck `core/references/world-deck/WORLDS.md`, batch-2 contact sheets
`~/Everlife-Creative/references/restora-z-2nd-batch-2026-10-29/_sheets/`, layout zones `core/references/prompt-layout-zones.md`.

## 3. Finishing
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product spartan --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/Spartan Stack/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/spartan-copy-log.md`;
`deal_worlds.py --product spartan --n <N> --log` once approved.
