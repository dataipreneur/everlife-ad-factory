"""Modern-brand finishing for static ads (photo + overlaid type). Needs the product's "product_zones" in its
product.json to keep type off the product; products without it are refused (use finish_batch.py).

Design rules (from the team's Pinterest references): one short sentence-case line, an elegant serif with ONE
italic accent, lots of air, a single colour mood, the brand quiet and small. Proof = the team's APPROVED footer
panel (Trustpilot 4.9 badge, Doctor Prescribed, Ships Free From Pharmacy; art cut from their screenshots by
make_footer_assets.py, never drawn or generated) anchored at the bottom, with the verbatim disclaimer.
Legibility for 50+: no type under 24 px (at 1080 wide); headline ≥ 72 px; subline ≥ 36 px.
The photo is laid out automatically: scaled/positioned so the product sits between the headline and the panel
(top filled by softly extending the photo's own plain background). A 1:1 raw works for every ratio. No boxes
behind headlines, no shadows or outlines on type, no all-caps condensed headlines.

usage: finish_modern.py <raw image> <copy.json> <out.png> [--ratio 4:5|1:1|9:16] [--template NAME] [--tone auto|dark|light]

templates
  hero     centred headline at the top (serif, accent in italic), optional subline, quiet footer
  strip    left-aligned headline (editorial) + approved footer panel; "strip_line" becomes the subline
  notify   headline + a frosted iOS-style notification card            copy: "notify": {"title": "...", "body": "..."} (app = product.json notify_app)
  toggle   headline + two iOS toggle rows (off → on)                  copy: "toggles": [["3:00 am", "Wide awake", false], ["7:00 am", "Rested", true]]
  chips    headline + 3 thin frosted chips with line icons            copy: "chips": ["Trazodone · aids in falling asleep", ...]

copy keys: "m_head": "Non-addictive.|*No grogginess.*"  ("|" = line break, *…* = italic accent)
           "product": "<id>" (required), "m_sub": "optional one short line", "cta": optional (strip shows it small)
All words come from copy.json (bible copy only); the disclaimer comes from product.json (verbatim).
"""
import argparse, json, math, os, re
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat

T = os.environ.get("EVERLIFE_TOOLS", os.path.expanduser("~/Everlife-Creative/tools"))
FD = f"{T}/assets/fonts"
SIZES = {"1:1": (1080, 1080), "4:5": (1080, 1350), "9:16": (1080, 1920)}
CREAM, NAVY, GREEN = (250, 247, 240), (16, 24, 44), (0, 182, 122)
ACCENT_DARK, ACCENT_LIGHT = (201, 186, 255), (88, 78, 190)   # lavender on dark, deep violet on light
PANEL = {"dark": (15, 24, 17), "light": (251, 251, 246)}      # the approved footer panels' own background colours
RULE = {"dark": (52, 62, 55), "light": (222, 222, 214)}
DISC = {"dark": (196, 202, 196), "light": (92, 96, 100)}
FOOT = f"{T}/assets/footer"
MIN_TYPE = 24          # px at 1080 wide; nothing smaller anywhere (buyers are 50+)
DISC_LH = 31


def serif(size, italic=False):
    return ImageFont.truetype(f"{FD}/InstrumentSerif-{'Italic' if italic else 'Regular'}.ttf", size)


