# Lovara IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product lovara`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to Lovara.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops:**
- Claims: only the ✅ lines in `product-bible.md` (quick-hit benefits, "Feel More Connected", ingredient claims on their OWN
  ingredient). Pre-screen ❌ never; ⚠ only with the user's explicit OK + flagged for Jeremy. Weak headline / Weak benefit → avoid.
- Lovara is women's intimacy support (desire, sensitivity, comfort, responsiveness). No "ED", "erectile", "performance",
  "Viagra", "instant", no timing promises ("tonight", "in 30 min"), no guarantees, no explicit sexual wording, never "Spark".
- Ingredient names appear only inside their own approved claim (F4/F9 rows), never as a product promise; the ingredient list is under
  review (Justin), so prefer product-level "Supports…" lines until it's confirmed.
- **No beds or bedroom scenes**, no lingerie, no body shots, no lips macro, no generic stock-style couples (bible), no before/after. A woman is clothed, candid,
  30–55, shoulder-up or waist-up, daytime (kitchen, café, terrace, garden, studio, bathroom counter), an ordinary non-famous face,
  a different woman in every ad.
- Never a strength, dose or count. No needles, syringes or vials.
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically studied" for the product.
- Offer: only "Save up to 45%" (percent, never a $ price).
- Images: the name "LOVARA" big, never "by Everlife". Proof wording exact; disclaimer verbatim (the finisher adds both).

**Headline tiers:**
- **Tier A (default):** a ✅ bible headline, word for word or lightly trimmed. The pool is small (4): say so up front.
- **Tier B (max 2 per batch):** fresh wording whose every claim maps to a ✅ line. Mark it **PROPOSED**; it needs the user's explicit
  OK for that exact line and goes in SESSION.md as "Tier B, needs Jeremy".
- Never repeat a headline in the copy log; when the pool runs out, ask: reuse least-used with a new layout (the Sermorelin rule), allow
  Tier B, a ⚠ line with the user's OK, or new approved headlines from Jeremy.

## 1. Product facts for the prompt
- **Product:** Lovara (`lovara`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `lovara_bottle.png`, pill: `lovara_capsule.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Hero:** the Lovara capsule (metallic rose-gold, printed LOVARA; the bottle is secondary, large and legible when shown); min width 0.35 of canvas; never: beds or bedroom scenes, lingerie, body shots, lips macro, needles, another product's bottle or pill.
- **Cast & mood:** tasteful, product-led; people clothed, shoulder-up/waist-up, daylight; never a bed or bedroom; no body shots. The dealer filters those worlds out.
- **World translation family for the dealer:** `intimacy` (each world card's `translate.intimacy` line, else `translate.generic`).

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
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product lovara --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/Lovara/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/lovara-copy-log.md`;
`deal_worlds.py --product lovara --n <N> --log` once approved.
