# MOTS-c IMAGE ads: Batch Mode (the default for every image request)

Same machine as the Restora-Z / PT-141 batches (creative lead: "speed, Creatify, batches of at least 5 different types, mobile
friendly, easy to read for older people"). GPT Image 2.5 on Creatify designs the **whole ad** with the real vial render (the only
product image); `finish_batch.py` adds the Everlife logo at the TOP and the approved proof footer (Trustpilot 4.9 / Doctor Prescribed / Ships
Free art, verbatim disclaimer) inside the Meta 9:16 safe area (feed: over the calm bottom ~18%).

**FINISHING RULE (Mitansh, 2026-10-29, all products): the raw is finished AS IS with `finish_batch.py --ratio 9:16 --product <id> --fit trusted --shift 0`. No repositioning, no scaling, no padding, no blur, no auto-shift: "0 blurring, the raw ones look better". Bake the layout into the prompt and QA it; a colliding raw is re-rolled or accepted.**

**Disclaimer position (Mitansh, 2026-10-29, all products):** on 9:16 the proof row (Trustpilot 4.9 / Doctor Prescribed / Ships Free) stays in the safe area ending at y 1385; the row is ~32% bigger and ~1000 px wide (crosses the Reels side bands, accepted by Mitansh 2026-10-29); the verbatim disclaimer is laid separately at the very bottom of the frame (36 px margin) by `finish_batch.py` (default `EVERLIFE_DISC_AT=bottom`; `footer` = the old under-the-row placement). Feed ratios are unchanged (row + disclaimer at the bottom).

**Footer position (2026-10-29):** on 9:16 the footer STARTS at y 1184 and ends at y 1385 (bottom of the Reels safe area). `finish_batch.py`
refuses (exit 2) when content runs under it.

