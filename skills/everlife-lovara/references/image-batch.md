# Lovara IMAGE ads: Batch Mode (the default for every image request)

> **⛔ NEVER `reposition_916.py`, edge-stretch, blur or padding colour on a raw (Mitansh, 2026-11-02: "why the hell are these things blurry on the edges! Who told you to do that!").** This overrides every older line in this skill that calls `reposition_916.py` "the fix". Finish the raw AS IS: `finish_batch.py <raw> <out> --ratio 9:16 --product <id> --fit trusted --shift 0`. **If its text or product runs into the footer, ALWAYS fix it in code first (Mitansh, 2026-11-02: "make sure to do it always"):** `$T/venv/bin/python -I $T/mirror_fit_916.py <raw> repo/rN.png --top <content top> --bottom <content bottom>` (0 credits: uniform scale into the band 0.115–0.635, margins filled by mirror-tiling a thin text-free edge strip), then the finisher as above on `repo/rN.png`. LOOK at the result. Re-roll (cost approved) ONLY when a person, text or the product touches a side edge of the raw (the mirror would copy it) or the tool refuses (scale < 0.65). Never ship a smeared edge.
> **👀 SHOW FIRST, THEN RE-ROLL (Mitansh, 2026-11-02: "show me first!"):** after a batch, finish what can be finished (as-is or `mirror_fit_916.py`), open the contact sheet and SHOW the user every result (finished + the raws that failed QA, with why). Never start a re-roll on your own QA call, not even the "one automatic re-roll" older lines mention: the user decides which ads to re-roll, with the cost shown.

