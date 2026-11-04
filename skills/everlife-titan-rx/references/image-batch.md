# Titan-Rx IMAGE ads: Batch Mode (the default for every image request)

> **⛔ NEVER `reposition_916.py`, edge-stretch, blur or padding colour on a raw (Mitansh, 2026-11-02: "why the hell are these things blurry on the edges! Who told you to do that!").** This overrides every older line in this skill that calls `reposition_916.py` "the fix". Finish the raw AS IS: `finish_batch.py <raw> <out> --ratio 9:16 --product <id> --fit trusted --shift 0`. **If its text or product runs into the footer, ALWAYS fix it in code first (Mitansh, 2026-11-02: "make sure to do it always"):** `$T/venv/bin/python -I $T/mirror_fit_916.py <raw> repo/rN.png --top <content top> --bottom <content bottom>` (0 credits: uniform scale into the band 0.115–0.635, margins filled by mirror-tiling a thin text-free edge strip), then the finisher as above on `repo/rN.png`. LOOK at the result. Re-roll (cost approved) ONLY when a person, text or the product touches a side edge of the raw (the mirror would copy it) or the tool refuses (scale < 0.65). Never ship a smeared edge.
> **👀 SHOW FIRST, THEN RE-ROLL (Mitansh, 2026-11-02: "show me first!"):** after a batch, finish what can be finished (as-is or `mirror_fit_916.py`), open the contact sheet and SHOW the user every result (finished + the raws that failed QA, with why). Never start a re-roll on your own QA call, not even the "one automatic re-roll" older lines mention: the user decides which ads to re-roll, with the cost shown.

