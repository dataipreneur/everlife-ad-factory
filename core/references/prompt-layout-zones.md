# ⛔ PROMPT LAYOUT ZONES: the safe-zone rules every image prompt MUST carry (HARD, every product, every skill)

**Mitansh, 2026-11-04:** "Mainly whenever you write prompts for image models, that's when these things are most important!"
This file wins over every LAYOUT line in any skill, recipe, style board or older reference (12% tops, "central 70–76%",
"5% margin", "base at 48%", …). If a skill's own LAYOUT block disagrees with this file, use this file.

Why: the finisher lays the Everlife logo at the top and the proof row + disclaimer at the bottom, AS IS: it never moves, shrinks,
pads, blurs or stretches a raw (all banned). So the raw has to leave those places empty itself. Today's 9:16 prompts asked for
"top 12% empty, central 76%": 5 of 8 raws had the headline under the logo and the width ran past the safe column. The numbers
below are the toolkit's real ones (`core/tools/safezones.py`, `finish_batch.py`) plus the drift the models actually show.

## The facts the zones come from (final canvas)
| | 9:16 (1080×1920) | 4:5 (1080×1350) |
|---|---|---|
| Meta safe area | x 156–924, y 144–1385 | 60 px margin |
| Everlife logo (finisher) | y 150–194, centred, 311 px wide | y 60–104, centred |
| Proof row (trust / count) | ends at y 1385, starts ~y 1280 | bottom ~14%: row + disclaimer, from ~y 1166 |
| Disclaimer | very bottom, y ~1830–1885 | inside the bottom footer |
| Reels profile corner | x 156–375 × y 1216–1385: nothing there | — |
| Reels icons (right side) | x > 924: never text there | — |
| Model drift | text lands up to ~5% off; PRODUCTS land 15–30% LOWER than asked | content lands ~10% lower |

## 9:16 STRICT LAYOUT (paste it into EVERY 9:16 prompt, with these numbers; never paraphrase it shorter)
GPT Image 2.5 renders 9:16 at 1152×2048; percentages hold for any model or size.
```
STRICT LAYOUT (9:16, 1152x2048), follow exactly:
- ZONE A, y 0-330 px (top 16%): EMPTY HEADROOM. Only plain, calm background (name it: <plain wall / open sky / plain paper /
  dark backdrop>). NO text, NO product, NO head, NO card, NO bright light or busy texture. The very first line of text starts
  BELOW y 340.
- ZONE B, y 340-1150 px (16%-56%): ALL text, cards, buttons and the product. The product's lowest point (base, tablet, shadow
  edge) at about y 800 (39%); the CTA button ends above y 950 (46%). <person ads: the head at y 450-700>.
- ZONE C, y 1150-2048 px (56%-100%): ONLY the plain continuing background or surface (floor, table top, fabric, wall), calm and
  low-texture, NO text, NO product, NO hands, NO objects, NO signs.
- WIDTH: every letter, card, button and the product inside x 190-960 px (the central 67%). Nothing important near the side
  edges; nothing at all on the right edge.
- Do NOT draw any logo, wordmark, star rating, Trustpilot row, badge or small print: those are added later.
```
- **No proof row planned (`--proof none`):** ZONE B may run to y 1270 (62%); ZONE C starts there. Everything else is the same.
- **Why the product/CTA asks are so high:** asked at y 900 / 1050, PT-141 batch 15 (2026-11-04) landed the bottle base and CTA at
  ~y 1150-1250, right on the trust row. Products and buttons drift ~15% lower; the asks above already include that. Never relax them.

## 4:5 STRICT LAYOUT (paste it into EVERY 4:5 prompt)
GPT Image 2.5 renders 4:5 (`portrait_5_4`) at 832×1040. Pixel bands alone get ignored on 4:5; the element ORDER is what works.
```
STRICT LAYOUT (4:5, 832x1040), follow exactly:
- TOP 14% (y 0-145 px): EMPTY HEADROOM, plain calm background only. No text, product or head. The first line starts below y 150.
- Elements from top to bottom, in this order: 1 <headline> 2 <supporting lines> 3 <CTA button> 4 the product. The CTA comes
  BEFORE the product; the product is the LAST and LOWEST element, about <30>% of the height tall, its base at about y 660 (63%).
- BOTTOM 33% (y 700-1040 px): only the plain continuing background or surface, calm and low-texture: no text, product,
  hands, objects or signs.
- WIDTH: everything inside x 60-772 px (7% from each side).
- Do NOT draw any logo, wordmark, star rating, Trustpilot row, badge or small print.
```
- **No proof row planned:** the bottom empty band may shrink to 22% (the disclaimer still sits there).

