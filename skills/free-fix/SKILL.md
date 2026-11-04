---
name: free-fix
description: Free Fix — repair failed Everlife static ads in code for 0 credits instead of re-rolling. Use when the user says "free fix", "fix it for free", "fix by code", "move these and fix them", or when finished 9:16 / 4:5 statics fail QA because the headline sits under the Everlife logo, or the vial / bottle / CTA lands on the proof row (Trustpilot / 100,000+ footer). Works for every everlife-* product. Not for videos, garbled labels or compliance problems (those need a re-roll).
---

# Free Fix (0 credits)

Mitansh, 2026-11-04: GLP-1 batch 1 had 6 of 8 ads failing placement (text under the logo, vial or CTA on the proof row).
He asked "move these and fix all of them for free by code". This skill is that fix.

**How it works:** scale the raw's art **uniformly** (never stretched) so its content band (first text line → lowest
product / CTA pixel) fits between the logo and the footer. Then fill the freed-up margins by **mirror-tiling the raw's own
plain edge** (wall, stone, floor). No AI, no blur, no padding colour. Then finish as normal with the finisher's auto-lift
switched off, so it doesn't undo the placement.

> The 11-04 prompt-zones rule says "re-roll, don't mirror-fit". This skill is the exception, and only runs when the user
> asks for a free / code fix. Everything else (proof split, safe area, verbatim disclaimer, logo) stays as is.

Paths: `S=~/.claude/skills/free-fix/scripts` · `T=~/Everlife-Creative/tools` · `PY=$T/venv/bin/python` · run from the batch folder.

## 1. Find what failed
LOOK at every finished ad. Failures this fixes: the headline under or touching the logo · the product, CTA or text under
the proof row · the finisher refusing "type or product sits under the Everlife logo".

## 2. Measure each raw's content band
```
$PY $S/grid.py /tmp/grid.jpg gen/ad1_916.png gen/ad1_45.png ...
```
Read off the following, as fractions of the RAW height:
- `--top`: the top of the first text line. Be exact: misreading by 0.03 put "GLP-1" into the logo on the first try.
- `--bottom`: the lowest product, shadow or CTA pixel.

## 3. Pick the route and the band
Scale k = (band_bottom − band_top) / (bottom − top). **k must be ≥ 0.65** (50+ legibility); the tool refuses below that.

| Ratio | Band (`--band-top` – `--band-bottom`) | Command |
|---|---|---|
| 9:16 | 0.12 – 0.635 | `$PY -I $T/mirror_fit_916.py raw out --top T --bottom B` (or `fit_any.py --size 1080x1920`) |
| 4:5 trust row | 0.12 – 0.835 | `$PY -I $S/fit_any.py raw out --top T --bottom B --band-top 0.12 --band-bottom 0.835` |
| 4:5 count / none | 0.12 – 0.84 | same, `--band-bottom 0.84` |

**9:16 too tall (k < 0.65)?** Build it from the ad's **4:5 raw** if that raw has the right order (text → CTA → product):
`fit_any.py gen/adN_45.png repo/adN_916.png --size 1080x1920 --top T --bottom B --band-top 0.12 --band-bottom 0.635`.

## 4. Fill options (fit_any.py), so no text or product gets copied into the margins
- `--strip 28`: side strip in px (the edge columns must be plain background).
- `--vtop 10`: top fill strip in rows. Keep it thin, or letters get mirrored above the logo.
- `--vbot 16–24`: bottom fill strip. It must be below the product, or the vial gets copied into the footer.
- `--patch x0,y0,x1,y1` + `--patch-src <raw>`: fill the bottom by tiling a PLAIN patch instead. Use it for big bottom
  fills (e.g. 9:16 built from a 4:5). Take the patch from the plainest full-width surface, such as the raw 9:16's table
  front below its last line (`--patch-src gen/adN_916.png --patch 0,0.955,1,1`). Avoid patches with shadow bands: they
  repeat as visible stripes.

## 5. Finish (lift OFF, the planned proof, same value on both ratios)
```
export EVERLIFE_LIFT=0
$PY -I $T/finish_batch.py repo/adN_916.png qa/adN_916_fit.png --ratio 9:16 --product <id> --proof <trust|count|none> --fit trusted --shift 0
$PY -I $T/finish_batch.py repo/adN_45.png  qa/adN_45_fit.png  --ratio 4:5  --product <id> --proof <trust|count|none>
```
Never switch a planned proof to `none` to make it fit.

## 6. QA (look at every one, full size)
- The first text line is clear of the logo; the product, CTA and every line are clear of the proof row.
- **No mirrored copies:** letter fragments above the logo, a second vial or label in the footer, a mirrored arm or edge.
- No obvious repeating stripes in the fills; the label is still sharp; the type is still readable at story size.

Fail → adjust the band / strip / patch and re-run (free). Then `finish_batch.py --proof-check qa` must pass. Copy the
finals with the house names, build the contact sheet and `open` it.

## 7. When Free Fix can't help (offer a re-roll with its cost instead)
- k < 0.65 and no usable 4:5 raw.
- A person, text or the product touches a side edge (the mirror would copy it).
- No plain surface to tile.
- A wrong or garbled label, a compliance problem or a missing string.
