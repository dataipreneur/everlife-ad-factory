# After the scaffold: adapt, inherit, test

## 1. Files to rewrite (the script lists where the template's name still appears)
| File | Make it about the new product |
|---|---|
| `SKILL.md` | name + description (when to use, what NOT to use it for), product truths, audience (never asked when the bible fixes it), form, hook angles from the bible's ✅ headlines, setup questions, paths (`output/<Product>/`, `<id>-copy-log.md`) |
| `product.json` | `hero.never` from the bible's Hard NOs + creative direction; `keep_case` (+ ingredient spellings); `kicker_default`, `split_titles`, `notify_icon`; `pill_end_scale` after looking at an end card |
| `references/product-bible.md` | "Product facts" (name on creative, what it is, form, audience, creative direction, language scope, offer, proof, disclaimer verbatim, landing page = facts only) and the **pre-screen**: every TODO row gets ✅ / ⚠ Jeremy / ❌ with a reason against the GLOBAL Hard NOs; clean pools listed at the end |
| `references/image-batch.md` | product truths in §0, framework recipes (§1) in the product's register, colours (§2b), the **bottle wording from the real render** in the prompt template, hero ≥ 35%, output path, `--product <id>` |
| `references/video-prompting.md` | the spine for this audience, settings, cast rules, copy rules, model routing; the AI-avatar rule |
| `references/finishing.md` | the copy.json example (`"product": "<id>"`, header "<NAME> BY EVERLIFE", `head_always`, ✅ benefit rows) |
| `references/personas.md` | two buyer personas from the bible's "Who it's for" and what each punishes; the rubric with this product's offer |
| `references/reference-guide.md` | angles → frameworks → which shared pins; the product's own reference ads (`~/Everlife-Creative/reference-ads/`), layout only |
| `references/lessons.md` | keep the cross-product lessons, drop the template product's specifics, add the new product's expected risks |
| `references/reviews.md`, `styles/*.md` | the product's name, scenes and gates |
| `assets/RENDERS.md` | what each render shows (label text, colours), how it was made, what's still missing |

## 2. Product facts to write (from the card; never invent)
Name on creative · what it is (bible one-liner) · form + count/strength from the render's label (never stated in copy unless approved) ·
audience · creative direction · product Hard NOs · language scope (words never to use) · offer (percent only) · proof wording ·
disclaimer verbatim · landing page (facts only).

## 3. Rules every new product inherits (don't wait to be told again)
- Images never say "by Everlife"; the product name runs big (one of the two largest texts). Videos: "<Product> by Everlife" in the
  header (on screen the whole time, `head_always`) and the first spoken line.
- A different person in every ad; every cast line says "an ordinary, non-famous face; must not resemble any celebrity"; videos with a
  face are cast from a preview still the user picks first.
- Tablet/capsule held (thumb + index or open palm) beside the bottle, never covering the label; real pill only; ≥ 15% of the width
  (models draw it ~half size: fix with a 1-credit "twice as large" edit).
- Every ad gets its own font pairing and accent; men's headlines never elegant/italic serif or script; women's colours per Justin
  (pinks, tans, neutrals, warm tones, white, teal; ≥ 1 teal, ≤ 1 pink-led, advertorials on white).
- Winners first (≥ 3 of every 5 slots from a winner when the product has winners), then Meta refs, then Pinterest.
- 9:16: proof row inside the Reels safe area, disclaimer alone at the bottom on 2 lines (`disclaimer_at: bottom`); video action
  between 8% and 58% of the height; 9:16 statics from the approved 4:5.