**THE FIX IS LOCAL AND FREE (2026-10-29, Mitansh: "solve this once and for all"):** every image model lands content 10-25% lower than
the LAYOUT block asks (GPT Image 2.5: 8-15%; Nano Banana Pro: 70-75% of the frame on 5/5 raws), and paid "scale down and move up"
edits DO NOT WORK on Nano Banana Pro (5/5 ignored the move, one swapped the vial for a white one: 7.5 credits wasted). NEVER buy a
reposition edit. Run `reposition_916.py` on the raw (0 credits, nothing re-rendered), then the finisher:
```
$T/venv/bin/python -I $T/reposition_916.py gen/raw.png repo/rN.png --top <content top> --bottom <content bottom> \
    [--crop-top F] [--crop-bottom F] [--composite <vial render> x0 y0 x1 y1]
$T/venv/bin/python -I $T/finish_batch.py repo/rN.png FINAL_N.png --ratio 9:16 --product mots-c
```
It scales the artwork into the safe band (text + product above y 1184), keeps the scene FULL-BLEED under the footer (never crop the
bottom: Mitansh rejected the cropped/blurred version, "why is everything blurred"), and fills the thin slivers at the edges with a
sharp edge-stretch (default `--fill reflect` = edge mode; `--fill plate` = blur, rejected). Then run the finisher with `--fit trusted`
(the finisher's edge detector counts the scene as content; trusted means the tool already placed text + product above the footer). `--top/--bottom` = content band as fractions of the raw height (read them off the raw).
`--crop-top/--crop-bottom` drop scene rows outside the content (a bucket, a crossbeam, legs). If anything sits ABOVE the headline
(a rack, a model-drawn logo), set `--crop-top` = `--top`, or the finisher shifts the image down for the logo and the bottom overflows.
`--composite` pastes the real transparent render over the generated vial's box: fixes a garbled or wrong-strength label with no AI
(matched perfectly on batch 1). Keep the artwork at >= 0.65 scale; a full-frame portrait (F13) = `--crop-bottom` at the bench line.
Still ask the model for the lowest element at **40%** and the top 12% empty: less overshoot = bigger final artwork.

Renders: `assets/RENDERS.md`. The Creatify project is created on the first run (`assets/creatify.json`).

**Batch size (Mitansh, 2026-10-29): default 4, not 5.** Creatify runs 4 image tasks per project at once, so a batch of 4 finishes
in one wave; 8 and 12 run in waves of 4. Compare models with two batches of 4.

## 0. Copy rules: hard stops vs references
**⚠ PROVISIONAL DISCLAIMER (2026-10-30):** product.json carries the standard ad disclaimer (the bible's MOTS-c page still says "Disclaimer pending"; Priestley: "use it for now"). The finishers render it. Drafts may be made; every SESSION.md flags each asset "provisional disclaimer: Jeremy to confirm"; nothing goes live until he confirms (then replace product.json's text with his and `bible_sync.py --check` must show ✅).

**Hard stops:**
- Claims: only the ✅ lines of the pre-screen (`product-bible.md`, APPROVED UPDATE); ⚠ lines (the glucose lines, "Supports Energy
  Balance", the "upgrade / activated / optimized" headlines) only with the user's explicit OK + flagged for Jeremy; ❌ never.
- MOTS-c is METABOLIC support for energy and endurance. **No weight, fat, body-composition, appetite or "fat and skinny" words or
  images; no body areas; no melt / burn / ripped / shred; no before/after.** No disease words (diabetes, blood sugar control,
  insulin). "Supports", never "boosts / burns / builds". No timing promises, no guarantees.
- **No needles, syringes, pens, injecting or "needle-free"** in words or pictures. The vial is a still object.
- One product image: the Rx vial. Never a strength, dose, mL or count in copy.
- People: active adults 30–55, men and women, in motion or just after; never a physique shot (`direction.md`).
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically" for the product.
- **Offer: "Save up to 40%"** (Creative Messaging doc), exact string; never the lander's "Start MOTS-C — 40% Off", never a $ price.
- "MOTS-C" big in every ad; never "by Everlife" on images. Proof exact; disclaimer verbatim (the footer handles both).

**Headline tiers:** Tier A = the Creative Messaging doc's ✅ headlines, verbatim (prefer the top of its ranking) or an ✅ benefit · ⚠ lines: explicit OK per line, Jeremy · Tier B (max 2): PROPOSED, Jeremy.

## 1. Frameworks (reference ads in the SHARED library `core/references/static-refs/<folder>/`; overview `OVERVIEW.jpg`; which pin for which angle: `reference-guide.md`)
| Code | Framework | Folder | MOTS-c recipe |
|---|---|---|---|
| F1 | Old way vs New way | 01_Us_vs_Them | "More coffee / more gels" vs "Support cellular energy": methods only, no brands, no bodies |
| F2 | Bold Claim | 02_Bold_Claim | "MOTS-C" huge + one Tier A line + the vial hero + up to 3 ✅ benefits |
| F3 | Phone UI | 03_iPhone_Notes_Phone_UI | a training plan / run log with one ✅ line per row; the vial beside the phone |
| F4 | Features & Benefits | 04_Features_and_Benefits | vial hero + three ✅ rows with simple icons (cell · energy · distance) |
| F5 | Before/After | 05_Before_and_After | ❌ **skip**: body-composition category, never |
| F6 | Offer | 06_Offer | "Save up to 40%" + the vial + one or two ✅ lines (test-1 M4: a lemon-yellow tab beside the vial on a pedestal) |
| F7 | Review card | 07_Testimonial_Social_Proof | ❌ blocked until `reviews.md` has screened MOTS-c reviews |
| F8 | Question | 08_Question | pronoun-free question ("Energy for the long run?") + answer line + product |
| F9 | Reasons Why | 09_Reasons_Why_Education | three ✅ lines, numbered, vial hero |
| F10 | Sticky Note | 10_Sticky_Notes_To_Do | a note on a fridge ("Sat: 10 miles") next to the vial |
| F11 | Visual Metaphor | 11_EXTRA_Visual_Metaphor | one object: a lit filament, a sunrise over a trail, a fresh battery icon; the vial on real material |
| F12 | Brand Mood | 12_EXTRA_Brand_Mood_Product_Hero | premium still life: stone, slate, morning light, lemon-yellow accent |
| F13 | Portrait + line | (people) | a runner / cyclist / swimmer 30–55 just after a session, shoulder-up, calm; vial on the bench; never a physique |
| F14 | Premium DTC | 13_Premium_DTC | the Hims/Ro codes: ONE sentence-case headline, one tiny line, vial as an object, 60% empty |

**Random (recommended):** N different frameworks (skip F5, F7). Weight towards F2, F12, F14, F13, F9.

## 1b. Creative-system pass (shared, `core/references/creative-system.md`, adopted 2026-10-29)
**Winners Board (read first, `core/winners-board/WINNERS-BOARD.md` §4):** before the batch table, read this product's image
entries on the shared board: one slot mutates a board winner (exactly one variable), retired recipes are skipped, and the
table opens with the board line (`Board: last 15 … · median …`). Board unreachable → "no history yet", say so, carry on.

Before the batch table, check every slot against the shared system: a different **structure** per slot (split, stacked panels,
timeline, poster, billboard, calendar, type-only, article), at least one **article-style** slot per 5, a different **product angle**,
a **named typeface**, an **own palette**, a rotating **product-name treatment** and **headline placement**; the form's hero
(`product.json → hero`) at **≥ 35% of the canvas width**, real and label-wrapped, with `hero.never` written into the prompt; the CTA
and every line as exact strings in TEXT (then QA'd); "NO logo or wordmark anywhere" (or an empty masthead box for `logo_in_box.py`).
Finishing: `reposition_916.py` (free, local) when anything dips into the footer; `unfade_cta.py` when a CTA sits just above it;
`finish_batch.py --logo-w 40%` for the large real logo; 9:16 only via `compose916.py` from the approved 4:5. Checklist at the end of
that file.

## 2. Flow
1. Inputs from SKILL.md step 1: audience, angle, boldness. **Round 3 (ONE AskUserQuestion, 4 questions):**
   **Mood** "Surprise me: different each ad (Recommended)" / "Ultra premium, vial only: Hims/Ro codes + vial-refs (Mitansh's favourite,
   batch 3 2026-10-29)" / "Outdoor endurance at dawn: trail, quiet road, pool lane, rower (men and women)" / "Everyday energy: kitchen, desk, school run (non-workout; doc 2026-10-30)"
   **Ultra premium** = `core/references/ultra-premium.md` (the shared spec for every product; its gate rules win) + `core/references/static-refs/13_Premium_DTC/README.md`
   codes on every slot (ONE sentence-case two-line headline, second line tonal, at most one tiny line or three quiet lines, product as an
   object on real material with one hard light and one long shadow, monochrome field, 60% empty, no bullets/icons/badges/caps/logo), each slot
   borrowing the staging of one named pin from `vial-refs/` (V31 monochrome hero, V20 black luxury, V40/V37 pale editorial) or a Hims tile
   (tan-on-walnut, amber-on-amber top-down); product only, no people; GPT Image 2.5. It overrides Copy density (headline + tiny line / +1 line / +3 quiet lines mixed) and People (product only). · **Copy density** "Headline + 3 lines (Recommended: the brief
   asks for hooks + bullets on some)" / "Headline + 1 line" / "Headline only" · **People** "Mix: about half with a person (Recommended,
   per the brief)" / "Product only" / "Every ad with a person" · **How many** "4 (Recommended: one wave, Creatify runs 4 at a time)" / "8" / "12".
2. Read the bible + copy log + `winners/winners.md` (one cat). Per slot: pick a framework, an angle (rotating when "mix"), **look at 1 reference ad** (layout only). Write concept (1 line), headline (Tier A), supporting lines per
   density (quick-hit lines, exact), mood, type & colour (§2b), prompt. Show ONE table: # · framework · angle · person? ·
   headline · tier · supporting lines · type & colour · ≈1 credit.
   **Persona pass before the table** (`personas.md`): the personas in `personas.md`; no two supporting lines sharing
   a noun; every "mitochondrial" / "metabolism" paired with a plain line; nothing about weight or bodies. "Dan says" under the table.
   AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". Each Tier B / ⏳ / ⚠ line needs its own OK first.
3. Generate: `composer_edit_image(project_id, prompt, images=[<vial render path>], out='gen/b<date>_<n>.png', aspect_ratio='9:16')` for the default model; Nano Banana → §2c (Model Playground tools)
   from `assets/creatify.json`. Max 4 in flight.
4. QA every result (Read it), strictly: text EXACTLY the approved strings; the vial's label matches the render (not garbled, not mirrored);
   **no syringe, needle, pen, dropper or droplet trail anywhere**; no capsules or pills anywhere; people active 30–55, never a physique,
   no body-composition cue; "MOTS-C" big; nothing breaks a Hard NO. Fail → one automatic re-roll naming the fix.
5. Finish: `reposition_916.py` on every 9:16 raw (0 credits), then `finish_batch.py repo/rN.png FINAL.png --ratio 9:16 --product mots-c`
   (verbatim disclaimer from product.json). Name finals `YYYY-MM_Static_MOTSc-<Men|Women|Both>_BaseNN_VV_<framework>_1080x1920-MP.png`.
6. Save to `~/Everlife-Creative/output/MOTS-c/<date>_batch-<n>/` (FINALs + `prompts.md` + `contact_sheet.jpg`), open the
   contact sheet, log the headlines, offer "Another batch?" / "Variations of #k" / "4:5 of the winners".

## 2b. Type & colour: be different every time (creative lead, 2026-10-28)
Every ad gets its own pairing and accent; never two alike in one batch, never the same look two batches in a row.

| Headline face | Partner for supporting text |
|---|---|
| Heavy condensed grotesque (the performance category's look), sentence case or caps | light humanist sans |
| Wide extended sans, bold | regular sans |
| Slab serif, bold | light sans |
| Elegant high-contrast serif, roman | clean geometric sans |
| Chunky rounded sans | mono-spaced labels |
| Thin editorial sans, tracked out | serif body |
| Stencil / industrial sans (race-bib and trail signage) | regular sans |
| Serif with ONE italic word | small-caps sans |

Accent from the scene or product: lemon yellow (the vial label), sky blue, stone; or, chalk white, steel grey, concrete, rubber black, safety-tape yellow (sparingly),
forest, tan, walnut; women: blush, rose, tan, beige, cream, mocha, burgundy (never orange, never green). Vary headline placement
(top-left, centred, split either side of the product) and light (hard side light, overcast, golden hour, studio).

## 2c. Image model (one more question in the setup round; shared rules in `core/references/image-models.md`)
**All three run through the Creatify connector's model playground, no API keys** (`model_playground_list_models` → `model_playground_get_model_schema`
→ `model_playground_generate`, `image_urls` = the vial render's cdn_url in `assets/creatify.json`; 5 parallel calls are fine):
`nano-banana-pro/edit` (1.5 cr, aspect_ratio 9:16, resolution 2K) · `nano-banana-2.1/edit` (1 cr) · `gpt-image-2.5-flare/edit` (1 cr,
image_size portrait_16_9, quality high, resolution 2K). Download the output url with curl. Batch 1 (Nano Banana Pro): best type and
scenes, 4/5 labels perfect, draws its own EVERLIFE wordmark on ~2/5 (crop it), content at 70-75% (reposition locally).
**Image model:** "GPT Image 2.5 via the connector (Recommended)" / "Nano Banana 2.1" / "Nano Banana Pro" (these three only,
Mitansh 2026-10-29). One model per batch. Default = `composer_edit_image` as before. Nano Banana = the Creatify MCP server's
Model Playground (`model_playground_get_model_schema` → `model_playground_generate(model_name="nano-banana-2.1/edit" |
"nano-banana-pro/edit", input_params={prompt, image_urls:[<render cdn_url>], aspect_ratio:"9:16", resolution:"1K"})` →
`model_playground_get` → curl the output into `gen/`). Needs the `creatify` MCP signed in (`/mcp`) and the render's `cdn_url` in
`assets/creatify.json` (one-time, see the shared file). Same workspace credits: GPT Image 2.5 = 1 / image; Nano Banana 2.1 = 1 at
1K (1.5 at 2K); Nano Banana Pro = 1.5. Same prompt, same QA, same finishing. Write the model into `prompts.md` and SESSION.md.
If the `creatify` MCP tools are not in this session, say so (new session + `/mcp`) and offer GPT Image 2.5 for this batch.

## 3. Prompt template (fill everything; keep the quotes exact)
```
Design a finished, premium static social ad for "MOTS-c", a doctor-prescribed metabolic peptide for cellular energy and
endurance (compounded Rx vial), in the style of a modern premium DTC wellness brand. Framework: <name>: <layout from the reference ad>.

PRODUCT: image 1 is the real product. Use the attached product reference exactly: same shape, colours and label, label facing camera,
sharp, never mirrored, never redesigned. It is a squat clear glass vial with a silver flip-off cap over a brushed-silver crimp; a bright lemon-yellow label with the black EVERLIFE wordmark, 'MOTS-C' large in black, '10MG/ML', 'RX ONLY', '5ML'. The vial stands or lies on the surface as a still object. NO syringe, needle,
pen, dropper, droplets or injection of any kind anywhere; NO capsules, pills or tablets anywhere. Show ONLY this vial. The product is
large and legible.

TYPOGRAPHY & COLOUR (this ad's own look): headline in <pairing from §2b>, with ONE phrase in <accent>; supporting text in <partner face>.
For readers aged 50+: headline at least 9% of canvas height per line; every other line at least 3.5%; strong contrast; no thin grey
text; max 3 supporting lines; no shadows or outlines on type. Product name on one line, never hyphen-broken.

TEXT: render ONLY these strings, exactly, nothing else (no extra words, no Everlife or other logos or wordmarks, no 'by Everlife',
no stars, badges, prices, website or disclaimer):
  Name: "MOTS-C"   (big and bold: one of the two largest texts in the ad)
  Headline: "<headline>"   (accent on: "<phrase>")
  Supporting: "<quick-hit line 1>" / "<line 2>" / "<line 3>"

SCENE & STYLE: <scene from direction.md: trail at dawn, quiet road, rowing machine, pool lane, bright kitchen before a run>, real texture and depth (never a flat colour), <light>, premium, calm, energetic. <PERSON, if any: a <man | woman> 30–55, an active runner / cyclist / swimmer, an ordinary non-famous face, in motion or just after, shoulder-up or full-body in motion; never a physique shot.> Palette: lemon yellow (the vial) against charcoal, slate, white, sky blue or stone. No scales, tape measures, waistlines, bellies, abs or mirrors; no before/after; no needles, syringes, pens or injecting; no medical settings.

LAYOUT (9:16): 5% clear margin on every edge. The TOP 12% is calm continuation of the background (no text, no product): the Everlife
logo is laid there. EVERYTHING ELSE (headline, lines, product, shadow) sits in the TOP 52% of the canvas; ask for the lowest element
at 40% of the canvas height (the model lands it lower). The BOTTOM 48% is calm, plain continuation of the background (surface, wall,
floor: no text, no product, no hands, no key objects): the proof footer is laid at ~61–72% and Meta's Reels/Stories UI covers the rest.
LAYOUT (4:5 / 1:1): 5% margin; TOP 10% calm for the logo; BOTTOM 18% calm for the proof footer; product base above that line.
```
QA that the label matches the vial render.

## 4. After the batch
- Contact sheet first, then let the user pick winners. Winners → the other ratio only after approval.
- **Rate the batch (Winners Board, `core/winners-board/WINNERS-BOARD.md` §5):** after the contact sheet, one AskUserQuestion
  question per ad (Winner / Good / Weak / Kill, max 4 per screen), then write every rated ad with its recipe to the shared
  board in one `ArtifactData` batch. Board unreachable → the pending file (§7), and say so.
