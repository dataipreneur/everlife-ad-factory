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


# Per-part alpha edge (levels from the panel colour → clear … solid). The icon circles sit only 16-32 levels from the panel, so
# their band must be low; the Trustpilot badge has a soft drop shadow in the reference panel (4-32 levels), which must stay OUT,
# so its band is high (Mitansh 2026-11-05: the first fix turned that shadow into a cream halo).
EDGE = {"badge": (32, 44), "doctor": (6, 12), "ships": (6, 12)}


def cut(img, box, pad=10, edge=(6, 12)):
    x0, y0, x1, y1 = box
    c = np.asarray(img.crop((x0 - pad, y0 - pad, x1 + pad, y1 + pad)).convert("RGB")).astype(np.float32)
    border = np.concatenate([c[:3].reshape(-1, 3), c[-3:].reshape(-1, 3), c[:, :3].reshape(-1, 3), c[:, -3:].reshape(-1, 3)])
    bg = np.median(border, 0)
    dist = np.abs(c - bg).max(2)
    # SOLID art (Mitansh 2026-11-05: "blurry … not solid" rows over photos): the old soft ramp (≤4 clear → ≥40 solid) left the
    # icon circles, which sit only 16-32 levels from the panel colour, 35-75% transparent, and the badge edges soft. Over a photo
    # they ghosted. Now: anything 12+ levels from the panel is fully opaque; only a 6-level band (6-12) anti-aliases the edge.
    lo, hi = edge
    a = np.clip((dist - lo) / (hi - lo), 0, 1)
    rgba = np.dstack([c, a * 255]).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA")


def compose_row(tone):
    """proof_row_clear(.png | _dark.png): the three parts in one row at the finisher's layout, for the video tools (standard_footer)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import finish_batch as fb
    foot = fb.build_footer(1080, tone, "", fb.PROOF_W, with_disclaimer=False, proof="trust")
    bbox = foot.getbbox()
    return foot.crop(bbox)


def card(img, box, pad=14, radius=16):
    """The Trustpilot badge as a SOLID card: the badge with its own panel background, nothing keyed out (Mitansh 2026-11-05:
    "use the images directly to put on top of them"). Rounded corners only; every pixel inside is opaque."""
    x0, y0, x1, y1 = box
    c = img.crop((x0 - pad, y0 - pad, x1 + pad, y1 + pad)).convert("RGBA")
    mask = Image.new("L", c.size, 0)
    from PIL import ImageDraw
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, c.width - 1, c.height - 1], radius=radius, fill=255)
    c.putalpha(mask)
    return c


USER_BADGE = {"dark": os.path.join(OUT, "user", "trustpilot_dark.png"),     # white "Trustpilot" wordmark, for dark backgrounds
              "light": os.path.join(OUT, "user", "trustpilot_light.png")}   # dark wordmark, for light backgrounds
BADGE_BOX = {"dark": (358, 145), "light": (377, 155)}   # the standard badge part size the finisher scales from


def user_badge(tone):
    """Mitansh's transparent Trustpilot badge (2026-11-05), hardened so every badge pixel is solid, fitted into the standard box."""
    im = Image.open(USER_BADGE[tone]).convert("RGBA")
    a = np.asarray(im).astype(np.float32)
    a[:, :, 3] = np.clip((a[:, :, 3] - 40) / 60, 0, 1) * 255          # ≥100 → solid, ≤40 → clear (removebg leaves soft interiors)
    im = Image.fromarray(a.astype(np.uint8), "RGBA"); im = im.crop(im.getbbox())
    bw, bh = BADGE_BOX[tone]; inner = (bw - 24, bh - 24)
    sc = min(inner[0] / im.width, inner[1] / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    box = Image.new("RGBA", (bw, bh), (0, 0, 0, 0)); box.alpha_composite(im, ((bw - im.width) // 2, (bh - im.height) // 2))
    return box


def main(dark_png, light_png):
    os.makedirs(OUT, exist_ok=True)
    for tone, path in (("dark", dark_png), ("light", light_png)):
        im = Image.open(path)
        for name, box in BOXES[tone].items():
            if name == "badge" and os.path.exists(USER_BADGE[tone]):
                user_badge(tone).save(f"{OUT}/{name}_{tone}.png")          # the real transparent badge wins
            else:
                (card(im, box) if name == "badge" else cut(im, box, edge=EDGE[name])).save(f"{OUT}/{name}_{tone}.png")
    print("saved", sorted(os.listdir(OUT)))
    assets = os.path.dirname(OUT)
    compose_row("dark").save(os.path.join(assets, "proof_row_clear.png"))          # white text: for dark backgrounds
    compose_row("light").save(os.path.join(assets, "proof_row_clear_dark.png"))    # dark text: for light backgrounds
    print("composed proof_row_clear.png / proof_row_clear_dark.png from the solid parts")


if __name__ == "__main__":
    main(*sys.argv[1:3])
