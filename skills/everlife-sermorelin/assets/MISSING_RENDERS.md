# Product renders: what's in, what's missing (plain Sermorelin, sublingual tablet, 1000 + 500 mcg)

| File | Strength | Status |
|---|---|---|
| `sermorelin_tablet.png` | both (assumed) | ✅ added 2026-10-28 (user download "Sermorelin tablet.png", from the asset library). Round orange tablet with an embossed "S", transparent, matches every current men's winner. ⚠ **Small:** 631×654 canvas, the tablet itself ~250 px across (the GHK tablet is ~1,240 px). Fine as a generation reference; soft if composited large on an end card. A higher-res version would help. A faint light fringe shows on the upper-right edge. Still to confirm that 500 and 1000 mcg share this tablet. |
| `sermorelin1000_bottle.png` | 1000 | ✅ added 2026-10-28 (user download "SERMORELIN 1000 MCG BOTTLE.png"), 682×1491, transparent outside the jar. Label: EVERLIFE (vertical) · RX · SERMORELIN · PRESCRIPTION · 30 SUBLINGUAL TABS · 1000 MCG. Checked against everlifemd.com/sermorelin/v1L_v2f: identical jar, cap and label to the site's 500 mcg bottle except the strength line. |
| `sermorelin1000_bottle_ref.jpg` | 1000 | ✅ made 2026-10-28 from the PNG above, flattened on white (no other change), for image-ad references. |
| `sermorelin500_bottle.png` | 500 | ✅ added 2026-10-29 (user download "SERMORELIN 500 MCG BOTTLE .png"), 682×1491, transparent outside the jar. Same jar, cap and label as the 1000 render; pixel diff: only the "SERMORELIN" band text (slightly re-set, reads the same) and the strength line "500 MCG" differ. Matches the website's bottle. |
| `sermorelin500_bottle_ref.jpg` | 500 | ✅ made 2026-10-29 from the PNG above, flattened on white (no other change), for image-ad references. |

The same download included "SERMORELIN TABLET (2).png": byte-identical to `sermorelin_tablet.png`, so the asset
library offers one tablet render for both strengths (confirm with design if the 500 mcg tablet looks different).

⚠ **Tablets inside the bottle don't match the tablet render** (pale, oblong placeholders inside the amber glass), same as
the Sermorelin GHK renders. The website's bottle has the same placeholders, so the render is correct. Ask image/video
models for "the label facing camera" and never zoom into the glass; flag at review if the inside tablets are noticeable.

**Not added on purpose:** "SERMORELIN INJECTION 3ML/5ML.png" (also downloaded 2026-10-28): injections, vials and needles
never appear in creative. Never use a Sermorelin GHK render (red label, green tablet: a different product).

Where: Drive asset library `1EJkg6ts2jwNWvVPgflHgxvsR3PquYfJF` (owner ed@everlifemd.com, per-product folders) and
`1CYPd3P2vpjUkkQvD2WPOJ0P_kcmy7HvP` (TABLETS/CAPSULES, owner ronnel@everlifemd.com).

Next once approved: register the product in Marketing Studio (preflight prints the command) and create the Creatify
project (see `creatify.json`). Delete this file only when every row is ✅.
