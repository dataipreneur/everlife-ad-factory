"""Alternative overlay looks for full_layout.py (selected by copy.json "style").

Every style keeps the fixed pieces from full_layout: the transparent Trustpilot row + verbatim
disclaimer at the bottom (drawn by full_layout), the Everlife logo, the ingredient end card with
each ingredient's own bible claim, the 100,000+ line and the CTA. Only the look changes.

  tiktok     native in-app look: headline in white sticker boxes, word-by-word highlighted
             captions, light cream end card
  editorial  quiet premium look: thin serif italic headline, lowercase serif subtitles with no
             boxes, dark end card with ingredient columns and an outline CTA
"""
import re
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import safezones as sz

SX0, SY0, SX1, SY1 = sz.SAFE
SAFE_W = sz.SAFE_W

W, H = 1080, 1920
SUP = "/System/Library/Fonts/Supplemental"
HN = "/System/Library/Fonts/HelveticaNeue.ttc"


def _font(bl, path, size, name):
    return bl.font(path, size, name)


def _cased(text, C):
    """Undo .title()/.lower() damage to names that must keep their casing ("GHK", not "Ghk").
    The list is the product's "keep_case" (product.json), set on C by full_layout."""
    for name in C["keep_case"]:
        text = re.sub(re.escape(name), name, text, flags=re.I)
    return text


LOGO916 = 432   # bible v3 §03: logo 40% of the 1080 px width on 9:16
HEAD_DY = 28    # opening headers sit lower to clear the taller logo


def _logo(bl, P, color, width):
    """Everlife logo recoloured (the source PNG is cream; its alpha is the mark)."""
    lg = Image.open(f"{P}/source/logo_cream.png").convert("RGBA")
    a = lg.split()[-1]
    out = Image.new("RGBA", lg.size, color + (0,))
    out.putalpha(a)
    return out.resize((width, int(lg.height * width / lg.width)), Image.LANCZOS)


def _render(P, name, size, by="height"):
    r = Image.open(f"{P}/source/{name}").convert("RGBA")
    r = r.crop(r.getbbox())
    if by == "height":
        return r.resize((int(r.width * size / r.height), size), Image.LANCZOS)
    return r.resize((size, int(r.height * size / r.width)), Image.LANCZOS)


def _word_times(cap):
    """[(word, start, end)] for a caption; falls back to even spacing if the text was edited."""
    s, e, text = cap[0], cap[1], cap[2]
    words = text.split()
    wt = cap[3] if len(cap) > 3 else []
    if len(wt) != len(words):
        step = (e - s) / max(1, len(words))
        wt = [[s + i * step, s + (i + 1) * step] for i in range(len(words))]
    out = []
    for i, w in enumerate(words):
        ws = max(s, wt[i][0])
        we = wt[i + 1][0] if i + 1 < len(words) else e
        out.append((w, round(ws, 2), round(max(we, ws + 0.05), 2)))
    return out


