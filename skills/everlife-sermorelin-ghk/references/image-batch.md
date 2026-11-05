# Sermorelin GHK IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product sermorelin-ghk`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to Sermorelin GHK.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops:**
- Claims: only approved quick-hit benefits, more approved benefits, or a per-ingredient claim on its OWN ingredient
  (Sermorelin / GHK / L-Citrulline Malate). Pre-screen ❌ lines never; ⚠ lines only with the user's explicit OK + flagged for Jeremy.
- No body composition, fat, "melt/burn/ripped/shred", no "physique transformation", no body before/after (shirtless heroes ARE allowed: 💪 hardcore-men.md).
- "GHK" only (never -Cu / copper peptide); "growth hormone" spelled out; "easy sublingual delivery"; no needles; no "all natural".
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically studied" for the product.
- Offer: only "Save up to 47%" (percent, never a $ price).
- Proof wording exact; disclaimer verbatim (the footer handles both).

> 🔥 **Boldness question (Mitansh 2026-11-02)** sets the Tier B count; Claude writes the new lines itself (hardcore voice, see SKILL.md step 1 Q4).
> ⚠ **PENDING CREATIVE-LEAD CONFIRMATION**: headline rule changed 2026-10-28 at Priestley's request (original in
> `_originals/2026-10-28/`), to match the global gate (CLAUDE.md ranks above skills: headlines only from the bible/brief,
> new hooks need explicit approval). Remove this note once the creative lead and Jeremy confirm, or revert if they don't.

**Headline tiers:**
- **Tier A (default):** a headline from the chosen audience page or its headline bank, word for word or lightly trimmed;
  never a "Weak headline", "Hard NO conflict" or pre-screen ⚠ line (e.g. "Forge a Stronger Physique", "Lean. Defined. Glowing.").
- **Tier B (how many = the 🔥 boldness answer in SKILL.md step 1: Safe 0 · Balanced 1 · Bold 2 · All-in every slot; default Bold):** fresh wording whose every claim maps to an approved claim, **or** a winner's headline
  that isn't in the bible (e.g. "Support your strongest era", "Lean. Strong. Ready."). Mark it **PROPOSED**; it needs the
  user's explicit OK for that exact line (not the batch click) and goes in SESSION.md as "Tier B, needs Jeremy".
- **Reuse (Priestley, 2026-10-29: the approved pool is used up):** a bible headline or CTA may be reused across batches,
  least-recently-used first (check the copy log); never twice in one batch; never with the same framework/layout it had
  before. New lines only as Tier B (max 2, approved line by line). Ask Justin for fresh headlines when the pool feels stale.
- Facts: Citrulline is NOT a peptide ("2 peptides + 1", never "3 peptides").

## 1. Product facts for the prompt
- **Product:** Sermorelin GHK (`sermorelin-ghk`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `sghk500_bottle.png`, pill: `sghk_tablet.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Hero:** the sublingual tablet (the bottle is secondary, large and legible when shown); min width 0.35 of canvas; never: needles, bedroom framing, body comparison.
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
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product sermorelin-ghk --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/Sermorelin GHK/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/sermorelin-ghk-copy-log.md`;
`deal_worlds.py --product sermorelin-ghk --n <N> --log` once approved.
