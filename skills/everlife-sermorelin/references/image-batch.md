# Sermorelin IMAGE ads: Batch Mode (the default for every image request)

> **⛔ NEVER `reposition_916.py` / shrink / edge-stretch / blur a raw (Mitansh, 2026-11-02: "why the hell are these things blurry on the edges! Who told you to do that!").** This overrides every older line in this skill that calls `reposition_916.py` "the fix". Finish the raw AS IS: `finish_batch.py <raw> <out> --ratio 9:16 --product <id> --fit trusted --shift 0`. If its text or product runs into the footer, the raw is a FAIL: re-roll it with the LAYOUT block (ask for the lowest element at 40%, top 12% empty), with the cost approved. Never ship a smeared edge.

Same machine as the Restora-Z and Sermorelin GHK batches (creative lead, 2026-10-27: "speed, Creatify, batches of at least
5 different types, mobile friendly, easy to read for older people"). GPT Image 2.5 on Creatify designs the **whole ad**
with the real bottle and tablet; `finish_batch.py` adds only the Everlife logo and the approved footer (Trustpilot 4.9 /
Doctor Prescribed / Ships Free art, verbatim disclaimer) as a compact transparent strip over the calm bottom band
(prompt asks for 22%).

**Blocked until the renders exist** (`assets/MISSING_RENDERS.md`) and `assets/creatify.json` has a project.

## 0. Copy rules: hard stops vs references
**Hard stops:**
- Claims: only the ✅ approved benefits in `product-bible.md` (clean pool). Pre-screen ❌ lines never; ⚠ lines only with
  the user's explicit OK + flagged for Jeremy.
- No body composition, fat, "dad bod", "melt/burn/ripped/shred", no "physique transformation", no body before/after, no
  shirtless heroes, no age-reversal ("the new 40") unless Jeremy clears it.
- "growth hormone" spelled out; never imply the tablet *is* growth hormone; "easy sublingual delivery"; no needles,
  injections or vials; no "all natural"; never "GHK", "Citrulline" or "3-in-1" (that's the other product).
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically studied" for the product, no
  "Breaking News".
- Offer: only "Save up to 65%" (percent, never a $ price unless the brief is a price test; never "vs HGH" without Jeremy).
- Proof wording exact; disclaimer verbatim (the footer handles both).

**Headline tiers:**
- **Tier A (default):** a headline from the chosen audience page's clean pool (`product-bible.md`), word for word or
  lightly trimmed. Never a "Weak headline", "Hard NO conflict" or pre-screen ❌/⚠ line.
- **Tier B (max 2 per batch):** fresh wording whose every claim maps to a ✅ benefit. Mark it **PROPOSED**; it needs the
  user's explicit OK for that exact line (not the batch click) and goes in SESSION.md as "Tier B, needs Jeremy".
- Never repeat a headline in the copy log. **The Tier A pool is very small** (3 men's, 4 women's): say so up front and ask
  whether to allow Tier B, use a ⚠ line with the user's OK, or request new approved headlines from Jeremy.

## 1. Frameworks (references: see §2 priority order; generic set in `core/references/static-refs/<folder>/`, overview `OVERVIEW.jpg`)
| Code | Framework | Folder | Sermorelin recipe |
|---|---|---|---|
| F1 | Old way vs New way | 01_Us_vs_Them | "Old routine" (more coffee, more pre-workout) vs "Doctor-prescribed Sermorelin, easy sublingual delivery". Categories only; no HGH, injections or bodies |
| F2 | Bold Claim | 02_Bold_Claim | one huge approved headline + tablet hero + up to 3 callouts to ✅ benefits |
| F3 | Phone UI | 03_iPhone_Notes_Phone_UI | Notes checklist ("Morning training / Energy / Strength") of ✅ benefits; bottle beside the phone |
| F4 | Features & Benefits | 04_Features_and_Benefits | tablet hero + three rows: the three ✅ benefits, one icon each |
| F5 | Before/After | 05_Before_and_After | ❌ **skip**: body before/after is banned; a "routine" contrast belongs in F1 |
| F6 | Offer | 06_Offer | "Save up to 65%" + tablet + bottle, one ✅ benefit line |
| F7 | Review card | 07_Testimonial_Social_Proof | ❌ blocked until `reviews.md` has screened plain-Sermorelin reviews |
| F8 | Question | 08_Question | pronoun-free question from an approved territory ("Low on energy by 3 p.m.?", "Lost a step at the gym?") + answer line + product |
| F9 | Reasons Why | 09_Reasons_Why_Education | "3 reasons it's on the counter": doctor prescribed · easy sublingual delivery · supports natural growth hormone activity |
| F10 | Sticky Note | 10_Sticky_Notes_To_Do | sticky note on a gym bag / bathroom mirror ("Tomorrow: 6 a.m. hike") next to the bottle |
| F11 | Visual Metaphor | 11_EXTRA_Visual_Metaphor | one object idea: the tablet as a barbell collar, the tablet on a stopwatch, the bottle in a dumbbell rack |
| F12 | Brand Mood | 12_EXTRA_Brand_Mood_Product_Hero | premium still life (warm stone, chalk, linen), one colour mood, short serif line |

**Random (recommended):** N different frameworks (skip F5, F7), mixing text-heavy (F1, F3, F4, F9) and visual (F2, F8,
F10, F11, F12). **Slot 1 is always F2 as "tablet in hand"** (a real 45+ hand holding ONE tablet to the lens + a huge
condensed Tier A headline): the all-time winners' format (~1,500 sales, `winners/winners.md` ⭐); it counts as one of
the ≥ 3 winner slots (§2 step 2). Then weight towards F4, F11, F6, F12 (name/tablet hero).

## 2. Flow (1 question, then generate)
> **🎨 STYLES = `core/references/style-library/MOOD-QUESTION.md` (Mitansh 2026-11-02; replaces the Frameworks options below):** 1 "🎲 Surprise me (Recommended)" = a random style per ad from the 15 Drive styles, different every batch (`core/scripts/pick_styles.py`) · 2 "📚 Pick from the 15 styles" (the follow-up picker). The F-framework table stays as a fallback. Each slot Reads its style board (`core/references/style-library/STYLES.md`): layout only, this skill's claims, palette and product rules win.
1. **One AskUserQuestion** (audience is already set in SKILL.md step 1): **How many?** "5 (Recommended)" / "10" / "15" ·
   **Placement:** "4:5 Feed (Recommended)" / "9:16" / "4:5 + 9:16" / "1:1" · **Frameworks:** "🎲 Random mix (Recommended)" / "Pick frameworks" · **Look:** "Standard: winners + frameworks (Recommended)" / "✨ Ultra premium, product only" (Hims/Ro codes on every slot:
   `core/references/ultra-premium.md`; overrides winners-first and people, tablet stays the hero).
2. Read the bible + copy log + `winners/winners.md` (one cat). **Winners first, then frameworks** (hand-off from the GHK
   skill, 2026-10-29; rule `core/references/REFERENCE-PRIORITY.md`):
   - **At least 3 of every 5 slots (6 of 10, 9 of 15) start from a winner for this audience**: pick the winner first,
     take its framework, look at its card + preview (⭐ all-time: tablet in hand M2/M5/M6/F2, name/tablet hero F1/F4;
     weekly: M5 name lockup, M3 features & benefits + offer, M2 visual metaphor). A different winner per slot; if the
     audience has fewer usable winners (women have few), use them all and say so in the table.
   - "Both" audiences: count per audience (men's slots from M winners, women's from F winners).
   - Only the remaining slots pick a framework first and look at 1 reference: a matching winner if one is left → a Meta
     Ad Library ref in `core/references/meta-refs/<framework folder>/`, if any → a Pinterest ref: this skill's
     `references/pinterest/<framework folder>/` first (read its `SOURCES.md` row: what to take, what not to copy), then
     `core/references/static-refs/<framework folder>/`.
   Follow the "Don't copy" lists. Record the source for each ad in `prompts.md` and SESSION.md. Write concept (1 line),
   headline (Tier A by default), ≤ 3 supporting lines (✅ benefits, exact), its font + colour (§2b), prompt. Show ONE
   table: # · source (winner ID / Meta / Pinterest file) · framework · territory · headline · tier (A / B PROPOSED) ·
   supporting lines · font / colour · ≈1 credit, with a count line above it ("3 winners · 2 Pinterest").
   AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". **That click approves the batch and
   its Tier A lines; each Tier B or ⚠ line needs its own explicit OK first** (ask before the generate question).
3. Generate: `composer_edit_image(project_id, prompt, images=[bottle, tablet] (add type_specimen only for the house
   editorial look, §2b), out='gen/b<date>_<n>.png', aspect_ratio=<final ratio>)` from `assets/creatify.json`. Max 4 in flight.
   **The tablet is HELD** (bible v3 page 4): between thumb and index finger in a "pull" toward the camera, or resting in
   an open palm; sharp, foreground, **beside the bottle, never covering its label**. Vary the hold per ad (fingertips
   raised to the lens, open palm low in frame, hand beside the face, palm up on a bench, two fingers offering it
   forward); never the same hold or angle twice in a batch. No two ads in a batch share a framework or an accent colour.
   **Every ad gets its own person** (Priestley, 2026-10-29: "why the same guy in every picture?"; batch 2 used one
   casting line 5 times and got one face 5 times). Write a different CAST per ad and never paste the same description
   twice: vary age within the range (men 42–50, women 40–58), ethnicity, hair (colour, length, grey level, shaved),
   beard/stubble/clean-shaven, build within the brief, wardrobe colour. Add each ad's casting to the planning table.
   Every cast line ends "an ordinary, non-famous face; must not resemble any celebrity" (a video drew a Stallone
   look-alike, 2026-10-29); QA rejects any celebrity likeness.
4. QA every result (Read it), strictly: text EXACTLY the approved strings; "SERMORELIN" present and one of the two
   biggest pieces of text (bible: "Product names run big"; Priestley, 2026-10-29: a small name line counts as "no
   product name"), and **no "by Everlife"** anywhere; no two ads in the batch show the same-looking person; the bottle
   label matches the render (not garbled, not mirrored); the **tablet is identical to the tablet render** (no invented
   pill, not the other past tablet shape), held, at least ~15% of the canvas width (17% when a person shares the frame);
   **no vial, syringe or second container**; every line big enough for 50+; men 42–50, hardcore fitness-model build,
   fitted top, never shirtless or flexing; women 40–60, clothed; men's headline not in an elegant/italic serif or script;
   women's batch: ≤ 1 pink-led ad, ≥ 1 teal ad, advertorials on white, ≤ 2 of 5 "explore" colours; no Everlife logo or
   wordmark drawn by the model (finishing adds the real one); nothing breaks a Hard NO.
   Fail → one automatic re-roll naming the fix. Still bad → flag, don't ship.
5. Finish: `$T/venv/bin/python -I $T/finish_batch.py gen.png FINAL_<n>_<framework>.png --ratio 4:5 --product sermorelin`
   (the verbatim disclaimer comes from product.json).
6. Save to `~/Everlife-Creative/output/Sermorelin/<date>_batch-<n>/` (FINALs + `prompts.md` + `contact_sheet.jpg`),
   open the contact sheet, log the headlines, offer "Another batch?" / "Variations of #k" / "9:16 of the winners".

## 2b. Type & colour: different every time (creative lead 2026-10-28; men's rule + Justin's women's colours 2026-10-29)
Fonts and colours are not house-locked. Every ad in a batch gets its own pairing and accent; never two alike in a batch,
never the same look two batches running. Write it into the prompt's TYPOGRAPHY & COLOUR block (50+ legibility, no
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

**Men's ads:** never the elegant serif, the serif with an italic word, or the brush/handwritten accent (reviewer,
2026-10-29: "men shouldn't use that font"). Men pick from heavy condensed grotesque (every men's winner), wide extended
bold sans, bold slab serif, chunky bold sans. The serif rows stay available for women.

Accent colour: from the scene or the product, never from habit (the label orange, brass/gold, deep navy, charcoal on
cream, cream on charcoal, ink on sand, forest, teal, sky, slate, mocha, rose, blush, burgundy, warm white). Bible v3
sets no palette limit for Sermorelin.
**Women (Justin's direction, 2026-10-29, "preferred options, not strict limitations"):**
- No colour is banned. Preferred (they have performed): pinks, tans, neutrals, warm tones, **white** and **teal**; most
  ads in a women's batch lead with one of these.
- Up to 2 of every 5 women's ads explore a current colour or type trend that suits the concept.
- Advertorial / article ads sit on a **white** background.
- At least one teal-led or teal-accent ad per women's batch; keep the teal soft/pale so it sets off the orange label.
- At most one pink-led ad per batch; no two women's ads with the same lead colour.
Vary the headline placement (top-left, centred, bottom third above the footer band, split around the product) and the
light (morning, golden hour, soft overcast, studio).

The type specimen (`assets/type_specimen.png`) is not attached by default: only when the brief asks for the house
editorial look, and then say "match image 3".

## 3. Prompt template (fill everything; keep the quotes exact)
```
Design a finished, premium static social ad for "Sermorelin", a doctor-prescribed sublingual peptide tablet, in the
style of a modern DTC wellness brand. Framework: <name>: <layout from the reference ad you viewed>.

PRODUCT: image 1 is the real bottle and image 2 the real tablet. Use the attached tablet reference exactly; do not
invent, alter, or substitute a different pill. Use the attached bottle reference exactly: same shape, colours and label,
label facing camera, sharp, never mirrored, never redesigned; the label wraps around the bottle and follows its angle.
The TABLET is the hero: real tablet only (never glowing orbs, spheres or icons), large, in focus, foreground, at least
15% of the canvas width, HELD <this ad's hold: between thumb and index finger pulled toward the camera / resting in an
open palm / …>, beside the bottle and never covering its label. The bottle is large and legible (at least 30% of the
canvas height). Show ONLY this bottle and tablet: no vial, no second container. ARRANGEMENT for this ad: <its own
product arrangement, different from every other ad in the batch>.

TYPOGRAPHY & COLOUR (this ad's own look, different from every other ad in the batch): headline in <pairing from §2b,
e.g. "a heavy condensed grotesque in all caps">, with ONE phrase picked out in <accent colour>; supporting text in <its
partner face>. For readers aged 50+: headline at least 9% of canvas height per line; every other line at least 3.5%;
strong contrast; no thin grey text; max 3 supporting lines. Never split or hyphenate "Sermorelin".

TEXT: render ONLY these strings, exactly, nothing else (no extra words, no Everlife or other logos or wordmarks, stars,
badges, prices, website, disclaimer):
  Name: "SERMORELIN"   (big; every ad. Never add "by Everlife" on images: Priestley, 2026-10-29; the finisher adds the Everlife logo)
  Headline: "<headline>"   (accent on: "<phrase>", in the accent colour named above)
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"

SCENE & STYLE: <scene>, real texture and depth (never a flat colour), warm sun-lit light, premium.
<MEN: palette <this ad's own>; any person: <THIS ad's own man: age 42–50, ethnicity, hair, beard, wardrobe colour,
all different from every other ad in the batch>, a fit silver fox with a hardcore fitness-model physique (visibly
muscular, lean, athletic; tattoos optional), rugged and confident, fully clothed in a fitted training tee or long
sleeve, no bare torso, no flexing poses; a real gym or hard training.>
<WOMEN: lead colour <this ad's own per §2b: pinks / tans / neutrals / warm tones / white / soft teal, or an "explore"
trend colour for up to 2 of 5; white background for advertorials; pink-led at most once per batch>; any person: <THIS
ad's own woman: age 40–58, ethnicity, hair, wardrobe, all different from every other ad>, natural fit build, candid,
clothed.> No bedroom, no shirtless, no before/after, no needles, syringes or vials, no
mirrors showing bodies.

LAYOUT (4:5 / 1:1): 5% clear margin on every edge. The TOP 14% is calm continuation of the background (no text, no
product): the Everlife logo is laid there. The BOTTOM 22% is calm continuation of the background (no text, product or
hands): the proof footer is laid there. The whole product (bottle, tablet, hands, plinth tops) ends ABOVE 72% of the
canvas height and all text above 76%.
LAYOUT (9:16, same as Sermorelin GHK: "use as much of the artboard as possible around the safe zones"): the TOP 12% is
calm continuation of the background (the Everlife logo is laid there). ALL TEXT (name, headline, lines, badges) stays
inside the central column (15% in from the left and right edges). PICTURES are full-bleed: the product, hands, person and
scene may use the whole width and come down to 56% of the canvas height (the model lands ~8% lower; the Trustpilot row
sits at ~67–72%). Below that, the scene simply continues (floor, surface, fabric) with no text, product or hands: Meta's
UI and the bottom disclaimer sit there.
```
Ask high on purpose: GPT Image 2.5 on Creatify places the product lower than asked (GHK batch 4, 2026-10-29: "between
45% and 78%" needed 6 reposition edits in 7; "ends above 72%" needed 0 in 3; PT-141 batch 4: "base at 48%" came back at
58–65%, so 9:16 asks for 40% to land near 50%).

**9:16 statics: proof row inside the Reels safe area, disclaimer alone at the bottom** (Mitansh's PR #5 + the GHK team
feedback in PR #7, 2026-10-29). Meta's caption and "Learn more" button cover the bottom 535 px of a Reel, so the
Trustpilot / Doctor Prescribed / Ships Free row ends at y 1385 (~67–72% of the frame), and the verbatim disclaimer sits
alone at the very bottom, full width, always 2 lines (`"disclaimer_at": "bottom"` in product.json; flagged for Jeremy:
Reels' UI can partly cover it). Source of truth: `core/tools/safezones.py` and `core/references/safe-zones/`: if their
numbers change, follow them, not this note. `finish_batch.py` refuses (exit 2) a 9:16 raw whose content runs under the footer; fix = ONE
reposition edit (1 credit): "Keep everything identical (headline, type, colours, product, scene, light). Scale the
product and the text block down together (about 35%) and move them up so the lowest element ends at 50% of the canvas
height. Fill the bottom half with calm, plain continuation of the same background: no text, no product, no hands."
4:5 and 1:1 are unaffected.
Bottle wording for the PRODUCT block, per strength (both: "amber glass jar with a black ribbed cap; orange label with the
vertical white EVERLIFE wordmark, a white 'RX' box top right, a white band 'SERMORELIN', small text 'PRESCRIPTION',
'30 SUBLINGUAL TABS'"), plus:
- **1000 mcg** (checked against `assets/sermorelin1000_bottle.png`, 2026-10-28): '1000 MCG'.
- **500 mcg** (checked against `assets/sermorelin500_bottle.png`, 2026-10-29): '500 MCG'.
QA that the label shows the session's strength. Never describe the tablet in words.
