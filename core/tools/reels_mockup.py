#!/usr/bin/env python3
"""reels_mockup.py: wrap a 9:16 creative (png or mp4) in an Instagram-Reels-style phone frame, for internal preview only.

usage: reels_mockup.py <creative.png|.mp4> <out.png|.mp4> [--account "EverlifeMD"] [--caption "..."] [--cta "Learn more"]
       [--likes 3] [--ffmpeg PATH]
The UI is drawn with Pillow primitives (no Instagram assets). Phone canvas 1080x2400; creative sits at y=100..2020.
"""
import argparse, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 2400
TOP = 100          # status bar height; creative starts here
CRE_H = 1920
NAV_Y = 2230       # bottom nav icons centre


def font(px, bold=False):
    here = os.path.dirname(os.path.abspath(__file__))
    for p in (os.path.join(here, "assets", "fonts", "Inter.ttf"), "/System/Library/Fonts/Supplemental/Arial.ttf"):
        if os.path.exists(p):
            f = ImageFont.truetype(p, px)
            try:
                f.set_variation_by_name("Bold" if bold else "Regular")
            except Exception:
                pass
            return f
    return ImageFont.load_default()


def heart(d, cx, cy, s, fill=None, outline=(255, 255, 255), w=6):
    pts = []
    for i in range(0, 361, 4):
        t = math.radians(i)
        x = 16 * math.sin(t) ** 3
        y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        pts.append((cx + x * s / 17, cy + y * s / 17 - s * 0.05))
    if fill:
        d.polygon(pts, fill=fill)
    d.line(pts + [pts[0]], fill=outline, width=w, joint="curve")


def bubble(d, cx, cy, s, w=6):
    d.ellipse([cx - s, cy - s * 0.9, cx + s, cy + s * 0.9], outline=(255, 255, 255), width=w)
    d.polygon([(cx - s * 0.55, cy + s * 0.62), (cx - s * 0.85, cy + s * 1.05), (cx - s * 0.2, cy + s * 0.85)], fill=(255, 255, 255))
    d.polygon([(cx - s * 0.5, cy + s * 0.55), (cx - s * 0.78, cy + s * 0.95), (cx - s * 0.22, cy + s * 0.78)], fill=(0, 0, 0))


def plane(d, cx, cy, s, w=6):
    pts = [(cx - s, cy - s * 0.35), (cx + s, cy - s * 0.95), (cx + s * 0.25, cy + s), (cx - s * 0.05, cy + s * 0.15)]
    d.polygon(pts, outline=(255, 255, 255), width=w)
    d.line([(cx - s * 0.05, cy + s * 0.15), (cx + s, cy - s * 0.95)], fill=(255, 255, 255), width=w)


def more(d, cx, cy, s, w=6):
    d.line([(cx - s, cy - s * 0.4), (cx + s, cy - s * 0.4)], fill=(255, 255, 255), width=w)
    d.line([(cx - s, cy + s * 0.4), (cx + s * 0.35, cy + s * 0.4)], fill=(255, 255, 255), width=w)


def home(d, cx, cy, s, w=6):
    d.polygon([(cx - s, cy), (cx, cy - s), (cx + s, cy)], outline=(255, 255, 255), width=w)
    d.rectangle([cx - s * 0.8, cy - s * 0.1, cx + s * 0.8, cy + s], outline=(255, 255, 255), width=w)
    d.rectangle([cx - s * 0.25, cy + s * 0.35, cx + s * 0.25, cy + s], fill=(255, 255, 255))


def reels(d, cx, cy, s, active=True):
    if active:
        d.rounded_rectangle([cx - s * 2.0, cy - s * 1.35, cx + s * 2.0, cy + s * 1.35], radius=s * 0.9, fill=(38, 38, 38))
    d.rounded_rectangle([cx - s, cy - s, cx + s, cy + s], radius=s * 0.3, fill=(255, 255, 255))
    d.polygon([(cx - s * 0.25, cy - s * 0.45), (cx - s * 0.25, cy + s * 0.45), (cx + s * 0.5, cy)], fill=(0, 0, 0))


def search(d, cx, cy, s, w=6):
    d.ellipse([cx - s, cy - s, cx + s * 0.6, cy + s * 0.6], outline=(255, 255, 255), width=w)
    d.line([(cx + s * 0.4, cy + s * 0.4), (cx + s, cy + s)], fill=(255, 255, 255), width=w)


