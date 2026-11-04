#!/usr/bin/env python3
"""setup.py <source folder> <work dir> <prefix>  -> copies every image to <work>/src/<prefix>NN.png, writes map.tsv,
prints the size counts and builds read_N.jpg sheets (6 ads each) so every ad's text can be read before prompting."""
import sys, os, shutil, collections
from PIL import Image, ImageDraw
src, work, pre = sys.argv[1], os.path.expanduser(sys.argv[2]), sys.argv[3]
for d in ("src", "raw", "final"): os.makedirs(os.path.join(work, d), exist_ok=True)
files = sorted(f for f in os.listdir(src) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")))
sizes = collections.Counter(); rows = []
for i, f in enumerate(files, 1):
    n = f"{pre}{i:02d}"; im = Image.open(os.path.join(src, f)); sizes[im.size] += 1
    im.convert("RGB").save(os.path.join(work, "src", n + ".png")); rows.append(f"{n}\t{f}")
open(os.path.join(work, "map.tsv"), "w").write("\n".join(rows) + "\n")
print("sizes:", dict(sizes), "| files:", len(files))
fs = [r.split("\t")[0] for r in rows]
for k in range(0, len(fs), 6):
    W, H = 640, 960 if list(sizes)[0][1] / list(sizes)[0][0] > 1.5 else 800
    sh = Image.new("RGB", (3 * W, 2 * H), "white"); d = ImageDraw.Draw(sh)
    for i, n in enumerate(fs[k:k + 6]):
        x, y = (i % 3) * W, (i // 3) * H
        sh.paste(Image.open(os.path.join(work, "src", n + ".png")).convert("RGB").resize((W, H)), (x, y)); d.text((x + 5, y + 5), n, fill="red")
    sh.save(os.path.join(work, f"read_{k // 6 + 1}.jpg"), quality=88)
