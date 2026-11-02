# Epithalon product render (vial)

- `epithalon_bottle.png`: cut out from a white background (562×1280 RGBA). Source: asset library
  `VIALS/EPITHALON/EPITALON 10MG-ML 5ML VIAL (screenshot 2026-11-02).jpg`, Priestley's download 2026-11-02, a **screenshot**
  (592×1280 RGB JPG on white, no transparency).
- `epithalon_bottle_ref.jpg`: the same vial flattened on white (the image-model reference).

Looked at 2026-11-02: the right product (Epithalon vial). The cut-out was checked on green: clean edges, no white halo; the clear
glass (shoulder, neck, base below the label) is kept as part of the vial, with the render's own white reflections. The vial's
base sits on the bottom edge of the source. **Wish list:** a full-resolution render from the asset library. This one is a
screenshot: fine as a model reference and at end-card size, soft if composited large.

**Label, exactly (top to bottom):** clear glass vial with a stepped brushed-silver flip-off cap over a silver crimp; a matte
**teal** label wrapping the body; the **black EVERLIFE wordmark** (the stylised E's) upper left; **EPITALON** large in white,
centred; **10MG/ML** in white below it; a thin light-blue horizontal rule; **RX ONLY** (left) and **5ML** (right) in white.

**Vial wording for prompts:** "a squat clear glass vial with a stepped brushed-silver flip-off cap over a silver crimp; a matte teal
label with the black EVERLIFE wordmark at the upper left, 'EPITALON' large in white, '10MG/ML' below it, a thin light-blue rule,
'RX ONLY' and '5ML' in white at the bottom."

## ⚠ Spelling: open question for Justin
The bible page and every piece of copy say **"Epithalon"**; the vial label reads **"EPITALON"** (no H). Copy always uses the
bible's "Epithalon". The label is never edited, "corrected" or redrawn in renders, prompts or finishing (`keep_case` in
product.json holds both spellings). QA checks the generated label reads EPITALON, like the render. Justin to confirm which
spelling the product page and the bible should carry.

Never use another product's render (MOTS-c, BPC-157, the stacks, the GHK-Cu/Epithalon stack).
