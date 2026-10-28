"""Review-burst animation: verbatim Trustpilot review cards that slam in one after another into a collage,
with the product name highlighted (the style the team liked in the "Moon Sheep" ad). Renders a transparent-free
PNG frame sequence (white background) that full_layout.py overlays as a ~2.4 s insert.

usage (standalone): review_burst.py <reviews.json> R1,R3,R4,R2 <out_dir> [--w 1080 --h 1920 --fps 24 --dur 2.4]
"""
import argparse, json, math, os, re
from PIL import Image, ImageDraw, ImageFont

AV = "/System/Library/Fonts/Avenir Next.ttc"
GREEN, INK, GREY, HL = (0, 182, 122), (25, 25, 28), (110, 110, 118), (255, 236, 61)
AVATAR = [(230, 120, 170), (250, 214, 180), (120, 150, 160), (180, 120, 110), (200, 225, 200), (190, 200, 240)]
HIGHLIGHT = r"Restora[- ]?Z"  # product-name regex; full_layout sets it from copy.json "highlight"


def font(size, name="Regular"):
    for i in range(20):
        try:
            f = ImageFont.truetype(AV, size, index=i)
        except OSError:
            break
        if " ".join(f.getname()).lower().endswith(name.lower()):
            return f
    return ImageFont.truetype(AV, size)


def star(d, cx, cy, r, fill):
    pts = []
    for k in range(10):
        ang = -math.pi / 2 + k * math.pi / 5
        rr = r if k % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=fill)


def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    return lines + [cur]


def draw_highlighted(d, x, y, line, f, progress=1.0):
    """Draw a line; yellow-highlight every product-name match of HIGHLIGHT (highlight grows with progress)."""
    for m in re.finditer(HIGHLIGHT, line, flags=re.I):
        x0 = x + d.textlength(line[:m.start()], font=f)
        x1 = x + d.textlength(line[:m.end()], font=f)
        x1 = x0 + (x1 - x0) * max(0.0, min(1.0, progress))
        asc, desc = f.getmetrics()
        d.rectangle([x0 - 2, y + 2, x1 + 2, y + asc + desc - 2], fill=HL)
    d.text((x, y), line, font=f, fill=INK)


def card(rv, width, idx, hl_progress=1.0):
    """One Trustpilot-style review card (white), verbatim text."""
    pad = 34
    nf, mf, tf, bf = font(38, "Demi Bold"), font(28), font(36, "Bold"), font(33)
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    body = rv.get("excerpt", rv["text"])
    blines = wrap(tmp, body, bf, width - 2 * pad)[:7]
    tlines = wrap(tmp, rv["title"], tf, width - 2 * pad)[:2]
    h = pad + 86 + 20 + 46 + 14 + 46 * len(tlines) + 12 + 44 * len(blines) + pad
    im = Image.new("RGBA", (width, h), (255, 255, 255, 255))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, width - 1, h - 1], 14, outline=(225, 225, 230), width=2)
    col = AVATAR[idx % len(AVATAR)]
    d.ellipse([pad, pad, pad + 72, pad + 72], fill=col)
    ini_f = font(28, "Demi Bold")
    d.text((pad + 36 - d.textlength(rv["initials"], font=ini_f) / 2, pad + 18), rv["initials"], font=ini_f, fill=(60, 40, 50))
    d.text((pad + 92, pad + 2), rv["name"], font=nf, fill=INK)
    d.text((pad + 92, pad + 44), f"US • {rv['count']}", font=mf, fill=GREY)
    d.text((width - pad - d.textlength(rv["date"], font=mf), pad + 6), rv["date"], font=mf, fill=GREY)
    y = pad + 86 + 20
    for k in range(5):
        x = pad + k * 50
        on = k < rv["stars"]
        d.rectangle([x, y, x + 44, y + 44], fill=GREEN if on else (220, 220, 225))
        star(d, x + 22, y + 23, 17, (255, 255, 255))
    y += 46 + 14
    for ln in tlines:
        draw_highlighted(d, pad, y, ln, tf, hl_progress); y += 46
    y += 12
    for ln in blines:
        draw_highlighted(d, pad, y, ln, bf, hl_progress); y += 44
    return im


def ease_out_back(t, s=1.7):
    t -= 1
    return t * t * ((s + 1) * t + s) + 1


def render(reviews, ids, out_dir, W=1080, H=1920, fps=24, dur=2.4):
    os.makedirs(out_dir, exist_ok=True)
    ids = [i for i in ids if i in reviews][:5]
    import safezones as sz
    sx0, sy0, sx1, sy1 = sz.safe_box(W, H)
    cw = int((sx1 - sx0) * 0.94)
    cards = [card(reviews[i], cw, k) for k, i in enumerate(ids)]
    # collage slots: staggered, overlapping, slightly offset left/right
    slots, y = [], sy0 + 16
    for k, c in enumerate(cards):
        x = sx0 if k % 2 == 0 else sx1 - cw
        slots.append((x, y))
        y += int(c.height * 0.62)
    total_h = y + int(cards[-1].height * 0.38)
    limit = sz.NOTCH[1] - 260 if (W, H) == (1080, 1920) else sy1   # stay above the proof block / Reels UI
    if total_h > limit:
        sc = (limit - sy0) / (total_h - sy0)
        slots = [(x, int(sy0 + 16 + (yy - sy0 - 16) * sc)) for x, yy in slots]
    n = int(fps * dur)
    hero_end = 0.55  # seconds the first card is shown big ("zoomed in"), highlight swipes on
    gap = (dur - hero_end - 0.5) / max(1, len(cards) - 1)
    for f in range(n):
        t = f / fps
        frame = Image.new("RGBA", (W, H), (255, 255, 255, 255))
        # first card: zoomed-in hero, then settles into its slot
        for k, c in enumerate(cards):
            if k == 0:
                if t < hero_end:
                    p = t / hero_end
                    hc = card(reviews[ids[0]], cw, 0, hl_progress=min(1, p * 1.6))
                    scale = 1.14 - 0.06 * p
                    big = hc.resize((int(hc.width * scale), int(hc.height * scale)), Image.LANCZOS)
                    frame.alpha_composite(big, ((W - big.width) // 2, max(sy0, (sy0 + sz.NOTCH[1] - big.height) // 2)))
                    continue
                p = min(1, (t - hero_end) / 0.18)
                scale = 1.08 - 0.08 * ease_out_back(p)
            else:
                start = hero_end + k * gap - gap * 0.6
                if t < start:
                    continue
                p = min(1, (t - start) / 0.16)
                scale = 1.25 - 0.25 * ease_out_back(p)
            img = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
            sx, sy = slots[k]
            frame.alpha_composite(img, (int(sx - (img.width - c.width) / 2), int(sy - (img.height - c.height) / 2)))
        frame.convert("RGB").save(f"{out_dir}/{f:03d}.png")
    return n


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("reviews"); ap.add_argument("ids"); ap.add_argument("out")
    ap.add_argument("--w", type=int, default=1080); ap.add_argument("--h", type=int, default=1920)
    ap.add_argument("--fps", type=int, default=24); ap.add_argument("--dur", type=float, default=2.4)
    a = ap.parse_args()
    R = json.load(open(a.reviews))
    print(render(R, a.ids.split(","), a.out, a.w, a.h, a.fps, a.dur), "frames")