## ⛔ Proof row ↔ layout: plan it BEFORE writing the prompt (Mitansh 2026-11-04, HARD, every batch)
The proof split (~42% trust / ~28% count / ~30% none) is assigned to LAYOUTS, never handed out in order. Today's batch 15 gave the
trust row to two tall-bottle-on-the-right layouts: the bottle was the lowest element, landed on the footer, and both footers had
to be dropped (2 of 8 ads ended with proof).
1. **Proof slots = layouts with a natural shelf:** everything (text, CTA, product, tablet, shadow) ends high, with a clean, flat
   surface below it: a table edge, a counter, a billboard catwalk, a newspaper column end, a card bottom, a plain floor.
   In the prompt, a proof slot asks the product base at y 800 (39%) and the CTA above y 950 (46%) on 9:16 (4:5: product base at
   ~60%, bottom 33% plain) AND names that shelf: "below y 1150 only the plain <table top / floor> continues".
2. **"none" slots = layouts where the product or a person is the lowest element** (tall bottle standing at the bottom, hand-held
   product, person-led, product lying in the foreground, AMA/phone screens running long). Plan them as none up front.
3. **Balance the split across the batch at planning time:** run `finish_batch.py --proof-plan N`, then swap which AD gets which
   proof so each proof lands on a shelf layout. Show the Proof column in the batch table with the shelf named (e.g. "trust ·
   marble table edge"). If the batch has too few shelf layouts for the split, change a layout, don't force the footer onto one.
4. **QA before finishing:** on every proof ad, the lowest product/CTA pixel in the raw must be above y 1150 (9:16) / 80% (4:5).
   Below that = re-roll that size with the asks 10% higher (cost shown), not a dropped footer. Dropping the footer is only for
   rows the user explicitly OKs, and every drop is reported against the split.

## Rules that go with the zones
1. **Every prompt, every model** (GPT Image 2.5, Nano Banana 2.1/Pro, Seedance start frames, resize re-lays, re-rolls, edits).
   Write the STRICT LAYOUT block; never "keep the top calm", "leave room for the logo" or a bare percentage.
2. **Name the surfaces** in ZONE A and ZONE C (the wall, the sky, the table top). Unnamed empty zones get filled with props,
   light beams, signs or texture, which trips the logo check or sits under the footer.
3. **Calm footer ground:** the footer has no haze behind it any more (2026-11-04), so ZONE C / the bottom band must be even and
   low-texture: no marble veins, linen folds, newsprint or bokeh highlights right under the proof row and disclaimer.
4. **Product size and position are numbers**, never "large" alone: "about 30% of the width, base at y 900".
5. **Text sizes stay legible for 50+:** headline ≥ 9% of the height per line, other lines ≥ 3.5%; big type still has to fit the
   column, so cut words before you shrink type.
6. **Before submitting, check the prompt**: ZONE A / B / C (or the 4:5 order) present with numbers, width band present, "no
   logo / stars / small print" present. A prompt without them is not sent.
7. **QA every raw against the zones at full size** before finishing: first text line below the logo band, product and CTA above
   the footer line, nothing outside the width band. A raw that breaks a zone is re-rolled with the block repeated and the
   offending element moved higher by ~10%; or, if only the footer collides, finished with `--proof none` (free, noted in the
   batch's proof split). **Never** fix it with a shift, mirror-fit, pad, stretch, blur or haze.
7b. **AUTO-LIFT Q/A FIX, built into `finish_batch.py` (Mitansh 2026-11-04: "This is where we should be having the headers to
   start with!"):** on EVERY finish (9:16, 4:5, 1:1) the finisher measures the raw's empty headroom and moves the whole ad UP so
   its first content row sits right under the logo band (9:16 y 230, 4:5 y 140). Only empty headroom is cut; the bottom gap gets a
   SHARP mirror of the raw's own plain bottom rows (no blur, no stretch, no pad); it skips itself when that bottom isn't a plain
   surface (then re-roll if the footer collides). The log line "lift: moved the ad up Npx" shows it ran. Nothing to call: every
   skill gets it. `core/tools/lift_916.py` does the same by hand. Still banned: the old down-shift (blurred top), pads, haze.
7c. **Solid dark footer panel (4:5 / 1:1, Mitansh 2026-11-04: "use such darker footer"):** `finish_batch.py --panel dark`
   (or `EVERLIFE_FOOTER_PANEL=dark`) lays the approved green-black footer card (trust row, hairline rule, disclaimer) as an
   OPAQUE panel across the bottom, crisp, not a haze. Use it when the bottom band is busy (billboard posts, texture) and the
   product ends above it. Feed ratios only; 9:16 keeps the open footer in the safe area.
8. If the finisher refuses ("logo spot busy", "content runs to y …"), that is the zone rule catching a bad raw: re-roll, don't
   force it (`--fit force` is for QA previews only).

Source of the proven 9:16 block: Sermorelin GHK hardcore-v3 batch (2026-11-02, 4/4 first try) and its lessons; 4:5 order rule:
Sermorelin GHK hardcore-refs-b2 (2026-11-02). Numbers re-checked against `safezones.py` / `finish_batch.py` 2026-11-04.
