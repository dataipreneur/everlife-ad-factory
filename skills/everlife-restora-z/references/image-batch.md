# Restora-Z IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product restora-z`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to Restora-Z.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops (never cross):**
- Pain points: ONLY the bible's 12 *Approved pain points*.
- Claims: every claim must map to an *approved claim*: quick-hit benefits, more approved benefits, or a per-ingredient
  claim (only on its own ingredient: Trazodone / Hydroxyzine / Doxepin).
- Every Hard NO (product + global, see `global-rules.md`): no disease or cure words, no "clinically proven", no guarantees,
  no first person, no "Are you/Do you…?" questions, no before/after bodies or faces, no named competitor except Ambien
  (and Ambien only with its real pill photo, which we don't have yet, so **no Ambien in images for now**), no lines flagged
  "Hard NO conflict" (Insomnia Solved, Knock Out Insomnia, The Last Sleep Medication…, Non-Addictive Safe Long-Term).
- Proof wording exact; disclaimer verbatim (the footer handles both).

> ⚠ **PENDING CREATIVE-LEAD CONFIRMATION**: headline rule changed 2026-10-28 at Priestley's request (original in
> `_originals/2026-10-28/`). It replaces the 2026-10-27 "rework freely" rule because the global gate (CLAUDE.md, which ranks
> above skills) says headlines come only from the bible/brief and new hooks need explicit approval. Remove this note once
> the creative lead and Jeremy confirm, or revert if they don't.

**Headline tiers:**
- **Tier A (default):** a bible headline/hook (product page or headline bank) word for word, or lightly trimmed, never a
  line flagged "Hard NO conflict", "Weak headline" or "Pending approval". Lead with "sleep" where it reads naturally.
- **Tier B (max 2 per batch):** fresh wording (wordplay, a twist) whose every claim maps to an approved claim, **or** a
  winner's headline that isn't in the bible. Mark it **PROPOSED** in the batch table; it needs the user's explicit OK for
  that exact line (not the batch click) and goes in SESSION.md as "Tier B, needs Jeremy".
- Never repeat a headline in the copy log. When unused Tier A headlines run low, say so and ask whether to allow more
  Tier B or request new approved headlines from Jeremy.

## 1. Product facts for the prompt
- **Product:** Restora-Z (`restora-z`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `rz_bottle.png`, pill: `rz_capsule.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Hero:** the Restora-Z capsule (the bottle is secondary and must be large and legible when shown); min width 0.35 of canvas; never: glass orbs or icons instead of the real tablets, a broken product name.
- **Cast & mood:** real people 45–65, warm sun-lit candid rooms.
- **World translation family for the dealer:** `generic` (each world card's `translate.generic` line, else `translate.generic`).

## 2. This product's references
| File | Read for |
|---|---|
| `references/product-bible.md` | every claim, headline, CTA, offer |
| `references/lessons.md` | paid-for mistakes; read before writing |
| `references/reviews.md` | any review world (verbatim ✅ reviews only) |

Shared: the World Deck `core/references/world-deck/WORLDS.md`, batch-2 contact sheets
`~/Everlife-Creative/references/restora-z-2nd-batch-2026-10-29/_sheets/`, layout zones `core/references/prompt-layout-zones.md`.

## 3. Finishing
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product restora-z --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/Restora-Z/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/restora-z-copy-log.md`;
`deal_worlds.py --product restora-z --n <N> --log` once approved.
