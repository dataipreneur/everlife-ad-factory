# Titan-Rx IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product titan-rx`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to Titan-Rx.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops:**
- Claims: only ✅ quick-hit benefits and more approved benefits from `product-bible.md`. Pre-screen ❌ lines never;
  ⏳ Pending-approval and ⚠ lines only with the user's explicit OK + flagged for Jeremy. Weak headline / Weak benefit → avoid.
- Titan-Rx is a once-daily 3-in-1 men's performance formula: Tadalafil + Vardenafil + L-Arginine in one oral capsule.
  **Each claim only on its own ingredient** (bible); default: no ingredient claims (all ⚠/❌), the three named together as a fact.
  **Never "arousal"** in any form. "ED" only in the bible's ⏳ ED headlines with Jeremy's written approval; "Erectile…" and "…ED
  Treatment" ❌; no Viagra, Cialis, Levitra or any competitor, no "instant", no timing promises ("tonight", "in minutes"), no
  guarantees. Mechanism first; "supports", never "builds"/"boosts"/"enhances".
- **CTA:** the session's bible CTA ("Ships Free From Pharmacy" by default; never "Get Started Now").
- **No beds or bedroom scenes**, no lingerie, no bare torsos, no flexing, no body shots, no couples in bed, no before/after. A man
  (only when the People answer says so) is the bible's talent: rugged, strong, 40–65, a hardcore-training feel, clothed,
  candid, shoulder-up or waist-up, in a gym, garage, workshop, kitchen or terrace; a different man in every ad.
- Form: copy may say "once-daily" / "daily capsule"; never a strength, dose or count, never "sublingual" or "on-demand". Exactly one
  capsule. No needles, syringes or vials, no other pills.
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically studied" for the product.
- **Offer: none.** "Save up to 49%" is [VERIFY CURRENT] in the bible → no offer, no "% off", no price until verified.
- **Name:** "TITAN-RX" big in every ad (one of the two largest texts), on one line; never "by Everlife" on images.
- Proof wording exact; disclaimer verbatim (the footer handles both).

> ⚠ **PENDING CREATIVE-LEAD CONFIRMATION**: headline rule changed 2026-10-28 at Priestley's request (original in
> `_originals/2026-10-28/`), to match the global gate (CLAUDE.md ranks above skills: headlines only from the bible/brief,
> new hooks need explicit approval). Remove this note once the creative lead and Jeremy confirm, or revert if they don't.

**Headline tiers:**
- **Tier A (default):** a headline from the bible page or its headline bank, word for word or lightly trimmed;
  never a "Weak headline", "Hard NO conflict" or pre-screen ⚠/❌ line (e.g. "Your Key to a Long Lasting Night", "Real Men Take TitanRx").
- **Tier B (max 2 per batch):** fresh wording whose every claim maps to an approved claim, **or** a winner's headline
  that isn't in the bible (e.g. "Strong every day.", "Daily support. Zero planning."). Never a new claim, never "ED". Mark it **PROPOSED**; it needs the
  user's explicit OK for that exact line (not the batch click) and goes in SESSION.md as "Tier B, needs Jeremy".
- Never repeat a headline in the copy log. The Tier A pool is small (4 ✅ headlines + 12 ✅ benefit lines usable as
  headlines): when it runs low, say so and ask whether to allow more Tier B or request new approved headlines from Jeremy.

## 1. Product facts for the prompt
- **Product:** Titan-Rx (`titan-rx`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `titan-rx_bottle.png`, pill: `titan-rx_capsule.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Hero:** the Titan-Rx capsule (exactly one, as the render: chrome, printed TITAN-RX; the matte black bottle is secondary, large and legible when shown); min width 0.35 of canvas; never: beds or bedroom scenes, lingerie, body shots, shirtless or flexing torsos, couples in bed, lips macro, needles, syringes or vials, a benefit tied to the wrong ingredient, another product's bottle or pill, more than one capsule.
- **Cast & mood:** tasteful, product-led; people clothed, shoulder-up/waist-up, daylight; never a bed or bedroom; no body shots. The dealer filters those worlds out.
- **World translation family for the dealer:** `intimacy` (each world card's `translate.intimacy` line, else `translate.generic`).

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
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product titan-rx --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/Titan-Rx/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/titan-rx-copy-log.md`;
`deal_worlds.py --product titan-rx --n <N> --log` once approved.
