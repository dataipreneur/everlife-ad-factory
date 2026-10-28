"""Batch static finisher: the generated ad + a COMPACT, TRANSPARENT approved footer laid over its calm bottom.

The image model designs the whole ad (headline, benefits, product, scene) and leaves the bottom ~18% calm. We lay a
soft gradient + the footer there: Everlife logo, the approved Trustpilot 4.9 / Doctor Prescribed / Ships Free art (cut
from the team's screenshots) and the verbatim disclaimer. The creative lead asked for it 35% smaller and transparent (2026-10-27).

usage: finish_batch.py <generated.png> <out.png> --ratio 4:5|9:16|1:1 --product <id> [--tone auto|dark|light]
       (--product takes the verbatim disclaimer from product.json; the older --disclaimer "<verbatim>" still works)
       finish_batch.py --content-ratio 4:5        prints the aspect ratio to request from the image model
"""
import argparse, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

T = os.path.dirname(os.path.abspath(__file__))
FD, FOOT = f"{T}/assets/fonts", f"{T}/assets/footer"
SIZES = {"4:5": (1080, 1350), "9:16": (1080, 1920), "1:1": (1080, 1080)}
# what to ask the image model for: the final shape itself (the footer is laid over the calm bottom ~18%)
MODEL_RATIO = {"4:5": "4:5", "9:16": "9:16", "1:1": "1:1"}
LIGHT = (251, 251, 246)
DISC_SIZE, DISC_LH = 21, 26   # compact footer (creative lead: 35% smaller, transparent)


def sans(size, weight="Regular"):
    f = ImageFont.truetype(f"{FD}/Inter.ttf", size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def wrap(d, text, font, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    return lines + [cur]


def art(name, tone, scale):
    im = Image.open(f"{FOOT}/{name}_{tone}.png").convert("RGBA")
    return im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)


def build_footer(W, tone, disclaimer):
    """Compact transparent footer: logo, approved proof art row, disclaimer. Returns an RGBA layer (no background)."""
    fw = W - 80
    s = 0.56
    parts = [art("badge", tone, s), art("doctor", tone, s), art("ships", tone, s)]
    rh = max(p.height for p in parts)
    d0 = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    lines = wrap(d0, disclaimer, sans(DISC_SIZE), fw)
    logo = Image.open(f"{T}/assets/logo_cream.png").convert("RGBA")
    lw = 150
    logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    ink = (16, 24, 44)
    if tone == "light":
        a = logo.split()[-1]; logo = Image.new("RGBA", logo.size, ink + (0,)); logo.putalpha(a)
    h = 10 + logo.height + 8 + rh + 6 + DISC_LH * len(lines) + 22
    foot = Image.new("RGBA", (W, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(foot)
    y = 10
    foot.alpha_composite(logo, ((W - lw) // 2, y)); y += logo.height + 8
    gap = 22
    tw = sum(p.width for p in parts) + 4 * gap + 2
    x = (W - tw) // 2
    rule = (255, 255, 255, 90) if tone == "dark" else (16, 24, 44, 60)
    for i, p in enumerate(parts):
        foot.alpha_composite(p, (x, y + (rh - p.height) // 2)); x += p.width + gap
        if i < 2:
            d.line([(x, y + 8), (x, y + rh - 8)], fill=rule, width=1); x += 1 + gap
    y += rh + 6
    col = (236, 238, 236, 255) if tone == "dark" else (40, 44, 56, 255)
    f = sans(DISC_SIZE, "Medium")
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=col); y += DISC_LH
    return foot


def scrim(W, h, tone, top_fade=120):
    """Soft gradient behind the footer so it reads on any photo (transparent at the top, ~70% at the bottom)."""
    col = (8, 12, 26) if tone == "dark" else (250, 249, 245)
    band = Image.new("RGBA", (W, h + top_fade), col + (0,))
    bd = ImageDraw.Draw(band)
    for i in range(band.height):
        t = min(1.0, i / top_fade)
        bd.line([(0, i), (W, i)], fill=col + (int(185 * t ** 1.2),))
    return band


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("gen", nargs="?"); ap.add_argument("out", nargs="?")
    ap.add_argument("--ratio", default="4:5", choices=SIZES)
    ap.add_argument("--product", default="", help="product id: the verbatim disclaimer comes from its product.json")
    ap.add_argument("--disclaimer", default="", help="verbatim disclaimer (older usage; must match --product if both)")
    ap.add_argument("--tone", default="auto", choices=["auto", "dark", "light"])
    ap.add_argument("--content-ratio", help="print the model aspect ratio for this final ratio and exit")
    a = ap.parse_args()
    if a.content_ratio:
        print(MODEL_RATIO[a.content_ratio]); return
    if a.product:
        import sys
        sys.path.insert(0, T)
        import product
        PR = product.load(a.product)
        if a.disclaimer and a.disclaimer != PR["disclaimer"]:
            raise SystemExit(f"❌ --disclaimer differs from {a.product}'s product.json (it must be the bible text, verbatim)")
        a.disclaimer = PR["disclaimer"]
    if not a.disclaimer:
        raise SystemExit("❌ pass --product <id> (or the verbatim bible disclaimer with --disclaimer)")
    W, H = SIZES[a.ratio]
    gen = Image.open(a.gen).convert("RGB")
    g = np.asarray(gen.resize((64, 64))).reshape(-1, 3).astype(np.float64)
    bottom = np.asarray(gen.crop((0, int(gen.height * 0.85), gen.width, gen.height)).resize((64, 16))).reshape(-1, 3).astype(np.float64)
    lum = lambda c: 0.299 * c[..., 0] + 0.587 * c[..., 1] + 0.114 * c[..., 2]
    tone = a.tone if a.tone != "auto" else ("dark" if lum(bottom).mean() < 150 else "light")
    # scale to the full width; if the generation is shorter than the canvas (e.g. an old 1:1), extend its own
    # bottom softly; if taller, keep the top
    sc = W / gen.width
    gw, gh = W, int(gen.height * sc)
    g2 = gen.resize((gw, gh), Image.LANCZOS)
    out = Image.new("RGB", (W, H))
    if gh < H:
        from PIL import ImageFilter
        strip = g2.crop((0, gh - max(8, gh // 40), gw, gh)).resize((W, H - gh + 60)).filter(ImageFilter.GaussianBlur(26))
        out.paste(strip, (0, gh - 60))
        mask = Image.new("L", (gw, gh), 255)
        md = ImageDraw.Draw(mask)
        for i in range(60):
            md.line([(0, gh - 1 - i), (gw, gh - 1 - i)], fill=int(255 * i / 60))
        out.paste(g2, (0, 0), mask)
    else:
        out.paste(g2.crop((0, 0, W, H)), (0, 0))
    foot = build_footer(W, tone, a.disclaimer)
    bottom_pad = 48 if (W, H) == (1080, 1920) else 0          # 9:16: same bottom line as the videos
    fy = H - foot.height - bottom_pad
    sc_layer = scrim(W, foot.height + bottom_pad, tone)
    o = out.convert("RGBA")
    o.alpha_composite(sc_layer, (0, H - sc_layer.height))
    o.alpha_composite(foot, (0, fy))
    out = o.convert("RGB")
    out.save(a.out, quality=95)
    print(f"done {a.out}  tone={tone}  footer={foot.height}px ({foot.height / H * 100:.0f}% of height, transparent)")


if __name__ == "__main__":
    main()