class TikTok:
    INK = (17, 17, 17)
    HL = (255, 214, 10)  # active-word highlight
    CREAM = (250, 246, 238)
    NAVY = (14, 26, 48)

    def __init__(self, bl, C, P, end_t):
        self.bl, self.C, self.P, self.end_t = bl, C, P, end_t
        self.head = _font(bl, HN, 56, "Bold")
        self.cap_y = 1000      # set by full_layout (just above the proof block)
        self.block_top = 1030  # set by full_layout
        self.issues = []
        self.cap = _font(bl, HN, 54, "Bold")
        self.small = _font(bl, HN, 30, "Medium")

    def _sticker_lines(self, img, lines, y, font, fill, ink, pad=(26, 14), gap=8, radius=16):
        d = ImageDraw.Draw(img)
        for ln in lines:
            w = d.textlength(ln, font=font)
            asc, desc = font.getmetrics()
            h = asc + desc
            x0 = (W - w) / 2 - pad[0]
            d.rounded_rectangle([x0, y, x0 + w + 2 * pad[0], y + h + 2 * pad[1]], radius, fill=fill)
            d.text(((W - w) / 2, y + pad[1]), ln, font=font, fill=ink)
            y += h + 2 * pad[1] + gap
        return y

    def top(self):
        img = self.bl.canvas()
        img.alpha_composite(_logo(self.bl, self.P, (255, 255, 255), LOGO916), ((W - LOGO916) // 2, SY0 + 8))
        heads = [_cased(h.title(), self.C) for h in self.C["head"]]
        d0 = ImageDraw.Draw(img)
        f = self.head
        while max(d0.textlength(h, font=f) for h in heads) + 52 > SAFE_W and f.size > 30:
            f = _font(self.bl, HN, f.size - 2, "Bold")
        self._sticker_lines(img, heads, 212 + HEAD_DY, f, (255, 255, 255, 250), self.INK)
        return img

    def caption_layers(self, caps, L, tag):
        """One layer per spoken word: the whole line in white boxes, the current word highlighted."""
        layers = []
        y = self.cap_y
        for ci, cap in enumerate(caps):
            words = _word_times(cap)
            for wi, (w, ws, we) in enumerate(words):
                img = self.bl.canvas()
                d = ImageDraw.Draw(img)
                texts = [x[0] for x in words]
                widths = [d.textlength(t, font=self.cap) for t in texts]
                space = 16
                total = sum(widths) + space * (len(texts) - 1) + 44
                if total > SAFE_W:  # fall back to the active word alone for long lines (keeps inside the safe area)
                    texts, widths = [w], [d.textlength(w, font=self.cap)]
                    active = 0
                    total = widths[0] + 44
                else:
                    active = wi
                x = (W - total) / 2
                d.rounded_rectangle([x, y, x + total, y + 84], 18, fill=(255, 255, 255, 245))
                x += 22
                for k, (t, tw) in enumerate(zip(texts, widths)):
                    if k == active:
                        d.rounded_rectangle([x - 8, y + 10, x + tw + 8, y + 74], 12, fill=self.HL)
                    d.text((x, y + 14), t, font=self.cap, fill=self.INK)
                    x += tw + space
                name = f"cap_{tag}_{ci}_{wi}.png"
                img.save(f"{L}/{name}")
                layers.append((name, ws, min(we, cap[1])))
        return layers

    def end_layers(self, L):
        bl, C, P = self.bl, self.C, self.P
        base = Image.new("RGBA", (W, H), self.CREAM + (255,))
        glow = bl.canvas()
        ImageDraw.Draw(glow).ellipse([160, 330, 920, 820], fill=(255, 225, 190, 200))
        base.alpha_composite(glow.filter(ImageFilter.GaussianBlur(120)))
        # bottom fade so the transparent proof row stays legible on a light card
        bl.gradient_band(base, self.block_top - 380, H, 0, 255)
        d = ImageDraw.Draw(base)
        base.alpha_composite(_logo(bl, P, self.NAVY, LOGO916), ((W - LOGO916) // 2, SY0 + 8))
        tf = _font(bl, HN, 60, "Bold")
        heads = [_cased(ln.title(), C) for ln in C["end_head"]]
        while max(d.textlength(ln, font=tf) for ln in heads) > SAFE_W and tf.size > 30:
            tf = _font(bl, HN, tf.size - 2, "Bold")
        for i, ln in enumerate(heads):
            bl.centered(d, 205 + 68 * i, ln, tf, self.NAVY)
        b = _render(P, C["bottle"], 300)
        base.alpha_composite(b, (W // 2 + 100 - b.width // 2, 345))
        c = _render(P, C["pill"], round(300 * C.get("pill_scale", 1)), by="width")
        cy = min(560, 652 - c.height // 2)  # a tall pill render (e.g. a wide tablet) would cover the label at 668
        base.alpha_composite(c, (W // 2 - 130 - c.width // 2, cy - c.height // 2))
        lab = _font(bl, HN, 32, "Bold")
        bl.centered(d, 668, _cased(C["ingredients_label"].title().replace("3-In-1", "3-in-1"), C), lab, self.NAVY)
        layers = [("end.png", self.end_t, 99)]
        base.save(f"{L}/end.png")
        nf, cf = _font(bl, HN, 36, "Bold"), _font(bl, HN, 30, "Medium")
        # "end_rows": "benefits" lists the approved benefits instead of name + claim rows (for long ingredient claims)
        rows = [("", b) for b in C["benefits"]] if C.get("end_rows") == "benefits" else C["ingredients"]
        for i, (name, claim) in enumerate(rows):
            img = bl.canvas()
            dd = ImageDraw.Draw(img)
            y = 716 + i * 64
            dd.rounded_rectangle([SX0 + 4, y, SX1 - 4, y + 56], 28, fill=(255, 255, 255, 255))
            dd.ellipse([SX0 + 22, y + 16, SX0 + 46, y + 40], fill=(0, 182, 122))
            dd.text((SX0 + 28, y + 12), "✓", font=_font(bl, f"{SUP}/Arial Unicode.ttf", 22, "Regular"), fill="white")
            if name:
                dd.text((SX0 + 62, y + 9), _cased(name.title(), C), font=nf, fill=self.NAVY)
                cf2 = cf
                while dd.textlength(claim, font=cf2) > SAFE_W - 300 and cf2.size > 20:
                    cf2 = _font(bl, HN, cf2.size - 1, "Medium")
                tw = dd.textlength(claim, font=cf2)
                dd.text((SX1 - 22 - tw, y + 13), claim, font=cf2, fill=(90, 96, 108))
            else:
                bf = _font(bl, HN, 32, "Bold")
                while dd.textlength(claim, font=bf) > SAFE_W - 90 and bf.size > 24:
                    bf = _font(bl, HN, bf.size - 1, "Bold")
                dd.text((SX0 + 62, y + 11), claim, font=bf, fill=self.NAVY)
            img.save(f"{L}/end_ing{i}.png")
            layers.append((f"end_ing{i}.png", round(self.end_t + 0.25 + 0.3 * i, 2), 99))
        foot = bl.canvas()
        fd = ImageDraw.Draw(foot)
        bl.centered(fd, 916, "Over 100,000 happy customers", self.small, self.NAVY)
        fd.rounded_rectangle([(W - 560) / 2, 956, (W + 560) / 2, 1022], 33, fill=self.NAVY)
        bl.centered(fd, 965, _cased(C["cta"].title(), C), _font(bl, HN, 40, "Bold"), (255, 255, 255))
        if 1022 > self.block_top - 6:
            self.issues.append(f"tiktok end-card CTA collides with proof block ({self.block_top})")
        foot.save(f"{L}/end_foot.png")
        layers.append(("end_foot.png", self.end_t, 99))
        return layers


class Editorial:
    IVORY = (246, 241, 230)
    GOLD = (214, 186, 132)
    INK = (12, 16, 28)

    def __init__(self, bl, C, P, end_t):
        self.bl, self.C, self.P, self.end_t = bl, C, P, end_t
        self.serif_i = _font(bl, f"{SUP}/Baskerville.ttc", 64, "Italic")
        self.serif = _font(bl, f"{SUP}/Baskerville.ttc", 46, "Regular")
        self.label = _font(bl, HN, 22, "Medium")
        self.cap_y = 1000
        self.block_top = 1030
        self.issues = []

    def top(self):
        bl = self.bl
        img = bl.canvas()
        bl.gradient_band(img, 0, 520, 150, 0)
        img.alpha_composite(_logo(bl, self.P, self.IVORY, LOGO916), ((W - LOGO916) // 2, SY0 + 10))
        d = ImageDraw.Draw(img)
        kicker = self.C.get("kicker", "")
        if kicker:
            bl.centered(d, 214 + HEAD_DY, "  ·  ".join(kicker.upper().split()), self.label, self.GOLD)
        y = 252 + HEAD_DY
        for i, ln in enumerate(self.C["head"]):
            t = _cased(ln.capitalize() if i == 0 else ln.lower(), self.C)
            fi = self.serif_i
            while d.textlength(t, font=fi) > SAFE_W and fi.size > 30:
                fi = _font(bl, f"{SUP}/Baskerville.ttc", fi.size - 2, "Italic")
            bl.centered(d, y, t, fi, self.IVORY)
            y += 72
        d.line([(W / 2 - 40, y + 14), (W / 2 + 40, y + 14)], fill=self.GOLD, width=2)
        return img

    def caption_layers(self, caps, L, tag):
        bl = self.bl
        layers = []
        for i, cap in enumerate(caps):
            img = bl.canvas()
            d = ImageDraw.Draw(img)
            text = _cased(cap[2].lower(), self.C)
            if len(text) > 30:  # long lines drop a size so they stay on one line
                f = _font(bl, f"{SUP}/Baskerville.ttc", 40, "Regular")
            else:
                f = self.serif
            w = d.textlength(text, font=f)
            # soft dark band so the serif reads on bright footage (no shadow on the type itself)
            band = bl.canvas()
            w = d.textlength(text, font=f) if d.textlength(text, font=f) < w else w
            ImageDraw.Draw(band).rounded_rectangle([(W - w) / 2 - 34, self.cap_y, (W + w) / 2 + 34, self.cap_y + 86], 43,
                                                   fill=self.INK + (175,))
            img.alpha_composite(band.filter(ImageFilter.GaussianBlur(6)))
            d = ImageDraw.Draw(img)
            while d.textlength(text, font=f) > SAFE_W - 68 and f.size > 26:
                f = _font(bl, f"{SUP}/Baskerville.ttc", f.size - 2, "Regular")
            bl.centered(d, self.cap_y + 16, text, f, self.IVORY)
            name = f"cap_{tag}_{i}.png"
            img.save(f"{L}/{name}")
            layers.append((name, cap[0], cap[1]))
        return layers

    def end_layers(self, L):
        bl, C, P = self.bl, self.C, self.P
        base = Image.new("RGBA", (W, H), self.INK + (250,))
        glow = bl.canvas()
        ImageDraw.Draw(glow).ellipse([200, 360, 880, 800], fill=(196, 160, 98, 70))
        base.alpha_composite(glow.filter(ImageFilter.GaussianBlur(130)))
        d = ImageDraw.Draw(base)
        base.alpha_composite(_logo(bl, P, self.IVORY, LOGO916), ((W - LOGO916) // 2, SY0 + 8))
        hf = _font(bl, f"{SUP}/Baskerville.ttc", 60, "Italic")
        for i, ln in enumerate(C["end_head"]):
            t = ln.title() if "+" in ln else (ln.capitalize() if i == 0 else ln.lower())  # keep drug names capitalised
            t = _cased(t, C)
            f = hf
            while d.textlength(t, font=f) > SAFE_W and f.size > 30:
                f = _font(bl, f"{SUP}/Baskerville.ttc", f.size - 2, "Italic")
            bl.centered(d, 214 + 72 * i, t, f, self.IVORY)
        b = _render(P, C["bottle"], 290)
        base.alpha_composite(b, (W // 2 + 100 - b.width // 2, 360))
        c = _render(P, C["pill"], round(290 * C.get("pill_scale", 1)), by="width")
        base.alpha_composite(c, (W // 2 - 125 - c.width // 2, 570 - c.height // 2))
        bl.centered(d, 680, "   ".join(C["ingredients_label"].upper()), self.label, self.GOLD)
        base.save(f"{L}/end.png")
        layers = [("end.png", self.end_t, 99)]
        nf = _font(bl, f"{SUP}/Baskerville.ttc", 38, "SemiBold")
        cf = _font(bl, f"{SUP}/Baskerville.ttc", 31, "Italic")
        colw = SAFE_W // 3
        x0 = SX0
        for i, (name, claim) in enumerate(C["ingredients"]):
            img = bl.canvas()
            dd = ImageDraw.Draw(img)
            x = x0 + i * colw
            if i:
                dd.line([(x, 722), (x, 852)], fill=self.GOLD + (180,), width=1)
            nm = _cased(name.title(), C)
            nf2 = nf
            while dd.textlength(nm, font=nf2) > colw - 16 and nf2.size > 22:
                nf2 = _font(bl, f"{SUP}/Baskerville.ttc", nf2.size - 2, "SemiBold")
            dd.text((x + (colw - dd.textlength(nm, font=nf2)) / 2, 728), nm, font=nf2, fill=self.IVORY)
            ty = 782
            for ln in bl.wrap(dd, _cased(claim.lower(), C), cf, colw - 30)[:2]:
                dd.text((x + (colw - dd.textlength(ln, font=cf)) / 2, ty), ln, font=cf, fill=(250, 238, 212))
                ty += 36
            img.save(f"{L}/end_ing{i}.png")
            layers.append((f"end_ing{i}.png", round(self.end_t + 0.3 + 0.35 * i, 2), 99))
        foot = bl.canvas()
        fd = ImageDraw.Draw(foot)
        bl.centered(fd, 880, "Over 100,000 happy customers", _font(bl, HN, 26, "Regular"), self.IVORY)
        fd.rounded_rectangle([(W - 540) / 2, 926, (W + 540) / 2, 998], 36, outline=self.GOLD, width=3)
        cta = _cased(C["cta"].title(), C)
        bl.centered(fd, 942, cta, _font(bl, f"{SUP}/Baskerville.ttc", 38, "SemiBold"), self.IVORY)
        if 998 > self.block_top - 6:
            self.issues.append(f"editorial end-card CTA collides with proof block ({self.block_top})")
        foot.save(f"{L}/end_foot.png")
        layers.append(("end_foot.png", self.end_t, 99))
        return layers


def make(style, bl, C, P, end_t):
    return {"tiktok": TikTok, "editorial": Editorial}[style](bl, C, P, end_t)
