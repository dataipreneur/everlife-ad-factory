# GHK Peptide Cream IMAGE ads: Batch Mode (the default for every image request)

> **⛔ NEVER `reposition_916.py`, edge-stretch, blur or padding colour on a raw (Mitansh, 2026-11-02: "why the hell are these things blurry on the edges! Who told you to do that!").** This overrides every older line in this skill that calls `reposition_916.py` "the fix". Finish the raw AS IS: `finish_batch.py <raw> <out> --ratio 9:16 --product <id> --fit trusted --shift 0`. **If its text or product runs into the footer, ALWAYS fix it in code first (Mitansh, 2026-11-02: "make sure to do it always"):** `$T/venv/bin/python -I $T/mirror_fit_916.py <raw> repo/rN.png --top <content top> --bottom <content bottom>` (0 credits: uniform scale into the band 0.115–0.635, margins filled by mirror-tiling a thin text-free edge strip), then the finisher as above on `repo/rN.png`. LOOK at the result. Re-roll (cost approved) ONLY when a person, text or the product touches a side edge of the raw (the mirror would copy it) or the tool refuses (scale < 0.65). Never ship a smeared edge.
> **👀 SHOW FIRST, THEN RE-ROLL (Mitansh, 2026-11-02: "show me first!"):** after a batch, finish what can be finished (as-is or `mirror_fit_916.py`), open the contact sheet and SHOW the user every result (finished + the raws that failed QA, with why). Never start a re-roll on your own QA call, not even the "one automatic re-roll" older lines mention: the user decides which ads to re-roll, with the cost shown.

