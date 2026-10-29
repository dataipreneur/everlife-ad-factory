# Reference priority

Rule agreed 2026-10-28 (Priestley, from the Restora-Z team). **Wired into: Sermorelin GHK and plain Sermorelin** (for now; Restora-Z is
unchanged and adopts it only if its owner decides to). When you pick the idea and layout for an ad, look for a
reference in this order and take the first one that fits the chosen ad type:

| Priority | Source | Where | Notes |
|---|---|---|---|
| **1** | **Our own performing winners** | `skills/<product>/references/winners/` (`winners.md` cards + previews, `winners.json`) | From the Winning Ads report (CPA-ranked). Prefer high-purchase winners; 3-purchase ones are ideas to test, not proof. A skill without a winners folder yet skips to 2. |
| **2** | **Meta Ad Library** (other brands' ads currently running on Meta) | `core/references/meta-refs/` (shared) or `skills/<product>/references/meta-refs/` (product-specific) | Only "if they had something": use when the folder has an ad for this ad type. See "Adding Meta references" below. |
| **3** | **Pinterest** | a skill's own `references/pinterest/` first (Sermorelin GHK: 32 themed ads from its own category, the way Restora's are sleep ads; plain Sermorelin: 58 same-category ads), then the shared `core/references/static-refs/` (12 ad-type folders, `OVERVIEW.jpg`) | 50 pins from board 1 (`pinNN`), 20 from board 2 (`b2pinNN`), 20 from a document (`DOC_NN`). Mostly sleep brands: they work for any tablet product, but take the **layout only**, never their theme, colours or words. |

**Winners lead the batch, not only the tie-break** (Priestley, 2026-10-29, Sermorelin GHK): pick the winners first and take
their ad types; at least 3 of every 5 ads start from a winner for that audience. Only the remaining slots choose an ad type
first and fall through to Meta / Pinterest. (Picking the ad type first let 4 of 5 women's ads in batch 2 fall to Pinterest.)

The ad types are the same at every level (F1–F12 in each skill's `image-batch.md`), so one ad type can be matched in all three.

## Rules that apply to every level
- **References decide the idea and the layout, never the words.** Headlines, claims, offers, proof and the disclaimer come only
  from the creative bible (Tier A headlines; Tier B only as approved). A winner's or another brand's wording is never copied.
- **The image generator never sees a reference.** Only Claude looks at it; the generator gets the product renders and the type
  specimen. This keeps a reference's rule breaks (e.g. "GHK-Cu", "Save 70% vs HGH", competitor names) out of our ads.
- **Follow each winner card's "Don't copy" list.**
- **Never name or show another brand** in our ads, even when a Meta or Pinterest reference is another brand's ad.
- **Record the reference** for every ad in `prompts.md` and the session sheet: level (1 winner / 2 Meta / 3 Pinterest) and file.

## Adding Meta references
1. Find ads in the Meta Ad Library (facebook.com/ads/library), e.g. men's health, peptides, longevity, women's wellness,
   supplements in tablet form. Download or screenshot the ad image (or a frame of a video).
2. Save it as `<ad-type folder>/<brand>_<YYYY-MM-DD>_<short-note>.jpg`, using the same folder names as `static-refs`
   (`01_Us_vs_Them` … `12_EXTRA_Brand_Mood_Product_Hero`). Shared refs go in `core/references/meta-refs/`; refs that only
   suit one product go in that skill's `references/meta-refs/`.
3. Add one line to the folder's `SOURCES.md`: file, brand, Ad Library link, date seen, why it's useful.
4. Keep it small: a few strong examples per ad type beat a big pile. Remove ads that stop running or age badly.
