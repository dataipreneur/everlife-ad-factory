# Sermorelin IMAGE ads: Batch Mode (the default for every image request)

Same machine as the Restora-Z and Sermorelin GHK batches (creative lead, 2026-10-27: "speed, Creatify, batches of at least
5 different types, mobile friendly, easy to read for older people"). GPT Image 2.5 on Creatify designs the **whole ad**
with the real bottle and tablet; `finish_batch.py` adds only the approved footer (Everlife logo, Trustpilot 4.9 / Doctor
Prescribed / Ships Free art, verbatim disclaimer) as a compact transparent strip over the calm bottom ~18%.

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

## 1. Frameworks (reference ads in `core/references/static-refs/<folder>/`, overview `OVERVIEW.jpg`)
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
F10, F11, F12). Weight towards F2, F4, F11, F6 (winners: M5 name lockup, M3 name box + icon lines, M2 "S" dumbbell plate).

## 2. Flow (1 question, then generate)
1. **One AskUserQuestion** (audience is already set in SKILL.md step 1): **How many?** "5 (Recommended)" / "10" / "15" ·
   **Placement:** "4:5 Feed (Recommended)" / "9:16" / "4:5 + 9:16" / "1:1" · **Frameworks:** "🎲 Random mix (Recommended)" / "Pick frameworks".
2. Read the bible + copy log + `winners/winners.md` (one cat). Per slot: pick a framework, **look at 1 reference ad**:
   first a matching winner (its card + preview image: M5 bold name lockup, M3 features & benefits + offer, M2 visual
   metaphor, F1 tablet hero / repeated name, M4 video), else one from the generic folder. Follow the card's "Don't copy" list. Write concept
   (1 line), headline (Tier A by default), ≤ 3 supporting lines (✅ benefits, exact), prompt. Show ONE table:
   # · framework · territory · headline · tier (A / B PROPOSED) · supporting lines · ≈1 credit.
   AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". **That click approves the batch and
   its Tier A lines; each Tier B or ⚠ line needs its own explicit OK first** (ask before the generate question).
3. Generate: `composer_edit_image(project_id, prompt, images=[bottle, tablet, type_specimen], out='gen/b<date>_<n>.png',
   aspect_ratio=<final ratio>)` from `assets/creatify.json`. Max 4 in flight.
4. QA every result (Read it), strictly: text EXACTLY the approved strings; the bottle label matches the render (not garbled,
   not mirrored); the **tablet is identical to the tablet render** (no invented pill, not the other past tablet shape);
   **no vial, syringe or second container**; every line big enough for 50+; people look 35–65, fit but not bodybuilders,
   clothed; women's ads in pink/tan/beige with no orange in the scene; nothing breaks a Hard NO.
   Fail → one automatic re-roll naming the fix. Still bad → flag, don't ship.
5. Finish: `$T/venv/bin/python -I $T/finish_batch.py gen.png FINAL_<n>_<framework>.png --ratio 4:5 --product sermorelin`
   (the verbatim disclaimer comes from product.json).
6. Save to `~/Everlife-Creative/output/Sermorelin/<date>_batch-<n>/` (FINALs + `prompts.md` + `contact_sheet.jpg`),
   open the contact sheet, log the headlines, offer "Another batch?" / "Variations of #k" / "9:16 of the winners".

## 3. Prompt template (fill everything; keep the quotes exact)
```
Design a finished, premium static social ad for "Sermorelin", a doctor-prescribed sublingual peptide tablet, in the
style of a modern DTC wellness brand. Framework: <name>: <layout from the reference ad you viewed>.

PRODUCT: image 1 is the real bottle and image 2 the real tablet. Use the attached tablet reference exactly; do not
invent, alter, or substitute a different pill. Use the attached bottle reference exactly: same shape, colours and label,
label facing camera, sharp, never mirrored, never redesigned. The TABLET is the hero (large, in focus, foreground); the
bottle, if shown, is large and legible. Show ONLY this bottle and tablet: no vial, no second container.

TYPOGRAPHY: image 3 is the type specimen. Headline in an elegant high-contrast serif (like Instrument Serif) with ONE
phrase in an accent colour; other text in a clean geometric sans (like Inter). For readers aged 50+: headline at least
9% of canvas height per line; every other line at least 3.5%; strong contrast; max 3 supporting lines.

TEXT: render ONLY these strings, exactly, nothing else (no extra words, logos, stars, badges, prices, website, disclaimer):
  Headline: "<headline>"   (accent on: "<phrase>")
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"

SCENE & STYLE: <scene>, real texture and depth (never a flat colour), warm sun-lit light, calm and premium.
<MEN: palette warm stone, charcoal, sand, brass; any person a fit, mature man 40–65, fully clothed in training or casual
wear, natural build (NOT a bodybuilder), calm and candid.>
<WOMEN: palette blush pink, tan, beige, cream (no orange and no green in the scene; the product keeps its own colours);
any person a woman 40–65, natural, candid, clothed.> No bedroom, no shirtless, no before/after, no needles, syringes or
vials, no mirrors showing bodies.

LAYOUT: 5% clear margin on every edge. The BOTTOM 18% is calm continuation of the background (no text, product or hands).
9:16 only: keep the top 8% free of text.
```
Bottle wording for the PRODUCT block, per strength: **fill in only after `sermorelin1000_bottle_ref.jpg` /
`sermorelin500_bottle_ref.jpg` are added and checked** (read the label off the asset-library render: name, strength,
tablet count). QA that the label shows the session's strength. Never describe the tablet in words.
