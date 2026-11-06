"""Cut the APPROVED footer art (Trustpilot 4.9 badge, Doctor Prescribed, Ships Free From Pharmacy) into transparent PNGs, one
set per tone. The art is never redrawn or generated.
  python make_footer_assets.py                       # from assets/footer/approved_row.jpg + user/trustpilot_<tone>.png (2026-11-05)
  python make_footer_assets.py <dark stacked screenshot> <light stacked screenshot>   # older route: the stacked reference panels
Sources, newest wins: ALL THREE pieces come from the approved row Mitansh sent on 2026-11-05 (the badge keyed by region so its
white stars / "4.9" / "EXCELLENT" stay solid; see badge_from_approved_row); older: the user/ removebg badge; Doctor Prescribed +
Ships Free = keyed from the approved row (assets/footer/approved_row.jpg: black on white, 1:1 with the finished size; "Try to directly
include these"). Panel colours = the screenshots' own backgrounds (kept in finish_modern.PANEL_DARK / PANEL_LIGHT)."""
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


APPROVED_ROW = os.path.join(OUT, "approved_row.jpg")      # the row Mitansh sent 2026-11-05 (988x148, black on white)
ROW_X = {"doctor": (368, 588), "ships": (657, 978)}       # icon + two text lines, measured on that image (dividers excluded)
ROW_UP = 1.30             # keeps each piece in the reference's proportion to the badge once the finisher scales the row
PIECE_H = 143             # the piece canvas height the finisher centres on (same as the older cut pieces)
PIECE_FILL = {"light": (18, 22, 30), "dark": (240, 242, 240)}


