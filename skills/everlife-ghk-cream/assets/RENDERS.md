# GHK Peptide Cream product renders (✅ all in: topical cream, no tablet by design)

Source folder: `~/Everlife-Creative/asset-library/TABLETS-CAPSULES/GHK CREAM PEPTIDE/` (Drive asset library
1CYPd3P2vpjUkkQvD2WPOJ0P_kcmy7HvP → TABLETS-CAPSULES/GHK CREAM PEPTIDE). Three .webp files, each 502 × 2101, RGBA. Each was LOOKED
at (2026-11-02); all three show the same bottle, differing only in the strength line:

| File | Label reads (top → bottom) | Used? |
|---|---|---|
| `GHK-PEPTIDE CREAM.webp` | EVERLIFE · GHK · Peptide Cream · (gold rule, no strength) · RX ONLY · 30G | ✅ **main render** |
| `GHK-PEPTIDE CREAM 5_.webp` | EVERLIFE · GHK · Peptide Cream · 0.5% · RX ONLY · 30G | not used (the bible names no strength) |
| `GHK-PEPTIDE CREAM 2_.webp` | EVERLIFE · GHK · Peptide Cream · 2% · RX ONLY · 30G | not used (the bible names no strength) |

**The bottle:** a slim cylindrical airless pump bottle (about 1:4), polished champagne-gold cap (top third) and champagne-gold base,
deep navy matte label band in the middle. On the label: "EVERLIFE" wordmark in champagne gold (the E's drawn as three bars), "GHK" in
large white serif, "Peptide Cream" in white serif below it, a short gold rule, then a thin gold line with a gold dot, "RX ONLY" bottom
left and "30G" bottom right in small white sans. No "-Cu", no "copper" anywhere on the label.

Files in `assets/`:
- `ghk-cream_bottle.png` — the main render, transparency kept (only the rounded edges/corners are transparent; the bottle itself is
  opaque). Made by `new_product.py create` (crop to content), then **15,103 fully transparent pixels whose hidden RGB was coloured
  (10,964 non-white, chroma up to 51) were set to white**, so no hidden colour reaches an image model or Marketing Studio.
- `ghk-cream_bottle_ref.jpg` — the same render flattened on white (quality 92): attach this one to image models.

Missing / open:
- No tablet or capsule: correct for a topical cream (`product.json` `renders.pill` = null; the end card shows the bottle alone).
- No image of the cream itself (colour, texture, a swatch): keep it off camera until the team provides or confirms one.
- Check the render against the website when the landing page exists (bible: LP [PLACEHOLDER]).

LOOK at every render before use (right product, label, strength, clean background). Never use another product's render (Sermorelin
GHK's tablet and bottle are a different product).
