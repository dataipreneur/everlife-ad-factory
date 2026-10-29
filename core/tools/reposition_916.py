#!/usr/bin/env python3
"""reposition_916.py: fit a generated 9:16 ad raw into the Meta safe band WITHOUT any AI edit (0 credits).

The model (GPT Image / Nano Banana) lands content 8-25% lower than asked and ignores "scale down and move up" edits.
This tool scales the artwork so its content band sits between --band-top and --band-bottom of the canvas (defaults match
finish_batch.py: logo zone above 12.5%, footer from ~61.7%), centres it, and fills the rest with a blurred, darkened
plate made from the same image (colour-matched background), with a feathered seam. Nothing inside the artwork is re-rendered.

usage: reposition_916.py RAW OUT [--top F --bottom F] [--crop-top F --crop-bottom F] [--composite RENDER x0 y0 x1 y1]
  --top/--bottom   content band in fractions of the raw height (auto-detected when omitted)
  --crop-*         rows of the raw to keep (fractions); the rest is replaced by the plate
  --composite      paste a transparent product render over box (x0 y0 x1 y1) of the raw first (fixes a garbled label)
"""
import argparse, sys
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import numpy as np

def detect_band(im, thresh=14.0, pad=0.015):
    g = np.asarray(ImageOps.grayscale(im), dtype=np.float32)
    bg = np.median(np.concatenate([g[:int(g.shape[0]*0.03)], g[-int(g.shape[0]*0.03):]]))
    act = np.maximum(g.std(axis=1), np.abs(g.mean(axis=1) - bg))
    rows = np.where(act > thresh)[0]
    if len(rows) == 0: return 0.0, 1.0
    h = g.shape[0]
    return max(0.0, rows[0]/h - pad), min(1.0, rows[-1]/h + pad)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('raw'); ap.add_argument('out')
    ap.add_argument('--top', type=float); ap.add_argument('--bottom', type=float)
    ap.add_argument('--crop-top', type=float, default=0.0); ap.add_argument('--crop-bottom', type=float, default=1.0)
    ap.add_argument('--band-top', type=float, default=0.13); ap.add_argument('--band-bottom', type=float, default=0.65)
    ap.add_argument('--composite', nargs=5, metavar=('RENDER','X0','Y0','X1','Y1'))
    ap.add_argument('--blur', type=float, default=70); ap.add_argument('--darken', type=float, default=0.45)
    ap.add_argument('--feather', type=int, default=12)
    ap.add_argument('--fill', choices=['reflect','plate'], default='reflect', help='reflect = sharp mirrored continuation of the artwork edges (default, no blur); plate = blurred darkened plate')
    a = ap.parse_args()

    src = Image.open(a.raw).convert('RGB'); W, H = src.size
    if a.composite:
        r = Image.open(a.composite[0]).convert('RGBA'); x0,y0,x1,y1 = map(int, a.composite[1:])
        bh = y1-y0; r = r.resize((int(r.width*bh/r.height), bh), Image.LANCZOS)
        src.paste(r, ((x0+x1)//2 - r.width//2, y0), r)
    t, b = (a.top, a.bottom) if a.top is not None and a.bottom is not None else detect_band(src)
    t = max(t, a.crop_top); b = min(b, a.crop_bottom)
    k = min(1.0, (a.band_bottom - a.band_top) / max(b - t, 1e-6))
    crop = src.crop((0, int(a.crop_top*H), W, int(a.crop_bottom*H)))
    art = crop.resize((max(1,int(W*k)), max(1,int(crop.height*k))), Image.LANCZOS)
    x = (W - art.width)//2
    # move ONLY when necessary (Mitansh 2026-10-29: no stretched/blurred pads): natural placement first,
    # shift down only if the headline sits above the logo zone, shift up only if the content bottom overflows the band
    y = 0
    top_at = (t - a.crop_top)*H*k
    if top_at < a.band_top*H: y = int(a.band_top*H - top_at)
    bot_at = y + (b - a.crop_top)*H*k
    if bot_at > a.band_bottom*H: y -= int(bot_at - a.band_bottom*H)

    if a.fill == 'reflect':
        arr = np.asarray(art)
        top = max(0, y); left = max(0, x)
        bottom = max(0, H - (y + art.height)); right = max(0, W - (x + art.width))
        # crop the artwork if it overflows the canvas, then reflect-pad the rest (seamless, sharp, no blur)
        cy0 = max(0, -y); cx0 = max(0, -x)
        arr = arr[cy0:cy0 + min(art.height - cy0, H), cx0:cx0 + min(art.width - cx0, W)]
        def pad(a, n, axis):
            while n > 0:
                m = min(n, a.shape[axis] - 1)
                a = np.pad(a, [(m, 0) if axis == 0 else (0, 0), (m, 0) if axis == 1 else (0, 0), (0, 0)][:3] if False else
                           ((m, 0), (0, 0), (0, 0)) if axis == 0 else ((0, 0), (m, 0), (0, 0)), mode='edge')
                n -= m
            return a
        # pad top/left by reflecting; bottom/right by flipping then reflecting
        arr = pad(arr, top, 0); arr = pad(arr, left, 1)
        arr = pad(arr[::-1], bottom, 0)[::-1]; arr = pad(arr[:, ::-1], right, 1)[:, ::-1]
        plate = Image.fromarray(arr[:H, :W])
        if plate.size != (W, H):
            full = Image.new('RGB', (W, H)); full.paste(plate, (0, 0)); plate = full
    else:
        # background plate: cover-fit the artwork, blur, darken
        s = max(W/art.width, H/art.height)
        plate = art.resize((int(art.width*s)+2, int(art.height*s)+2), Image.BILINEAR)
        plate = plate.crop(((plate.width-W)//2, (plate.height-H)//2, (plate.width-W)//2+W, (plate.height-H)//2+H))
        plate = plate.filter(ImageFilter.GaussianBlur(a.blur))
        plate = ImageEnhance.Brightness(plate).enhance(1.0 - a.darken)

        # feathered mask for the artwork (edges only; feather never reaches inner content)
        mask = Image.new('L', art.size, 255)
        f = min(a.feather, art.width//6, art.height//6)
        if f > 0:
            m = np.asarray(mask, dtype=np.float32)
            ramp = np.linspace(0, 1, f, dtype=np.float32)
            m[:f, :] *= ramp[:, None]; m[-f:, :] *= ramp[::-1][:, None]
            m[:, :f] *= ramp[None, :]; m[:, -f:] *= ramp[::-1][None, :]
            mask = Image.fromarray(m.astype(np.uint8))
        # don't feather edges that touch the canvas edge (content runs off-frame there)
        plate.paste(art, (x, y), mask)
    plate.save(a.out)
    print(f"{a.out}: band {t:.3f}-{b:.3f} -> k={k:.2f}, art {art.size} at ({x},{y}); content bottom {(y+(b-a.crop_top)*H*k)/H:.3f}")

if __name__ == '__main__': main()
