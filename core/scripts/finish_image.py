"""Brand a generated image into a finished static ad (legacy layouts; Batch Mode uses finish_batch.py).

usage: finish_image.py <raw image> <copy.json> <out.png> [--ratio 4:5|1:1|9:16] [--layout NAME]

copy.json must name the product ("product": "<id>"); its product.json supplies the verbatim disclaimer and the
defaults below (article kicker, split titles) and says whether the compare layout is allowed at all.
Every layout adds the fixed brand pieces: Everlife logo, the transparent Trustpilot / Doctor Prescribed /
Ships Free row and the verbatim disclaimer. The middle of the ad depends on --layout:

  standard   headline (+kicker), 3 ingredient or benefit cards, CTA pill
  checklist  headline, ❌/✅ list            copy: "checklist": [["x","Another gummy"],["check","Restora-Z …"]]
  compare    headline, two-column ✓/✗ table copy: "compare_titles": ["Restora-Z","Ambien"],
             "compare_left": [...], "compare_right": [...]          (Ambien: approved claims only + real pill image)
  quote      review card with stars           copy: "quote": "<verbatim Trustpilot review>", "quote_name": "Jane M."
  article    editorial article frame         copy: "kicker", "head", "dek"
  letter     "Dear …" letter panel             copy: "letter": [lines], "signoff": "The Everlife Team"
  split      pain points left → benefits right copy: "split_left": [...], "split_right": [...]
  frame      places a finished ad inside a blank frame in the photo   copy: "frame_box": [x,y,w,h] (raw px),
             "frame_ad": "<path to a finished ad png>"

All words come from copy.json (bible copy only). The generated picture must contain no text.
"""
import argparse, json, os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

T = os.environ.get("EVERLIFE_TOOLS", os.path.expanduser("~/Everlife-Creative/tools"))
AV_COND = "/System/Library/Fonts/Avenir Next Condensed.ttc"
AV = "/System/Library/Fonts/Avenir Next.ttc"
SERIF = "/System/Library/Fonts/Supplemental/Baskerville.ttc"
UNI = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
NAVY, GOLD, CREAM, TEAL = (14, 26, 48), (236, 205, 140), (251, 250, 245), (98, 200, 190)
GREEN, RED, INK = (0, 182, 122), (214, 48, 64), (30, 34, 44)
SIZES = {"1:1": (1080, 1080), "4:5": (1080, 1350), "9:16": (1080, 1920)}


def font(path, size, name="Regular"):
    for i in range(20):
        try:
            f = ImageFont.truetype(path, size, index=i)
        except OSError:
            break
        if " ".join(f.getname()).lower().endswith(name.lower()):
            return f
    return ImageFont.truetype(path, size)


def tw(d, t, f):
    return d.textlength(t, font=f)


def centered(d, W, y, text, f, fill):
    d.text(((W - tw(d, text, f)) / 2, y), text, font=f, fill=fill)


