# Restora-Z IMAGE ads: Batch Mode (the default for every image request)

> **⛔ NEVER `reposition_916.py` / shrink / edge-stretch / blur a raw (Mitansh, 2026-11-02: "why the hell are these things blurry on the edges! Who told you to do that!").** This overrides every older line in this skill that calls `reposition_916.py` "the fix". Finish the raw AS IS: `finish_batch.py <raw> <out> --ratio 9:16 --product <id> --fit trusted --shift 0`. If its text or product runs into the footer, the raw is a FAIL: re-roll it with the LAYOUT block (ask for the lowest element at 40%, top 12% empty), with the cost approved. Never ship a smeared edge.

Creative lead, 2026-10-27: "I want speed! Use Creatify and batches, at least 5 images of different types at once,
random by default, mobile friendly, the new creative font, easy to read for older people."

The image model (GPT Image 2.5 on Creatify) designs the **whole ad**: layout, headline, benefits and scene, with the
real bottle and capsule. We add only the **approved footer** (`finish_batch.py`): a COMPACT, TRANSPARENT strip (~17% of the height) laid over the
ad's calm bottom on a soft gradient: the Trustpilot 4.9 / Doctor Prescribed / Ships Free art and the verbatim
disclaimer (creative lead 2026-10-27: "35% smaller and transparent").

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


**Batch size (Mitansh, 2026-10-29): default 4, not 5.** Creatify runs 4 image tasks per project at once, so a batch of 4 finishes
in one wave; 8 and 12 run in waves of 4. Compare models with two batches of 4.

## 0. Copy rules: hard stops vs references
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

## 1. The frameworks (reference ads in `core/references/static-refs/<folder>/`, overview: `core/references/static-refs/OVERVIEW.jpg`)
| Code | Framework | Folder | Everlife recipe |
|---|---|---|---|
| F1 | Myth vs Fact / Old way vs New way | 01_Us_vs_Them | two columns or split: "Myth" (a common sleep belief or old routine, e.g. counting sheep / scrolling at 2 am) vs "Fact" (an approved claim). No brands named. |
| F2 | Bold Claim | 02_Bold_Claim | one huge approved-claim headline + product hero + 3 small callout arrows to approved benefits |
| F3 | iPhone Notes / phone UI | 03_iPhone_Notes_Phone_UI | iOS Notes page, reminder or alarm toggles; checklist of approved benefits; the real bottle beside the phone |
| F4 | Features & Benefits | 04_Features_and_Benefits | "3-in-1" product hero with three icon rows: each ingredient + ONE of its own claims |
| F5 | Night → Morning | 05_Before_and_After | split frame: 3 am restless (blue, dark) vs 7 am refreshed (warm light). Same room or objects, **no faces or bodies compared** |
| F6 | Offer | 06_Offer | ❌ blocked: bible offers are [PLACEHOLDER]. Only if the user gives a real, approved offer |
| F7 | Review card | 07_Testimonial_Social_Proof | one verbatim ✅ Trustpilot review from `reviews.md` in a clean quote card + 5 stars + the bottle. No reviewer photo next to a name |
| F8 | Question | 08_Question | big pronoun-free question from an approved pain point ("Up at 3 a.m. again?", "Wide awake at 2 a.m.?") + answer line + product |
| F9 | Reasons Why | 09_Reasons_Why_Education | "3 reasons to switch up your nights" numbered list of approved claims, product hero |
| F10 | Sticky Note | 10_Sticky_Notes_To_Do | handwritten sticky note(s) on a nightstand/mirror ("Tonight: actually sleep") next to the bottle |
| F11 | Visual Metaphor | 11_EXTRA_Visual_Metaphor | one clever object idea (pillows spilling from the bottle, capsule as a tiny bed, sleep "on" switch) + short headline |
| F12 | Brand Mood | 12_EXTRA_Brand_Mood_Product_Hero | premium still life, one colour mood, short serif line |

**Random (recommended):** pick N different frameworks (no repeats, skip F6), mixing text-heavy (F1, F3, F4, F9) and
visual (F2, F5, F8, F10, F11, F12). Weight towards F2, F4, F8, F11, F3, which match the winners.

