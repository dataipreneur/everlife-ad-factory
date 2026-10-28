# Product renders: what's in, what's missing (one skill, two strengths, one tablet)

| File | Strength | Status |
|---|---|---|
| `sghk_tablet.png` | both | ✅ added 2026-10-28 (user download "SERMORELIN GHK TABLET.webp", converted to PNG, 2304×1792, transparent). Green rounded-diamond tablet with an embossed "S". Accepted by the user because it appears next to the Sermorelin GHK bottle in nearly every live Sermorelin GHK winner (Winning Ads page, Oct 9–15). Still to confirm with Ed/Ronnel that both strengths use this tablet. |
| `sghk1000_bottle_ref.jpg` | 1000 | ✅ added 2026-10-28 (user download "Sermorelin GHK 1000.jpg"). Checked against everlifemd.com/sermorelin-ghk/f-fb: same jar, cap and label design as the site's 500 mcg bottle; label reads SERMORELIN GHK 1000 · 30 TABLETS · 1000 MCG. 496×1080 JPG on black, no transparency: fine as a generation reference, not for compositing. |
| `sghk1000_bottle.png` | 1000 | 🟡 **stand-in** added 2026-10-28: cut out locally from the user's "1000 on white" JPG ("2026-10-28 16.26.17.jpg", from the asset library): white background removed from the outer edge only, label pixels untouched, edge trimmed 1 px. 494×1078 (smaller than the 500's 864 px: fine at end-card size). Replace with the designers' official NOBG file when it arrives. |
| `sghk500_bottle_ref.jpg` | 500 | ✅ added 2026-10-28 (user download "2026-10-28 16.26.02.jpg"): 500 mcg bottle on white, 584×1280. Label SERMORELIN GHK · 30 TABLETS · 500 MCG, same design as the site. |
| `sghk500_bottle.png` | 500 | ✅ added 2026-10-28 (user download "SERMORELINGHK NOBG 2.webp", converted to PNG): **transparent**, 864×1891, label 500 MCG. Same render as the 500 bottle on everlifemd.com/sermorelin-ghk. |

Also received 2026-10-28 ("2026-10-28 16.26.17.jpg"): the 1000 bottle on a **white** background, 496×1080, same picture
as `sghk1000_bottle_ref.jpg` (black background). Not added: still not a cut-out.

Which ads work today: **500, 1000 and "either"**, images and videos (1000 videos use the stand-in cut-out above).

Where: Drive asset library, folder **SERMORELIN GHK** (`1EJkg6ts2jwNWvVPgflHgxvsR3PquYfJF`, owner ed@everlifemd.com), plus
`1CYPd3P2vpjUkkQvD2WPOJ0P_kcmy7HvP` (TABLETS/CAPSULES, owner ronnel@everlifemd.com) for the tablet. The Drive connector can't
list these folders (it only sees files shared directly), so download them by hand or paste their file links.

Before adding (product-correctness gate): open each image and check it against the live product page. Never trust a filename.
When the 1000 transparent bottle is in: run preflight (registers the product in Marketing Studio) and create the Creatify
project (see `creatify.json`). Delete this file only when every row is ✅.

## ⚠ Open: tablets inside the bottle vs the tablet render (2026-10-28)
Both bottle renders (500 and 1000) show **round tan tablets inside the jar**; the tablet render is a **green rounded diamond with an embossed "S"**. Every ad that shows the bottle and the tablet together (ours and the live winners) shows both. Ask Ed/Ronnel/pharmacy which tablet is real, and for a bottle render with the correct tablets inside. Until answered, ads showing both are held at review. Never repaint the jar's contents in a prompt (that alters the approved render).

**Answered 2026-10-28 (real footage):** in winner BASE125 (a filmed creator video) the tablets that come out of the real Sermorelin GHK bottle are the **green rounded-diamond "S"**. The tablet render is right; the **bottle renders' tan tablets are placeholders**. Still needed: bottle renders (500 and 1000) with the green tablets inside, from the design team. Until then, ads showing the bottle carry the render's tan tablets: creative lead decides whether to run them.
