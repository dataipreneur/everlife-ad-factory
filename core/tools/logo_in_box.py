#!/usr/bin/env python3
"""logo_in_box.py IN OUT: find the EMPTY WHITE BOX the image model left in the masthead (top 16%, right 45%) and centre the real
Everlife logo in it (ink colour, 82% of the box width, max 60% of the box height). Connected-component detection: naive row/col
scans grab white letters. Numbers from the Restora-Z comic batches (2026-10-29)."""
import os, sys
from collections import deque
import numpy as np
from PIL import Image
T = os.environ.get("EVERLIFE_TOOLS", os.path.expanduser("~/Everlife-Creative/tools"))
INK = (20, 28, 45)

def find_box(img, white=228, min_w=0.12, min_h=0.035, solid=0.85, ds=4):
    W, H = img.size
    x0, y1 = int(W * 0.55), int(H * 0.16)
    reg = img.crop((x0, 0, W, y1)).convert("RGB").resize(((W - x0) // ds, y1 // ds))
    a = np.asarray(reg); m = (a > white).all(axis=2)
    seen = np.zeros_like(m, bool); best = None
    for sy in range(m.shape[0]):
        for sx in range(m.shape[1]):
            if not m[sy, sx] or seen[sy, sx]: continue
            q = deque([(sy, sx)]); seen[sy, sx] = True; pts = []
            while q:
                y, x = q.popleft(); pts.append((y, x))
                for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < m.shape[0] and 0 <= nx < m.shape[1] and m[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True; q.append((ny, nx))
            ys, xs = zip(*pts); bw, bh = (max(xs)-min(xs)+1), (max(ys)-min(ys)+1)
            if bw*ds < min_w*W or bh*ds < min_h*H or len(pts) < solid*bw*bh: continue
            if best is None or bw*bh > best[0]: best = (bw*bh, min(xs), min(ys), bw, bh)
    if not best: return None
    _, bx, by, bw, bh = best
    return (x0 + bx*ds, by*ds, x0 + (bx+bw)*ds, (by+bh)*ds)

def main():
    src, out = sys.argv[1], sys.argv[2]
    img = Image.open(src).convert("RGBA")
    box = find_box(img)
    if not box: raise SystemExit("❌ no empty white box found in the masthead (top 16%, right 45%); prompt one or use finish_batch's logo")
    x0, y0, x1, y1 = box; bw, bh = x1-x0, y1-y0
    logo = Image.open(f"{T}/assets/logo_cream.png").convert("RGBA")
    lw = int(bw*0.82); lh = int(logo.height*lw/logo.width)
    if lh > bh*0.60: lh = int(bh*0.60); lw = int(logo.width*lh/logo.height)
    logo = logo.resize((lw, lh), Image.LANCZOS); alpha = logo.split()[-1]
    ink = Image.new("RGBA", logo.size, INK + (0,)); ink.putalpha(alpha)
    img.alpha_composite(ink, (x0 + (bw-lw)//2, y0 + (bh-lh)//2))
    img.convert("RGB").save(out, quality=95); print(f"done {out}: box {box}, logo {lw}x{lh}")
if __name__ == "__main__": main()