Same machine as the other product batches (creative lead, 2026-10-27: "speed, Creatify, batches of different types, mobile
friendly, easy to read for older people"). GPT Image 2.5 on Creatify designs the **whole ad** with the real bottle and capsule
renders; `finish_batch.py` adds the Everlife logo at the TOP and the approved proof footer (Trustpilot 4.9 / Doctor Prescribed /
Ships Free art) plus the verbatim disclaimer.

**Proof split (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of ads carry NO proof element; 70% carry a footer proof: of those, 60% the trust row and 40% the Trustpilot 4.9 badge + "Over 100,000 happy customers" (overall ~42% trust / ~28% count / ~30% none; logo + verbatim disclaimer on every ad). Run `finish_batch.py --proof-plan N`, add a **Proof** column to the batch table, and pass it on every finish (`--proof trust` / `--proof count` / `--proof none`, same value on the ad's 4:5 and 9:16), e.g. `finish_batch.py raw.png FINAL.png --ratio 4:5 --product lovara --proof count`. Rule: `core/references/creative-system.md` §2. **PROOF SPLIT IS HARD (Mitansh 2026-11-02, no conflicts):** ~42/28/30 per batch and per ratio; proof slots get a clean shelf in the LAYOUT (9:16: product, CTA, sticker, faces end above y 1150 of 1920); never swap a planned proof to "none" yourself (re-roll with cost or ask); `finish_batch.py --proof-check <batch folder>` must pass before showing.

Renders: `assets/RENDERS.md` (bottle + capsule). The Creatify project is in `assets/creatify.json`.

**Batch size: default 4** (Creatify runs 4 image tasks per project at once; 8 and 12 run in waves of 4).
**Finishing (shared rules, Mitansh 2026-10-29):** 4:5 is the master; 9:16 is made from the approved 4:5 with `compose916.py`, or a
9:16 raw is finished as is with `finish_batch.py --ratio 9:16 --product lovara --fit trusted --shift 0` after `reposition_916.py` when
anything dips into the footer. Never buy a reposition edit. The 9:16 proof row stays in the Reels safe area and the disclaimer sits at
the very bottom (`"disclaimer_at": "bottom"`).

## 0. Copy rules: hard stops vs references
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

## 1. Frameworks (reference ads: priority `core/references/REFERENCE-PRIORITY.md`; shared library `core/references/static-refs/<folder>/`)
| Code | Framework | Folder | Lovara recipe |
|---|---|---|---|
| F1 | Old way vs New way | 01_Us_vs_Them | "Waiting for the mood" vs "3-in-1 intimacy support". Ideas only, no brands, no bodies |
| F2 | Bold Claim | 02_Bold_Claim | one huge Tier A headline ("From Distant to Deeply Connected") + the capsule hero + up to 3 ✅ callouts |
| F3 | Phone UI | 03_iPhone_Notes_Phone_UI | a Notes page or text thread with one ✅ line per row; the bottle beside the phone |
| F4 | Features & Benefits | 04_Features_and_Benefits | capsule hero + three rows of ✅ benefits with simple icons (or one row per ingredient with ITS claim, once the list is confirmed) |
| F5 | Before/After | 05_Before_and_After | ❌ **skip** |
| F6 | Offer | 06_Offer | "Save up to 45%" + product + one ✅ benefit line |
| F7 | Review card | 07_Testimonial_Social_Proof | ❌ blocked until `reviews.md` has screened Lovara reviews |
| F8 | Question | 08_Question | pronoun-free question from an approved territory ("Feeling distant lately?" only as Tier B, PROPOSED) + answer line + product |
| F9 | Reasons Why | 09_Reasons_Why_Education | "3-in-1, explained": three ✅ lines, numbered, capsule hero; advertorial on white |
| F10 | Sticky Note | 10_Sticky_Notes_To_Do | a note on a fridge, planner or bathroom-counter tile next to the bottle; never a bedroom |
| F11 | Visual Metaphor | 11_EXTRA_Visual_Metaphor | one object idea: two coffee cups touching, a door left ajar to a sunlit room, a ribbon untied, a rose opening |
| F12 | Brand Mood | 12_EXTRA_Brand_Mood_Product_Hero | premium still life (blush silk, travertine, white linen, soft teal), short serif line |
| F13 | Portrait + line | (people) | one candid woman 30–55, shoulder-up, laughing or calm, daytime; headline beside her face; product in the lower third |

**Random (recommended):** N different frameworks (skip F5, F7), mixing text-heavy (F1, F3, F4, F9) and visual (F2, F8, F10–F13).
Default **product-only** (`lessons.md`: Mitansh found GPT Image people-statics "generic" for PT-141; premium-DTC product shots
won). People (F13, or a woman inside F2/F8/F12) only when the user asks, tested in 2–3 shots first.

## 1b. Creative-system pass (shared, `core/references/creative-system.md`)
A different **structure** per slot, at least one **article-style** slot per 5 (on white), a different **product angle**, a **named
typeface**, an **own palette**, rotating **product-name treatment** and **headline placement**; the hero (`product.json → hero`) at
**≥ 35% of the canvas width**, real and label-wrapped, with `hero.never` written into the prompt; the CTA and every line as exact strings
(then QA'd); "NO logo or wordmark anywhere" (the finisher adds the real one).

**Winners Board (read first, `core/winners-board/WINNERS-BOARD.md` §4):** before the batch table, read this product's image
entries on the shared board: one slot mutates a board winner (exactly one variable), retired recipes are skipped, and the
table opens with the board line (`Board: last 15 … · median …`). Board unreachable → "no history yet", say so, carry on.

## 2. Flow (setup lives in SKILL.md step 1; here: write, critique, approve, generate)
1. Inputs from SKILL.md step 1: hook angle, boldness, mood, copy density, image model, how many.
2. Read the bible + copy log (+ winners when they exist). Per slot: pick a framework, **look at 1 reference ad** in priority order
   (layout only, never the words or the scene: the PMG Lovara samples break the rules), write concept (1 line), headline, supporting
   lines (approved, exact), the woman's casting when there is one (age, ethnicity, hair, wardrobe: different every ad), palette, prompt.
   **Persona pass** (`personas.md`), then ONE table: # · framework · person? · headline · tier · supporting lines · type & colour ·
   ≈1 credit. AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". **That click approves the batch
   and its Tier A lines; each Tier B or ⚠ line needs its own explicit OK first.**
3. Generate: `composer_edit_image(project_id, prompt, images=[bottle_ref, capsule], out='gen/b<date>_<n>.png', aspect_ratio="4:5")`
   for the default model; Nano Banana → `core/references/image-models.md`. Max 4 in flight.
4. QA every result (Read it), strictly: text EXACTLY the approved strings; "LOVARA" big and no "by Everlife"; the bottle label
   matches the render (not garbled, not mirrored); the **capsule is identical to the capsule render**, held or hero, ≥ 15% of the width;
   every line big enough for 50+; the woman looks 30–55, clothed, candid, shoulder-up/waist-up, an ordinary face (no celebrity
   likeness), different from every other ad; **no bed, bedroom, lingerie, lips macro anywhere**; colours from §2b; nothing breaks a
   Hard NO. Fail → one automatic fix (an edit of the raw naming the fix). Still bad → flag, don't ship.
5. Finish: `$T/venv/bin/python -I $T/finish_batch.py gen.png FINAL_<n>_<framework>.png --ratio 4:5 --product lovara`.
6. Save to `~/Everlife-Creative/output/Lovara/<date>_batch-<n>/` (FINALs + `prompts.md` + `contact_sheet.jpg`), open the contact sheet,
   log the headlines, offer "Another batch?" / "Variations of #k" / "9:16 of the winners".

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

**Colours (bible + Justin's women's direction, 2026-10-29):** pinks, tans, warm neutrals, warm tones, **white** and **teal**; no colour
banned. Most ads lead with these; up to 2 of every 5 may explore a current trend colour; advertorial/article ads on **white**; at least
one teal-led or teal-accent ad per batch; at most one pink-led ad; no two ads with the same lead colour. Vary placement and light.

## 3. Prompt template (fill everything; keep the quotes exact)
```
Design a finished, premium static social ad for "Lovara", a doctor-prescribed women's intimacy-support prescription (a 3-in-1 oral capsule blend), in the style of a modern, tasteful DTC women's wellness brand. Framework: <name>: <layout from the reference ad>.

PRODUCT: image 1 is the real bottle and image 2 the real capsule. Use the attached capsule reference exactly; do not invent, alter, or
substitute a different pill; exactly one capsule, large, in focus, foreground, at least 15% of the canvas width, <held between thumb and
index finger | resting in an open palm | on a surface>, beside the bottle and never covering its label. Use the attached bottle
reference exactly: same shape, colours and label, label facing camera, sharp, never mirrored, never redesigned; the label wraps around
the bottle and follows its angle. It is a frosted blush-pink glass bottle with a rose-gold ribbed cap; white marble-texture label with
'EVERLIFE' in rose-gold, 'LOVARA' in black, a white 'Rx' box top right, small text 'PRESCRIPTION MEDICATION', '30 CAPSULES'. Show ONLY this bottle and ONE
capsule: no other product. ARRANGEMENT for this ad: <its own arrangement>.

TYPOGRAPHY & COLOUR (this ad's own look): headline in <pairing from §2b>, with ONE phrase picked out in <accent colour>; supporting text
in <partner face>. For readers aged 50+: headline at least 9% of canvas height per line; every other line at least 3.5%; strong
contrast; no thin grey text; no shadows or outlines on type.

TEXT: render ONLY these strings, exactly, nothing else (no extra words, no Everlife or other logos or wordmarks, no 'by Everlife', no
stars, badges, prices, website or disclaimer):
  Name: "LOVARA"   (big and bold: one of the two largest texts in the ad)
  Headline: "<headline>"   (accent on: "<phrase>")
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"

SCENE & STYLE: <scene: a daytime, non-bedroom setting>, real texture and depth (never a flat colour), soft natural light, calm,
tasteful and premium. <PERSON, if any: a <ethnicity> woman, age <30–55>, <hair>, <wardrobe>, natural fit build, candid (laughing, calm
or eyes to camera), framed head-and-shoulders or waist-up, an ordinary, non-famous face (must not resemble any celebrity, actor or public
figure), fully clothed; not posed as a model, not glamour.> Palette: <this ad's own lead colour per §2b>. No bed, no bedroom, no
lingerie, no body shots, no lips close-up, no generic stock-style couples, no before/after, no needles, syringes or vials, no mirrors showing bodies.

LAYOUT (4:5): 5% clear margin on every edge. The TOP 14% is calm continuation of the background (no text, no product): the Everlife
logo is laid there later. The BOTTOM 22% is calm continuation of the background (no text, product or hands): the proof footer is laid
there later. The whole product (bottle, capsule, hands) ends ABOVE 66% of the canvas height and all text above 72% (ask high: the image
model places things lower than asked).
```
Never describe the capsule's shape, colour or markings in words beyond "use the attached capsule reference exactly".

## 4. After the batch
- Contact sheet first, then let the user pick winners. Winners → 9:16 only after approval (compose916.py from the 4:5).
- **Rate the batch (Winners Board, `core/winners-board/WINNERS-BOARD.md` §5):** after the contact sheet, one AskUserQuestion
  question per ad (Winner / Good / Weak / Kill, max 4 per screen), then write every rated ad with its recipe to the shared
  board in one `ArtifactData` batch. Board unreachable → the pending file (§7), and say so.
