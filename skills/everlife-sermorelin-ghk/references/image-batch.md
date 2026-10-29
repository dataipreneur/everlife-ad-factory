# Sermorelin GHK IMAGE ads: Batch Mode (the default for every image request)

Same machine as the Restora-Z batch (creative lead, 2026-10-27: "speed, Creatify, batches of at least 5 different types,
mobile friendly, easy to read for older people"). GPT Image 2.5 on Creatify designs the **whole ad** with the real bottle
and tablet; `finish_batch.py` adds the Everlife logo at the TOP and the approved proof footer (Trustpilot 4.9 / Doctor
Prescribed / Ships Free art, verbatim disclaimer) as a compact transparent strip over the calm bottom ~18%.

**Blocked until the renders exist** (`assets/MISSING_RENDERS.md`) and `assets/creatify.json` has a project.

## 0. Copy rules: hard stops vs references
**Hard stops:**
- Claims: only approved quick-hit benefits, more approved benefits, or a per-ingredient claim on its OWN ingredient
  (Sermorelin / GHK / L-Citrulline Malate). Pre-screen ❌ lines never; ⚠ lines only with the user's explicit OK + flagged for Jeremy.
- No body composition, fat, "melt/burn/ripped/shred", no "physique transformation", no body before/after, no shirtless heroes.
- "GHK" only (never -Cu / copper peptide); "growth hormone" spelled out; "easy sublingual delivery"; no needles; no "all natural".
- No "Are you/Do you…?" questions, no first person, no named competitors, no "clinically studied" for the product.
- Offer: only "Save up to 47%" (percent, never a $ price).
- Proof wording exact; disclaimer verbatim (the footer handles both).

> ⚠ **PENDING CREATIVE-LEAD CONFIRMATION**: headline rule changed 2026-10-28 at Priestley's request (original in
> `_originals/2026-10-28/`), to match the global gate (CLAUDE.md ranks above skills: headlines only from the bible/brief,
> new hooks need explicit approval). Remove this note once the creative lead and Jeremy confirm, or revert if they don't.

**Headline tiers:**
- **Tier A (default):** a headline from the chosen audience page or its headline bank, word for word or lightly trimmed;
  never a "Weak headline", "Hard NO conflict" or pre-screen ⚠ line (e.g. "Forge a Stronger Physique", "Lean. Defined. Glowing.").
- **Tier B (max 2 per batch):** fresh wording whose every claim maps to an approved claim, **or** a winner's headline
  that isn't in the bible (e.g. "Support your strongest era", "Lean. Strong. Ready."). Mark it **PROPOSED**; it needs the
  user's explicit OK for that exact line (not the batch click) and goes in SESSION.md as "Tier B, needs Jeremy".
- **Reuse (Priestley, 2026-10-29: the approved pool is used up):** a bible headline or CTA may be reused across batches,
  least-recently-used first (check the copy log); never twice in one batch; never with the same framework/layout it had
  before. New lines only as Tier B (max 2, approved line by line). Ask Justin for fresh headlines when the pool feels stale.
- Facts: Citrulline is NOT a peptide ("2 peptides + 1", never "3 peptides").

