"""Batch static finisher: the generated ad + the COMPACT, TRANSPARENT approved footer, inside the Meta 9:16 safe area.

The image model designs the whole ad (headline, benefits, product, scene). We lay the Everlife logo at the TOP (creative
lead, 2026-10-28) and the approved footer (Trustpilot 4.9 / Doctor Prescribed / Ships Free art + the verbatim disclaimer,
35% smaller and transparent, creative lead 2026-10-27) on a soft scrim.

  9:16  the footer ends at the bottom of the Meta safe area (safezones.FOOTER_BOTTOM = y 1385: above the Reels
        caption/CTA band; team Safe zones page, Standards 03; matches the live Reels reference, band at ~63–72%). Creative lead 2026-10-29, after a
        live Reels screenshot showed the bottom-anchored footer under the "Learn more" button
        (core/references/safe-zones/reels_placement_2026-10-29.jpg). The raw's content (headline, product, benefits)
        must END ABOVE the footer: the prompt's LAYOUT block keeps it in the top ~52% and the bottom ~45% calm (spare room). If a
        raw's content runs under the footer, the image is first shifted UP as far as the logo's headroom allows
        (the calm top is cropped, the calm bottom extended; --shift auto, max 320 px); if that is not enough the
        finisher refuses (exit 2): re-roll it, or fix the raw with one reposition edit (image-batch.md §4). Raws made before 2026-10-29 were composed to fill the frame: they need that
        edit (an automatic scale-down-and-extend was tried and rejected: blurred bars, logo on the headline).
  4:5 / 1:1  feed placements have no overlay: the footer sits over the calm bottom ~18%, as before.

usage: finish_batch.py <generated.png> <out.png> --ratio 4:5|9:16|1:1 --product <id> [--tone auto|dark|light]
       [--shift auto|<px>] (negative px = up) [--fit none|force]
       (--product takes the verbatim disclaimer from product.json; the older --disclaimer "<verbatim>" still works)
       finish_batch.py --content-ratio 4:5        prints the aspect ratio to request from the image model
"""
import argparse, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, T)
import safezones as sz  # noqa: E402

FD, FOOT = f"{T}/assets/fonts", f"{T}/assets/footer"
SIZES = {"4:5": (1080, 1350), "9:16": (1080, 1920), "1:1": (1080, 1080)}
# what to ask the image model for: the final shape itself
MODEL_RATIO = {"4:5": "4:5", "9:16": "9:16", "1:1": "1:1"}
LIGHT = (251, 251, 246)
DISC_SIZE, DISC_LH = 21, 26   # compact footer (creative lead: 35% smaller, transparent)
LOGO_W = 311                   # Everlife logo at the top; 311 ≈ 200 × 1.35 × 1.15 (Mitansh, 2026-10-28: "35% bigger", then "15% more")
LOGO_TOP = {"9:16": 150, "4:5": 60, "1:1": 56}   # inside the safe band (9:16: Stories UI covers the top 144 px)
LOGO_POS = "center"            # center | left | right (creative-system §2: large logo 40% centre, 36% in a corner)
LOGO_SMART = os.environ.get("EVERLIFE_LOGO_SMART", "0") != "0"   # auto-pick a clear spot for the logo (centre → right → left, then one row lower); never over the ad's type (Mitansh 2026-10-29)
LOGO_T = float(os.environ.get("LOGO_T", "135"))   # top band brighter than this → dark-ink logo (creative team, 2026-10-29)
DISC_AT = os.environ.get("EVERLIFE_DISC_AT", "bottom")   # 9:16: "bottom" = proof row stays in the safe area, the disclaimer sits at the very bottom of the frame (Mitansh, 2026-10-29, all products); "footer" = old, under the row
DISC_BOTTOM_MARGIN = 36
PROOF_SCALE = float(os.environ.get("EVERLIFE_PROOF_SCALE", "1.3225"))   # proof row +15% then +15% again (Mitansh, 2026-10-29, all products)
PROOF_W = int(os.environ.get("EVERLIFE_PROOF_W", "1000"))   # 9:16 proof-row column: wider than the 768 px safe column so the bigger row fits (crosses the Reels side bands by ~116 px; Mitansh 2026-10-29)
MAX_SHIFT = 140                # max nudge DOWN (logo headroom)
MAX_UP = 320                   # max nudge UP (9:16: pull the content above the safe-area footer)
CONTENT_GAP = 20               # px of calm background wanted between the raw's last content row and the footer


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


