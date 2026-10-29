"""Build 1080x1920 overlay layers for the Restora-Z UGC ads.

LEGACY: run on its own, this is the original Restora-Z-only layer builder (its copy below is from the Restora-Z winner
Base207 / the Restora-Z bible page). full_layout.py imports it only for fonts, colours and drawing helpers, and replaces
every product value (disclaimer, benefits, CTA, renders) from the job's product.json + copy.json. Don't add product copy here.
Everything important sits inside the 9:16 safe band y 143-1275.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

P = sys.argv[1]  # project dir
SRC, OUT = f"{P}/source", f"{P}/layers"
W, H = 1080, 1920

AV_COND = "/System/Library/Fonts/Avenir Next Condensed.ttc"
AV = "/System/Library/Fonts/Avenir Next.ttc"


def font(path, size, name):
    for i in range(20):
        try:
            f = ImageFont.truetype(path, size, index=i)
        except OSError:
            break
        if " ".join(f.getname()).lower().endswith(name.lower()):
            return f
    raise SystemExit(f"font {name} not in {path}")


NAVY = (14, 26, 48)
GOLD = (236, 205, 140)
CREAM = (251, 250, 245)
TEAL = (98, 200, 190)
RED = (214, 48, 64)

HEAD = font(AV_COND, 70, "Heavy Italic")
SUB = font(AV_COND, 40, "Demi Bold Italic")
CHIP_T = font(AV_COND, 32, "Bold")
CHIP_B = font(AV, 23, "Medium")
PROOF = font(AV, 28, "Demi Bold")
PROOF_S = font(AV, 24, "Medium")
DISC = font(AV, 22, "Regular")
STICK = font(AV_COND, 44, "Heavy")
END_H = font(AV_COND, 76, "Heavy Italic")
END_NAME = font(AV_COND, 96, "Heavy")
END_B = font(AV, 36, "Demi Bold")
CTA = font(AV_COND, 50, "Heavy")

DISCLAIMER = ("AI-generated depictions and simulated portrayals used for illustrative advertising "
              "purposes. Not actual patients or medical providers. Disclaimer: Individual results "
              "may vary. Doctor-prescribed compounded sleep medication.")


def canvas():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def centered(d, y, text, f, fill):
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill)


def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = word
    return lines + [cur]


def gradient_band(img, y0, y1, alpha_top, alpha_bot):
    band = Image.new("RGBA", (W, y1 - y0))
    bd = ImageDraw.Draw(band)
    for i in range(y1 - y0):
        a = int(alpha_top + (alpha_bot - alpha_top) * i / max(1, y1 - y0 - 1))
        bd.line([(0, i), (W, i)], fill=NAVY + (a,))
    img.alpha_composite(band, (0, y0))


def logo(img, y, width):
    lg = Image.open(f"{SRC}/logo_cream.png")
    lg = lg.resize((width, int(lg.height * width / lg.width)), Image.LANCZOS)
    img.alpha_composite(lg, ((W - width) // 2, y))


def header_block(img):
    gradient_band(img, 0, 470, 235, 0)
    logo(img, 150, 466)
    d = ImageDraw.Draw(img)
    centered(d, 205, "A DIFFERENT APPROACH TO", HEAD, GOLD)
    centered(d, 277, "SLEEP SUPPORT.", HEAD, GOLD)
    centered(d, 360, "Three established ingredients,", SUB, CREAM)
    centered(d, 404, "compounded into one formula.", SUB, CREAM)


BAR_BG = (250, 249, 244)


def proof_block(img, bottom=1272, rw=960, pad=22, lh=30):
    """Everlife proof bar (Trustpilot badge, Doctor Prescribed, Ships Free) + verbatim disclaimer.

    The badge/icon row is the team's own bar artwork; the disclaimer is Restora-Z's bible text.
    Returns the bar's top y.
    """
    d = ImageDraw.Draw(img)
    row = Image.open(f"{SRC}/proof_row.png").convert("RGBA")
    row = row.resize((rw, int(row.height * rw / row.width)), Image.LANCZOS)
    lines = wrap(d, DISCLAIMER, DISC, 990 if pad < 22 else 950)
    h = pad + row.height + pad * 0.7 + 1 + pad * 0.6 + lh * len(lines) + pad * 0.7
    h = int(h)
    top = bottom - h
    d.rounded_rectangle([28, top, W - 28, bottom], 28, fill=BAR_BG + (255,))
    img.alpha_composite(row, ((W - rw) // 2, top + pad))
    ly = int(top + pad + row.height + pad * 0.7)
    d.line([(70, ly), (W - 70, ly)], fill=(222, 219, 211), width=1)
    ty = ly + pad * 0.6
    for ln in lines:
        centered(d, ty, ln, DISC, (112, 112, 106))
        ty += lh
    return top


END_HEAD = ["SLEEP EASIER,", "SLEEP LONGER"]
BENEFITS = ["Supports Falling + Staying Asleep", "Helps Reduce Nighttime Wake-Ups", "3-in-1 Sleep Formula"]
CTA_TEXT = "EXPLORE RESTORA-Z"
BOTTLE, PILL = "rz_bottle.png", "rz_capsule.png"

INGREDIENTS = [  # bible-approved ingredient claims, each on its own ingredient
    ("HYDROXYZINE", "Supports deep relaxation"),
    ("TRAZODONE", "Aids in falling asleep"),
    ("DOXEPIN", "Improves sleep maintenance"),
]


def chips(img):
    d = ImageDraw.Draw(img)
    y = 474
    for i, (name, claim) in enumerate(INGREDIENTS):
        d.rounded_rectangle([30, y, 360, y + 96], 20, fill=NAVY + (215,))
        d.ellipse([48, y + 18, 68, y + 38], fill=TEAL)
        d.text((80, y + 8), name, font=CHIP_T, fill=CREAM)
        d.text((48, y + 54), claim, font=CHIP_B, fill=GOLD)
        y += 96
        if i < 2:
            d.text((172, y - 6), "+", font=CHIP_T, fill=CREAM)
            y += 26


def sticker(text, fill, fg):
    img = canvas()
    d = ImageDraw.Draw(img)
    w = d.textlength(text, font=STICK) + 70
    x0, y0 = (W - w) / 2, 925
    d.rounded_rectangle([x0, y0, x0 + w, y0 + 70], 35, fill=fill)
    centered(d, y0 + 9, text, STICK, fg)
    return img


def endcard():
    img = canvas()
    img.alpha_composite(Image.new("RGBA", (W, H), NAVY + (222,)))
    from PIL import ImageFilter
    glow = canvas()
    ImageDraw.Draw(glow).ellipse([140, 360, 940, 860], fill=TEAL + (120,))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(110)))
    d = ImageDraw.Draw(img)
    logo(img, 150, 466)
    for i, ln in enumerate(END_HEAD):
        centered(d, 205 + 75 * i, ln, END_H, GOLD)
    # real product renders: bottle large + capsule hero in front
    bottle = Image.open(f"{SRC}/{BOTTLE}").convert("RGBA")
    bottle = bottle.crop(bottle.getbbox())
    bh = 340
    bottle = bottle.resize((int(bottle.width * bh / bottle.height), bh), Image.LANCZOS)
    if PILL:
        img.alpha_composite(bottle, (W // 2 - bottle.width // 2 + 120, 362))
        cap = Image.open(f"{SRC}/{PILL}").convert("RGBA")
        cap = cap.crop(cap.getbbox())
        cw = 400
        cap = cap.resize((cw, int(cap.height * cw / cap.width)), Image.LANCZOS)
        img.alpha_composite(cap, (W // 2 - cw // 2 - 150, 530))
    else:                                # a form without a tablet/capsule: the bottle alone, centred
        img.alpha_composite(bottle, (W // 2 - bottle.width // 2, 362))
    by = 716
    for b in BENEFITS:
        tw = d.textlength("✓  " + b, font=END_B)
        x = (W - tw) / 2
        d.text((x, by), "✓", font=font("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 36, "Regular"),
               fill=TEAL)
        d.text((x + d.textlength("✓  ", font=END_B), by), b, font=END_B, fill=CREAM)
        by += 52
    cw2 = 560
    centered(d, by + 4, "Over 100,000 happy customers", PROOF_S, GOLD)  # locked proof line
    top = proof_block(img)
    d.rounded_rectangle([(W - cw2) / 2, top - 92, (W + cw2) / 2, top - 20], 36, fill=GOLD)
    centered(d, top - 88, CTA_TEXT, CTA, NAVY)
    return img


def caption(text):
    img = canvas()
    d = ImageDraw.Draw(img)
    f = font(AV_COND, 50, "Heavy")
    lines = wrap(d, text, f, 860)
    y = 832 - 31 * (len(lines) - 1)
    for ln in lines:
        w = d.textlength(ln, font=f)
        d.rounded_rectangle([(W - w) / 2 - 22, y - 6, (W + w) / 2 + 22, y + 60], 16, fill=(255, 255, 255, 240))
        centered(d, y - 2, ln, f, NAVY)
        y += 68
    return img


if __name__ == "__main__":
    import json, os
    os.makedirs(OUT, exist_ok=True)
    base = canvas()
    header_block(base)
    chips(base)
    proof_block(base)
    base.save(f"{OUT}/base.png")
    sticker("NON-ADDICTIVE", GOLD, NAVY).save(f"{OUT}/st1.png")
    sticker("PHARMACIST COMPOUNDED", GOLD, NAVY).save(f"{OUT}/st2.png")
    sticker("3-IN-1 SLEEP FORMULA", RED, CREAM).save(f"{OUT}/st3.png")
    endcard().save(f"{OUT}/end.png")
    # captions: argv[2] = json list of [start, end, text]
    if len(sys.argv) > 2:
        for i, (s, e, t) in enumerate(json.load(open(sys.argv[2]))):
            caption(t).save(f"{OUT}/cap_{sys.argv[3]}_{i}.png")
    print("ok")