def sans(size, weight="Regular"):
    f = ImageFont.truetype(f"{FD}/Inter.ttf", size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def parse_line(line):
    """'Non-addictive. *No grogginess.*' -> [(text, italic), ...]"""
    parts = re.split(r"(\*[^*]+\*)", line)
    return [(p.strip("*"), p.startswith("*")) for p in parts if p]


def line_width(d, runs, size):
    return sum(d.textlength(t, font=serif(size, it)) for t, it in runs)


def luminance(img, box):
    crop = img.crop(box).convert("L")
    return ImageStat.Stat(crop).mean[0]


def soft_scrim(img, y0, y1, dark, strength):
    """A soft, gradient wash (not a box) so type reads on busy photos."""
    W = img.width
    col = (10, 14, 28) if dark else (255, 252, 246)
    band = Image.new("RGBA", (W, max(1, y1 - y0)))
    bd = ImageDraw.Draw(band)
    h = y1 - y0
    for i in range(h):
        a = int(strength * math.sin(math.pi * i / max(1, h - 1)) ** 0.8)
        bd.line([(0, i), (W, i)], fill=col + (a,))
    img.alpha_composite(band, (0, max(0, y0)))


import sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import safezones as sz  # noqa: E402
import product  # noqa: E402


def busy_map(img):
    """Edge-energy map: high where the product / props / faces are. Used to keep type off them."""
    g = img.convert("L").filter(ImageFilter.GaussianBlur(1.5)).filter(ImageFilter.FIND_EDGES)
    a = np.asarray(g, dtype=np.float32)
    return a


def box_cost(em, x0, y0, x1, y1):
    x0, y0, x1, y1 = [int(max(0, v)) for v in (x0, y0, x1, y1)]
    sub = em[y0:y1, x0:x1]
    return float(sub.mean()) if sub.size else 999.0


def _span(idx, gap=12):
    best, cur = (idx[0], idx[0]), [idx[0], idx[0]]
    for i in idx[1:]:
        if i - cur[1] <= gap:
            cur[1] = i
        else:
            if cur[1] - cur[0] > best[1] - best[0]:
                best = tuple(cur)
            cur = [i, i]
    return tuple(cur) if cur[1] - cur[0] > best[1] - best[0] else best


def _box(mask, frac=0.012):
    rows = np.where(mask.sum(1) > max(6, mask.shape[1] * frac))[0]
    cols = np.where(mask.sum(0) > max(6, mask.shape[0] * frac))[0]
    if len(rows) < 15 or len(cols) < 15:
        return None
    r0, r1 = _span(rows); c0, c1 = _span(cols)
    return [int(c0), int(r0), int(c1), int(r1)]


def _colour_box(h, s_, v, spec):
    return _box((h > spec["hue"][0]) & (h < spec["hue"][1]) & (s_ > spec["sat_min"]) & (v > spec["val_min"]),
                frac=spec.get("frac", 0.012))


def product_zones(img, Z, pad=40):
    """Untouchable zones: the bottle (extended up over its cap/shoulder) and the pill, found separately by colour
    so type can sit beside them. Z = product.json "product_zones" (e.g. Restora-Z: teal label, fully saturated
    capsule, whose satin highlights sit ~0.67 saturation, hence its 0.85 floor)."""
    hsv = np.asarray(img.convert("RGB").convert("HSV"), dtype=np.float32)
    h, s_, v = hsv[..., 0] * 360 / 255, hsv[..., 1] / 255, hsv[..., 2] / 255
    zones = []
    b = _colour_box(h, s_, v, Z["bottle"])
    if b:
        bh = b[3] - b[1]
        b[1] = int(b[1] - Z["bottle"].get("extend_up", 0) * bh)
        zones.append(b)
    c = _colour_box(h, s_, v, Z["pill"])
    if c and (not b or not (b[0] <= c[0] and c[2] <= b[2] and b[1] <= c[1] and c[3] <= b[3])):
        zones.append(c)
    return [(z[0] - pad, z[1] - pad, z[2] + pad, z[3] + pad) for z in zones]


def product_box(img, Z, pad=40):
    z = product_zones(img, Z, pad)
    if not z:
        return None
    return (min(a[0] for a in z), min(a[1] for a in z), max(a[2] for a in z), max(a[3] for a in z))


def overlaps(a, b):
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


class Collision(Exception):
    pass


class Modern:
    def __init__(self, raw, C, ratio, tone, PR):
        self.C, self.PR, self.Z = C, PR, PR["product_zones"]
        self.W, self.H = SIZES[ratio]
        src = Image.open(raw).convert("RGB")
        if tone == "auto":
            tone = "dark" if luminance(src, (0, 0, src.width, int(src.height * 0.35))) < 140 else "light"
        self.tone = tone
        self.dark = tone == "dark"
        if self.dark:   # card/panel = a deep shade of the photo's own palette, so it belongs to the image
            m = np.asarray(src.resize((64, 64))).reshape(-1, 3).astype(np.float64)
            lum = 0.299 * m[:, 0] + 0.587 * m[:, 1] + 0.114 * m[:, 2]
            base = m[lum <= np.percentile(lum, 40)].mean(0)
            k = 22.0 / max(1.0, float(0.299 * base[0] + 0.587 * base[1] + 0.114 * base[2]))
            self.panel = tuple(int(min(255, max(0, c * k))) for c in base)
        else:
            self.panel = PANEL["light"]
        self.ink = CREAM if self.dark else NAVY
        self.accent = ACCENT_DARK if self.dark else ACCENT_LIGHT
        self.muted = (225, 222, 235) if self.dark else (70, 74, 90)
        self.warnings = []
        self.safe = sz.safe_box(self.W, self.H)          # x0, y0, x1, y1 where copy may live
        self.story = (self.W, self.H) == (sz.W, sz.H)
        self.bottom = sz.FOOTER_BOTTOM if self.story else (self.H - 40)   # footer content ends here
        self.sw = self.safe[2] - self.safe[0] if self.story else self.W - 120   # headline width
        self.card = self.story and not sz.BOTTOM_MODE   # 9:16 safe mode: rounded card; otherwise full-width bottom panel
        self.fw = self.sw - 44 if self.card else self.sw                        # footer content width
        self.foot_mode = "row" if ratio == "1:1" else "stack"
        self.footer_top = self.bottom - self.footer_height()   # solid panel starts here
        self.head_y = max(int(self.H * 0.085), self.safe[1] + 70)
        self.head_end = self.headline_end(self.head_y)
        self.img = self.place_photo(src)
        self.em = busy_map(self.img)            # computed on the clean photo, before any type
        self.free_floor = int(self.H * 0.22)
        top = self.em[: int(self.H * 0.25)]
        self.calm = float(np.percentile(top, 60)) + 6.0
        self.zones = product_zones(self.img, self.Z)     # untouchable zones (bottle + cap, pill; with margin)
        self.zones_tight = product_zones(self.img, self.Z, pad=0)
        self.prod = product_box(self.img, self.Z)

    # ---------------- layout: footer size, headline size, photo placement
    def art(self, name, scale):
        im = Image.open(f"{FOOT}/{name}_{self.tone}.png").convert("RGBA")
        return im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.LANCZOS)

    def art_scale(self):
        if self.foot_mode == "stack":   # badge on its own row, then Doctor | Ships
            return min(0.86, (self.fw - 60) / 892)
        return min(0.86, (self.fw - 100) / 1250)  # one row: badge | doctor | ships

    def disc_lines(self):
        d0 = ImageDraw.Draw(Image.new("RGB", (4, 4)))
        f = sans(MIN_TYPE)
        lines, cur = [], ""
        for w_ in self.C["disclaimer"].split():
            t_ = (cur + " " + w_).strip()
            if d0.textlength(t_, font=f) <= self.fw:
                cur = t_
            else:
                lines.append(cur); cur = w_
        return lines + [cur]

    def footer_height(self):
        s = self.art_scale()
        bh, ih = self.art("badge", s).height, self.art("doctor", s).height
        n = len(self.disc_lines())
        if self.foot_mode == "stack":
            h = 26 + bh + 25 + ih + 29 + n * DISC_LH
        else:
            h = 26 + max(bh, ih) + 33 + n * DISC_LH
        return h + (22 if self.card else 0)

    def head_size(self):
        d = ImageDraw.Draw(Image.new("RGB", (4, 4)))
        lines = [parse_line(l) for l in self.C["m_head"].split("|")]
        maxw = self.sw - 8
        size = max(72, int(self.C["m_size"])) if self.C.get("m_size") else (96 if self.story else int(self.W * 0.105))
        while max(line_width(d, r, size) for r in lines) > maxw and size > 64:
            size -= 4
        return size, lines

    def sub_text(self):
        return self.C.get("m_sub") or self.C.get("strip_line")

    def sub_size(self, size):
        d = ImageDraw.Draw(Image.new("RGB", (4, 4)))
        ss = max(36, int(size * 0.36))
        while self.sub_text() and d.textlength(self.sub_text(), font=sans(ss)) > self.sw - 8 and ss > 30:
            ss -= 2
        return ss

    def headline_end(self, y):
        size, lines = self.head_size()
        h = int(size * 1.02) * len(lines)
        if self.sub_text():
            h += int(size * 0.22) + self.sub_size(size) + 20
        return y + h

    def place_photo(self, src):
        """Scale + position the raw so the product sits centred between the headline and the footer panel."""
        W, H = self.W, self.H
        zs = product_zones(src, self.Z, pad=0)
        if zs:
            px0, py0 = min(z[0] for z in zs), min(z[1] for z in zs)
            px1, py1 = max(z[2] for z in zs), max(z[3] for z in zs)
        else:
            px0, py0, px1, py1 = src.width * 0.3, src.height * 0.35, src.width * 0.7, src.height * 0.75
        b0, b1 = self.head_end + 28, self.footer_top - (28 if self.card else 60)
        bh = b1 - b0
        hp = max(1, py1 - py0)
        s_min = max(W / src.width, H / src.height) if self.card else W / src.width   # 9:16 photo covers the frame
        s0 = max(s_min, min(s_min * 1.5, 0.8 * bh / hp)) if hp * s_min < 0.55 * bh else s_min
        best = None
        for k in range(13):   # zoom in a little at a time until the product can sit inside its band
            s = s0 * (1 + 0.05 * k)
            nw, nh = int(src.width * s), int(src.height * s)
            dy = int((b0 + b1) / 2 - (py0 + py1) / 2 * s)
            if self.card:
                dy = max(H - nh, min(0, dy))
            top_, bot_ = py0 * s + dy, py1 * s + dy
            best = (s, nw, nh, dy)
            if top_ >= b0 - 4 and bot_ <= b1 + 4 and hp * s <= bh + 4:
                break
            if hp * s > bh:
                break
        s, nw, nh, dy = best
        if hp * s > bh + 4:
            self.warnings.append(f"product is {int(hp * s)} px tall but this format only has {bh} px between "
                                 f"headline and footer; make it smaller with a Creatify zoom-out edit (product ≈ 17% of a 9:16 frame / 25% of a 1:1)")
        ph = src.resize((nw, nh), Image.LANCZOS)
        dx = int(min(0, max(W - nw, W / 2 - (px0 + px1) / 2 * s)))
        canvas = Image.new("RGB", (W, H), self.panel)
        if dy > 0:   # extend the photo's own plain top upward (soft); never invent content
            strip = ph.crop((0, 0, nw, max(8, nh // 40))).resize((nw, dy + 80)).filter(ImageFilter.GaussianBlur(28))
            canvas.paste(strip, (dx, 0))
        if dy + nh < H and not self.card:
            strip = ph.crop((0, nh - max(8, nh // 40), nw, nh)).resize((nw, H - dy - nh + 80)).filter(ImageFilter.GaussianBlur(28))
            canvas.paste(strip, (dx, dy + nh - 80))
        mask = Image.new("L", (nw, nh), 255)
        md = ImageDraw.Draw(mask)
        for i in range(70):
            if dy > 0:
                md.line([(0, i), (nw, i)], fill=int(255 * i / 70))
            if dy + nh < H:
                md.line([(0, nh - 1 - i), (nw, nh - 1 - i)], fill=int(255 * i / 70))
        canvas.paste(ph, (dx, dy), mask)
        return canvas.convert("RGBA")

    def find_spot(self, w, h, y_min, y_max, xs):
        """Best (x, y) for a w×h box between y_min..y_max at candidate x positions, avoiding busy areas
        and staying inside the safe area."""
        x_lo, x_hi = self.safe[0], self.safe[2] - w
        xs = sorted({min(max(x, x_lo), max(x_lo, x_hi)) for x in xs})
        y_max = min(y_max, self.footer_top - 16)
        best = None
        for x in xs:
            for y in range(int(y_min), int(max(y_min, y_max - h)) + 1, 8):
                c = box_cost(self.em, x - 28, y - 28, x + w + 28, y + h + 28)
                if any(overlaps((x, y, x + w, y + h), z) for z in self.zones):
                    c += 1000.0  # never on the product
                if best is None or c < best[0]:
                    best = (c, x, y)
        return best

    @property
    def d(self):
        return ImageDraw.Draw(self.img)

    def logo(self, width, x, y, color=None):
        lg = Image.open(f"{T}/assets/logo_cream.png").convert("RGBA")
        lg = lg.resize((width, int(lg.height * width / lg.width)), Image.LANCZOS)
        if color:
            a = lg.split()[-1]
            lg = Image.new("RGBA", lg.size, color + (0,)); lg.putalpha(a)
        self.img.alpha_composite(lg, (int(x), int(y)))
        return lg.height

    def headline(self, y, size=None, align="center", x0=70, maxw=None):
        W = self.W
        x0 = max(x0, self.safe[0])
        y = max(y, self.safe[1] + 70)
        size, lines = self.head_size()
        d = self.d
        prod_top = min([z[1] for z in self.zones_tight], default=10 ** 6)
        if self.headline_end(y) + 12 > prod_top:
            self.warnings.append("headline would touch the product; regenerate with more empty space at the top")
        lh = int(size * 1.02)
        for runs in lines:
            lw = line_width(d, runs, size)
            x = (W - lw) / 2 if align == "center" else x0
            for t, it in runs:
                f = serif(size, it)
                d.text((x, y), t, font=f, fill=self.accent if it else self.ink)
                x += d.textlength(t, font=f)
            y += lh
        sub = self.sub_text()
        if sub:
            sf = sans(self.sub_size(size), "Regular")
            y += int(size * 0.22)
            x = (W - d.textlength(sub, font=sf)) / 2 if align == "center" else x0
            d.text((x, y), sub, font=sf, fill=self.muted)
            y += sf.size + 20
        return y

    def disclaimer(self, y):
        """Verbatim disclaimer, centred, MIN_TYPE px. Returns the y below it."""
        d, f = self.d, sans(MIN_TYPE)
        for ln in self.disc_lines():
            d.text(((self.W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=DISC[self.tone])
            y += DISC_LH
        return y

    def footer(self):
        """The APPROVED footer panel, anchored at the bottom: Trustpilot 4.9 badge, Doctor Prescribed,
        Ships Free From Pharmacy (exact art), rules, verbatim disclaimer. Content stays inside the safe area."""
        W, H, top = self.W, self.H, self.footer_top
        if any(z[3] > top - (12 if self.card else 30) for z in self.zones_tight):
            self.warnings.append("the product reaches into the footer; regenerate with the product smaller/higher")
        if self.card:   # rounded card, same shape as the approved footer screenshots
            cx0, cx1 = self.safe[0], self.safe[2]
            sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(sh).rounded_rectangle([cx0, top + 6, cx1, self.bottom + 6], 30, fill=(0, 0, 0, 90))
            self.img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
            cd = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(cd).rounded_rectangle([cx0, top, cx1, self.bottom], 30, fill=self.panel + (240,))
            self.img.alpha_composite(cd)
        else:
            fade = 130
            band = Image.new("RGBA", (W, H - top + fade))
            bd = ImageDraw.Draw(band)
            for i in range(band.height):
                bd.line([(0, i), (W, i)], fill=self.panel + (min(255, int(255 * (i / fade) ** 1.3)),))
            self.img.alpha_composite(band, (0, top - fade))
        d = self.d
        s = self.art_scale()
        badge, doc, ship = self.art("badge", s), self.art("doctor", s), self.art("ships", s)
        x0, x1 = (W - self.fw) // 2, (W + self.fw) // 2
        y = top + 26
        if self.foot_mode == "stack":
            self.img.alpha_composite(badge, ((W - badge.width) // 2, y))
            y += badge.height + 12
            d.line([(x0, y), (x1, y)], fill=RULE[self.tone], width=1); y += 13
            gap = 30
            tw = doc.width + 2 * gap + 1 + ship.width
            xa = (W - tw) // 2
            self.img.alpha_composite(doc, (xa, y))
            xd = xa + doc.width + gap
            d.line([(xd, y + 10), (xd, y + doc.height - 10)], fill=RULE[self.tone], width=1)
            self.img.alpha_composite(ship, (xd + gap + 1, y))
            y += max(doc.height, ship.height) + 12
        else:
            gap = 24
            parts = [badge, doc, ship]
            tw = sum(p.width for p in parts) + 4 * gap + 2
            x = (W - tw) // 2
            rh = max(p.height for p in parts)
            for i, p in enumerate(parts):
                self.img.alpha_composite(p, (x, y + (rh - p.height) // 2))
                x += p.width + gap
                if i < 2:
                    d.line([(x, y + 10), (x, y + rh - 10)], fill=RULE[self.tone], width=1)
                    x += 1 + gap
            y += rh + 16
        d.line([(x0, y), (x1, y)], fill=RULE[self.tone], width=1); y += 17
        end = self.disclaimer(y)
        if self.story:
            self.issues_check([(x0, top + 30, x1, end)])
        return top

    def issues_check(self, boxes):
        for b in boxes:
            for v in sz.violations(b, self.W, self.H, "footer"):
                self.warnings.append(v)

    def mark(self):
        """Everlife mark at the top centre."""
        return self.logo(190, (self.W - 190) / 2, max(int(self.H * 0.035), self.safe[1] + 8), None if self.dark else NAVY)

    # ---------------- templates
    def t_hero(self):
        soft_scrim(self.img, -200, int(self.H * float(self.C.get("scrim_to", 0.40))), self.dark, 150)  # copy.json "scrim_to" shortens the headline wash
        self.mark()
        self.headline(self.head_y)
        self.footer()

    def t_strip(self):
        soft_scrim(self.img, -150, int(self.H * float(self.C.get("scrim_to", 0.36))), self.dark, 140)
        self.mark()
        self.headline(self.head_y, align="left", x0=(self.W - self.sw) // 2)
        self.footer()

    def frosted(self, box, radius=34, light=True):
        x0, y0, x1, y1 = [int(v) for v in box]
        region = self.img.crop((x0, y0, x1, y1)).filter(ImageFilter.GaussianBlur(26))
        tint = Image.new("RGBA", region.size, (255, 255, 255, 150) if light else (20, 24, 40, 150))
        region.alpha_composite(tint)
        mask = Image.new("L", region.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, region.width - 1, region.height - 1], radius, fill=255)
        self.img.paste(region, (x0, y0), mask)

    def t_notify(self):
        W, H = self.W, self.H
        soft_scrim(self.img, -200, int(H * 0.38), self.dark, 150)
        self.mark()
        self.headline(self.head_y)
        n = self.C["notify"]
        cw, ch = min(W - 160, self.safe[2] - self.safe[0]), 200
        c, x0, y0 = self.find_spot(cw, ch, int(H * 0.36), self.footer_top - 70, [80])
        if c > self.calm and self.prod:
            side = max(self.prod[0] - 60, W - self.prod[2] - 60)
            if side >= 560:
                cw = side
                xs = [56] if self.prod[0] - 60 >= W - self.prod[2] - 60 else [self.prod[2] + 4]
                c, x0, y0 = self.find_spot(cw, ch, int(H * 0.36), self.footer_top - 70, xs)
        if c > self.calm:
            self.warnings.append(f"notification card overlaps busy image area (cost {c:.0f}); regenerate with more empty space")
        self.frosted((x0, y0, x0 + cw, y0 + ch), 36, light=True)
        d = self.d
        # app icon (product.json "notify_icon")
        d.rounded_rectangle([x0 + 28, y0 + 30, x0 + 98, y0 + 100], 18, fill=NAVY)
        if self.PR.get("notify_icon") == "moon":
            d.ellipse([x0 + 46, y0 + 46, x0 + 80, y0 + 80], fill=(201, 186, 255))
            d.ellipse([x0 + 56, y0 + 40, x0 + 90, y0 + 74], fill=NAVY)  # crescent moon
        else:
            d.ellipse([x0 + 49, y0 + 51, x0 + 77, y0 + 79], fill=CREAM)
        d.text((x0 + 120, y0 + 26), n.get("app", self.PR["notify_app"]).upper(), font=sans(26, "SemiBold"), fill=(70, 74, 90))
        d.text((x0 + cw - 28 - d.textlength(n.get("time", "now"), font=sans(26)), y0 + 26), n.get("time", "now"), font=sans(26), fill=(90, 94, 110))
        d.text((x0 + 120, y0 + 66), n["title"], font=sans(38, "SemiBold"), fill=(20, 22, 30))
        d.text((x0 + 120, y0 + 120), n["body"], font=sans(32), fill=(50, 54, 66))
        self.footer()

    def t_toggle(self):
        W, H = self.W, self.H
        soft_scrim(self.img, -200, int(H * 0.38), self.dark, 150)
        self.mark()
        self.headline(self.head_y)
        rows = self.C["toggles"]
        cw, rh = min(W - 200, self.safe[2] - self.safe[0]), 150
        c, x0, y0 = self.find_spot(cw, rh * len(rows), int(H * 0.36), self.footer_top - 70, [100])
        if c > self.calm and self.prod:
            left, right = self.prod[0] - 60, W - self.prod[2] - 60
            side = max(left, right)
            if side >= 520:
                cw = side
                xs = [56] if left >= right else [self.prod[2] + 4]
                c, x0, y0 = self.find_spot(cw, rh * len(rows), int(H * 0.36), self.footer_top - 70, xs)
        if c > self.calm:
            self.warnings.append(f"toggle card overlaps busy image area (cost {c:.0f}); regenerate with more empty space")
        self.frosted((x0, y0, x0 + cw, y0 + rh * len(rows)), 40, light=True)
        d = self.d
        for i, (tm, label, on) in enumerate(rows):
            yy = y0 + i * rh
            if i:
                d.line([(x0 + 30, yy), (x0 + cw - 30, yy)], fill=(200, 200, 210), width=2)
            d.text((x0 + 38, yy + 18), tm, font=sans(56, "SemiBold"), fill=(20, 22, 30))
            d.text((x0 + 40, yy + 90), label, font=sans(32), fill=(70, 74, 90))
            tx, ty = x0 + cw - 140, yy + 40
            d.rounded_rectangle([tx, ty, tx + 108, ty + 56], 28, fill=GREEN if on else (205, 205, 212))
            kx = tx + (56 if on else 4)
            d.ellipse([kx, ty + 4, kx + 48, ty + 52], fill=(255, 255, 255))
        self.footer()

    def icon(self, d, kind, cx, cy, r, col):
        if kind == "moon":  # four-point sparkle (line icon)
            for dx, dy in ((0, r), (r, 0)):
                d.line([(cx - dx, cy - dy), (cx + dx, cy + dy)], fill=col, width=3)
            k = r * 0.45
            d.line([(cx - k, cy - k), (cx + k, cy + k)], fill=col, width=2)
            d.line([(cx - k, cy + k), (cx + k, cy - k)], fill=col, width=2)
        elif kind == "clock":
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=3)
            d.line([(cx, cy), (cx, cy - r + 7)], fill=col, width=3); d.line([(cx, cy), (cx + r - 9, cy)], fill=col, width=3)
        else:
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=3)
            d.line([(cx - 8, cy + 1), (cx - 2, cy + 8), (cx + 10, cy - 7)], fill=col, width=3)

    def t_chips(self):
        W, H = self.W, self.H
        soft_scrim(self.img, -200, int(H * 0.40), self.dark, 160)
        self.mark()
        y = self.headline(self.head_y)
        chips = self.C["chips"][:3]
        y_max = self.footer_top - 70  # stay above the footer panel
        kinds = ["moon", "clock", "check"]
        d0 = self.d
        candidates = []
        # A) one-line chips ("Trazodone · aids in falling asleep"), centred or to a side
        for fs in (36, 34, 32):  # legibility for 50+
            f = sans(fs, "Medium")
            ch, gap = int(fs * 2.8), int(fs * 0.5)
            cw = int(max(d0.textlength(t, font=f) for t in chips) + 120)
            if cw > self.safe[2] - self.safe[0]:
                continue
            stack_h = 3 * ch + 2 * gap
            c, x, yy = self.find_spot(cw, stack_h, y + 28, y_max, sorted({(W - cw) // 2, 56, W - 56 - cw}))
            candidates.append((c, "one", fs, ch, gap, cw, x, yy))
        # B) stacked chips (name on top, claim below) in a narrow column beside the product
        for fs in (36, 34, 32):
            fn, fc = sans(fs + 2, "SemiBold"), sans(fs, "Regular")
            parts = [t.split("·", 1) if "·" in t else [t, ""] for t in chips]
            cw = int(max(max(d0.textlength(a.strip(), font=fn), d0.textlength(b.strip(), font=fc)) for a, b in parts) + 120)
            ch, gap = int(fs * 3.6), int(fs * 0.5)
            stack_h = 3 * ch + 2 * gap
            c, x, yy = self.find_spot(cw, stack_h, y + 28, y_max, sorted({56, W - 56 - cw, (W - cw) // 2}))
            candidates.append((c, "two", fs, ch, gap, cw, x, yy))
        # prefer the biggest type that clears the product; one-line before stacked
        ok = [k for k in candidates if k[0] <= self.calm]
        pick = ok[0] if ok else min(candidates, key=lambda k: k[0])
        c, mode, fs, ch, gap, cw, x0, y0 = pick
        if c > self.calm:
            self.warnings.append(f"chips overlap busy image area (cost {c:.0f} > {self.calm:.0f}); pick another template or regenerate with more empty space")
        for i, txt in enumerate(chips):
            yy = y0 + i * (ch + gap)
            self.frosted((x0, yy, x0 + cw, yy + ch), 24, light=not self.dark)
            d = self.d
            self.icon(d, kinds[i], x0 + 48, yy + ch // 2, int(min(ch, 76) * 0.26), self.ink)
            if mode == "one":
                f = sans(fs, "Medium")
                d.text((x0 + 86, yy + (ch - f.size) // 2 - 3), txt, font=f, fill=self.ink)
            else:
                a, b = (txt.split("·", 1) + [""])[:2]
                d.text((x0 + 86, yy + ch // 2 - fs - 6), a.strip(), font=sans(fs + 2, "SemiBold"), fill=self.ink)
                d.text((x0 + 86, yy + ch // 2 + 4), b.strip(), font=sans(fs, "Regular"), fill=self.muted)
        self.footer()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw"); ap.add_argument("copy"); ap.add_argument("out")
    ap.add_argument("--ratio", default="4:5", choices=SIZES)
    ap.add_argument("--template", default="hero", choices=["hero", "strip", "notify", "toggle", "chips"])
    ap.add_argument("--tone", default="auto", choices=["auto", "dark", "light"])
    a = ap.parse_args()
    C = json.load(open(a.copy))
    PR = product.for_copy(C, a.copy)
    C["disclaimer"] = PR["disclaimer"]
    if not PR.get("product_zones"):
        raise SystemExit(f"❌ finish_modern can't find {PR['name']} in a photo yet (no \"product_zones\" in its product.json), "
                         "so it can't keep type off the product. Use finish_batch.py, or calibrate product_zones first.")
    order = [a.template] + [t for t in ("hero",) if t != a.template]
    for tpl in order:
        m = Modern(a.raw, C, a.ratio, a.tone, PR)
        getattr(m, "t_" + tpl)()
        if not m.warnings:
            break
        if tpl != order[-1]:
            print(f"NOTE: '{tpl}' can't fit without touching the product ({m.warnings[0]}); falling back to '{order[order.index(tpl)+1]}'")
    m.img.convert("RGB").save(a.out, quality=95)
    for w in m.warnings:
        print("WARNING:", w)
    print("done", a.out)
    if m.warnings:
        raise SystemExit(2)  # collision: do NOT deliver; change template, or regenerate the image with more space


if __name__ == "__main__":
    main()
