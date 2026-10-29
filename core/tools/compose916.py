#!/usr/bin/env python3
"""compose916.py APPROVED_4x5 PLATE_9x16 OUT [--panel 740x925@170,150] [--feather 32]
Builds a 9:16 from an APPROVED 4:5 ad: the ad becomes an exact panel feathered into a text-free 9:16 background plate generated
FROM that ad (Creatify playground, 1 credit: "a 9:16 background plate continuing this ad's scene, same palette and light, NO text,
NO product, NO logo; horizon at <h>%"). Then: finish_batch.py OUT FINAL --ratio 9:16 --fit trusted (logo + safe-area footer).
Numbers from the Restora-Z batch-33 builder (5/5 passed where native 9:16 re-makes failed 5/5)."""
import argparse, re
import numpy as np
from PIL import Image
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("approved"); ap.add_argument("plate"); ap.add_argument("out")
    ap.add_argument("--panel", default="740x925@170,150"); ap.add_argument("--feather", type=int, default=32); a = ap.parse_args()
    pw, ph, px, py = map(int, re.match(r"(\d+)x(\d+)@(\d+),(\d+)", a.panel).groups())
    plate = Image.open(a.plate).convert("RGB").resize((1080, 1920), Image.LANCZOS)
    panel = Image.open(a.approved).convert("RGB").resize((pw, ph), Image.LANCZOS)
    f = a.feather; m = np.ones((ph, pw), np.float32); r = np.linspace(0, 1, f, dtype=np.float32)
    m[:f] *= r[:, None]; m[-f:] *= r[::-1][:, None]; m[:, :f] *= r[None, :]; m[:, -f:] *= r[::-1][None, :]
    mask = Image.fromarray((m*255).astype(np.uint8))
    plate.paste(panel, (px, py), mask); plate.save(a.out, quality=95); print(f"done {a.out}: panel {pw}x{ph} at ({px},{py})")
if __name__ == "__main__": main()
