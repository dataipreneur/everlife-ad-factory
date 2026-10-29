# Sermorelin GHK IMAGE ads: Batch Mode (the default for every image request)

Same machine as the Restora-Z batch (creative lead, 2026-10-27: "speed, Creatify, batches of at least 5 different types,
mobile friendly, easy to read for older people"). GPT Image 2.5 on Creatify designs the **whole ad** with the real bottle
and tablet; `finish_batch.py` adds the Everlife logo at the TOP and the approved proof footer (Trustpilot 4.9 / Doctor
Prescribed / Ships Free art, verbatim disclaimer) as a compact transparent strip inside the Meta 9:16 safe area (feed: over the calm bottom ~18%).

**Footer position (2026-10-29):** on 9:16 the footer ends at y 1385, the bottom of the Reels safe area (the reference ad's band sits at ~63–72% of the frame; the footer may cross the lower-left profile notch, Mitansh 2026-10-29) (`core/tools/safezones.py`,
team Safe zones page), because the bottom ~535 px of a Reel sits under Meta's "Learn more" button and caption
(`core/references/safe-zones/reels_placement_2026-10-29.jpg`). So a 9:16 raw must keep everything in its top ~52%
(LAYOUT block below); `finish_batch.py` refuses (exit 2) when a raw's content runs under the footer. Fix = ONE reposition
edit on the raw (Creatify `composer_edit_image`, 1 credit): "Keep everything identical (headline, type, colours, product,
scene, light). Scale the product and the text block down together (about 35%) and move them up so the lowest element ends
at 50% of the canvas height. Fill the bottom half with calm, plain continuation of the same background: no text, no
product, no hands." Then re-run `finish_batch.py`. Feed ratios (4:5, 1:1) are unchanged: footer over the calm bottom ~18%.


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
- Never repeat a headline in the copy log. The Tier A pool is small (≈20 men's, ≈13 women's usable lines): when it runs
  low, say so and ask whether to allow more Tier B or request new approved headlines from Jeremy.
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
2. Read the bible + copy log + `winners/winners.md` (one cat). Per slot: pick a framework, **look at 1 reference ad**:
   first a matching winner (its card + preview image: M8/M2 bold claim, M3 offer + callouts, M4 features & benefits,
   M9 identity post, M10 tablet in hand, F2 brand mood, F1 article, F3 letter, F5 animated), else one from the generic
   folder. Follow the card's "Don't copy" list. Write concept
   (1 line), headline (Tier A by default, see §0 ⚠ pending), ≤ 3 supporting lines (approved claims, exact), prompt. Show
   ONE table: # · framework · territory · headline · tier (A / B PROPOSED) · supporting lines · ≈1 credit.
   AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". **That click approves the batch and
   its Tier A lines; each Tier B line needs its own explicit OK first** (ask before the generate question).
3. Generate: `composer_edit_image(project_id, prompt, images=[bottle, tablet]  (add type_specimen only for the house look, see §2b), out='gen/b<date>_<n>.png',
   aspect_ratio=<final ratio>)` from `assets/creatify.json`. Max 4 in flight.
4. QA every result (Read it), strictly: text EXACTLY the approved strings; the bottle label matches the render (not garbled,
   not mirrored) and the **tablet is identical to the tablet render** (no invented pill); every line big enough for 50+;
   people look 35–60, fit but not bodybuilders, clothed; women's ads in pink/tan/beige; nothing breaks a Hard NO.
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

Accent colour: take it from the scene or the product, never from habit. Options: the label red, brass/gold, deep navy,
charcoal on cream, cream on charcoal, ink on sand, forest, teal, sky, slate, mocha, rose, blush, burgundy, warm white.
Product rules win: women's creative only pinks, tans, beige, cream, mocha, rose, burgundy (no orange, no green);
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
label facing camera, sharp, never mirrored, never redesigned. The TABLET is the hero (large, in focus, foreground); the
bottle, if shown, is large and legible.

TYPOGRAPHY & COLOUR (this ad's own look, different from every other ad in the batch): headline in <pairing from the
menu, e.g. "a heavy condensed grotesque in all caps">, with ONE phrase picked out in <accent colour from the palette>;
supporting text in <its partner face>. For readers aged 50+: headline at least 9% of canvas height per line; every other
line at least 3.5%; strong contrast; no thin grey text; max 3 supporting lines.

TEXT: render ONLY these strings, exactly, nothing else (no extra words, logos, stars, badges, prices, website, disclaimer):
  Headline: "<headline>"   (accent on: "<phrase>", in the accent colour named above)
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"

SCENE & STYLE: <scene>, real texture and depth (never a flat colour), warm sun-lit light, calm and premium.
<MEN: palette warm stone, charcoal, sand, brass; any person a fit, mature man 40–60, fully clothed in training or casual
wear, natural build (NOT a bodybuilder), calm and candid.>
<WOMEN: palette blush pink, tan, beige, cream (no orange, no green); any person a woman 40–60, natural, candid, glowing
skin, clothed.> No bedroom, no shirtless, no before/after, no needles or syringes, no mirrors showing bodies.

LAYOUT (9:16): 5% clear margin on every edge. The TOP 12% is calm continuation of the background (no text, no product):
the Everlife logo is laid there. EVERYTHING ELSE (headline, benefits, bottle, tablet) sits in the TOP 52% of the canvas;
the lowest element ends at 50% height. The BOTTOM 48% is calm continuation of the background (surface, wall, fabric: no
text, no product, no hands, no key objects): the proof footer is laid at ~61–72% and Meta's Reels/Stories UI covers the rest.
LAYOUT (4:5 / 1:1): 5% margin; TOP 10% calm for the logo; BOTTOM 18% calm for the proof footer; product base above that line.
```
> GPT Image 2.5 lands the product 8–15% LOWER than the LAYOUT block asks (batch-4 PT-141, 2026-10-29: "base at 48%" came back at
> 58–65%). Ask for the lowest element at **40%** (cap/nozzle tip at 13%) to get ~50%. `finish_batch.py` then shifts the image up by
> whatever headroom is left under the logo band (max 320 px) before it refuses; a refusal means one reposition edit (1 credit).
```
```
Bottle wording for the PRODUCT block, per strength (both: "amber glass jar with a black ribbed cap; deep red label with
the vertical white EVERLIFE wordmark, a white 'RX' box top right, small text 'PRESCRIPTION', '30 TABLETS'"), plus:
- **1000 mcg** (checked against `assets/sghk1000_bottle_ref.jpg`, 2026-10-28): white band 'SERMORELIN GHK 1000', '1000 MCG'.
- **500 mcg** (wording read from the website's product image, 2026-10-28; recheck against the asset-library render
  when it's added): white band 'SERMORELIN GHK', '500 MCG'.
- **Either:** use the bottle on file and its wording.
QA that the label shows the session's strength (1000 vs 500), not the other one. Never describe the tablet in words.
