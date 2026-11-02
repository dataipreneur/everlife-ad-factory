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

## 4. Tests (all free)
1. `bible_sync.py <saved html> --check` → the new product's line is ✅.
2. `bash skills/everlife-<id>/core/scripts/preflight.sh` → only optional items open (Marketing Studio registration, Nano Banana MCP).
3. `core/tests/regression.py smoke` before and after adding the product's block (copy the Lovara block: static finish with its
   disclaimer, wrong disclaimer refused, end-card renders in `default` + `tiktok` with a pre-seeded `T_caps.json`). Other products'
   results must not change.
4. Look at an end-card frame: product and headline both clear.

## 5. Hand-off line for the user
"Built on `<id>-skill`, committed locally, nothing pushed, no credits. Tests N/N. Blocked on: … Human inputs open: … Next: approve the
4-image test (~4 credits)."
