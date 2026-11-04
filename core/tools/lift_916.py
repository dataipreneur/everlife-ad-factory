#!/usr/bin/env python3
"""lift_916.py: move a 9:16 raw UP (free) when the model left too much empty headroom, so the product / CTA clears the proof row.

    lift_916.py <raw.png> <out.png> --up <px>          # px on the 1080x1920 canvas
    lift_916.py <raw.png> <out.png> --auto             # as far up as the logo band allows (first content row stays >= y 230)

Mitansh 2026-11-04: "youre leaving way way more space empty on the top ... they can easily shift upwards!" The top <px> rows (empty
headroom only) are cut and the bottom gap is filled with a SHARP mirror of the raw's own bottom rows (no blur, no stretch, no
padding colour). Only for raws whose bottom band is a plain surface (floor, table top, fabric, paper): the script refuses when the
bottom strip it would mirror carries text or hard edges, or when the lift would push content into the logo band.
Then finish with `finish_batch.py out.png … --shift 0`.
"""
import argparse, os, sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import finish_batch as fb  # noqa: E402

W, H = 1080, 1920
LOGO_CLEAR = 230          # the logo sits at y 150-194; the ad's first content row must stay at or below this

ap = argparse.ArgumentParser()
ap.add_argument("raw"); ap.add_argument("out")
g = ap.add_mutually_exclusive_group(required=True)
g.add_argument("--up", type=int)
g.add_argument("--auto", action="store_true")
a = ap.parse_args()

im = Image.open(a.raw).convert("RGB")
if im.size != (W, H):
    im = im.resize((W, H), Image.LANCZOS)
top = min(fb.first_content_row(im, int(H * 0.45)), fb.content_top(im, int(H * 0.45)))
room = top - LOGO_CLEAR
up = room if a.auto else a.up
if up <= 0:
    sys.exit(f"nothing to lift: first content row at y {top} (logo needs it at y >= {LOGO_CLEAR})")
if up > room:
    sys.exit(f"❌ --up {up} would put content (first row y {top}) under the logo; max is {room}")
strip = im.crop((0, H - up, W, H))
# the strip we mirror must be calm: low edge density (a plain surface), never text or a product
e = np.asarray(strip.convert("L").resize((270, max(1, up // 4)))).astype(np.float64)
busy = (np.abs(np.diff(e, axis=1)) > 28).mean()
if busy > 0.06:
    sys.exit(f"❌ the bottom {up}px is not a plain surface (edge density {busy:.2f}); re-roll instead of lifting")
out = Image.new("RGB", (W, H))
out.paste(im.crop((0, up, W, H)), (0, 0))
out.paste(strip.transpose(Image.FLIP_TOP_BOTTOM), (0, H - up))
out.save(a.out)
print(f"lifted {up}px (first content row now y {top - up})  -> {a.out}")
