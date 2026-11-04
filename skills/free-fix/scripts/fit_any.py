#!/usr/bin/env python3
"""Uniformly scale a raw (any aspect) so its content band [top,bottom] lands in [band_top,band_bottom] of a WxH canvas;
fill margins by mirror-tiling the raw's own thin edge strips (same method as mirror_fit_916.py, but aspect-preserving)."""
import argparse
import numpy as np
from PIL import Image


def tile(edge, n, axis, before):
    flipped = np.flip(edge, axis=axis)
    reps, tot, i = [], 0, 0
    while tot < n:
        blk = flipped if i % 2 == 0 else edge
        reps.append(blk); tot += blk.shape[axis]; i += 1
    ext = np.concatenate(reps[::-1] if before else reps, axis=axis)
    sl = [slice(None)] * 3
    sl[axis] = slice(ext.shape[axis] - n, None) if before else slice(0, n)
    return ext[tuple(sl)]


ap = argparse.ArgumentParser()
ap.add_argument('raw'); ap.add_argument('out')
ap.add_argument('--size', default='1080x1350')
ap.add_argument('--top', type=float, required=True); ap.add_argument('--bottom', type=float, required=True)
ap.add_argument('--band-top', type=float, required=True); ap.add_argument('--band-bottom', type=float, required=True)
ap.add_argument('--strip', type=int, default=28)
ap.add_argument('--vtop', type=int, default=12)
ap.add_argument('--vbot', type=int, default=20)
ap.add_argument('--patch-src', default='')
ap.add_argument('--patch', default='', help='x0,y0,x1,y1 fractions of the raw: plain surface patch to tile for the bottom fill')
a = ap.parse_args()
W, H = map(int, a.size.split('x'))
src = Image.open(a.raw).convert('RGB')
rw, rh = src.size
h = round((a.band_bottom - a.band_top) * H / (a.bottom - a.top))
w = round(rw * h / rh)
if w > W:  # never wider than the canvas
    w = W; h = round(rh * W / rw)
k = w / W
if k < 0.65:
    raise SystemExit(f'scale {k:.2f} < 0.65: too small for 50+ readers')
art = np.asarray(src.resize((w, h), Image.LANCZOS))
x0 = (W - w) // 2
y0 = round(a.band_top * H - a.top * h)
if y0 < 0:
    art = art[-y0:]; y0 = 0
art = art[:H - y0]; h = art.shape[0]
s = a.strip
left = tile(art[:, :s], x0, 1, True) if x0 > 0 else art[:, :0]
right = tile(art[:, -s:], W - x0 - w, 1, False) if W - x0 - w > 0 else art[:, :0]
band = np.concatenate([left, art, right], axis=1)
full = band
if y0 > 0:
    full = np.concatenate([tile(band[:a.vtop], y0, 0, True), full], axis=0)
nb = H - y0 - h
if nb > 0:
    if a.patch:
        px0, py0, px1, py1 = map(float, a.patch.split(','))
        ps = Image.open(a.patch_src).convert('RGB') if a.patch_src else src
        sc = np.asarray(ps.resize((W, round(ps.height * W / ps.width)), Image.LANCZOS))
        pt = sc[round(py0 * sc.shape[0]):round(py1 * sc.shape[0]), round(px0 * W):round(px1 * W)]
        row = tile(pt, W, 1, False)
        fill = tile(row, nb, 0, False)
    else:
        fill = tile(band[-a.vbot:], nb, 0, False)
    full = np.concatenate([full, fill], axis=0)
Image.fromarray(full[:H, :W]).save(a.out)
print(f'{a.out}: k={k:.2f} art {w}x{h} at ({x0},{y0}); fill sides {x0}px top {y0}px bottom {H - y0 - h}px')
