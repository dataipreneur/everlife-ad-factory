# Sermorelin IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product sermorelin`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to Sermorelin.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops:**
- Claims: only the ✅ approved benefits in `product-bible.md` (clean pool). Pre-screen ❌ lines never; ⚠ lines only with
  the user's explicit OK + flagged for Jeremy.
- No body composition, fat, "dad bod", "melt/burn/ripped/shred", no "physique transformation", no body before/after (shirtless
  heroes ARE allowed: 💪 hardcore-men.md), no age-reversal ("the new 40") unless Jeremy clears it.
- "growth hormone" spelled out; never imply the tablet *is* growth hormone; "easy sublingual delivery"; no needles,
  injections or vials; no "all natural"; never "GHK", "Citrulline" or "3-in-1" (that's the other product).
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically studied" for the product, no
  "Breaking News".
- Offer: only "Save up to 65%" (percent, never a $ price unless the brief is a price test; never "vs HGH" without Jeremy).
- Proof wording exact; disclaimer verbatim (the footer handles both).

**Headline tiers:**
- **Tier A (default):** a headline from the chosen audience page's clean pool (`product-bible.md`), word for word or
  lightly trimmed. Never a "Weak headline", "Hard NO conflict" or pre-screen ❌/⚠ line.
- **Tier B (max 2 per batch):** fresh wording whose every claim maps to a ✅ benefit. Mark it **PROPOSED**; it needs the
  user's explicit OK for that exact line (not the batch click) and goes in SESSION.md as "Tier B, needs Jeremy".
- Never repeat a headline in the copy log. **The Tier A pool is very small** (3 men's, 4 women's): say so up front and ask
  whether to allow Tier B, use a ⚠ line with the user's OK, or request new approved headlines from Jeremy.

## 1. Product facts for the prompt
- **Product:** Sermorelin (`sermorelin`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `sermorelin1000_bottle.png`, pill: `sermorelin_tablet.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Cast & mood:** men's slots follow `core/references/hardcore-men.md` (the dealer tags 40% HARDCORE); women's slots pinks, tans, beige. Copy never ties the body to the product.
- **World translation family for the dealer:** `men` (each world card's `translate.men` line, else `translate.generic`).

## 2. This product's references
| File | Read for |
|---|---|
| `references/product-bible.md` | every claim, headline, CTA, offer |
| `references/winners/winners.md` | reference level 1: our own winners, open first |
| `references/pinterest` | category references (layout + idea only) |
| `references/lessons.md` | paid-for mistakes; read before writing |
| `references/reviews.md` | any review world (verbatim ✅ reviews only) |

Shared: the World Deck `core/references/world-deck/WORLDS.md`, batch-2 contact sheets
`~/Everlife-Creative/references/restora-z-2nd-batch-2026-10-29/_sheets/`, layout zones `core/references/prompt-layout-zones.md`.

## 3. Finishing
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product sermorelin --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/Sermorelin/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/sermorelin-copy-log.md`;
`deal_worlds.py --product sermorelin --n <N> --log` once approved.
