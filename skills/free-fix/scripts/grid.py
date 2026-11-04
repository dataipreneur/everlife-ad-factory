#!/usr/bin/env python3
"""Draw a 5% grid over one or more raws so the content band (--top / --bottom) can be read off.
grid.py out.jpg raw1.png [raw2.png ...]   (3 per row, 450 px wide each)"""
import sys
from PIL import Image, ImageDraw, ImageFont

out, files = sys.argv[1], sys.argv[2:]
try:
    font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 16)
except Exception:
    font = ImageFont.load_default()
tiles = []
for p in files:
    im = Image.open(p).convert('RGB')
    W = 450
    H = round(im.height * W / im.width)
    im = im.resize((W, H))
    d = ImageDraw.Draw(im)
    for k in range(1, 20):
        y = round(H * k / 20)
        d.line([(0, y), (W, y)], fill=(255, 0, 0) if k % 2 == 0 else (255, 160, 0), width=1)
        d.text((2, y - 16), '%.2f' % (k / 20), fill='red', font=font)
    d.text((W - 200, 4), p.split('/')[-1][:28], fill='red', font=font)
    tiles.append(im)
cols = min(3, len(tiles))
rows = [tiles[i:i + cols] for i in range(0, len(tiles), cols)]
heights = [max(t.height for t in r) for r in rows]
sheet = Image.new('RGB', (cols * 460, sum(heights) + 10 * len(rows)), 'white')
y = 0
for r, h in zip(rows, heights):
    for i, t in enumerate(r):
        sheet.paste(t, (i * 460, y))
    y += h + 10
sheet.save(out, quality=88)
print(out)
