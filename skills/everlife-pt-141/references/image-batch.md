# PT-141 IMAGE ads

**Follow `core/references/image-flow.md`** (the shared golden flow, from the Restora-Z 2nd batch): one question → deal the
worlds (`core/scripts/deal_worlds.py --product pt-141`) → write every ad from its slot → generate **9:16 AND 4:5 in one run** →
`finish_batch.py` (logo, proof per slot, verbatim disclaimer) → QA by looking → show one sheet → log. Rules (claims, zones,
proof split, safe area, disclaimer) live in the gates + `core/references/global-rules.md` + the code; this file holds only
what is specific to PT-141.

## 0. Copy rules (product-specific; kept from the original skill)
**Hard stops:**
- Claims: only approved quick-hit benefits and more approved benefits from `product-bible.md`. Pre-screen ❌ lines never;
  ⏳ Pending-approval and ⚠ lines only with the user's explicit OK + flagged for Jeremy. Weak headline / Weak benefit → avoid.
- PT-141 is DESIRE support (brain-based, non-hormonal, on-demand). No "ED", "erectile", "performance", "Viagra", "instant",
  "ignite", no timing promises ("tonight", "in minutes"), no guarantees. Mechanism first; "supports", never "builds"/"boosts".
- **No beds or bedroom scenes**, no lingerie, no body shots, no couples in bed, no before/after. A person is clothed, candid,
  30–55, shoulder-up or waist-up, in a daytime setting (kitchen, hallway, terrace, café, car, bathroom counter, garden).
- Form: copy may say "nasal spray" / "sublingual tablet" / "easy sublingual delivery"; never a strength, dose or count.
  Never show the tablet with the spray. No needles, syringes or vials; the spray is held, never sprayed on camera.
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically studied" for the product.
- Offer: only "Save up to 23%" (percent, never a $ price).
- Proof wording exact; disclaimer verbatim (the footer handles both).

> ⚠ **PENDING CREATIVE-LEAD CONFIRMATION**: headline rule changed 2026-10-28 at Priestley's request (original in
> `_originals/2026-10-28/`), to match the global gate (CLAUDE.md ranks above skills: headlines only from the bible/brief,
> new hooks need explicit approval). Remove this note once the creative lead and Jeremy confirm, or revert if they don't.

**Headline tiers:**
- **Tier A (default):** a headline from the bible page or its headline bank, word for word or lightly trimmed;
  never a "Weak headline", "Hard NO conflict" or pre-screen ⚠ line.
- **Tier B (max 2 per batch):** fresh wording whose every claim maps to an approved claim, **or** a winner's headline
  that isn't in the bible. Mark it **PROPOSED**; it needs the
  user's explicit OK for that exact line (not the batch click) and goes in SESSION.md as "Tier B, needs Jeremy".
- Never repeat a headline in the copy log. The Tier A pool is small (8 unflagged headlines + 7 approved benefit lines usable as
  headlines): when it runs low, say so and ask whether to allow more Tier B or request new approved headlines from Jeremy.

## 1. Product facts for the prompt
- **Product:** PT-141 (`pt-141`). Product truth for the prompt's first line: `product.json` → `_about` / `hero.element`.
- **Renders to attach (assets/):** bottle: `pt141_spray.png`, pill: `pt141_tablet.png`. Use them exactly; never describe the pill's shape or markings in text.
- **Forms (one per ad; the image question asks which):** **spray** = nasal spray (bottle `pt141_spray.png`); **sublingual** = sublingual tablet (bottle `pt141_sublingual_bottle.png`, pill `pt141_tablet.png`)
- **Hero:** the nasal spray bottle OR the sublingual tablet, whichever form the ad is for (one form per ad); min width 0.35 of canvas; never: the other form in the same ad, needles, beds or bedroom scenes.
- **Cast & mood:** tasteful, product-led; people clothed, shoulder-up/waist-up, daylight; never a bed or bedroom; no body shots. The dealer filters those worlds out.
- **World translation family for the dealer:** `intimacy` (each world card's `translate.intimacy` line, else `translate.generic`).

## 2. This product's references
| File | Read for |
|---|---|
| `references/product-bible.md` | every claim, headline, CTA, offer |
| `references/winners/winners.md` | reference level 1: our own winners, open first |
| `references/team-refs` | the team's own approved statics for this product |
| `references/personas.md` | the critique pass per ad |
| `references/lessons.md` | paid-for mistakes; read before writing |
| `references/reviews.md` | any review world (verbatim ✅ reviews only) |
| `assets/RENDERS.md` | what each render is |

Shared: the World Deck `core/references/world-deck/WORLDS.md`, batch-2 contact sheets
`~/Everlife-Creative/references/restora-z-2nd-batch-2026-10-29/_sheets/`, layout zones `core/references/prompt-layout-zones.md`.

## 3. Finishing
`$T/finish_batch.py <raw> FINAL_<n>_<world>_<WxH>.png --ratio <9:16|4:5> --product pt-141 --proof <slot proof>` for every raw of
every ad, both sizes. Collisions with the proof row → the `free-fix` skill (0 cr) first; else re-roll that size (cost shown).
Output: `~/Everlife-Creative/output/PT-141/<date>_batch-<n>/` with `prompts.md`, `deal.json`, both contact sheets. Post finals to
Ad Review; log waves with `teamlog.py gens --wave`; append headlines to `~/Everlife-Creative/pt-141-copy-log.md`;
`deal_worlds.py --product pt-141 --n <N> --log` once approved.