- Intimate wellness: no beds, bedrooms, lingerie, couples, lips; shoulder-up. Peptides: never needles, syringes or "needle-free".
- Higgsfield "no response received" = the upload failing: upload first (`higgsfield upload create`) and pass the IDs.
- **Hardcore men (REQUIRED for men's-muscle products: TRT / Enclomiphene, Tesamorelin, Tesamorelin/Ipamorelin, any "serious gym-goer with a hardcore training feel" product; Jeremy 2026-11-02).** Add the product id to `core/references/hardcore-men.json` and the 💪 banner from `core/references/hardcore-men.md` to SKILL.md, image-batch.md, video-prompting.md and finishing.md; no "clothed / no shirtless / no flexing" lines for men.
- **The 15 Drive styles in the image Mood question (REQUIRED, Mitansh 2026-11-02).** Add the 🎨 MOOD override line from `core/references/style-library/MOOD-QUESTION.md` right above the skill's image Mood (or Frameworks) question: option 1 "🎲 Surprise me (Recommended)" = `core/scripts/pick_styles.py`, option 2 "📚 Pick from the 15 styles", options 3–4 = the product's own top moods. Add product notes to `core/references/style-library/STYLES.md` if a style needs a product-specific gate.
- **"✨ Ultra premium, product only" in the image setup (REQUIRED, Mitansh 2026-11-02).** Every product offers it: as a Mood option
  where the skill asks mood (SKILL.md or image-batch.md, asked ONCE, never in both), else as a "Look" question in the image round.
  It points to `core/references/ultra-premium.md`; add the product's row to that file's "Per product" table (its own field colour,
  from the real render). **Vial products:** staging from `skills/everlife-bpc-157/references/vial-refs/` (V31 / V20 / V40 / V37) and
  its "Compliance traps" list; replace BPC-157's "one vial, slate blue" with the new vial's own colours and the skill's vials-per-ad
  rule. **Tablet / capsule / bottle / spray products:** the Hims tiles in `13_Premium_DTC/`; the tablet stays the hero.
- **"🧑‍💼 AI Avatar Video" in "What are we making?" (REQUIRED, Mitansh 2026-11-02).** Offer it in the format question (max 4 options:
  merge "Video ad or animated still" if needed) with a bullet pointing to `core/references/ai-avatar-video.md` and naming this product's casting,
  hero form and banned settings. Register the product in Higgsfield Marketing Studio (preflight prints the command).
- **Winners Board (REQUIRED, Priestley 2026-11-02).** `references/image-batch.md` reads the shared board before the batch
  table and ends "After the batch" with the "Rate the batch (Winners Board)" step, both pointing at
  `core/winners-board/WINNERS-BOARD.md` (§4 read, §5 write). Use the new product's `product.json` id as `product` on the board.

## 3b. Lessons from the 7-product build (2026-11-02): check these before the first test
- **Template leftovers are words, not just the name.** The 7 skills kept ~150 lines of their template's world (BPC-157:
  recovery, gym, tattooed bodybuilders, ice baths, the "slate" vial, BPC-157's own headlines as examples; PT-141: the spray).
  `grep -i` the template's name AND its scenes/props/colours/headlines in `styles/`, `video-prompting.md`, `image-batch.md`
  (moods, type notes), `lessons.md` (its "<template>-specific risks" section must be rewritten), `animated-still.md`,
  `reference-guide.md`, `mens-direction.md`. Replace examples only with the new product's ✅ lines.
- **Form rules travel with the template.** A vial template says "no capsules or pills anywhere": wrong for a product with a
  tablet (NAD+). Make the video PRODUCT block and the QA lines (`finishing.md`, `image-batch.md`) match the new forms.
- **`product.env` must name the real renders** (GLP-1 shipped with the placeholder `<id>_bottle.png`): preflight's
  "Real product render present" must be ✅. Same for the name (`PRODUCT_NAME` = the bible's name) and the output folder.
- **`finishing.md` kicker:** "defaults to …" must match the new `product.json` `kicker_default`.
- **Hook Engine:** add the "Hook Engine (mandatory for every video)" section before Step 0 (`core/hook-engine/HOOK-ENGINE.md`)
  and a `references/hook-bank.md` (8 hooks, the product's limits first, every bridge an exact ✅ line); see any of the 7.
- **Marketing Studio:** register the product (title = `PRODUCT_NAME`) with copies whose transparent pixels are set to white
  (preflight's hidden-pixel ⚠); one form per product when the skill says one form per ad.
- **Stale "nothing yet" notes:** after the first batch, update "no ads / no winners yet" lines in `lessons.md`,
  `video-prompting.md` and `reference-guide.md`.

## 4. Tests (all free)
1. `bible_sync.py <saved html> --check` → the new product's line is ✅.
2. `bash skills/everlife-<id>/core/scripts/preflight.sh` → only optional items open (Marketing Studio registration, Nano Banana MCP).
3. `core/tests/regression.py smoke` before and after adding the product's block (copy the Lovara block: static finish with its
   disclaimer, wrong disclaimer refused, end-card renders in `default` + `tiktok` with a pre-seeded `T_caps.json`). Other products'
   results must not change.
4. Look at an end-card frame: product and headline both clear.
5. `grep -n "Ultra premium" skills/everlife-<id>/SKILL.md skills/everlife-<id>/references/image-batch.md` → the option is offered
   exactly once in the setup, and `core/references/ultra-premium.md` has the product's row.
6. `grep -n "AI Avatar Video" skills/everlife-<id>/SKILL.md` → offered in "What are we making?" with its `core/references/ai-avatar-video.md` bullet.

## 5. Hand-off line for the user
"Built on `<id>-skill`, committed locally, nothing pushed, no credits. Tests N/N. Blocked on: … Human inputs open: … Next: approve the
4-image test (~4 credits)."