def cut_from_approved_row(name, tone):
    """Doctor Prescribed / Ships Free from the approved row: black on white → alpha, filled near-black (light backgrounds) or
    off-white (dark backgrounds). The JPEG's soft edge is cleaned with one curve; nothing is redrawn."""
    from PIL import ImageFilter
    x0, x1 = ROW_X[name]
    a = np.asarray(Image.open(APPROVED_ROW).convert("RGB")).astype(np.float32)
    # SOLID: ink darker than lum 155 → fully opaque (the truck's thin lines never reached 125); lighter than 210 → clear; the band between is the edge
    # (the ghosted row over photos, Mitansh 2026-11-05 "this was the problem we had", came from soft alpha inside the art)
    alpha = np.clip((255 - a.mean(axis=2) - 45) / 55, 0, 1)[:, x0:x1] * 255   # lum ≤ 155 solid (thin truck lines too), ≥ 210 clear
    ys = np.where(alpha.max(axis=1) > 40)[0]
    alpha = alpha[max(0, ys[0] - 4):min(alpha.shape[0], ys[-1] + 5)]
    mask = Image.fromarray(alpha.astype(np.uint8))
    mask = mask.resize((round(mask.width * ROW_UP), round(mask.height * ROW_UP)), Image.LANCZOS)
    m = np.clip((np.asarray(mask).astype(np.float32) - 8) * 1.08, 0, 255); m[m < 24] = 0                      # re-harden after the resize; no faint haze
    mask = Image.fromarray(m.astype(np.uint8))
    piece = Image.new("RGBA", mask.size, PIECE_FILL[tone] + (255,)); piece.putalpha(mask)
    canvas = Image.new("RGBA", (mask.width + 20, PIECE_H), (0, 0, 0, 0))
    canvas.alpha_composite(piece, (10, (PIECE_H - mask.height) // 2))
    return canvas


BADGE_X = (0, 330)        # the Trustpilot badge in the approved row (art at x 20-290; the first divider is at x 337)


def badge_from_approved_row(tone):
    """The Trustpilot 4.9 badge from the approved row, keyed by REGION, never by colour. Every shape (the star, the five boxes,
    the shield, the wordmark) is cut on LUMINANCE against the white paper (full JPEG resolution: a chroma key left ragged, pale
    edges); the green/teal shapes are then hole-filled so the white stars, "4.9" and "EXCELLENT" inside them are solid; the
    "Trustpilot" wordmark is recoloured like Doctor/Ships: near-black for light backgrounds, off-white for dark ones. The
    2026-10-27 badge keyed every white pixel out with the background, which made the stars and the 4.9 see-through on every
    light ad once the footer haze came off (2026-11-04)."""
    from PIL import ImageDraw, ImageFilter
    x0, x1 = BADGE_X
    rgb = np.asarray(Image.open(APPROVED_ROW).convert("RGB")).astype(np.float32)[:, x0:x1]
    lum = rgb.mean(axis=2); sat = rgb.max(axis=2) - rgb.min(axis=2)
    xs = np.arange(rgb.shape[1])[None, :]
    a_lum = np.clip((215 - lum) / 30, 0, 1)                                   # lum ≤ 185 solid, ≥ 215 paper; the band is the edge
    cand = Image.fromarray((sat >= 12).astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(5))   # near the coloured shapes
    shapes = Image.fromarray((((a_lum >= 0.5) & (np.asarray(cand) > 0)).astype(np.uint8)) * 255)
    pad = Image.new("L", (shapes.width + 4, shapes.height + 4), 0); pad.paste(shapes, (2, 2))
    ImageDraw.floodfill(pad, (0, 0), 128)                                     # 0 left inside = stars / "4.9" / "EXCELLENT"
    inside = np.asarray(pad)[2:-2, 2:-2] != 128                               # coloured shapes + their insides, all solid
    alpha = np.maximum(a_lum, inside.astype(np.float32))
    # the 1 px seams between the five star boxes never reach white in the JPEG (lum ~200): carve them so the boxes stay separate
    rows = np.where((sat[:, :200] >= 40).sum(axis=1) > 60)[0]; by0, by1 = rows.min(), rows.max()
    colmin = lum[by0 + 6:by1 - 6, :200].min(axis=0)
    for gx in np.where(colmin > 190)[0]:
        if 25 < gx < 190:
            alpha[by0:by1 + 1, gx] = np.where(lum[by0:by1 + 1, gx] > 185, 0, alpha[by0:by1 + 1, gx])
    out = rgb.copy()
    edge = (alpha > 0) & (alpha < 1)                                          # un-blend the edges from the white paper
    out[edge] = np.clip((rgb[edge] - (1 - alpha[edge])[:, None] * 255) / alpha[edge][:, None], 0, 255)
    ink = (alpha > 0) & (~inside) & (xs < 200)                                # the wordmark only (left of the shield; its JPEG fringe too)
    out[ink] = np.array(PIECE_FILL[tone], np.float32)
    ys, xx = np.where(alpha > 0.02)
    y0, y1, xa, xb = ys.min(), ys.max() + 1, xx.min(), xx.max() + 1
    piece = Image.fromarray(np.dstack([out, alpha * 255]).astype(np.uint8)[y0:y1, xa:xb])
    piece = piece.resize((round(piece.width * ROW_UP), round(piece.height * ROW_UP)), Image.LANCZOS)
    a = np.asarray(piece).copy(); al = np.clip((a[:, :, 3].astype(np.float32) - 8) * 1.08, 0, 255); al[al < 24] = 0; a[:, :, 3] = al   # re-harden after the resize; no faint haze
    piece = Image.fromarray(a)
    canvas = Image.new("RGBA", (piece.width + 20, piece.height + 20), (0, 0, 0, 0))
    canvas.alpha_composite(piece, (10, 10))
    return canvas


def check_solid(path):
    """Refuse to keep a piece that is not solid (the same gate every finisher runs: standard_footer.assert_solid_footer_art)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import standard_footer as sf
    n, soft, soft_col = sf.footer_art_report(path)
    sf.assert_solid_footer_art(path)
    print(f"   ✓ {os.path.basename(path)}: interior {n} px, {soft:.1%} soft, coloured insides {soft_col:.1%} soft")


def main(dark_png=None, light_png=None):
    os.makedirs(OUT, exist_ok=True)
    for tone, path in (("dark", dark_png), ("light", light_png)):
        im = Image.open(path) if path else None
        for name, box in BOXES[tone].items():
            if name == "badge" and os.path.exists(APPROVED_ROW):
                badge_from_approved_row(tone).save(f"{OUT}/{name}_{tone}.png")   # the approved row wins (region-keyed, solid)
            elif name == "badge" and os.path.exists(USER_BADGE[tone]):
                user_badge(tone).save(f"{OUT}/{name}_{tone}.png")          # older: the removebg badge (soft insides)
            elif name != "badge" and os.path.exists(APPROVED_ROW):
                cut_from_approved_row(name, tone).save(f"{OUT}/{name}_{tone}.png")   # the approved row wins
            elif im is None:
                sys.exit(f"{name}_{tone}: no approved source (user/ badge or approved_row.jpg) and no screenshot given")
            else:
                (card(im, box) if name == "badge" else cut(im, box, edge=EDGE[name])).save(f"{OUT}/{name}_{tone}.png")
            check_solid(f"{OUT}/{name}_{tone}.png")
    print("saved", sorted(os.listdir(OUT)))
    assets = os.path.dirname(OUT)
    compose_row("dark").save(os.path.join(assets, "proof_row_clear.png"))          # white text: for dark backgrounds
    compose_row("light").save(os.path.join(assets, "proof_row_clear_dark.png"))    # dark text: for light backgrounds
    check_solid(os.path.join(assets, "proof_row_clear.png")); check_solid(os.path.join(assets, "proof_row_clear_dark.png"))
    print("composed proof_row_clear.png / proof_row_clear_dark.png from the solid parts")


if __name__ == "__main__":
    main(*sys.argv[1:3])   # no args = the approved sources only
