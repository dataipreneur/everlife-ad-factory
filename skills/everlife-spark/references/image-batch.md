# Spark IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product spark`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to Spark.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops:**
- Claims: only approved quick-hit benefits and more approved benefits from `product-bible.md`. Pre-screen ❌ lines never;
  ⏳ Pending-approval and ⚠ lines only with the user's explicit OK + flagged for Jeremy. Weak headline / Weak benefit → avoid.
- Spark is on-demand intimacy support for men and women: PT-141 + Apomorphine + Tadalafil in one sublingual tablet.
  **Never tie a benefit to one ingredient**: name the three together as a combo, or not at all. "ED" only in the bible's ⏳ ED
  headlines with explicit approval; no "erectile", "Viagra", "Cialis", "instant", no timing promises ("tonight", "in minutes"),
  no guarantees. Mechanism first; "supports", never "builds"/"boosts".
- **CTA:** "Save Up to 51%" is the PROVISIONAL default (Jeremy to confirm; "Get Started Now" is banned, bible 2026-11-03); the other bible CTAs are ⏳ and need the user's OK.
- **No beds or bedroom scenes**, no lingerie, no body shots, no couples in bed, no before/after. A person (only when asked) is
  clothed, candid, 30–65, shoulder-up or waist-up, in a daytime setting (kitchen, hallway, terrace, café, car, garden).
- Form: copy may say "sublingual tablet" / "easy sublingual delivery"; never a strength, dose or count. Exactly one tablet.
  No needles, syringes or vials.
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically studied" for the product.
- Offer: only "Save up to 51%" (percent, never a $ price).
- **Name:** "SPARK" big in every ad (one of the two largest texts); never "by Everlife" on images.
- Proof wording exact; disclaimer verbatim (the footer handles both).

> ⚠ **PENDING CREATIVE-LEAD CONFIRMATION**: headline rule changed 2026-10-28 at Priestley's request (original in
> `_originals/2026-10-28/`), to match the global gate (CLAUDE.md ranks above skills: headlines only from the bible/brief,
> new hooks need explicit approval). Remove this note once the creative lead and Jeremy confirm, or revert if they don't.

**Headline tiers:**
- **Tier A (default):** a headline from the bible page or its headline bank, word for word or lightly trimmed;
  never a "Weak headline", "Hard NO conflict" or pre-screen ⚠ line (e.g. "Forge a Stronger Physique", "Lean. Defined. Glowing.").
- **Tier B (max 2 per batch):** fresh wording whose every claim maps to an approved claim, **or** a winner's headline
  that isn't in the bible (e.g. "Support your strongest era", "Lean. Strong. Ready."). Mark it **PROPOSED**; it needs the
  user's explicit OK for that exact line (not the batch click) and goes in SESSION.md as "Tier B, needs Jeremy".
- Never repeat a headline in the copy log. The Tier A pool is small (3 approved headlines + 7 approved benefit lines usable as
  headlines): when it runs low, say so and ask whether to allow more Tier B or request new approved headlines from Jeremy.

## 1. Product facts for the prompt
- **Product:** Spark (`spark`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `spark_bottle.png`, pill: `spark_tablet.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Hero:** the Spark tablet (exactly one, as the render; the black + rose-gold bottle is secondary, large and legible when shown); min width 0.35 of canvas; never: beds or bedroom scenes, lingerie, body shots, lips macro, couples in bed, needles, syringes or vials, a benefit tied to one ingredient, another product's bottle or pill.
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
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product spark --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/Spark/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/spark-copy-log.md`;
`deal_worlds.py --product spark --n <N> --log` once approved.