## 1. Frameworks (reference ads in `core/references/static-refs/<folder>/`, overview `OVERVIEW.jpg`)
| Code | Framework | Folder | Sermorelin GHK recipe |
|---|---|---|---|
| F1 | Old way vs New way | 01_Us_vs_Them | "Old routine" (more reps, more coffee, more serums) vs "3-in-1 peptide support". Categories only, no brands, no bodies compared |
| F2 | Bold Claim | 02_Bold_Claim | one huge approved headline + tablet hero + 3 callouts to approved benefits |
| F3 | Phone UI | 03_iPhone_Notes_Phone_UI | Notes checklist ("Training plan / Skin routine / Energy") of approved benefits; bottle beside the phone |
| F4 | Features & Benefits | 04_Features_and_Benefits | "3-in-1" tablet hero, three rows: each ingredient + ONE of its own ✅ claims |
| F5 | Before/After | 05_Before_and_After | ❌ **skip**: body before/after is banned; a "routine" contrast belongs in F1 |
| F6 | Offer | 06_Offer | "Save up to 47%" + tablet + bottle, one approved benefit line |
| F7 | Review card | 07_Testimonial_Social_Proof | ❌ blocked until `reviews.md` has screened Sermorelin GHK reviews |
| F8 | Question | 08_Question | pronoun-free question from an approved territory ("Lost a step at the gym?", "Skin looking tired?") + answer line + product |
| F9 | Reasons Why | 09_Reasons_Why_Education | "3 reasons it's 3-in-1": one ✅ claim per ingredient, numbered, tablet hero |
| F10 | Sticky Note | 10_Sticky_Notes_To_Do | sticky note on a gym bag / bathroom mirror ("Tomorrow: 6 a.m. lift") next to the bottle |
| F11 | Visual Metaphor | 11_EXTRA_Visual_Metaphor | one object idea: the tablet on a barbell collar, three tablets as a podium "1-2-3", a dumbbell rack with the bottle in it |
| F12 | Brand Mood | 12_EXTRA_Brand_Mood_Product_Hero | premium still life (warm stone, chalk, linen), one colour mood, short serif line |

**Random (recommended):** N different frameworks (skip F5, F7), mixing text-heavy (F1, F3, F4, F9) and visual (F2, F8,
F10, F11, F12). Weight towards F2, F4, F11, F6.

## 2. Flow (1 question, then generate)
1. **One AskUserQuestion** (audience is already set in SKILL.md step 1): **How many?** "5 (Recommended)" / "10" / "15" ·
   **Placement:** "4:5 Feed (Recommended)" / "9:16" / "4:5 + 9:16" / "1:1" · **Frameworks:** "🎲 Random mix (Recommended)" / "Pick frameworks".
2. Read the bible + copy log + `winners/winners.md` (one cat). **Winners first, then frameworks** (Priestley, 2026-10-29):
   - **At least 3 of every 5 slots (6 of 10, 9 of 15) start from a winner for this audience**: pick the winner first, take
     its framework, look at its card + preview image (M8/M2 bold claim, M3 offer + callouts, M4 features & benefits,
     M9 identity post, M10 tablet in hand, F2 brand mood, F1 article, F3 letter, F5 animated). Use a different winner per
     slot; if the audience has fewer usable winners than that, use them all and say so in the table.
   - "Both" audiences: count per audience (men's slots from M winners, women's from F winners).
   - Only the remaining slots pick a framework first (for variety, or a framework no winner covers) and **look at 1
     reference ad** for it: a matching winner if one is left; else a Meta ref
   (`core/references/meta-refs/<framework folder>/`, if any); else a Pinterest ref: this skill's `references/pinterest/<framework folder>/`
   first (read its `SOURCES.md` row: what to take, what not to copy), then `core/references/static-refs/<framework folder>/`. Rule: `core/references/REFERENCE-PRIORITY.md`. Follow the card's "Don't copy" list. Write concept
   (1 line), headline (Tier A by default, see §0 ⚠ pending), ≤ 3 supporting lines (approved claims, exact), prompt. Show
   ONE table: # · source (winner ID / Meta / Pinterest file) · framework · territory · headline · tier (A / B PROPOSED) ·
   supporting lines · ≈1 credit, with a count line above it ("3 winners · 2 Pinterest").
   AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". **That click approves the batch and
   its Tier A lines; each Tier B line needs its own explicit OK first** (ask before the generate question).
3. Generate: `composer_edit_image(project_id, prompt, images=[bottle, tablet]  (add type_specimen only for the house look, see §2b), out='gen/b<date>_<n>.png',
   aspect_ratio=<final ratio>)` from `assets/creatify.json`. Max 4 in flight.
   **Always attach the bottle AND the tablet** (Priestley, 2026-10-28): our winners show both, and without the bottle the ad
   doesn't say what's for sale. The tan tablets inside the bottle render are a known issue (`assets/MISSING_RENDERS.md`):
   keep using the render until design or the pharmacy confirms a corrected one; never drop the bottle to avoid it, and
   flag it in the session sheet.
   **The tablet is HELD** (bible v3, 2026-10-29): between thumb and index finger in a "pull" toward the camera, or
   resting in an open palm, sharp and in the foreground, beside the bottle (never covering its label). **Vary the hold per
   ad** (Restora feedback, Berna): fingertips raised to the lens, open palm low in frame, hand beside the face, hand
   resting on a bench with the palm up, two fingers offering it forward…; never the same hold or angle twice in a batch. **No two ads in a batch share a framework or an accent colour.**