def build_footer(W, tone, disclaimer, fw, with_disclaimer=True):
    """Compact transparent footer, `fw` px wide, centred: approved proof art row (+ disclaimer unless it goes to the bottom). RGBA, no background."""
    s = 0.56 * PROOF_SCALE
    parts = [art("badge", tone, s), art("doctor", tone, s), art("ships", tone, s)]
    MIN_GAP = 18
    if sum(p.width for p in parts) + 4 * MIN_GAP + 2 > fw:            # auto-fit: as big as the column allows with real gaps
        s *= (fw - 2 - 4 * MIN_GAP) / sum(p.width for p in parts)
        parts = [art("badge", tone, s), art("doctor", tone, s), art("ships", tone, s)]
    gap = max(MIN_GAP, min(26, (fw - 2 - sum(p.width for p in parts)) // 4))
    rh = max(p.height for p in parts)
    d0 = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    lines = wrap(d0, disclaimer, sans(DISC_SIZE), fw) if with_disclaimer else []   # 21 px, wraps inside the safe column (Mitansh, 2026-10-29: keep this over bible v3's 2-line/13 px rule)
    h = 14 + rh + (6 + DISC_LH * len(lines) if lines else 0) + 22
    foot = Image.new("RGBA", (W, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(foot)
    y = 14
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


def build_disclaimer(W, tone, disclaimer, fw):
    """The verbatim disclaimer alone, centred, `fw` px wide: laid at the very bottom of a 9:16 frame (DISC_AT = bottom)."""
    d0 = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    lines = wrap(d0, disclaimer, sans(DISC_SIZE), fw)
    blk = Image.new("RGBA", (W, DISC_LH * len(lines) + 8), (0, 0, 0, 0))
    d = ImageDraw.Draw(blk)
    col = (236, 238, 236, 255) if tone == "dark" else (40, 44, 56, 255)
    f = sans(DISC_SIZE, "Medium"); y = 4
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=col); y += DISC_LH
    return blk


def _busy(img, box):
    """Edge density inside box (0..1): type and product edges score high, plain background low."""
    x0, y0, x1, y1 = box
    g = np.asarray(img.crop((x0, y0, x1, y1)).convert("L").resize((max(8, (x1 - x0) // 6), max(8, (y1 - y0) // 6))), dtype=np.float64)
    e = np.abs(np.diff(g, axis=0))[:, 1:] + np.abs(np.diff(g, axis=1))[1:, :]
    return float((e > 24).mean())


def smart_logo_spot(img, lw, lh, ly_default, sx0, sx1, pad=28):
    """Pick the logo position with the least content under it: try the default (top centre), then the two top corners,
    then the same three one logo-height lower (still inside the safe band). Returns (x, y)."""
    W = img.width
    xs = {"center": (W - lw) // 2, "left": max(60, sx0), "right": min(W - lw - 60, sx1 - lw)}
    cands = []
    for dy in (0, lh + pad):
        for name in ("center", "right", "left"):
            x, y = xs[name], ly_default + dy
            cands.append((_busy(img, (x - pad, y - pad, x + lw + pad, y + lh + pad)), dy, name, x, y))
    cands.sort(key=lambda c: (round(c[0], 2), c[1], ("center", "right", "left").index(c[2])))
    best = cands[0]
    if best[0] > 0.12:   # every spot is busy: fall back to top-right, the least harmful place over type
        return xs["right"], ly_default
    return best[3], best[4]


def logo_layer(tone):
    """The Everlife mark, cream on dark scenes, ink on light ones."""
    logo = Image.open(f"{T}/assets/logo_cream.png").convert("RGBA")
    logo = logo.resize((LOGO_W, int(logo.height * LOGO_W / logo.width)), Image.LANCZOS)
    if tone == "light":
        a = logo.split()[-1]; logo = Image.new("RGBA", logo.size, (16, 24, 44, 0)); logo.putalpha(a)
    return logo


def first_content_row(img, limit):
    """First row (within the top `limit` px) that carries text or an edge: row-wise contrast across the middle 80%."""
    g = np.asarray(img.convert("L"), dtype=np.float64)
    x0, x1 = int(g.shape[1] * 0.1), int(g.shape[1] * 0.9)
    band = g[:limit, x0:x1]
    std = band.std(axis=1)
    base = np.median(std[:max(4, limit // 20)])
    hit = np.nonzero(std > max(28.0, base + 18.0))[0]
    return int(hit[0]) if len(hit) else limit


def _content_rows(img):
    """Rows that carry text, product or a hard edge: edge density per row on a small, slightly blurred copy
    (calm backgrounds, fabric and marble stay under the threshold; type, bottles, nozzles and tablets do not)."""
    small = img.convert("L").resize((270, int(270 * img.height / img.width))).filter(ImageFilter.GaussianBlur(1.2))
    g = np.asarray(small, dtype=np.float64)
    e = np.zeros_like(g)
    e[1:, :] += np.abs(np.diff(g, axis=0)); e[:, 1:] += np.abs(np.diff(g, axis=1))
    x0, x1 = int(e.shape[1] * 0.06), int(e.shape[1] * 0.94)
    frac = (e[:, x0:x1] > 22).mean(axis=1)
    return np.nonzero(frac > 0.02)[0], img.height / small.height


def content_bottom(img):
    """Last row (full-size px) that carries content; 0 if none."""
    rows, k = _content_rows(img)
    return int((rows[-1] + 1) * k) if len(rows) else 0


def content_top(img, limit):
    """First row (full-size px, within `limit`) that carries content; `limit` if none."""
    rows, k = _content_rows(img)
    rows = rows[rows * k < limit]
    return int(rows[0] * k) if len(rows) else limit



def extend_bottom(img, W, H):
    """`img` (W wide, shorter than H): extend its calm bottom softly to H (blurred strip, feathered join)."""
    gh = img.height
    out = Image.new("RGB", (W, H))
    strip = img.crop((0, gh - max(8, gh // 40), W, gh)).resize((W, H - gh + 60)).filter(ImageFilter.GaussianBlur(26))
    out.paste(strip, (0, gh - 60))
    mask = Image.new("L", (W, gh), 255)
    md = ImageDraw.Draw(mask)
    for i in range(60):
        md.line([(0, gh - 1 - i), (W, gh - 1 - i)], fill=int(255 * i / 60))
    out.paste(img, (0, 0), mask)
    return out


def top_fade(W, h, tone):
    """Gentle fade behind the logo (strong at the very top, gone by h) so the mark reads on any photo."""
    col = (8, 12, 26) if tone == "dark" else (250, 249, 245)
    band = Image.new("RGBA", (W, h), col + (0,))
    bd = ImageDraw.Draw(band)
    for i in range(h):
        t = 1 - i / h
        bd.line([(0, i), (W, i)], fill=col + (int(120 * t ** 1.4),))
    return band


def scrim(W, h, tone, top_fade=120, bottom_fade=0):
    """Soft gradient behind the footer so it reads on any photo: transparent at the top, ~70% behind the footer, and
    (9:16) fading out again below it."""
    col = (8, 12, 26) if tone == "dark" else (250, 249, 245)
    band = Image.new("RGBA", (W, top_fade + h + bottom_fade), col + (0,))
    bd = ImageDraw.Draw(band)
    for i in range(band.height):
        if i < top_fade:
            t = i / top_fade
        elif i < top_fade + h:
            t = 1.0
        else:
            t = 1 - (i - top_fade - h) / bottom_fade
        bd.line([(0, i), (W, i)], fill=col + (int(185 * max(0.0, t) ** 1.2),))
    return band


def finish(gen_path, ratio, disclaimer, tone_opt="auto", shift_opt="auto", fit="none"):
    """Lay the logo + proof footer on one generated image (a path or a PIL image). Returns (RGB image, info dict).
    info: tone, top_tone, shift, fy, foot_h, story. Pass the first frame's tone and shift back in for every later video frame."""
    W, H = SIZES[ratio]
    story = (W, H) == (sz.W, sz.H) and not sz.BOTTOM_MODE
    wd = not (story and DISC_AT == "bottom")   # disclaimer inside the footer? (9:16 default: no, it goes to the bottom)
    gen = gen_path if isinstance(gen_path, Image.Image) else Image.open(gen_path).convert("RGB")
    lum = lambda c: 0.299 * c[..., 0] + 0.587 * c[..., 1] + 0.114 * c[..., 2]
    # scale to the full width; if the generation is shorter than the canvas (e.g. an old 1:1), extend its own
    # bottom softly; if taller, keep the top
    sc = W / gen.width
    gw, gh = W, int(gen.height * sc)
    g2 = gen.resize((gw, gh), Image.LANCZOS)
    out = extend_bottom(g2, W, H) if gh < H else g2.crop((0, 0, W, H))
    # Everlife logo at the top: find the headroom above the ad's first text/edge and nudge the image down if needed.
    # 9:16: if the content runs under the safe-area footer, nudge the image UP instead, as far as that headroom allows.
    ly = LOGO_TOP[ratio]
    logo_h = logo_layer("dark").height
    need = ly + logo_h + 26
    fw = min(PROOF_W, W - 80) if story else W - 80
    first = min(first_content_row(out, int(H * 0.3)), content_top(out, int(H * 0.3)))   # text (contrast) or product (edges)
    if shift_opt == "auto":
        shift = max(0, min(MAX_SHIFT, need - first))
        if story:
            fy0 = sz.FOOTER_BOTTOM - build_footer(W, "dark", disclaimer, fw, wd).height
            over = content_bottom(out) - (fy0 - CONTENT_GAP)
            if over > 0:
                shift = -max(0, min(MAX_UP, over, first - need))
    else:
        shift = max(-MAX_UP, min(MAX_SHIFT, int(shift_opt)))
    if shift > 0:
        shifted = Image.new("RGB", (W, H))
        shifted.paste(out, (0, shift))
        cap = out.crop((0, 0, W, max(8, shift // 6))).resize((W, shift + 40)).filter(ImageFilter.GaussianBlur(22))
        shifted.paste(cap, (0, 0))
        mask = Image.new("L", (W, 40), 0)
        md = ImageDraw.Draw(mask)
        for i in range(40):
            md.line([(0, i), (W, i)], fill=int(255 * (1 - i / 40)))
        shifted.paste(cap.crop((0, shift, W, shift + 40)), (0, shift), mask)
        out = shifted
    elif shift < 0:
        out = extend_bottom(out.crop((0, -shift, W, H)), W, H)
    # footer: 9:16 → ends at the bottom of the Meta safe area; feed (and the retired bottom mode) → bottom of the frame
    if story:
        foot_probe = build_footer(W, "dark", disclaimer, fw, wd)
        fy = sz.FOOTER_BOTTOM - foot_probe.height
        cb = content_bottom(out)
        if cb > fy - 6:            # the auto shift aims for CONTENT_GAP above the footer; allow the detector's 4 px steps
            if fit == "none":
                print(f"❌ {(os.path.basename(gen_path) if isinstance(gen_path, str) else 'frame')}: content runs to y {cb} but the footer starts at y {fy} "
                      f"(Meta 9:16 safe area ends at y {sz.FOOTER_BOTTOM}). Re-roll the raw with the 9:16 LAYOUT block "
                      f"(everything in the top ~52%, bottom ~45% calm; it was already shifted up {-shift}px) or fix it with "
                      f"one reposition edit; "
                      f"--fit force lays the footer over it for a QA preview only.")
                raise SystemExit(2)
        band = np.asarray(out.crop((0, fy - 60, W, sz.FOOTER_BOTTOM + 60)).resize((64, 16))).reshape(-1, 3).astype(np.float64)
    else:
        band = np.asarray(out.crop((0, int(H * 0.85), W, H)).resize((64, 16))).reshape(-1, 3).astype(np.float64)
    tone = tone_opt if tone_opt != "auto" else ("dark" if lum(band).mean() < 150 else "light")
    foot = build_footer(W, tone, disclaimer, fw, wd)
    o = out.convert("RGBA")
    if story:
        fy = sz.FOOTER_BOTTOM - foot.height
        sc_layer = scrim(W, foot.height, tone, top_fade=120, bottom_fade=160)
        o.alpha_composite(sc_layer, (0, fy - 120))
    else:
        bottom_pad = 48 if (W, H) == (1080, 1920) else 0          # retired bottom mode: same bottom line as the videos
        fy = H - foot.height - bottom_pad
        sc_layer = scrim(W, foot.height + bottom_pad, tone)
        o.alpha_composite(sc_layer, (0, H - sc_layer.height))
    o.alpha_composite(foot, (0, fy))
    if not wd:   # disclaimer at the very bottom of the 9:16 frame (under the Reels UI band; legal line, not a safe-area element)
        bb = np.asarray(out.crop((0, H - 160, W, H)).resize((64, 8))).reshape(-1, 3).astype(np.float64)
        dtone = "dark" if lum(bb).mean() < 150 else "light"
        disc = build_disclaimer(W, dtone, disclaimer, fw)
        dy = H - DISC_BOTTOM_MARGIN - disc.height
        o.alpha_composite(scrim(W, disc.height + DISC_BOTTOM_MARGIN, dtone, top_fade=70, bottom_fade=0), (0, dy - 70))
        o.alpha_composite(disc, (0, dy))
    top_band = np.asarray(out.crop((0, 0, W, ly + logo_h + 20)).resize((64, 8))).reshape(-1, 3).astype(np.float64)
    top_tone = "dark" if lum(top_band).mean() < LOGO_T else "light"
    lg = logo_layer(top_tone)
    sx0, sx1 = (sz.SAFE[0], sz.SAFE[2]) if story else (60, W - 60)   # corner logos stay inside the 9:16 safe band
    lx = {"center": (W - lg.width) // 2, "left": max(60, sx0), "right": min(W - lg.width - 60, sx1 - lg.width)}[LOGO_POS]
    if LOGO_POS == "center" and LOGO_SMART:
        lx, ly = smart_logo_spot(out, lg.width, lg.height, ly, sx0, sx1)   # never on top of the ad's own type (Mitansh, 2026-10-29)
    o.alpha_composite(top_fade(W, ly + logo_h + 30, top_tone), (0, 0))
    o.alpha_composite(lg, (lx, ly))
    # safe-zone check (9:16): the footer column and the logo must sit inside the Meta safe area
    if story:
        probs = sz.violations(((W - fw) // 2, fy, (W + fw) // 2, fy + foot.height), W, H, "footer")
        probs += sz.violations((lx, ly, lx + lg.width, ly + lg.height), W, H, "logo")
        if probs:
            print("❌ " + "; ".join(probs)); raise SystemExit(2)
    return o.convert("RGB"), {"tone": tone, "top_tone": top_tone, "shift": shift, "fy": fy, "foot_h": foot.height, "story": story}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("gen", nargs="?"); ap.add_argument("out", nargs="?")
    ap.add_argument("--ratio", default="4:5", choices=SIZES)
    ap.add_argument("--product", default="", help="product id: the verbatim disclaimer comes from its product.json")
    ap.add_argument("--disclaimer", default="", help="verbatim disclaimer (older usage; must match --product if both)")
    ap.add_argument("--tone", default="auto", choices=["auto", "dark", "light"])
    ap.add_argument("--shift", default="auto", help="auto: nudge the image down only if the logo needs room; or a px value")
    ap.add_argument("--fit", default="none", choices=["none", "force", "trusted"],
                    help="9:16 raw whose content runs under the footer: none = refuse (exit 2); force = lay the footer over "
                         "it anyway (QA previews only, never a FINAL); trusted = the raw came from reposition_916.py / compose916.py, "
                         "which already placed text + product above the footer: scene under the footer is allowed (FINAL ok)")
    ap.add_argument("--content-ratio", help="print the model aspect ratio for this final ratio and exit")
    ap.add_argument("--logo-w", default="", help="logo width: px or percent of the ad width (creative-system: 40%% centre, 36%% corner, small 30%%/28%%); default 311 px")
    ap.add_argument("--logo-pos", default="center", choices=["center", "left", "right"])
    a = ap.parse_args()
    global LOGO_W, LOGO_POS
    LOGO_POS = a.logo_pos
    if a.logo_w:
        LOGO_W = int(SIZES[a.ratio][0] * float(a.logo_w.rstrip("%")) / 100) if a.logo_w.endswith("%") else int(a.logo_w)
    if a.content_ratio:
        print(MODEL_RATIO[a.content_ratio]); return
    if a.product:
        import product
        PR = product.load(a.product)
        if a.disclaimer and a.disclaimer != PR["disclaimer"]:
            raise SystemExit(f"❌ --disclaimer differs from {a.product}'s product.json (it must be the bible text, verbatim)")
        a.disclaimer = PR["disclaimer"]
    if not a.disclaimer:
        raise SystemExit("❌ pass --product <id> (or the verbatim bible disclaimer with --disclaimer)")
    out, info = finish(a.gen, a.ratio, a.disclaimer, a.tone, a.shift, a.fit)
    tone, top_tone, shift, fy, story = info['tone'], info['top_tone'], info['shift'], info['fy'], info['story']
    ly = LOGO_TOP[a.ratio]; foot_h = info['foot_h']
    out.save(a.out, quality=95)
    where = f"y {fy}–{fy + foot_h} (safe area)" if story else "bottom"
    disc_where = "bottom of frame" if (story and DISC_AT == "bottom") else "in footer"
    print(f"done {a.out}  tone={tone}  logo=top@{ly}px({top_tone}) shift={shift}px  "
          f"footer={foot_h}px @ {where}  disclaimer={disc_where}")


if __name__ == "__main__":
    main()
