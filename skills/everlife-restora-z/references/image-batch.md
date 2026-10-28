# Restora-Z IMAGE ads: Batch Mode (the default for every image request)

Creative lead, 2026-10-27: "I want speed! Use Creatify and batches, at least 5 images of different types at once,
random by default, mobile friendly, the new creative font, easy to read for older people."

The image model (GPT Image 2.5 on Creatify) designs the **whole ad**: layout, headline, benefits and scene, with the
real bottle and capsule. We add only the **approved footer** (`finish_batch.py`): a COMPACT, TRANSPARENT strip (~17% of the height) laid over the
ad's calm bottom on a soft gradient: Everlife logo, the Trustpilot 4.9 / Doctor Prescribed / Ships Free art and the verbatim
disclaimer (creative lead 2026-10-27: "35% smaller and transparent").

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

## 2. Flow (fast: 1 question, then generate)
1. **One AskUserQuestion, 3 questions, each with a ✨ Recommended first option** (one Enter-press per question gets a great batch):
   - **How many?** "5 (Recommended)" / "10" / "15".
   - **Placement:** "4:5 Feed (Recommended)" / "9:16 Stories/Reels" / "4:5 + 9:16" / "1:1".
   - **Frameworks:** "🎲 Random mix (Recommended)" / "Pick frameworks" (then a multiSelect follow-up with the table).
   **Never ask the user for pain points or style here.** Claude picks them automatically from the bible: a different approved
   pain point per ad where it fits, each paired with its matching approved claim. Show the picks in the batch table instead.
2. Read the bible + copy log (one cat). For each slot: pick a framework, **look at 1 reference ad from its folder** (Read the jpg),
   and write: concept (1 line), headline (Tier A by default, see §0 ⚠ pending), up to 3 short supporting lines (approved
   claims, exact), and the prompt (template below). Show ONE compact table: # · framework · pain point (auto) · headline ·
   tier (A / B PROPOSED) · supporting lines · ≈1 credit.
   One AskUserQuestion: "Generate all N (≈N credits)" / "Swap some" / "Rewrite headlines". **That click approves the batch
   and its Tier A lines; each Tier B line needs its own explicit OK first** (ask before the generate question).
3. Generate: `composer_edit_image(project_id, prompt, images=[bottle, capsule, type_specimen], out='gen/b<date>_<n>.png',
   aspect_ratio=<MODEL_RATIO>)` from `assets/creatify.json`. **Max 4 in flight per project**: start 4, then the next as each finishes.
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

## 3. Prompt template (fill everything; keep the quotes exact)
```
Design a finished, premium static social ad for "Restora-Z", a prescription sleep product, in the style of a modern
DTC wellness brand. Framework: <framework name>: <one-line layout description taken from the reference ad you viewed>.

PRODUCT: image 1 is the real Restora-Z bottle and image 2 the real capsule. Use them exactly: same shape, colours and
label (EVERLIFE vertical wordmark, "RESTORA-Z", white Rx box), label facing camera, sharp, never mirrored, never
redesigned. At most one capsule unless the concept needs a few. Make the bottle a clear hero (about 30–45% of the canvas height).

TYPOGRAPHY: image 3 is the type specimen. Match it: headline in an elegant high-contrast serif (like Instrument Serif)
with ONE phrase in italic accent colour; all other text in a clean geometric sans (like Inter). Mobile-first and for
readers aged 50+: headline at least 9% of the canvas height per line; every other text line at least 3.5% of the
canvas height; strong contrast; no thin grey text; max 3 supporting lines.

TEXT: render ONLY these strings, exactly as written, nothing else (no extra words, no logos, no stars, no badges, no prices,
no website, no disclaimer):
  Headline: "<headline>"   (italic accent on: "<phrase>")
  Supporting: "<line 1>" / "<line 2>" / "<line 3>"
  <Framework-specific text, e.g. Notes title, sticky note words, Myth / Fact labels>

SCENE & STYLE: <scene, props, single colour mood (navy / lavender / blush / cream / pale sky)>, real texture and soft
light, calm and premium, lots of air, nothing cluttered. Women-focused looks: pinks, tans and beige. No beds-with-couples
or bedroom intimacy. Any person: real-looking 45–65, calm, candid, no before/after.

LAYOUT: keep a 5% clear margin on every edge. The BOTTOM 18% of the canvas is calm, plain continuation of the background
(surface, fabric, wall): no text, no product, no hands or key objects there (a transparent footer is laid over it).
Put the product base above that line. 9:16 only: also keep the top 8% free of text.
```

## 4. After the batch
- Contact sheet first, then let the user pick winners. Winners → `9:16` re-make (same prompt, MODEL_RATIO 2:3) only after approval.
- Log each headline + framework in `~/Everlife-Creative/restora-z-copy-log.md`.
- Everything is a draft → creative review → Jeremy. List any borderline line ("Chronic insomnia", "Calms anxiety") in `SESSION.md` for him.

## Legacy (only if the user asks)
`finish_modern.py` (photo + overlaid type templates) and the one-image-at-a-time flow in `image-prompting.md` still work, but
Batch Mode is the default.
