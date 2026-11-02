# Spark IMAGE ads: Batch Mode (the default for every image request)

> **⛔ NEVER `reposition_916.py`, edge-stretch, blur or padding colour on a raw (Mitansh, 2026-11-02: "why the hell are these things blurry on the edges! Who told you to do that!").** This overrides every older line in this skill that calls `reposition_916.py` "the fix". Finish the raw AS IS: `finish_batch.py <raw> <out> --ratio 9:16 --product <id> --fit trusted --shift 0`. **If its text or product runs into the footer, ALWAYS fix it in code first (Mitansh, 2026-11-02: "make sure to do it always"):** `$T/venv/bin/python -I $T/mirror_fit_916.py <raw> repo/rN.png --top <content top> --bottom <content bottom>` (0 credits: uniform scale into the band 0.115–0.635, margins filled by mirror-tiling a thin text-free edge strip), then the finisher as above on `repo/rN.png`. LOOK at the result. Re-roll (cost approved) ONLY when a person, text or the product touches a side edge of the raw (the mirror would copy it) or the tool refuses (scale < 0.65). Never ship a smeared edge.
> **👀 SHOW FIRST, THEN RE-ROLL (Mitansh, 2026-11-02: "show me first!"):** after a batch, finish what can be finished (as-is or `mirror_fit_916.py`), open the contact sheet and SHOW the user every result (finished + the raws that failed QA, with why). Never start a re-roll on your own QA call, not even the "one automatic re-roll" older lines mention: the user decides which ads to re-roll, with the cost shown.

> Adapted 2026-10-30 from the PT-141 skill. Spark has ONE form (sublingual tablet) and is for men and women. Where this file's
> history notes mention PT-141 batches, they are lessons carried over, not Spark facts. Default ratio: **4:5** (9:16 from the
> approved masters); default people: product only.

