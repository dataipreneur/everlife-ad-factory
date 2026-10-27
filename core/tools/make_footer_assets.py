"""Cut the APPROVED footer art (Trustpilot 4.9 badge, Doctor Prescribed, Ships Free From Pharmacy) out of the
team's reference screenshots into transparent PNGs, one set per tone. The art is never redrawn or generated.
  python make_footer_assets.py <dark stacked screenshot> <light stacked screenshot>
Panel colours = the screenshots' own backgrounds (kept in finish_modern.PANEL_DARK / PANEL_LIGHT)."""
import os, sys
import numpy as np
from PIL import Image

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "footer")
BOXES = {  # x0, y0, x1, y1 in the 1550x870 stacked screenshots (found by scanning for non-background pixels)
    "dark":  {"badge": (623, 115, 961, 240), "doctor": (244, 439, 618, 562), "ships": (856, 439, 1334, 562)},
    "light": {"badge": (591, 116, 948, 251), "doctor": (222, 441, 596, 564), "ships": (834, 441, 1312, 564)},
}


def cut(img, box, pad=10):
    x0, y0, x1, y1 = box
    c = np.asarray(img.crop((x0 - pad, y0 - pad, x1 + pad, y1 + pad)).convert("RGB")).astype(np.float32)
    border = np.concatenate([c[:3].reshape(-1, 3), c[-3:].reshape(-1, 3), c[:, :3].reshape(-1, 3), c[:, -3:].reshape(-1, 3)])
    bg = np.median(border, 0)
    dist = np.abs(c - bg).max(2)
    a = np.clip((dist - 4) / 36, 0, 1)                      # soft edge: ≤4 → clear, ≥40 → solid
    rgba = np.dstack([c, a * 255]).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA")


def main(dark_png, light_png):
    os.makedirs(OUT, exist_ok=True)
    for tone, path in (("dark", dark_png), ("light", light_png)):
        im = Image.open(path)
        for name, box in BOXES[tone].items():
            cut(im, box).save(f"{OUT}/{name}_{tone}.png")
    print("saved", sorted(os.listdir(OUT)))


if __name__ == "__main__":
    main(*sys.argv[1:3])