> Adapted 2026-11-02 from the Spark skill (itself from PT-141). Titan-Rx has ONE form (an oral capsule, once daily) and is for men
> 40–65+. Where this file's history notes mention PT-141, Spark or Lovara batches, they are lessons carried over, not Titan-Rx facts.
> Default ratio: **4:5** (9:16 from the approved masters); default people: product only (the setup's People question).

**🎯 FOCAL-POINT MIX (bible Standards 03, synced 2026-11-03; REPLACES "the pill is the hero, not the bottle" everywhere in this skill):** plan it in the batch table's **Focal** column before writing prompts, like the proof split: **40% pill-focused** (the tablet/capsule is the primary focal point: foreground, sharp, clearly visible; the old "tablet is the hero" wording below applies to THESE slots only) · **30% bottle-focused** (the bottle is the primary focal point: premium product photography, strong composition; the pill may appear smaller or not at all) · **30% person-focused** (a person is the primary focal point: lifestyle, emotion, relatability; product still in focus and identifiable). Batch of 4 = 2 / 1 / 1; batch of 8 = 3 / 3 / 2; odd counts round the pill share up. **Videos use the same split** (Justin, 2026-11-03: "Videos and statics should really be the same in the sense of how we’re presenting products"). Every ad, whatever its focus: product and benefit identifiable in under 2 s, product in focus, nothing covering it (`core/references/creative-system.md` §1).

**Proof split (Mitansh 2026-11-02, from bible Standards 02 · 06):** 30% of ads carry NO proof element; 70% carry a footer proof: of those, 60% the trust row and 40% the Trustpilot 4.9 badge + "Over 100,000 happy customers" (overall ~42% trust / ~28% count / ~30% none; logo + verbatim disclaimer on every ad). Run `finish_batch.py --proof-plan N`, add a **Proof** column to the batch table, and pass it on every finish (`--proof trust` / `--proof count` / `--proof none`, same value on the ad's 4:5 and 9:16), e.g. `finish_batch.py raw.png FINAL.png --ratio 4:5 --product titan-rx --proof count`. Rule: `core/references/creative-system.md` §2. **PROOF SPLIT IS HARD (Mitansh 2026-11-02, no conflicts):** ~42/28/30 per batch and per ratio; proof slots get a clean shelf in the LAYOUT (9:16: product, CTA, sticker, faces end above y 1150 of 1920); never swap a planned proof to "none" yourself (re-roll with cost or ask); `finish_batch.py --proof-check <batch folder>` must pass before showing.

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

## 1. Frameworks (reference ads in the SHARED library `core/references/static-refs/<folder>/`, overview `OVERVIEW.jpg`; which pin for which angle: `reference-guide.md`)
| Code | Framework | Folder | Titan-Rx recipe |
|---|---|---|---|
| F1 | Old way vs New way | 01_Us_vs_Them | "Plan around it" vs "Once-Daily, No Timing Required". Ideas only, no brands, no drug names, no bodies |
| F2 | Bold Claim | 02_Bold_Claim | one huge Tier A headline ("When It’s Go Time, Be Ready") + one capsule (hero) and the bottle + 3 callouts to ✅ benefits |
| F3 | Phone UI | 03_iPhone_Notes_Phone_UI | a reminders/notes screen with one ✅ line per row ("Once-Daily, No Timing Required" as the title); the bottle beside the phone |
| F4 | Features & Benefits | 04_Features_and_Benefits | capsule hero + three rows of ✅ benefits with simple line icons (daily · circulation · readiness) |
| F5 | Before/After | 05_Before_and_After | ❌ **skip**: no bodies, no "before" states for this product |
| F6 | Offer | 06_Offer | ❌ **blocked** until "Save up to 49%" is verified |
| F7 | Review card | 07_Testimonial_Social_Proof | ❌ blocked until `reviews.md` has screened Titan-Rx reviews |
| F8 | Question | 08_Question | pronoun-free question from a ✅ territory ("Ready every day?") + answer line + product |
| F9 | Reasons Why | 09_Reasons_Why_Education | "3-in-1 Performance Formula" numbered: three ✅ benefits (each a different idea); the formula fact "Tadalafil + Vardenafil + L-Arginine" once, small; capsule hero |
| F10 | Sticky Note | 10_Sticky_Notes_To_Do | a note on a gym whiteboard or a fridge ("Train. Eat. Repeat.") next to the bottle; no mirrors with bodies |
| F11 | Visual Metaphor | 11_EXTRA_Visual_Metaphor | one object idea: the capsule on a chalked barbell sleeve, on a steel plate, beside a coiled rope; the bottle on black stone in one hard light |
| F12 | Brand Mood | 12_EXTRA_Brand_Mood_Product_Hero | premium still life matched to the matte black + chrome bottle (black stone, gunmetal, brushed steel, one red accent) or a warm contrast (oak, leather, golden hour), short line |
| F13 | Portrait + line | (people) | only when the People answer allows: a rugged man 40–65, shoulder-up, clothed, candid, in a gym or garage; headline beside the face; capsule + bottle in the lower third. Never a bare torso, never a bed |
| F14 | Article | (creative-system article slot) | an editorial page, kicker "MEN'S PERFORMANCE", Tier A headline, a candid photo (product or a man shoulder-up), product + proof; no fake byline |

**Random (recommended):** N different frameworks (skip F5, F6, F7; F13 only with people), mixing text-heavy (F1, F3, F4, F9) and
visual (F2, F8, F10, F11, F12). Weight towards F2, F11, F12 and one F14 article per 5. No Titan-Rx winners are on hand yet.

## 1b. Creative-system pass (shared, `core/references/creative-system.md`, adopted 2026-10-29)
**Team logs (every batch, `core/team-logs/TEAM-LOGS.md`):** before writing copy, read this product's Copy Ledger rows the lean way (saved to files, then only the `teamlog.py summary` digest; TEAM-LOGS §2.2) (never reuse a logged headline, hook or CTA), the team's recent styles (`pick_styles.py --skip`) and proof split; log each generation to the Prompt & Outcome Log (inputs, exact prompt, refs, QA result); after the batch, log copy, styles, proofs and the run's spend. Unreachable → the pending file, never block. Build every record with `core/scripts/teamlog.py` (it saves the exact prompt and checks the record; TEAM-LOGS §6) and send what `teamlog.py pending <job>` lists, one batch per page, then `teamlog.py sent` (TEAM-LOGS §2.5; a wave is one `teamlog.py gens` call). `teamlog.py close <job>` must print ✅ before SESSION.md.

**Ad Review: read the flags first (`core/ad-review/AD-REVIEW.md` §3):** before the batch table, read this product's flagged ads (losers) and their reasons (saved to files; the same `teamlog.py summary` digest). Never repeat a flagged recipe (hook / headline + style + scene); a compliance flag bans anything close. Turn the top reasons into explicit checks for this batch, name them under the table, check them in QA. Unreachable → "no flags read", carry on.

Before the batch table, check every slot against the shared system: a different **structure** per slot (split, stacked panels,
timeline, poster, billboard, calendar, type-only, article), at least one **article-style** slot per 5, a different **product angle**,
a **named typeface**, an **own palette**, a rotating **product-name treatment** and **headline placement**; the form's hero
(`product.json → hero`) at **≥ 35% of the canvas width**, real and label-wrapped, with `hero.never` written into the prompt; the CTA
and every line as exact strings in TEXT (then QA'd); "NO logo or wordmark anywhere" (or an empty masthead box for `logo_in_box.py`).
Finishing: `reposition_916.py` (free, local) when anything dips into the footer; `unfade_cta.py` when a CTA sits just above it;
`finish_batch.py --logo-w 40%` for the large real logo; 9:16 only via `compose916.py` from the approved 4:5. Checklist at the end of
that file.

## 2. Flow (the two setup rounds live in SKILL.md step 1; here: write, critique, approve, generate)
1. Inputs from SKILL.md step 1: hook angle, boldness, CTA, mood, copy density, people, how many. Placement is 4:5
   (9:16 comes from the approved masters). Frameworks: random mix unless the user named some in chat. No offer.
2. Read the bible + copy log (one cat). Per slot: pick a framework, **look at 1 reference ad** (the framework folder; layout only,
   never the words or the scene). Write concept (1 line), headline (Tier A by default; Tier B only within the chosen boldness),
   supporting lines per the chosen copy density (0, 1 or 3; ✅ claims, exact), the chosen mood, prompt. Show ONE table:
   # · framework · person? · territory · headline · tier (A / B PROPOSED) · supporting lines · type & colour · ≈1 credit.
   **Persona pass before the table** (`personas.md`): read every slot as Skeptical Mike and Grounded Ray; no ingredient claims; no
   two supporting lines sharing a noun ("performance" ×3 is the Mike trap); no hype words; nothing couch-unsafe. Add a one-line
   "Mike says" under the table for any slot you changed.
   AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". **That click approves the batch and
   its Tier A lines; each Tier B line needs its own explicit OK first** (ask before the generate question).
3. Generate: `composer_edit_image(project_id, prompt, images=[<titan-rx_bottle_ref>, <titan-rx_capsule>], out='gen/b<date>_<n>.png',
   aspect_ratio=<final ratio>)` for the default model; Nano Banana → §2c (Model Playground tools) from `assets/creatify.json`. Max 4 in flight.
4. QA every result (Read it), strictly: text EXACTLY the approved strings; "TITAN-RX" big and on one line; the Titan-Rx bottle's label
   matches the render (not garbled, not mirrored); the **capsule is identical to the capsule render** (chrome, TITAN-RX print) and
   there is exactly one (no invented pill); **the capsule is the hero: larger in frame than the bottle** (Spark's test batch failed
   this 4/4: fix with a 1-credit edit); every line big enough for 50+; a man (if any) looks 40–65, clothed, no bare torso, candid,
   shoulder-up/waist-up, **no bed or bedroom anywhere in frame**; no model-drawn Everlife logo; no price or "% off"; nothing breaks a
   Hard NO. **Text or product in the bottom 22% → fix** (the 4:5 finisher does not refuse it).
   Fail → one fix edit naming the problem (1 credit, within the batch approval). Still bad → flag, don't ship.
5. Finish: `$T/venv/bin/python -I $T/finish_batch.py gen.png FINAL_<n>_<framework>.png --ratio 4:5 --product titan-rx`
   (the verbatim disclaimer comes from product.json).
6. Save to `~/Everlife-Creative/output/Titan-Rx/<date>_batch-<n>/` (FINALs + `prompts.md` + `contact_sheet.jpg`),
   open the contact sheet, log the headlines, offer "Another batch?" / "Variations of #k" / "9:16 of the winners".

## 2b. Type & colour: be different every time (creative lead, 2026-10-28)
Fonts and colours are **not** house-locked. Every ad in a batch gets its own pairing and its own accent; never two alike
in one batch, never the same look two batches in a row, and never default to the old "serif + purple accent" specimen.
Pick per ad and write it into the prompt's TYPOGRAPHY & COLOUR block (legibility rules still apply: 50+ readers, no
shadows or outlines on type, product name big).

| Headline face (pick one) | Partner for supporting text |
|---|---|
| Heavy condensed grotesque, all caps | light humanist sans |
| Bold high-contrast serif, roman (no italic) | clean geometric sans |
| Stencil / industrial sans, all caps | small-caps sans |
| Wide extended sans, bold | regular sans |
| Slab serif, bold | light sans |
| Chunky rounded sans | mono-spaced labels |
| Bold grotesque with ONE word in the red accent | regular sans |
| Thin editorial sans, tracked out, all caps | serif body |

Accent colour: take it from the scene or the product, never from habit. Options: the label red, brass/gold, deep navy,
charcoal on cream, cream on charcoal, ink on sand, forest, teal, sky, slate, mocha, rose, blush, burgundy, warm white.
Product rules win: Titan-Rx has no palette limit (the bible's women's palette applies only to GHK-Cu Cream and Glow Stack). Default
**dark and forged** (the bottle's matte black + chrome, one red accent from the chevron); one warm, sun-lit ad per batch of 4 keeps
variety (bible imagery: "warm, sun-lit"). Avoid supplement-bro looks (flames, lightning, neon red on black). Men's headlines never
elegant italic serif or script (inherited rule): prefer heavy condensed grotesque, wide extended sans, slab serif, tracked thin sans.
Vary the headline placement too (top-left, centred, bottom-third above the footer band, split either side of the product) and the
light (dawn, hard gym light, golden hour, overcast soft, studio).

No type specimen ships with this skill: the §2b pairing named in the prompt does the work.

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
Design a finished, premium static social ad for "Titan-Rx", a doctor-prescribed, once-daily men's performance prescription (one
oral capsule), in the style of a modern DTC men's health brand (Hims/Ro-level premium). Framework: <name>: <layout from the
reference ad>.

PRODUCT: image 1 is the real bottle and image 2 the real capsule. Use the attached capsule reference exactly; do not invent, alter,
or substitute a different pill; exactly one capsule. **The capsule is the hero:** large, in focus, in the foreground close to the
lens, at least 25% of the canvas width and visibly LARGER in frame than the bottle; the bottle sits smaller behind or beside it,
label legible, never covered by the capsule. Use the attached bottle reference exactly: same shape, colours and label, label facing
camera, sharp, never mirrored, never redesigned; the label wraps around the bottle. It is a matte black bottle with a black cap and
chrome rings; the label reads EVERLIFE, then a large brushed-chrome TITAN-RX with a red chevron in the A, then TADALAFIL +
VARDENAFIL + L-ARGININE, 3-IN-1 INTIMACY SUPPORT FOR MEN, a chrome male symbol and 30 CAPSULES. Show ONLY this bottle and ONE
capsule: no other product, no other pills. The product is large and legible.

TYPOGRAPHY & COLOUR (this ad's own look, different from every other ad in the batch): headline in <pairing from §2b>, with ONE
phrase picked out in <accent colour>; supporting text in <partner face>. For readers aged 50+: headline at least 9% of canvas
height per line; every other line at least 3.5%; strong contrast; no thin grey text; max 3 supporting lines. Product name on one
line, never hyphen-broken. No shadows or outlines on type.

TEXT: render ONLY these strings, exactly, nothing else (no extra words, no Everlife or other logos or wordmarks, no 'by Everlife',
no stars, badges, prices, percentages, website or disclaimer):
  Name: "TITAN-RX"   (big and bold: one of the two largest texts in the ad, on one line; as the product logotype: wide brushed-chrome
                      capitals with a small red chevron inside the A, like the bottle)
  <pills density only> Pills: "<✅ line 1>" / "<✅ line 2>" / "<✅ line 3>"   (three rounded outline pills, each with a simple line icon)
  Headline: "<headline>"   (accent on: "<phrase>", in the accent colour named above)
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"
  <CTA, when the framework has one: "<the session's CTA>">

SCENE & STYLE: <scene: a hardcore gym, a garage gym, a workshop, a kitchen counter, a terrace; never a bedroom>, real texture and
depth (never a flat colour), real light, calm, strong and premium. <PERSON, only when the People answer allows: a man 40–65,
rugged, strong and unmistakably masculine with a hardcore-training feel (fit, not a bodybuilder), fully clothed in <training tee /
hoodie / flannel / work jacket>, candid, framed head-and-shoulders or waist-up; not posed as a model, not flexing; an ordinary,
non-famous face that does not resemble any celebrity.> <palette: the §2b mood chosen for this ad; the bottle's matte black + chrome
works on black stone, gunmetal and brushed steel, and contrasts on warm oak, leather, sand or concrete in daylight.> No bed, no
bedroom, no lingerie, no bare torso, no body shots, no couples in bed, no before/after, no needles, syringes or vials, no fire or
lightning effects, no mirrors showing bodies.

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
> 58–65%). Ask for the lowest element at **40%** (cap tip at 13%) to get ~50%. `finish_batch.py` then shifts the image up by
> whatever headroom is left under the logo band (max 320 px) before it refuses; a refusal means one reposition edit (1 credit).

QA that the label is the Titan-Rx label. Never describe the capsule's shape, colour or markings in words beyond
"use the attached capsule reference exactly".

## 4. After the batch
- Contact sheet first, then let the user pick winners. Winners → the other ratio only after approval.
- **Post every finished ad (Ad Review, `core/ad-review/AD-REVIEW.md` §4):** after finishing, write each finished creative as an `entry` with its preview (no rating, no question to the operator), then `teamlog.py posted <job> <ad_id…>`. Reviewers flag the losers later; winners come from the data.