4. QA every result (Read it), strictly: text EXACTLY the approved strings; the bottle label matches the render (not garbled,
   not mirrored) and the **tablet is identical to the tablet render** (no invented pill); every line big enough for 50+;
   people look 40s–50s (men: hardcore fitness-model build, fitted top, never shirtless), clothed; "SERMORELIN GHK by Everlife" present; the tablet held (fingers or palm); women's batch: at most one pink-led ad, at least one teal ad, advertorials on white, no more than 2 of 5 "explore" colours (Justin, 2026-10-29); nothing breaks a Hard NO;
   the tablet is the real tablet, never replaced by glowing orbs, glass spheres or icons, and at least ~15% of the canvas
   width; the bottle label follows the bottle's curve and angle (not pasted flat); "Sermorelin" and "GHK" never split
   across lines or syllables; a benefits block has exactly 3 points; no Everlife logo or wordmark drawn by the model
   (finishing adds the real one);
   **the bottle is in shot, large, with "SERMORELIN GHK" legible** (product identifiable in under 2 seconds).
   Fail → one automatic re-roll naming the fix. Still bad → flag, don't ship.
5. Finish: `$T/venv/bin/python -I $T/finish_batch.py gen.png FINAL_<n>_<framework>.png --ratio 4:5 --product sermorelin-ghk`
   (the verbatim disclaimer comes from product.json).
6. Save to `~/Everlife-Creative/output/Sermorelin-GHK/<date>_batch-<n>/` (FINALs + `prompts.md` + `contact_sheet.jpg`),
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