**Proof split (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of ads carry NO proof element; 70% carry a footer proof: of those, 60% the trust row and 40% the Trustpilot 4.9 badge + "Over 100,000 happy customers" (overall ~42% trust / ~28% count / ~30% none; logo + verbatim disclaimer on every ad). Run `finish_batch.py --proof-plan N`, add a **Proof** column to the batch table, and pass it on every finish (`--proof trust` / `--proof count` / `--proof none`, same value on the ad's 4:5 and 9:16), e.g. `finish_batch.py raw.png FINAL.png --ratio 4:5 --product spark --proof count`. Rule: `core/references/creative-system.md` §2.

Same machine as the Restora-Z batch (creative lead, 2026-10-27: "speed, Creatify, batches of at least 5 different types,
mobile friendly, easy to read for older people"). GPT Image 2.5 on Creatify designs the **whole ad** with the real product
render(s) for the chosen form; `finish_batch.py` adds the Everlife logo at the TOP and the approved proof footer (Trustpilot 4.9 /
Doctor Prescribed / Ships Free art, verbatim disclaimer) as a compact transparent strip inside the Meta 9:16 safe area (feed: over the calm bottom ~18%).

**Superseded 2026-10-29 (creative-system §5): never buy a reposition edit. A raw whose text or product dips into the footer is fixed for free with `reposition_916.py` (full-bleed, edge-stretch slivers, no blur), then `finish_batch.py … --fit trusted`. The paragraph below is kept for history only.**

**FINISHING RULE (Mitansh, 2026-10-29, all products): the raw is finished AS IS with `finish_batch.py --ratio 9:16 --product <id> --fit trusted --shift 0`. No repositioning, no scaling, no padding, no blur, no auto-shift: "0 blurring, the raw ones look better". Bake the layout into the prompt and QA it; a colliding raw is re-rolled or accepted.**

**Disclaimer position (Mitansh, 2026-10-29, all products):** on 9:16 the proof row (Trustpilot 4.9 / Doctor Prescribed / Ships Free) stays in the safe area ending at y 1385; the row is ~32% bigger and ~1000 px wide (crosses the Reels side bands, accepted by Mitansh 2026-10-29); the verbatim disclaimer is laid separately at the very bottom of the frame (36 px margin) by `finish_batch.py` (default `EVERLIFE_DISC_AT=bottom`; `footer` = the old under-the-row placement). Feed ratios are unchanged (row + disclaimer at the bottom).

**Footer position (2026-10-29):** on 9:16 the footer ends at y 1385, the bottom of the Reels safe area (the reference ad's band sits at ~63–72% of the frame; the footer may cross the lower-left profile notch, Mitansh 2026-10-29) (`core/tools/safezones.py`,
team Safe zones page), because the bottom ~535 px of a Reel sits under Meta's "Learn more" button and caption
(`core/references/safe-zones/reels_placement_2026-10-29.jpg`). So a 9:16 raw must keep everything in its top ~52%
(LAYOUT block below); `finish_batch.py` refuses (exit 2) when a raw's content runs under the footer. Fix = ONE reposition
edit on the raw (Creatify `composer_edit_image`, 1 credit): "Keep everything identical (headline, type, colours, product,
scene, light). Scale the product and the text block down together (about 35%) and move them up so the lowest element ends
at 50% of the canvas height. Fill the bottom half with calm, plain continuation of the same background: no text, no
product, no hands." Then re-run `finish_batch.py`. Feed ratios (4:5, 1:1) are unchanged: footer over the calm bottom ~18%.


Renders: `assets/RENDERS.md`. The Creatify project is created on the first run (`assets/creatify.json`).

**Batch size (Mitansh, 2026-10-29): default 4, not 5.** Creatify runs 4 image tasks per project at once, so a batch of 4 finishes
in one wave; 8 and 12 run in waves of 4. Compare models with two batches of 4.

## 0. Copy rules: hard stops vs references
**Hard stops:**
- Claims: only approved quick-hit benefits and more approved benefits from `product-bible.md`. Pre-screen ❌ lines never;
  ⏳ Pending-approval and ⚠ lines only with the user's explicit OK + flagged for Jeremy. Weak headline / Weak benefit → avoid.
- Spark is on-demand intimacy support for men and women: PT-141 + Apomorphine + Tadalafil in one sublingual tablet.
  **Never tie a benefit to one ingredient**: name the three together as a combo, or not at all. "ED" only in the bible's ⏳ ED
  headlines with explicit approval; no "erectile", "Viagra", "Cialis", "instant", no timing promises ("tonight", "in minutes"),
  no guarantees. Mechanism first; "supports", never "builds"/"boosts".
- **CTA:** "Get Started Now" is the PROVISIONAL default (Jeremy to confirm); the other bible CTAs are ⏳ and need the user's OK.
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

## 1. Frameworks (reference ads in the SHARED library `core/references/static-refs/<folder>/`, overview `OVERVIEW.jpg`; which pin for which angle: `reference-guide.md`)
| Code | Framework | Folder | Spark recipe |
|---|---|---|---|
| F1 | Old way vs New way | 01_Us_vs_Them | "Plan everything around it" vs "Spontaneity, Back On". Ideas only, no brands, no drug names, no bodies |
| F2 | Bold Claim | 02_Bold_Claim | one huge Tier A headline ("Spontaneity, Back On") + the bottle and one tablet + 3 callouts to approved benefits |
| F3 | Phone UI | 03_iPhone_Notes_Phone_UI | a Notes page with one approved line per row ("From Ready to Right Now" as the title); the bottle beside the phone |
| F4 | Features & Benefits | 04_Features_and_Benefits | product hero + three rows of approved benefits with simple icons (on-demand · non-hormonal · 3-in-1) |
| F5 | Before/After | 05_Before_and_After | ❌ **skip**: no bodies, no "before" states for this product |
| F6 | Offer | 06_Offer | "Save up to 51%" + product + one approved benefit line |
| F7 | Review card | 07_Testimonial_Social_Proof | ❌ blocked until `reviews.md` has screened Spark reviews |
| F8 | Question | 08_Question | pronoun-free question from an approved territory ("Spontaneity, on demand?") + answer line + product |
| F9 | Reasons Why | 09_Reasons_Why_Education | "3-in-1" numbered: the combo line, then two approved benefits; product hero |
| F10 | Sticky Note | 10_Sticky_Notes_To_Do | a note on a fridge or planner ("Friday: no plans. Good.") next to the bottle; never a mirror with a body |
| F11 | Visual Metaphor | 11_EXTRA_Visual_Metaphor | one object idea: a match struck, a spark off flint, a light switch flipped on, the bottle on black stone with a single warm light |
| F12 | Brand Mood | 12_EXTRA_Brand_Mood_Product_Hero | premium still life matched to the black + rose-gold bottle (dark stone, brass, warm low light) or a contrast mood, short serif line |
| F13 | Portrait + line | (people) | only when the user asks for people: a candid woman or man 30–65, shoulder-up, calm, daytime; headline beside the face; product in the lower third. Never a bed |
| **F15** | **Winner recipe** (`winners/` S04/S13/S03) | (our winners) | huge "SPARK" logotype top, one ✅ headline, **three icon pills** (✅ lines, each a different idea), **the tablet huge and in front**, the bottle smaller behind or beside it, warm premium palette |
| **F16** | **Slider** (`winners/` S08, 23 purchases) | (our winners) | a "WAITING → SPARK MOMENT"-style slider bar with the real tablet as the knob; huge SPARK; one icon row. Bar labels must be neutral words, never timing promises |

**Random (recommended):** N different frameworks (skip F5, F7; F13 only with people), always including **F15 or F16** (our
winners), mixing text-heavy (F1, F3, F4, F9) and visual (F2, F8, F10, F11, F12). Weight towards F15, F16, F2, F11, F12.

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

## 2. Flow (the two setup rounds live in SKILL.md step 1; here: write, critique, approve, generate)
1. Inputs from SKILL.md step 1: hook angle, boldness, CTA, mood, copy density, spin-a-winner, how many. Placement is 4:5
   (9:16 comes from the approved masters). People: product only unless the user asked. Frameworks: random mix unless the
   user named some in chat.
2. Read the bible + copy log + `winners/winners.md` (one cat). Per slot: pick a framework, **look at 1 reference ad** (a Spark
   winner card when useful, else the framework folder; layout only, never the words or the scene). Write concept
   (1 line), headline (Tier A by default; Tier B only within the chosen boldness), supporting lines per the chosen copy density (0, 1 or 3; approved claims, exact), the chosen mood, prompt. Show
   ONE table: # · framework · person? · territory · headline · tier (A / B PROPOSED) · supporting lines · type & colour · ≈1 credit.
   **Persona pass before the table** (`personas.md`): read every slot as Skeptical Dave and Careful Maya; the three ingredients only
   ever together; no two supporting lines sharing a noun ("desire support" ×3 is the Dave trap); every "brain-based" /
   "non-hormonal" paired with a plain line; nothing couch-unsafe. Add a one-line "Dave says" under the table for any slot you changed.
   AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". **That click approves the batch and
   its Tier A lines; each Tier B line needs its own explicit OK first** (ask before the generate question).
3. Generate: `composer_edit_image(project_id, prompt, images=[<spark_bottle_ref>, <spark_tablet>]  (add type_specimen only
   for the house look, see §2b), out='gen/b<date>_<n>.png', aspect_ratio=<final ratio>)` for the default model; Nano Banana → §2c (Model Playground tools) from `assets/creatify.json`. Max 4 in flight.
4. QA every result (Read it), strictly: text EXACTLY the approved strings; "SPARK" big; the Spark bottle's label matches the render
   (not garbled, not mirrored); the **tablet is identical to the tablet render** and there is exactly one (no invented pill); **the
   tablet is the hero: larger in frame than the bottle** (test batch 2026-10-30 failed this 4/4: fix with a 1-credit edit);
   every line big enough for 50+; people (if any) look 30–65, clothed, candid, shoulder-up/waist-up, **no bed or bedroom anywhere in
   frame**; no model-drawn Everlife logo; nothing breaks a Hard NO. **Text or product in the bottom 22% → fix** (the 4:5 finisher does
   not refuse it).
   Fail → one fix edit naming the problem (1 credit, within the batch approval). Still bad → flag, don't ship.
5. Finish: `$T/venv/bin/python -I $T/finish_batch.py gen.png FINAL_<n>_<framework>.png --ratio 4:5 --product spark`
   (the verbatim disclaimer comes from product.json).
6. Save to `~/Everlife-Creative/output/Spark/<date>_batch-<n>/` (FINALs + `prompts.md` + `contact_sheet.jpg`),
   open the contact sheet, log the headlines, offer "Another batch?" / "Variations of #k" / "9:16 of the winners".

## 2b. Type & colour: be different every time (creative lead, 2026-10-28)
Fonts and colours are **not** house-locked. Every ad in a batch gets its own pairing and its own accent; never two alike
in one batch, never the same look two batches in a row, and never default to the old "serif + purple accent" specimen.
Pick per ad and write it into the prompt's TYPOGRAPHY & COLOUR block (legibility rules still apply: 50+ readers, no
shadows or outlines on type, product name big).

| Headline face (pick one) | Partner for supporting text |
|---|---|
| Heavy condensed grotesque, all caps (the winners' look) | light humanist sans |
| Elegant high-contrast serif, roman | clean geometric sans |
| Serif with ONE italic word | small-caps sans |
| Wide extended sans, bold | regular sans |
| Slab serif, bold | light sans |
| Chunky rounded sans | mono-spaced labels |
| Brush / handwritten accent word inside a sans headline | regular sans |
| Thin editorial sans, tracked out, all caps | serif body |

Accent colour: take it from the scene or the product, never from habit. Options: the label red, brass/gold, deep navy,
charcoal on cream, cream on charcoal, ink on sand, forest, teal, sky, slate, mocha, rose, blush, burgundy, warm white.
Product rules win: Spark has no palette limit (the bible's women's palette applies only to GHK-Cu Cream and Glow Stack). Default
**warm and light** (bible imagery: "warm, sun-lit"; most winners: gold, amber, cream, blush, teal + gold); one dark or bold ad per
batch of 4 keeps variety (S14 black + gold, V02 red velvet). Vary the headline placement too (top-left, centred, bottom-
third above the footer band, split either side of the product) and the light (morning, golden hour, overcast soft, studio).

The type specimen (`assets/type_specimen.png`) is no longer attached by default. Attach it only when the brief asks for
the house editorial look, and then say "match image 3".

## 2c. Image model (one more question in the setup round; shared rules in `core/references/image-models.md`)
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
Design a finished, premium static social ad for "Spark", a doctor-prescribed, on-demand intimacy-support prescription for men
and women (one sublingual tablet), in the style of a modern DTC wellness brand (Hims/Ro-level premium). Framework: <name>: <layout
from the reference ad>.

PRODUCT: image 1 is the real bottle and image 2 the real tablet. Use the attached tablet reference exactly; do not invent, alter,
or substitute a different pill; exactly one tablet. **The tablet is the hero:** large, in focus, in the foreground close to the
lens, at least 25% of the canvas width and visibly LARGER in frame than the bottle; the bottle sits smaller behind or beside it,
label legible, never covered by the tablet. Use the attached bottle reference exactly: same shape, colours and label, label facing camera, sharp, never
mirrored, never redesigned; the label wraps around the bottle. It is <bottle wording from assets/RENDERS.md>. Show ONLY this bottle
and ONE tablet: no other product. The product is large and legible.

TYPOGRAPHY & COLOUR (this ad's own look, different from every other ad in the batch): headline in <pairing from §2b>, with ONE
phrase picked out in <accent colour>; supporting text in <partner face>. For readers aged 50+: headline at least 9% of canvas
height per line; every other line at least 3.5%; strong contrast; no thin grey text; max 3 supporting lines. Product name on one
line, never hyphen-broken.

TEXT: render ONLY these strings, exactly, nothing else (no extra words, no Everlife or other logos or wordmarks, no 'by Everlife',
no stars, badges, prices, website or disclaimer):
  Name: "SPARK"   (big and bold: one of the two largest texts in the ad; as the product logotype: a wide, elegant serif in
                   rose-gold with a small eight-point star inside the A, like the bottle)
  <F15/F16 only> Pills: "<✅ line 1>" / "<✅ line 2>" / "<✅ line 3>"   (three rounded outline pills, each with a simple line icon)
  Headline: "<headline>"   (accent on: "<phrase>", in the accent colour named above)
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"
  <CTA, when the framework has one: "<the session's approved CTA>">

SCENE & STYLE: <scene: a daytime or warm-evening, non-bedroom setting>, real texture and depth (never a flat colour), real light,
calm, tasteful and premium. <PERSON, only when asked: a <woman | man> 30–65, attractive in a natural way, fully clothed in <day
wear>, candid, framed head-and-shoulders or waist-up; not posed as a model, not glamour; an ordinary, non-famous face.>
<palette: the §2b mood chosen for this ad; the bottle's own black + rose-gold works on dark stone, warm brass and deep red, and
contrasts on white or sand.> No bed, no bedroom, no lingerie, no body shots, no couples in bed, no before/after, no needles,
syringes or vials, no mirrors showing bodies.

LAYOUT (9:16): 5% clear margin on every edge. The TOP 12% is calm continuation of the background (no text, no product): the
Everlife logo is laid there. EVERYTHING ELSE (headline, tiny line, product, shadow) sits in the TOP 52% of the canvas; the
lowest element ends at 50% height. The BOTTOM 48% is calm, plain continuation of the background (surface, wall, fabric: no
text, no product, no hands, no key objects): the proof footer is laid at ~61–72% and Meta's Reels/Stories UI covers the rest.
LAYOUT (4:5, the default): 5% clear margin on every edge. The TOP 14% is calm continuation of the background (no text, no
product): the Everlife logo is laid there later. The BOTTOM 22% is calm continuation of the background (no text, product or
hands): the proof footer is laid there later. The whole product ends ABOVE 66% of the canvas height and all text above 72% (ask
high: the image model places things lower than asked). (Lovara batch-1, 2026-10-30: this block worked 3 of 4; check every final.)
```
> GPT Image 2.5 lands the product 8–15% LOWER than the LAYOUT block asks (batch-4 PT-141, 2026-10-29: "base at 48%" came back at
> 58–65%). Ask for the lowest element at **40%** (cap/nozzle tip at 13%) to get ~50%. `finish_batch.py` then shifts the image up by
> whatever headroom is left under the logo band (max 320 px) before it refuses; a refusal means one reposition edit (1 credit).
```
```
QA that the label is the Spark label. Never describe the tablet's shape, colour or markings in words beyond
"use the attached tablet reference exactly".

## 4. After the batch
- Contact sheet first, then let the user pick winners. Winners → the other ratio only after approval.
- **Rate the batch (Winners Board, `core/winners-board/WINNERS-BOARD.md` §5):** after the contact sheet, one AskUserQuestion
  question per ad (Winner / Good / Weak / Kill, max 4 per screen), then write every rated ad with its recipe to the shared
  board in one `ArtifactData` batch. Board unreachable → the pending file (§7), and say so.
