#!/usr/bin/env python3
"""Fit a 9:16 raw above the proof footer WITHOUT smearing (Mitansh, 2026-11-02: "make sure to do it always").

The standard fix when a raw's text or product runs into the footer band. It scales the whole raw (uniformly) so its
content band [--top, --bottom] lands in [--band-top, --band-bottom] of the 1080x1920 canvas, then fills the margins by
MIRROR-TILING a thin, text-free strip of the raw's own edge (strip, flipped strip, strip, ...). No edge-stretch of a
single pixel row, no blur, no padding colour, no AI. Real texture (linen, plaster, wall, sky) continues naturally.

  mirror_fit_916.py raw.png out.png --top 0.15 --bottom 0.76            # defaults: band 0.115-0.635, strip 28 px
  finish_batch.py out.png FINAL.png --ratio 9:16 --product <id> --fit trusted --shift 0

--top / --bottom: the content band as fractions of the raw's height (read them off the raw: top of the first text line,
bottom of the lowest product / button). The defaults for the band keep content under the Everlife logo (ends ~0.11) and
above the footer (starts y 1236 = 0.644).

LIMIT: the strip must be background. If a person, text or the product touches a side edge of the raw, the mirror copies
it (a mirrored arm / letter): the raw FAILS, re-roll it instead (cost approved). Always look at the result.
"""
import argparse
import numpy as np
from PIL import Image

W, H = 1080, 1920


def tile(edge, n, axis, before):
    """Mirror-tile `edge` outward to length n along axis (before = prepend side)."""
    flipped = np.flip(edge, axis=axis)
    reps, tot, i = [], 0, 0
    while tot < n:
        blk = flipped if i % 2 == 0 else edge
        reps.append(blk)
        tot += blk.shape[axis]
        i += 1
    ext = np.concatenate(reps[::-1] if before else reps, axis=axis)
    sl = [slice(None)] * 3
    sl[axis] = slice(ext.shape[axis] - n, None) if before else slice(0, n)
    return ext[tuple(sl)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('raw')
    ap.add_argument('out')
    ap.add_argument('--top', type=float, required=True)
    ap.add_argument('--bottom', type=float, required=True)
    ap.add_argument('--band-top', type=float, default=0.115)
    ap.add_argument('--band-bottom', type=float, default=0.635)
    ap.add_argument('--strip', type=int, default=28, help='px of text-free edge to mirror (side fill)')
    a = ap.parse_args()

    src = Image.open(a.raw).convert('RGB').resize((W, H), Image.LANCZOS)
    k = min(1.0, (a.band_bottom - a.band_top) / (a.bottom - a.top))
    if k < 0.65:
        raise SystemExit(f'scale {k:.2f} < 0.65: type would get too small for 50+ readers. Re-roll the raw instead.')
    w, h = round(W * k), round(H * k)
    art = np.asarray(src.resize((w, h), Image.LANCZOS))
    x0 = (W - w) // 2
    y0 = round(a.band_top * H - a.top * h)
    if y0 < 0:                       # the raw's empty top overflows the canvas: drop it
        art = art[-y0:]
        y0 = 0
    art = art[:H - y0]
    h = art.shape[0]

    s = min(a.strip, w // 4)
    left = tile(art[:, :s], x0, 1, True) if x0 > 0 else art[:, :0]
    right = tile(art[:, -s:], W - x0 - w, 1, False) if W - x0 - w > 0 else art[:, :0]
    band = np.concatenate([left, art, right], axis=1)
    full = band
    if y0 > 0:
        full = np.concatenate([tile(band[:s * 3], y0, 0, True), full], axis=0)
    if H - y0 - h > 0:
        full = np.concatenate([full, tile(band[-s * 6:], H - y0 - h, 0, False)], axis=0)
    Image.fromarray(full[:H, :W]).save(a.out)
    print(f'{a.out}: k={k:.2f}  art {w}x{h} at ({x0},{y0})  mirrored fill: sides {x0}px, top {y0}px, bottom {H - y0 - h}px')


if __name__ == '__main__':
    main()