def build_ui(account, caption, cta, likes):
    ui = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    d = ImageDraw.Draw(ui)
    # creative window is transparent
    d.rectangle([0, TOP, W, TOP + CRE_H], fill=(0, 0, 0, 0))
    # status bar
    d.text((40, 28), "8:56", font=font(40, True), fill=(255, 255, 255))
    for i, hgt in enumerate((14, 22, 30, 38)):
        d.rectangle([W - 300 + i * 16, 70 - hgt, W - 300 + i * 16 + 10, 70], fill=(255, 255, 255))
    for k in (1.0, 0.7, 0.4):
        d.arc([W - 395 - 40 * k, 50 - 40 * k, W - 395 + 40 * k, 50 + 40 * k], 225, 315, fill=(255, 255, 255), width=6)
    d.rounded_rectangle([W - 200, 30, W - 70, 72], radius=10, outline=(255, 255, 255), width=4)
    d.rectangle([W - 194, 36, W - 140, 66], fill=(255, 255, 255))
    d.rounded_rectangle([W - 66, 44, W - 58, 58], radius=3, fill=(255, 255, 255))
    # bottom-of-reel gradient (over the creative, like the app)
    grad = Image.new("RGBA", (W, 620), (0, 0, 0, 0))
    gp = grad.load()
    for y in range(620):
        a = int(220 * (y / 620) ** 1.6)
        for x in range(0, W, 1):
            gp[x, y] = (0, 0, 0, a)
    ui.alpha_composite(grad, (0, TOP + CRE_H - 620))
    d = ImageDraw.Draw(ui)
    # right-hand action column
    cx = W - 95
    heart(d, cx, 1540, 46)
    d.text((cx - 12, 1592), str(likes), font=font(32, True), fill=(255, 255, 255))
    bubble(d, cx, 1700, 44)
    plane(d, cx, 1840, 44)
    more(d, cx, 1965, 36)
    # Learn more button
    bx0, by0, bx1, by1 = 48, 1730, W - 200, 1860
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=28, fill=(237, 29, 36))
    d.text((bx0 + 44, by0 + 42), cta, font=font(44, True), fill=(255, 255, 255))
    ax = bx1 - 70
    d.line([(ax - 14, by0 + 52), (ax + 4, by0 + 70), (ax - 14, by0 + 88)], fill=(255, 255, 255), width=6, joint="curve")
    # account row
    d.ellipse([48, 1900, 152, 2004], fill=(60, 60, 70), outline=(255, 255, 255), width=3)
    d.text((80, 1928), "E", font=font(48, True), fill=(230, 220, 200))
    d.text((176, 1928), account, font=font(42, True), fill=(255, 255, 255))
    # black band below the reel: caption + Ad tag + nav
    d.rectangle([0, TOP + CRE_H, W, H], fill=(0, 0, 0, 255))
    cap = caption if len(caption) <= 44 else caption[:41] + "..."
    d.text((48, 2042), cap, font=font(40), fill=(255, 255, 255))
    d.text((48, 2108), "Ad", font=font(32), fill=(190, 190, 190))
    d.line([(0, 2170), (W, 2170)], fill=(40, 40, 40), width=2)
    xs = [110, 325, 540, 755, 970]
    home(d, xs[0], NAV_Y, 38)
    reels(d, xs[1], NAV_Y, 34)
    plane(d, xs[2], NAV_Y, 40)
    d.ellipse([xs[2] + 14, NAV_Y + 10, xs[2] + 54, NAV_Y + 50], fill=(237, 29, 36))
    d.text((xs[2] + 26, NAV_Y + 14), "1", font=font(26, True), fill=(255, 255, 255))
    search(d, xs[3], NAV_Y, 38)
    d.ellipse([xs[4] - 40, NAV_Y - 40, xs[4] + 40, NAV_Y + 40], fill=(90, 80, 70), outline=(255, 255, 255), width=3)
    d.rounded_rectangle([W / 2 - 150, 2340, W / 2 + 150, 2352], radius=6, fill=(255, 255, 255))
    return ui


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("creative"); ap.add_argument("out")
    ap.add_argument("--account", default="EverlifeMD")
    ap.add_argument("--caption", default="Stop treating recovery like an afterthought.")
    ap.add_argument("--cta", default="Learn more")
    ap.add_argument("--likes", default="3")
    ap.add_argument("--ffmpeg", default=os.environ.get("FF", "ffmpeg"))
    a = ap.parse_args()
    ui = build_ui(a.account, a.caption, a.cta, a.likes)
    is_video = a.creative.lower().endswith((".mp4", ".mov"))
    ui_path = os.path.splitext(a.out)[0] + "_ui.png"
    ui.save(ui_path)
    if not is_video:
        cre = Image.open(a.creative).convert("RGB").resize((W, CRE_H), Image.LANCZOS)
        canvas = Image.new("RGBA", (W, H), (0, 0, 0, 255))
        canvas.paste(cre, (0, TOP))
        canvas.alpha_composite(ui)
        canvas.convert("RGB").save(a.out, quality=95)
    else:
        cmd = [a.ffmpeg, "-y", "-v", "error", "-i", a.creative, "-i", ui_path,
               "-filter_complex",
               f"color=black:s={W}x{H}:r=30[bg];[0:v]scale={W}:{CRE_H}[v];[bg][v]overlay=0:{TOP}:shortest=1[b];[b][1:v]overlay=0:0",
               "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", a.out]
        subprocess.run(cmd, check=True)
    os.remove(ui_path)
    print("wrote", a.out)


if __name__ == "__main__":
    main()