Same machine as the other product batches (creative lead, 2026-10-27: "speed, Creatify, batches of different types, mobile
friendly, easy to read for older people"). GPT Image 2.5 on Creatify designs the **whole ad** with the real bottle render;
`finish_batch.py` adds the Everlife logo at the TOP and the approved proof footer (Trustpilot 4.9 / Doctor Prescribed / Ships Free
art) plus the verbatim (PROVISIONAL, Jeremy to confirm) disclaimer.

**🎯 FOCAL-POINT MIX (bible Standards 03, synced 2026-11-03; REPLACES "the pill is the hero, not the bottle" everywhere in this skill):** plan it in the batch table's **Focal** column before writing prompts, like the proof split: this product has no pill, so (Justin, 2026-11-03: "For non pill products the vial should be 75%") it is **75% product-focused** (the airless pump is the primary focal point: foreground, sharp, premium product photography) · **25% person-focused** (a person is the primary focal point; the airless pump still in focus and identifiable). Batch of 4 = 3 / 1. **Videos use the same split** (Justin, 2026-11-03: "Videos and statics should really be the same in the sense of how we’re presenting products"). Every ad, whatever its focus: product and benefit identifiable in under 2 s, product in focus, nothing covering it (`core/references/creative-system.md` §1).

**Proof split (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of ads carry NO proof element; 70% carry a footer proof: of those, 60% the trust row and 40% the Trustpilot 4.9 badge + "Over 100,000 happy customers" (overall ~42% trust / ~28% count / ~30% none; logo + verbatim disclaimer on every ad). Run `finish_batch.py --proof-plan N`, add a **Proof** column to the batch table, and pass it on every finish (`--proof trust` / `--proof count` / `--proof none`, same value on the ad's 4:5 and 9:16), e.g. `finish_batch.py raw.png FINAL.png --ratio 4:5 --product ghk-cream --proof count`. Rule: `core/references/creative-system.md` §2. **PROOF SPLIT IS HARD (Mitansh 2026-11-02, no conflicts):** ~42/28/30 per batch and per ratio; proof slots get a clean shelf in the LAYOUT (9:16: product, CTA, sticker, faces end above y 1150 of 1920); never swap a planned proof to "none" yourself (re-roll with cost or ask); `finish_batch.py --proof-check <batch folder>` must pass before showing.

Render: `assets/RENDERS.md` (the airless pump bottle; there is no tablet). The Creatify project goes in `assets/creatify.json`
(create it once, with the user's OK).

**Batch size: default 4** (Creatify runs 4 image tasks per project at once; 8 and 12 run in waves of 4).
**Finishing (shared rules, Mitansh 2026-10-29):** 4:5 is the master; 9:16 is made from the approved 4:5 with `compose916.py`, or a
9:16 raw is finished as is with `finish_batch.py --ratio 9:16 --product ghk-cream --fit trusted --shift 0` after `reposition_916.py`
when anything dips into the footer. Never buy a reposition edit. The 9:16 proof row stays in the Reels safe area and the disclaimer
sits at the very bottom (`"disclaimer_at": "bottom"`).

## 0. Copy rules: hard stops vs references
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

## 1. Frameworks (reference ads: priority `core/references/REFERENCE-PRIORITY.md`; shared library `core/references/static-refs/<folder>/`)
| Code | Framework | Folder | GHK cream recipe |
|---|---|---|---|
| F1 | Old way vs New way | 01_Us_vs_Them | "A ten-step shelf" vs "One peptide step". Ideas only: no brands, no faces, no skin comparison |
| F2 | Bold Claim | 02_Bold_Claim | one huge Tier A headline ("Firmer-Looking Skin Starts With Support") + the bottle hero + up to 3 ✅ callouts |
| F3 | Phone UI | 03_iPhone_Notes_Phone_UI | a Notes page "morning routine" with one ✅ line per row; the bottle beside the phone |
| F4 | Features & Benefits | 04_Features_and_Benefits | bottle hero + three rows of ✅ benefits with simple line icons |
| F5 | Before/After | 05_Before_and_After | ❌ **skip** (global Hard NO) |
| F6 | Offer | 06_Offer | "Save up to 75%" + product + one ✅ benefit line |
| F7 | Review card | 07_Testimonial_Social_Proof | ❌ blocked until `reviews.md` has screened GHK cream reviews |
| F8 | Question | 08_Question | pronoun-free question ("One step worth keeping?" only as Tier B, PROPOSED) + answer line + product |
| F9 | Reasons Why | 09_Reasons_Why_Education | "The peptide step, explained": three ✅ lines, numbered, bottle hero; advertorial on white |
| F10 | Sticky Note | 10_Sticky_Notes_To_Do | a note on a bathroom mirror or planner next to the bottle, one ✅ line |
| F11 | Visual Metaphor | 11_EXTRA_Visual_Metaphor | one object idea: a silk ribbon pulled taut, a smoothed linen sheet on a table, morning light across a beige wall |
| F12 | Brand Mood | 12_EXTRA_Brand_Mood_Product_Hero | premium still life (travertine, blush plaster, beige linen, warm stone), short serif line |
| F13 | Portrait + line | (people) | one candid woman 30–55, shoulder-up, fresh-faced in morning light; headline beside her; product in the lower third |

**Random (recommended):** N different frameworks (skip F5, F7), mixing text-heavy (F1, F3, F4, F9) and visual (F2, F8, F10–F13).
Default **product-only** (`lessons.md`: Mitansh's premium-DTC direction). People (F13, or a woman inside F2/F8/F12) only when the user
asks, tested in 2–3 shots first.

## 1b. Creative-system pass (shared, `core/references/creative-system.md`)
A different **structure** per slot, at least one **article-style** slot per 5 (on white), a different **product angle**, a **named
typeface**, an **own palette**, rotating **product-name treatment** and **headline placement**; the hero (`product.json → hero`) large
and real, label wrapped and legible (the slim pump: upright ≥ 20% of the width and ≥ 45% of the height, or on its side ≥ 35% wide),
with `hero.never` written into the prompt; the CTA and every line as exact strings (then QA'd); "NO logo or wordmark anywhere"
(the finisher adds the real one).

**Team logs (every batch, `core/team-logs/TEAM-LOGS.md`):** before writing copy, read this product's Copy Ledger rows (never reuse a logged headline, hook or CTA), the team's recent styles (`pick_styles.py --skip`) and proof split; log each generation to the Prompt & Outcome Log (inputs, exact prompt, refs, QA result); after the batch, log copy, styles, proofs and the run's spend. Unreachable → the pending file, never block.

**Winners Board (⏸ PAUSED 2026-11-03 (Priestley): SKIP this step: do not read the board, use no board winner or rating; see `WINNERS-BOARD.md` top) (read first, `core/winners-board/WINNERS-BOARD.md` §4):** before the batch table, read this product's image
entries on the shared board: one slot mutates a board winner (exactly one variable), retired recipes are skipped, and the
table opens with the board line (`Board: last 15 … · median …`). Board unreachable → "no history yet", say so, carry on.

## 2. Flow (setup lives in SKILL.md step 1; here: write, critique, approve, generate)
1. Inputs from SKILL.md step 1: channel, hook angle, boldness, mood, copy density, image model, how many.
2. Read the bible + copy log. Per slot: pick a framework, **look at 1 reference ad** in priority order (layout only, never the words or
   the scene), write concept (1 line), headline, supporting lines (approved, exact), the woman's casting when there is one (age,
   ethnicity, hair, wardrobe: different every ad), palette, prompt.
   **Persona pass** (`personas.md`), then ONE table: # · framework · person? · headline · tier · supporting lines · type & colour ·
   ≈1 credit. AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". **That click approves the batch
   and its Tier A lines; each Tier B or ⚠ line needs its own explicit OK first.**
3. Generate: `composer_edit_image(project_id, prompt, images=[bottle_ref], out='gen/b<date>_<n>.png', aspect_ratio="4:5")`
   for the default model (`assets/ghk-cream_bottle_ref.jpg`, flattened on white); Nano Banana → `core/references/image-models.md`.
   Max 4 in flight.
4. QA every result (Read it), strictly: text EXACTLY the approved strings; the name big and no "by Everlife", no "copper"; the bottle
   label matches the render (EVERLIFE / GHK / Peptide Cream / RX ONLY / 30G; no invented strength; not garbled, not mirrored); one
   bottle, no tablet or other product; every line big enough for 50+; the woman looks 30–55, candid, an ordinary face (no celebrity
   likeness), lean and fit at most, different from every other ad; **no before/after, no skin-condition close-up, no orange or green**;
   colours from §2b; nothing breaks a Hard NO. Fail → one automatic fix (an edit of the raw naming the fix). Still bad → flag, don't ship.
5. Finish: `$T/venv/bin/python -I $T/finish_batch.py gen.png FINAL_<n>_<framework>.png --ratio 4:5 --product ghk-cream`.
6. Save to `~/Everlife-Creative/output/GHK-Cu-Cream/<date>_batch-<n>/` (FINALs + `prompts.md` + `contact_sheet.jpg`), open the
   contact sheet, log the headlines, offer "Another batch?" / "Variations of #k" / "9:16 of the winners".

## 2b. Type & colour: different every time
Every ad gets its own pairing and accent; never two alike in a batch.

| Headline face (pick one) | Partner for supporting text |
|---|---|
| Elegant high-contrast serif, roman | clean geometric sans |
| Serif with ONE italic word | small-caps sans |
| Wide extended sans | regular sans |
| Chunky rounded sans | mono-spaced labels |
| Brush / handwritten accent word inside a sans headline | regular sans |
| Thin editorial sans, tracked out, all caps (regular weight, never hairline) | serif body |

**Colours (bible, binding for this product): pinks, tans and beige. No oranges or greens.** Lead colours to rotate: blush pink,
dusty rose, nude/tan, sand, beige, warm cream, travertine, soft white (advertorials on white). The bottle's navy and champagne gold
are the one dark contrast and may set the accent (navy type, a champagne-gold rule). Never teal-led, orange, terracotta, peach-orange,
coral, sage, olive or any green (plants and leaves included). No two ads with the same lead colour; vary placement and light.

## 3. Prompt template (fill everything; keep the quotes exact)
```
Design a finished, premium static social ad for "<NAME: GHK Peptide Cream | GHK-Cu Cream on H2>", a doctor-prescribed topical peptide skin cream in an airless pump bottle, in the style of a modern, premium DTC women's skincare brand. Framework: <name>: <layout from the reference ad>.

PRODUCT: image 1 is the real product. Use the attached bottle reference exactly: same shape, colours and label, label facing camera,
sharp, never mirrored, never redesigned; the label wraps around the slim cylinder and follows its angle. It is a slim airless pump
bottle with a polished champagne-gold cap and base and a deep navy label reading 'EVERLIFE', 'GHK', 'Peptide Cream', 'RX ONLY', '30G'
in white and gold. Do not add any percentage, strength or other text to the label. Show ONLY this one bottle: no tablets, capsules,
jars, tubes, droppers or any other product. The bottle is large, in focus and foreground: <upright, at least 45% of the canvas height |
lying on its side, at least 35% of the canvas width>. ARRANGEMENT for this ad: <its own arrangement>.

TYPOGRAPHY & COLOUR (this ad's own look): headline in <pairing from §2b>, with ONE phrase picked out in <accent colour>; supporting text
in <partner face>. For readers aged 50+: headline at least 9% of canvas height per line; every other line at least 3.5%; strong
contrast; no thin grey text; no shadows or outlines on type.

TEXT: render ONLY these strings, exactly, nothing else (no extra words, no Everlife or other logos or wordmarks, no 'by Everlife', no
stars, badges, prices, website or disclaimer):
  Name: "<GHK PEPTIDE CREAM | GHK-CU CREAM>"   (big and bold: one of the two largest texts in the ad, on one line or two, never hyphen-broken)
  Headline: "<headline>"   (accent on: "<phrase>")
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"

SCENE & STYLE: <scene: a sunlit bathroom counter, vanity, dressing table, kitchen window, studio set>, real texture and
depth (never a flat colour), soft natural morning light, calm, warm and premium. <PERSON, if any: a <ethnicity> woman, age <30–55>,
<hair>, <wardrobe>, lean and naturally fit (never muscular or bodybuilder), fresh-faced with natural skin texture, candid (laughing,
calm or eyes to camera), framed head-and-shoulders, an ordinary, non-famous face (must not resemble any celebrity, actor or public
figure); not posed as a model, not glamour.> Palette: <this ad's own lead colour per §2b>: pinks, tans and beige only, NO orange and
NO green anywhere (no plants, leaves, citrus or green fabric). No before/after, no split-face or side-by-side skin, no close-ups of
wrinkles, blemishes or skin problems, no muscular physique, no needles, syringes, droppers or vials, no bed or bedroom.

LAYOUT (4:5): 5% clear margin on every edge. The TOP 14% is calm continuation of the background (no text, no product): the Everlife
logo is laid there later. The BOTTOM 22% is calm continuation of the background (no text, product or hands): the proof footer is laid
there later. The whole product (bottle, hands) ends ABOVE 66% of the canvas height and all text above 72% (ask high: the image
model places things lower than asked).
```
Never show the cream itself as a swatch, smear or dab until the team confirms what it looks like (colour and texture are not on
file); the bottle carries the product.

## 4. After the batch
- Contact sheet first, then let the user pick winners. Winners → 9:16 only after approval (compose916.py from the 4:5).
- **Rate the batch (⏸ PAUSED 2026-11-03 (Priestley): SKIP this step: no rating question, no board entry, no preview upload) (Winners Board, `core/winners-board/WINNERS-BOARD.md` §5):** after the contact sheet, one AskUserQuestion
  question per ad (Winner / Good / Weak / Kill, max 4 per screen), then write every rated ad with its recipe to the shared
  board in one `ArtifactData` batch. Board unreachable → the pending file (§7), and say so.