## 1b. Creative-system pass (shared, `core/references/creative-system.md`, adopted 2026-10-29)
Before the batch table, check every slot against the shared system: a different **structure** per slot (split, stacked panels,
timeline, poster, billboard, calendar, type-only, article), at least one **article-style** slot per 5, a different **product angle**,
a **named typeface**, an **own palette**, a rotating **product-name treatment** and **headline placement**; the form's hero
(`product.json → hero`) at **≥ 35% of the canvas width**, real and label-wrapped, with `hero.never` written into the prompt; the CTA
and every line as exact strings in TEXT (then QA'd); "NO logo or wordmark anywhere" (or an empty masthead box for `logo_in_box.py`).
Finishing: `reposition_916.py` (free, local) when anything dips into the footer; `unfade_cta.py` when a CTA sits just above it;
`finish_batch.py --logo-w 40%` for the large real logo; 9:16 only via `compose916.py` from the approved 4:5. Checklist at the end of
that file.

## 2. Flow (fast: 1 question, then generate)
1. **One AskUserQuestion, 4 questions, each with a ✨ Recommended first option** (one Enter-press per question gets a great batch):
   - **How many?** "4 (Recommended: one wave, Creatify runs 4 at a time)" / "8" / "12".
   - **Placement:** "4:5 Feed (Recommended)" / "9:16 Stories/Reels" / "4:5 + 9:16" / "1:1".
   > **🎨 STYLES = `core/references/style-library/MOOD-QUESTION.md` (Mitansh 2026-11-02; replaces the Frameworks options below):** 1 "🎲 Surprise me (Recommended)" = a random style per ad from the 15 Drive styles, different every batch (`core/scripts/pick_styles.py`) · 2 "📚 Pick from the 15 styles" (the follow-up picker). The F-framework table stays as a fallback. Each slot Reads its style board (`core/references/style-library/STYLES.md`): layout only, this skill's claims, palette and product rules win.
   - **Frameworks:** "🎲 Random mix (Recommended)" / "Pick frameworks" (then a multiSelect follow-up with the table).
   - **Look:** "Standard (Recommended)" / "✨ Ultra premium, product only" (Hims/Ro codes on every slot: `core/references/ultra-premium.md`;
     overrides people, the tablet stays the hero). (4 questions now.)
   **Never ask the user for pain points or style here.** Claude picks them automatically from the bible: a different approved
   pain point per ad where it fits, each paired with its matching approved claim. Show the picks in the batch table instead.
2. Read the bible + copy log (one cat). For each slot: pick a framework, **look at 1 reference ad from its folder** (Read the jpg),
   and write: concept (1 line), headline (Tier A by default, see §0 ⚠ pending), up to 3 short supporting lines (approved
   claims, exact), and the prompt (template below). Show ONE compact table: # · framework · pain point (auto) · headline ·
   tier (A / B PROPOSED) · supporting lines · ≈1 credit.
   One AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". **That click approves the batch
   and its Tier A lines; each Tier B line needs its own explicit OK first** (ask before the generate question).
3. Generate: `composer_edit_image(project_id, prompt, images=[bottle, capsule]  (add type_specimen only for the house look, see §2b), out='gen/b<date>_<n>.png',
   aspect_ratio=<MODEL_RATIO>)` for the default model; Nano Banana → §2c (Model Playground tools) from `assets/creatify.json`. **Max 4 in flight per project**: start 4, then the next as each finishes.
   MODEL_RATIO = the final ratio itself (4:5 → "4:5", 9:16 → "9:16", 1:1 → "1:1"). For "4:5 + 9:16", generate both ratios.
4. QA every result (Read it), strictly:
   - text is EXACTLY the approved strings, spelled right, no invented words or badges;
   - product label reads EVERLIFE / RESTORA-Z with Rx box (not garbled), one capsule print reads RESTORA-Z;
   - every text line large (would read on a phone at arm's length);
   - nothing breaks a Hard NO.
   Fail → one automatic re-roll with the fix named in the prompt (≈1 credit, inside the approved batch budget). Still bad → flag it, don't ship.
5. Finish: `$T/finish_batch.py gen.png FINAL_<n>_<framework>.png --ratio 4:5 --product restora-z` (the verbatim
   disclaimer comes from product.json; the older `--disclaimer "<verbatim>"` still works and must match it).
6. Save to `~/Everlife-Creative/output/Restora-Z/<date>_batch-<n>/` (FINAL files + `prompts.md` + `contact_sheet.jpg`), open the
   contact sheet, append headlines to the copy log, and offer: "Another batch?" / "Variations of #k" / "9:16 versions of the winners".

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
Product rules win: women's creative only pinks, tans, beige, cream, mocha, rose, burgundy (no orange, no green);
Restora-Z moods navy / lavender / blush / cream / pale sky. Vary the headline placement too (top-left, centred, bottom-
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
Design a finished, premium static social ad for "Restora-Z", a prescription sleep product, in the style of a modern
DTC wellness brand. Framework: <framework name>: <one-line layout description taken from the reference ad you viewed>.

PRODUCT: image 1 is the real Restora-Z bottle and image 2 the real capsule. Use them exactly: same shape, colours and
label (EVERLIFE vertical wordmark, "RESTORA-Z", white Rx box), label facing camera, sharp, never mirrored, never
redesigned. At most one capsule unless the concept needs a few. Make the bottle a clear hero (about 30–45% of the canvas height).

TYPOGRAPHY & COLOUR (this ad's own look, different from every other ad in the batch): headline in <pairing from the
menu, e.g. "a heavy condensed grotesque in all caps">, with ONE phrase picked out in <accent colour from the palette>;
supporting text in <its partner face>. For readers aged 50+: headline at least 9% of canvas height per line; every other
line at least 3.5%; strong contrast; no thin grey text; max 3 supporting lines.

TEXT: render ONLY these strings, exactly as written, nothing else (no extra words, no logos, no stars, no badges, no prices,
no website, no disclaimer):
  Headline: "<headline>"   (accent on: "<phrase>", in the accent colour named above)
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"
  <Framework-specific text, e.g. Notes title, sticky note words, Myth / Fact labels>

SCENE & STYLE: <scene, props, single colour mood (navy / lavender / blush / cream / pale sky)>, real texture and soft
light, calm and premium, lots of air, nothing cluttered. Women-focused looks: pinks, tans and beige. No beds-with-couples
or bedroom intimacy. Any person: real-looking 45–65, calm, candid, no before/after.

LAYOUT (9:16): keep a 5% clear margin on every edge. The TOP 12% of the canvas is calm, plain continuation of the
background (no text, no product): the Everlife logo is laid there. EVERYTHING ELSE (headline, benefits, bottle, capsule)
sits in the TOP 52% of the canvas; the lowest element ends at 50% height. The BOTTOM 48% is calm, plain continuation of
the background (surface, fabric, wall): no text, no product, no hands or key objects there. The transparent proof footer
is laid at 52–63%; Meta's Reels/Stories UI covers the rest.
LAYOUT (4:5 / 1:1): 5% margin; TOP 10% calm for the logo; BOTTOM 18% calm for the proof footer; product base above that line.
```
> GPT Image 2.5 lands the product 8–15% LOWER than the LAYOUT block asks (batch-4 PT-141, 2026-10-29: "base at 48%" came back at
> 58–65%). Ask for the lowest element at **40%** (cap/nozzle tip at 13%) to get ~50%. `finish_batch.py` then shifts the image up by
> whatever headroom is left under the logo band (max 320 px) before it refuses; a refusal means one reposition edit (1 credit).
```
```

## 4. After the batch
- Contact sheet first, then let the user pick winners. Winners → `9:16` re-make (same prompt, MODEL_RATIO 2:3) only after approval.
- Log each headline + framework in `~/Everlife-Creative/restora-z-copy-log.md`.
- Everything is a draft → creative review → Jeremy. List any borderline line ("Chronic insomnia", "Calms anxiety") in `SESSION.md` for him.

## Legacy (only if the user asks)
`finish_modern.py` (photo + overlaid type templates) and the one-image-at-a-time flow in `image-prompting.md` still work, but
Batch Mode is the default.