def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if tw(d, t, f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    return lines + ([cur] if cur else [])


def fade(img, y0, y1, a0, a1, color=NAVY):
    W = img.width
    y0, y1 = max(0, y0), min(img.height, y1)
    band = Image.new("RGBA", (W, max(1, y1 - y0)))
    bd = ImageDraw.Draw(band)
    for i in range(y1 - y0):
        a = int(a0 + (a1 - a0) * i / max(1, y1 - y0 - 1))
        bd.line([(0, i), (W, i)], fill=color + (a,))
    img.alpha_composite(band, (0, y0))


def panel(img, box, fill, radius=24, blur=0):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle(box, radius, fill=fill)
    if blur:
        layer = layer.filter(ImageFilter.GaussianBlur(blur))
    img.alpha_composite(layer)


class Ad:
    def __init__(self, raw, C, ratio):
        self.C = C
        self.W, self.H = SIZES[ratio]
        self.k = self.H / 1350
        self.img = ImageOps.fit(Image.open(raw).convert("RGB"), (self.W, self.H), Image.LANCZOS,
                                centering=(0.5, 0.45)).convert("RGBA")

    @property
    def d(self):
        return ImageDraw.Draw(self.img)

    # ---- fixed brand pieces
    def top(self, with_head=True, head_lines=None):
        W, k, C = self.W, self.k, self.C
        fade(self.img, 0, int(340 * k), 215, 0)
        lg = Image.open(f"{T}/assets/logo_cream.png").convert("RGBA")
        lw = 373
        lg = lg.resize((lw, int(lg.height * lw / lg.width)), Image.LANCZOS)
        self.img.alpha_composite(lg, ((W - lw) // 2, int(38 * k)))
        y = int(38 * k) + lg.height + 14
        d = self.d
        if C.get("kicker") and with_head:
            centered(d, W, y, "  ·  ".join(C["kicker"].upper().split()), font(AV, 24, "Demi Bold"), GOLD)
            y += 36
        if with_head:
            hf = font(AV_COND, int(70 * min(1, k + 0.1)), "Heavy Italic")
            for ln in head_lines or C["head"]:
                while tw(d, ln, hf) > W - 80:
                    hf = font(AV_COND, hf.size - 4, "Heavy Italic")
                centered(d, W, y, ln, hf, GOLD)
                y += int(hf.size * 1.02)
        return y

    def bottom(self):
        W, H, C = self.W, self.H, self.C
        d = self.d
        disc_f = font(AV, 19, "Medium")
        dl = wrap(d, C["disclaimer"], disc_f, W - 90)
        row = Image.open(f"{T}/assets/proof_row_clear.png").convert("RGBA")
        rw = W - 90
        row = row.resize((rw, int(row.height * rw / row.width)), Image.LANCZOS)
        top = H - (row.height + 18 + 24 * len(dl) + 26)
        fade(self.img, top - int(300 * self.k), H, 0, 228)
        self.img.alpha_composite(row, ((W - rw) // 2, top))
        d = self.d
        ty = top + row.height + 12
        for ln in dl:
            centered(d, W, ty, ln, disc_f, (236, 236, 232))
            ty += 24
        return top

    def cta(self, y_bottom):
        if not self.C.get("cta"):
            return y_bottom
        d, W = self.d, self.W
        f = font(AV_COND, 40, "Heavy")
        cw = int(tw(d, self.C["cta"], f)) + 90
        cy = y_bottom - 84
        d.rounded_rectangle([(W - cw) / 2, cy, (W + cw) / 2, cy + 64], 32, fill=GOLD)
        centered(d, W, cy + 8, self.C["cta"], f, NAVY)
        return cy

    # ---- middle layouts
    def cards(self, y_bottom):
        C, W = self.C, self.W
        items = C.get("ingredients") or [[b, ""] for b in C.get("benefits", [])]
        if not items:
            return y_bottom
        d = self.d
        nf, cf = font(AV_COND, 28, "Bold"), font(AV, 19, "Medium")
        n, gap = len(items[:3]), 14
        cwd = (W - 60 - gap * (n - 1)) // n
        y0 = y_bottom - 96 - 22
        for i, (name, claim) in enumerate(items[:3]):
            x = 30 + i * (cwd + gap)
            d.rounded_rectangle([x, y0, x + cwd, y0 + 96], 18, fill=CREAM + (240,))
            nl = wrap(d, name, nf, cwd - 16)[:1]
            d.text((x + (cwd - tw(d, nl[0], nf)) / 2, y0 + 10), nl[0], font=nf, fill=NAVY)
            yy = y0 + 50
            for ln in wrap(d, claim, cf, cwd - 20)[:2]:
                d.text((x + (cwd - tw(d, ln, cf)) / 2, yy), ln, font=cf, fill=(70, 78, 92))
                yy += 22
        if C.get("ingredients_label"):
            centered(d, W, y0 - 34, C["ingredients_label"], font(AV_COND, 28, "Heavy Italic"), GOLD)
        return y0 - 40

    def checklist(self, y_top, y_bottom):
        W = self.W
        rows = self.C["checklist"]
        f = font(AV_COND, 46, "Bold")
        sym = font(UNI, 44)
        rh = 74
        y = y_top + 20
        d = self.d
        for kind, text in rows:
            w = int(tw(d, text, f)) + 110
            x = (W - w) // 2
            panel(self.img, [x, y, x + w, y + rh - 10], (255, 255, 255, 242), 16)
            d = self.d
            d.text((x + 18, y + 4), "✕" if kind == "x" else "✓", font=sym, fill=RED if kind == "x" else GREEN)
            d.text((x + 82, y + 6), text, font=f, fill=INK)
            y += rh
        return y

    def compare(self, y_top, y_bottom):
        C, W = self.C, self.W
        tl, tr = C["compare_titles"]
        L, R = C["compare_left"], C["compare_right"]
        n = max(len(L), len(R))
        hf, rf, sym = font(AV_COND, 44, "Heavy"), font(AV, 25, "Demi Bold"), font(UNI, 26)
        colw, gap = (W - 80) // 2, 0
        rowh = 58
        h = 70 + rowh * n + 20
        y0 = max(y_top + 10, (y_top + y_bottom) // 2 - h // 2)
        # compliance: an Ambien comparison must SHOW Ambien's actual pill → "compare_pills": [restora_png, ambien_png]
        pills = C.get("compare_pills")
        if pills:
            ph = 120
            y0 = max(y0, y_top + ph + 20)
            for i, pth in enumerate(pills):
                im = Image.open(pth).convert("RGBA")
                im = im.crop(im.getbbox() or (0, 0, im.width, im.height))
                im.thumbnail((colw - 80, ph), Image.LANCZOS)
                self.img.alpha_composite(im, (40 + i * colw + (colw - im.width) // 2, y0 - ph - 10 + (ph - im.height) // 2))
        panel(self.img, [40, y0, 40 + colw, y0 + h], NAVY + (232,), 22)
        panel(self.img, [40 + colw, y0, 40 + 2 * colw, y0 + h], (60, 64, 74, 215), 22)
        d = self.d
        d.text((40 + (colw - tw(d, tl, hf)) / 2, y0 + 12), tl, font=hf, fill=GOLD)
        d.text((40 + colw + (colw - tw(d, tr, hf)) / 2, y0 + 12), tr, font=hf, fill=(220, 220, 220))
        for i in range(n):
            yy = y0 + 76 + i * rowh
            if i < len(L):
                d.text((60, yy), "✓", font=sym, fill=GREEN)
                for j, ln in enumerate(wrap(d, L[i], rf, colw - 70)[:2]):
                    d.text((96, yy + j * 26 - (6 if len(wrap(d, L[i], rf, colw - 70)) > 1 else 0)), ln, font=rf, fill=CREAM)
            if i < len(R):
                x = 40 + colw + 20
                d.text((x, yy), "•", font=sym, fill=(200, 200, 200))
                for j, ln in enumerate(wrap(d, R[i], rf, colw - 70)[:2]):
                    d.text((x + 34, yy + j * 26 - (6 if len(wrap(d, R[i], rf, colw - 70)) > 1 else 0)), ln, font=rf, fill=(225, 225, 225))
        return y0 + h

    def quote(self, y_top, y_bottom):
        C, W = self.C, self.W
        qf, nf, sf = font(SERIF, 36, "Italic"), font(AV, 24, "Demi Bold"), font(UNI, 34)
        d = self.d
        lines = wrap(d, "“" + C["quote"].strip("“”\" ") + "”", qf, W - 220)
        h = 90 + 46 * len(lines) + 50
        y0 = max(y_top + 20, (y_top + y_bottom) // 2 - h // 2)
        panel(self.img, [70, y0, W - 70, y0 + h], (255, 255, 255, 240), 26)
        d = self.d
        centered(d, W, y0 + 22, "★★★★★", sf, GREEN)
        y = y0 + 78
        for ln in lines:
            centered(d, W, y, ln, qf, INK)
            y += 46
        centered(d, W, y + 6, "— " + C.get("quote_name", "Verified customer") + " · Trustpilot", nf, (90, 96, 108))
        return y0 + h

    def article(self, y_top, y_bottom):
        C, W, H = self.C, self.W, self.H
        d = self.d
        kf, hf, df = font(AV, 24, "Bold"), font(SERIF, 54, "SemiBold"), font(AV, 26, "Regular")
        hl = wrap(d, " ".join(C["head"]), hf, W - 160)
        dl = wrap(d, C.get("dek", ""), df, W - 160)
        h = 60 + 62 * len(hl) + 34 * len(dl) + 40
        y0 = y_top + 10
        panel(self.img, [50, y0, W - 50, y0 + h], (255, 255, 255, 246), 10)
        d = self.d
        d.text((80, y0 + 24), C.get("kicker", self.PR["kicker_default"]).upper(), font=kf, fill=RED)
        y = y0 + 62
        for ln in hl:
            d.text((80, y), ln, font=hf, fill=INK)
            y += 62
        for ln in dl:
            d.text((80, y + 6), ln, font=df, fill=(80, 84, 94))
            y += 34
        return y0 + h

    def letter(self, y_top, y_bottom):
        C, W = self.C, self.W
        d = self.d
        gf, bf, sf = font(SERIF, 40, "Italic"), font(SERIF, 30, "Regular"), font(SERIF, 30, "Italic")
        body = []
        for para in C["letter"]:
            body += wrap(d, para, bf, W - 220) + [""]
        h = 70 + 40 * len(body) + 70
        y0 = y_top + 10
        panel(self.img, [60, y0, W - 60, min(y0 + h, y_bottom - 100)], (248, 242, 228, 245), 18)
        d = self.d
        d.text((100, y0 + 28), C.get("greeting", "Dear Everlife Community,"), font=gf, fill=NAVY)
        y = y0 + 90
        for ln in body:
            if y > y_bottom - 160:
                break
            d.text((100, y), ln, font=bf, fill=INK)
            y += 40
        d.text((100, y), "— " + C.get("signoff", "The Everlife Team"), font=sf, fill=NAVY)
        return y + 50

    def split(self, y_top, y_bottom):
        C, W = self.C, self.W
        L, R = C["split_left"], C["split_right"]
        lf, hf = font(AV, 26, "Demi Bold"), font(AV_COND, 34, "Heavy")
        colw = (W - 100) // 2
        n = max(len(L), len(R))
        h = 64 + 66 * n
        y0 = max(y_top + 10, (y_top + y_bottom) // 2 - h // 2)
        if C.get("split_y") is not None:  # optional: panel top as a fraction of H, to keep the product clear
            y0 = max(y_top + 10, int(C["split_y"] * self.H))
        panel(self.img, [40, y0, 40 + colw, y0 + h], (20, 30, 60, 220), 20)
        panel(self.img, [60 + colw, y0, 60 + 2 * colw, y0 + h], (250, 238, 210, 235), 20)
        d = self.d
        titles = C.get("split_titles", self.PR["split_titles"])
        d.text((60, y0 + 14), titles[0], font=hf, fill=GOLD)
        d.text((80 + colw, y0 + 14), titles[1], font=hf, fill=NAVY)
        for i in range(n):
            yy = y0 + 64 + i * 66
            if i < len(L):
                for j, ln in enumerate(wrap(d, L[i], lf, colw - 40)[:2]):
                    d.text((60, yy + j * 28), ln, font=lf, fill=CREAM)
            if i < len(R):
                for j, ln in enumerate(wrap(d, R[i], lf, colw - 40)[:2]):
                    d.text((80 + colw, yy + j * 28), ln, font=lf, fill=NAVY)
        return y0 + h

    def frame(self, raw_size):
        C = self.C
        x, y, w, h = C["frame_box"]
        sx, sy = self.W / raw_size[0], self.H / raw_size[1]  # approx (fit keeps aspect when ratios match)
        ad = ImageOps.fit(Image.open(C["frame_ad"]).convert("RGBA"), (int(w * sx), int(h * sy)), Image.LANCZOS)
        self.img.alpha_composite(ad, (int(x * sx), int(y * sy)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw"); ap.add_argument("copy"); ap.add_argument("out")
    ap.add_argument("--ratio", default="4:5", choices=SIZES)
    ap.add_argument("--layout", default="standard",
                    choices=["standard", "checklist", "compare", "quote", "article", "letter", "split", "frame"])
    a = ap.parse_args()
    C = json.load(open(a.copy))
    sys.path.insert(0, T)
    import product
    PR = product.for_copy(C, a.copy)
    C["disclaimer"] = PR["disclaimer"]
    if a.layout == "compare" and not PR.get("compare_allowed"):
        raise SystemExit(f"❌ no approved comparison for {PR['name']} (product.json compare_allowed is false)")
    ad = Ad(a.raw, C, a.ratio)
    ad.PR = PR

    if a.layout == "frame":
        ad.frame(Image.open(a.raw).size)
        ad.top(with_head=False)
        ad.bottom()
    elif a.layout == "article":
        y = ad.top(with_head=False)
        bottom = ad.bottom()
        ad.article(y, bottom)
        ad.cta(bottom)
    elif a.layout == "letter":
        y = ad.top(with_head=False)
        bottom = ad.bottom()
        ad.letter(y, bottom - 84)
        ad.cta(bottom)
    else:
        y = ad.top()
        bottom = ad.bottom()
        cy = ad.cta(bottom)
        if a.layout == "standard":
            ad.cards(cy)
        else:
            getattr(ad, a.layout)(y, cy - 20)

    ad.img.convert("RGB").save(a.out, quality=95)
    print("done", a.out)


if __name__ == "__main__":
    main()
