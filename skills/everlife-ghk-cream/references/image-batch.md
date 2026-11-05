# GHK Peptide Cream IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product ghk-cream`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to GHK Peptide Cream.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops:**
- Claims: only the ✅ lines in `product-bible.md` (quick-hit benefits, ✅ headlines and CTAs). Pre-screen ❌ never; ⚠ only with the
  user's explicit OK + flagged for Jeremy. Weak headline → avoid.
- **Name:** "GHK PEPTIDE CREAM" on Meta / Google / TikTok; "GHK-CU CREAM" only on H2 (and then no line that says "GHK Peptide
  Cream"). Never "copper", never "-Cu" on its own, never "GHK-Cu" outside that H2 product name.
- Skin support only, "-looking" where the bible says it. No wrinkles, fine lines, sagging, spots, acne, scars or any skin condition;
  no "anti-aging", "reverse", "erase", "years younger", ages, timelines; no "builds/boosts collagen"; no "clinically"; no treatments or
  competitors (Botox, fillers, retinol, brand names); no body areas, body shape or weight.
- **No before/after, no side-by-side skin, no face close-up "results".** No bodybuilding or "huge" physique (bible Hard NO).
- Never a strength, percentage or size (the label render has none; never add one). No tablets, capsules, droppers, needles, vials.
- No "Are you/Do you…?" questions, no first person, no named competitors.
- Offer: only "Save up to 75%" (percent, never a $ price).
- Images: the name big, never "by Everlife". Proof wording exact; disclaimer verbatim (the finisher adds both).

**Headline tiers:**
- **Tier A (default):** a ✅ bible headline, word for word or lightly trimmed. The pool is small (4 on FB/GL/TK, 3 on H2): say so up front.
- **Tier B (max 2 per batch):** fresh wording whose every claim maps to a ✅ line. Mark it **PROPOSED**; it needs the user's explicit
  OK for that exact line and goes in SESSION.md as "Tier B, needs Jeremy".
- Never repeat a headline in the copy log; when the pool runs out, ask: reuse least-used with a new layout (the Sermorelin rule), allow
  Tier B, a ⚠ line with the user's OK, or new approved headlines from Jeremy.

## 1. Product facts for the prompt
- **Product:** GHK Peptide Cream (`ghk-cream`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `ghk-cream_bottle.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Hero:** the GHK Peptide Cream airless pump bottle (navy label, champagne-gold cap and base; label to camera). There is no tablet or capsule.; min width 0.2 of canvas; never: a strength or percentage on the bottle; another product's bottle, tube or jar; tablets, capsules or pills; needles, syringes, droppers or vials; before/after or side-by-side skin comparison; close-ups of wrinkles, blemishes, scars or any skin condition; bodybuilding or 'huge' physique imagery; body-shape, waist or weight cues; beds or bedroom scenes; orange or green colours.
- **Cast & mood:** women's palette (pinks, tans, beige, cream); no oranges or greens; 'glow' is a mood, never a skin promise.
- **World translation family for the dealer:** `skin` (each world card's `translate.skin` line, else `translate.generic`).

## 2. This product's references
| File | Read for |
|---|---|
| `references/product-bible.md` | every claim, headline, CTA, offer |
| `references/personas.md` | the critique pass per ad |
| `references/lessons.md` | paid-for mistakes; read before writing |
| `references/reviews.md` | any review world (verbatim ✅ reviews only) |
| `assets/RENDERS.md` | what each render is |

Shared: the World Deck `core/references/world-deck/WORLDS.md`, batch-2 contact sheets
`~/Everlife-Creative/references/restora-z-2nd-batch-2026-10-29/_sheets/`, layout zones `core/references/prompt-layout-zones.md`.

## 3. Finishing
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product ghk-cream --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/GHK Peptide Cream/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/ghk-cream-copy-log.md`;
`deal_worlds.py --product ghk-cream --n <N> --log` once approved.