**Men's ads (reviewer, 2026-10-29: "men shouldn't use that font", about an elegant serif with a gold italic word):** never
the elegant high-contrast serif, the serif with an italic word, or the brush/handwritten accent for a men's headline. Men
pick from: heavy condensed grotesque (the winners' look), wide extended bold sans, bold slab serif, chunky/bold sans;
keep "SERMORELIN GHK" big in type (bible: "Product names run big"). The serif rows stay available for women.

Accent colour: take it from the scene or the product, never from habit. Options: the label red, brass/gold, deep navy,
charcoal on cream, cream on charcoal, ink on sand, forest, teal, sky, slate, mocha, rose, blush, burgundy, warm white.
Product rules win. **Bible v3 (29 Oct) dropped the women's "pinks, tans and beige; no oranges or greens" rule** for every
product except GHK-Cu Cream and Glow Stack, so Sermorelin GHK women's ads may use any warm palette.
**Women: Justin's colour & typography direction (2026-10-29)**, "preferred options, not strict limitations":
- **No colour is banned.** Preferred (they have performed): pinks, tans, neutrals, warm tones, **white** and **teal**.
  Most ads in a women's batch lead with one of these.
- **Explore:** up to 2 of every 5 women's ads use a current colour or type trend that suits the concept and imagery.
- **Advertorial / article ads sit on a white background.**
- **At least one teal-led or teal-accent ad per women's batch.** Teal harmonises with the green-teal tablet; keep it soft
  or pale so it doesn't fight the bottle's deep red label.
- Still: at most one pink-led ad per batch, no two women's ads with the same lead colour, pink fine as an accent, varied
  fonts (§2b menu; serif rows allowed for women).
Restora-Z moods navy / lavender / blush / cream / pale sky. Vary the headline placement too (top-left, centred, bottom-
third above the footer band, split either side of the product) and the light (morning, golden hour, overcast soft, studio).

The type specimen (`assets/type_specimen.png`) is no longer attached by default. Attach it only when the brief asks for
the house editorial look, and then say "match image 3".

## 3. Prompt template (fill everything; keep the quotes exact)
```
Design a finished, premium static social ad for "Sermorelin GHK", a doctor-prescribed 3-in-1 sublingual peptide tablet,
in the style of a modern DTC wellness brand. Framework: <name>: <layout from the reference ad you viewed>.

PRODUCT: image 1 is the real bottle and image 2 the real tablet. Use the attached tablet reference exactly; do not
invent, alter, or substitute a different pill. Use the attached bottle reference exactly: same shape, colours and label,
label facing camera, sharp, never mirrored, never redesigned; the label wraps around the bottle and follows its angle and
perspective. The TABLET is the hero (large, in focus, foreground, at least 15% of the canvas width), shown as the real
tablet only: never as glowing orbs, glass spheres, icons or abstract shapes. The bottle is in every ad, large and
legible. ARRANGEMENT for this ad: <this ad's own product arrangement, different from every other ad in the batch>.

TYPOGRAPHY & COLOUR (this ad's own look, different from every other ad in the batch): headline in <pairing from the
menu, e.g. "a heavy condensed grotesque in all caps">, with ONE phrase picked out in <accent colour from the palette>;
supporting text in <its partner face>. For readers aged 50+: headline at least 9% of canvas height per line; every other
line at least 3.5%; strong contrast; no thin grey text; max 3 supporting lines (a benefits block has exactly 3). Never
split "Sermorelin" or "GHK" across two lines or hyphenate them.

TEXT: render ONLY these strings, exactly, nothing else (no extra words, no Everlife or other logos or wordmarks, stars,
badges, prices, website, disclaimer):
  Name: "SERMORELIN GHK by Everlife"   (big; "by Everlife" smaller; every ad, bible v3 + team feedback 2026-10-29)
  Headline: "<headline>"   (accent on: "<phrase>", in the accent colour named above)
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"

SCENE & STYLE: <scene>, real texture and depth (never a flat colour), warm sun-lit light, calm and premium.
<MEN: palette warm stone, charcoal, sand, brass; any person a man 42–50, a fit silver fox with a hardcore fitness-model
physique (visibly muscular, lean, athletic; tattoos optional), rugged and confident, fully clothed in a fitted training
tee or long sleeve, no bare torso, no flexing poses.>
<WOMEN: lead colour <this ad's own lead per §2b (Justin): preferred pinks / tans / neutrals / warm tones / white / teal (soft
or pale teal), or an "explore" trend colour for up to 2 of 5 ads; white background for advertorial ads; pink-led at most
once per batch>; any person a woman 40–60, natural, candid, glowing
skin, clothed.> No bedroom, no shirtless, no before/after, no needles or syringes, no mirrors showing bodies.

LAYOUT: 5% clear margin on every edge. The TOP 14% is calm continuation of the background (no text, no product; the bigger bible-v3 logo sits there):
the Everlife logo is laid there. The BOTTOM 22% is calm continuation of the background (no text, product or hands): the
proof footer is laid there. The whole product (bottle, tablets, hands, plinth tops) ends ABOVE 72% of the canvas height
and all text above 76%.
(For 4:5 and 1:1 the top band is 14% too.) Ask high on purpose: GPT Image 2.5 on Creatify places the product lower than asked
(batch 4, 2026-10-29: "between 45% and 78%" gave 6 reposition edits in 7; "ends above 72%" gave 0 in 3).
```
Bottle wording for the PRODUCT block, per strength (both: "amber glass jar with a black ribbed cap; deep red label with
the vertical white EVERLIFE wordmark, a white 'RX' box top right, small text 'PRESCRIPTION', '30 TABLETS'"), plus:
- **1000 mcg** (checked against `assets/sghk1000_bottle_ref.jpg`, 2026-10-28): white band 'SERMORELIN GHK 1000', '1000 MCG'.
- **500 mcg** (checked against `assets/sghk500_bottle.png`, 2026-10-28): white band 'SERMORELIN GHK', '500 MCG'.
- **Either:** use the bottle on file and its wording.
QA that the label shows the session's strength (1000 vs 500), not the other one. Never describe the tablet in words.
