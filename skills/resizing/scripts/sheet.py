#!/usr/bin/env python3
"""sheet.py <work dir> <out.jpg> <target tag 9x16|4x5> [ids...]  side-by-side: source left, new size right, with the
Meta 9:16 safe box (x156-924, y144-1385) drawn on 9:16 images. Skips ids without a final."""
import sys, os
from PIL import Image, ImageDraw
work, out, tag = sys.argv[1], sys.argv[2], sys.argv[3]; os.chdir(os.path.expanduser(work))
ids = [n for n in sys.argv[4:] if os.path.exists(f"final/{n}_{tag}.png")]
def load(p):
    im = Image.open(p).convert("RGB")
    if im.size == (1080, 1920): ImageDraw.Draw(im).rectangle([156, 144, 924, 1385], outline=(0, 255, 0), width=6)
    return im
w = 405; cols = min(4, len(ids)) or 1; rows = (len(ids) + cols - 1) // cols
sh = Image.new("RGB", (cols * (2 * w + 30), rows * 740), "white")
for i, n in enumerate(ids):
    x, y = (i % cols) * (2 * w + 30), (i // cols) * 740
    for j, p in enumerate((f"src/{n}.png", f"final/{n}_{tag}.png")):
        im = load(p); h = int(w * im.height / im.width); sh.paste(im.resize((w, h)), (x + j * (w + 5), y + (720 - h) // 2))
sh.save(out, quality=88); print("sheet:", ids)
