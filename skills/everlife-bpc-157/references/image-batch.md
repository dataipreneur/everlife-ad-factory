# BPC-157 IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product bpc-157`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to BPC-157.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops:**
- Claims: only the seven quick-hit benefits in `product-bible.md` §5 (+ "Supports tissue repair"). Section 6 is BLOCKED. Pre-screen
  ❌ lines never; ⏳ "Image – Pending approval" headlines and ⚠ glow/skin lines only with the user's explicit OK + flagged for Jeremy.
- BPC-157 is RECOVERY support. No "heal", "repair" (except the approved "Supports Connective Tissue Repair"), "regenerate", "injury",
  "pain", "inflammation", "torn", "cure", "treat", "boost", "fast" as an outcome, no timing promises, no guarantees. "Supports", never "builds".
- **No needles, syringes, pens, injecting or "needle-free"** in words or pictures. The vial stands or lies on a surface; a hand may hold it.
- One product image: the Rx vial. Copy never states a strength, dose, mL or count. No capsules, pills or tablets anywhere (the
  capsule form has no approved image).
- People: MEN = extremely masculine (`mens-direction.md`): bodybuilders / powerlifters 30–45, tattoos, chalk, hard light, shirtless or
  stringer fine; no before/after, no body comparison, no body-composition words in copy. WOMEN = strong and soft, 30–55, pinks, tans, beige;
  never orange or green.
- No "Are you/Do you…?" questions ("Is Your Recovery?" is ❌), no first person, no named competitors, no "clinically" for the product.
- Offer: only "Take up to 40% Off" (percent, never $).
- Proof wording exact; disclaimer verbatim (the footer handles both).

**Headline tiers:**
- **Tier A (default):** a hook from the bible's Men / Women / Unisex lists without a flag, verbatim or lightly trimmed (sentence case
  allowed for the premium look). Audience decides the list.
- **Tier B (max 2 per batch):** fresh wording whose every claim maps to a quick-hit benefit. Mark it **PROPOSED**; needs the user's
  explicit OK for that exact line and goes in SESSION.md as "Tier B, needs Jeremy".
- Never repeat a headline in the copy log. The pool is large (60+ unflagged hooks), so Tier B should rarely be needed.

## 1. Product facts for the prompt
- **Product:** BPC-157 (`bpc-157`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `bpc157_vial.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Hero:** the compounded Rx vial (the only approved image); min width 0.35 of canvas; never: syringe, needle, pen, dropper, droplets, capsules, pills, tablets, a second vial.
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
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product bpc-157 --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/BPC-157/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/bpc-157-copy-log.md`;
`deal_worlds.py --product bpc-157 --n <N> --log` once approved.
