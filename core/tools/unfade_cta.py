#!/usr/bin/env python3
"""unfade_cta.py RAW FINAL OUT [--ratio 4:5|9:16|1:1] [--shift PX] [--rows FULL_FROM FULL_TO BLEND_TO]
finish_batch's transparent footer fades the art above it; this restores the raw rows so a CTA or last line stays crisp.
Defaults (1080 wide): 4:5 restore 1000–1088 fully, blend back by 1118 (Restora-Z, 2026-10-29); 9:16 1064–1150 → 1184; 1:1 760–820 → 850.
--shift = the px the finisher printed (shift=…px), so raw rows line up with the final."""
import argparse
import numpy as np
from PIL import Image
ROWS = {"4:5": (1000, 1088, 1118), "9:16": (1064, 1150, 1184), "1:1": (760, 820, 850)}
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("raw"); ap.add_argument("final"); ap.add_argument("out")
    ap.add_argument("--ratio", default="4:5", choices=ROWS); ap.add_argument("--shift", type=int, default=0)
    ap.add_argument("--rows", type=int, nargs=3); a = ap.parse_args()
    fin = Image.open(a.final).convert("RGB"); W, H = fin.size
    raw = Image.open(a.raw).convert("RGB"); raw = raw.resize((W, int(raw.height*W/raw.width)), Image.LANCZOS)
    canvas = Image.new("RGB", (W, H)); canvas.paste(raw, (0, a.shift))
    f0, f1, b1 = a.rows or ROWS[a.ratio]
    F, R = np.asarray(fin).astype(np.float32), np.asarray(canvas).astype(np.float32)
    w = np.zeros(H, np.float32); w[f0:f1] = 1.0
    if b1 > f1: w[f1:b1] = np.linspace(1, 0, b1-f1, dtype=np.float32)
    out = F*(1-w[:, None, None]) + R*w[:, None, None]
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(a.out, quality=95); print(f"done {a.out}: rows {f0}-{f1} restored, blended to {b1}")
if __name__ == "__main__": main()
