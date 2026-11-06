"""One footer standard for every Everlife creative (images and video endings, every skill).

Justin, 2026-11-02 (forwarded by Mitansh): "this banner [the Trustpilot / Doctor Prescribed / Ships Free row] will always be the
same size on every creative. And then the disclaimer is always the same size - ideally formatted to 2 lines and nested at
bottom. Those 2 elements I really want to standardize." Mitansh: "the disclaimer size is not fixed [in video endings]; it always
has to be 2 lines fixed." Bible Standards 02 · 04: disclaimer at the bottom, two lines maximum, 13 px minimum.

Sizes are for a 1080 px wide frame (every ratio we make is 1080 wide):
  trust row   ROW_W px wide, centred (height follows the art)
  disclaimer  Inter Medium DISC_PX px, line height DISC_LH, wrapped in a DISC_W px column: exactly DISC_LINES lines.
DISC_PX is the largest size at which every product's verbatim disclaimer fits 2 lines (Restora-Z's, the longest, sets it).
A disclaimer that needs a third line at this size is refused (shorten nothing: ask Jeremy), never shrunk per ad.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "fonts")
ROW_W = 990          # trust row width (the image footer's size since 2026-10-29; videos now match it)
DISC_PX = 18         # disclaimer type size (bible minimum 13 px)
DISC_LH = 23         # disclaimer line height
DISC_W = 1000        # disclaimer column (40 px margins on a 1080 frame)
DISC_LINES = 2


def disc_font():
    f = ImageFont.truetype(os.path.join(FD, "Inter.ttf"), DISC_PX)
    try:
        f.set_variation_by_name("Medium")
    except Exception:
        pass
    return f


def disclaimer_lines(text):
    """The verbatim disclaimer as exactly the lines it is drawn in (at most DISC_LINES). Refuses a longer one."""
    d, f = ImageDraw.Draw(Image.new("RGB", (4, 4))), disc_font()
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= DISC_W:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    if len(lines) > DISC_LINES:
        raise SystemExit(f"❌ the disclaimer needs {len(lines)} lines at the standard {DISC_PX} px (max {DISC_LINES}): "
                         f"ask Jeremy for a shorter verbatim text; never shrink it per ad")
    return lines


def disclaimer_height():
    return DISC_LH * DISC_LINES


def draw_disclaimer(img, text, y, fill, W=1080):
    """Draw the standard disclaimer centred on `img` (RGBA) starting at y. Returns the y below it."""
    d, f = ImageDraw.Draw(img), disc_font()
    for ln in disclaimer_lines(text):
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=fill)
        y += DISC_LH
    return y


# ---------- Solid footer art gate (Mitansh 2026-11-05: "fix them for once and for all") ----------
# The ghosted Trustpilot rows (stars, "4.9" and "EXCELLENT" see-through over wood, marble and cream; grey stars) came from
# badge_light.png, cut on 2026-10-27 by keying the white panel background out of the reference screenshot: the badge's own white
# pixels went with it (80% of them at ~20% opacity) and the file shipped in every zip since. Every footer piece now goes through
# open_footer_art(): a piece whose interior is not solid, or whose green shapes have see-through insides, is refused with a plain
# message, so no finisher (images or videos) can draw a ghosted proof row again.
SOLID_MAX_SOFT = 0.01       # ≤ 1% of the pixels 2 px inside the silhouette may be under alpha 250 (JPEG noise); an edge is outside this
_SOLID_OK = {}


def footer_art_report(path):
    """(interior px, soft share inside the silhouette, soft share inside the coloured shapes incl. their holes) for one PNG."""
    import numpy as np
    from PIL import ImageFilter
    im = Image.open(path).convert("RGBA"); arr = np.asarray(im); a = arr[:, :, 3]
    sil = Image.fromarray(((a >= 128).astype(np.uint8)) * 255)              # the visible art (gaps between the truck's speed lines are not art)
    inner = np.asarray(sil.filter(ImageFilter.MinFilter(7))) > 0            # 3 px inside: never an anti-aliased edge pixel
    soft = float((a[inner] < 250).mean()) if inner.any() else 0.0
    rgb = arr[:, :, :3].astype(int); sat = rgb.max(axis=2) - rgb.min(axis=2)
    col = Image.fromarray((((sat >= 40) & (a >= 160)).astype(np.uint8)) * 255)   # the solid coloured shapes (a seam between boxes is not art)
    pad = Image.new("L", (col.width + 4, col.height + 4), 0); pad.paste(col, (2, 2))
    ImageDraw.floodfill(pad, (0, 0), 128)                                     # 128 = outside; 0 left = a hole inside a coloured shape
    region = Image.fromarray(((np.asarray(pad)[2:-2, 2:-2] != 128).astype(np.uint8)) * 255)
    region = np.asarray(region.filter(ImageFilter.MinFilter(7))) > 0         # the shapes AND their insides (stars, "4.9"), 3 px in from their edge
    soft_col = float((a[region] < 250).mean()) if region.any() else 0.0
    return int(inner.sum()), soft, soft_col


def assert_solid_footer_art(path):
    if path in _SOLID_OK:
        return
    n, soft, soft_col = footer_art_report(path)
    if soft > SOLID_MAX_SOFT or soft_col > SOLID_MAX_SOFT:
        raise SystemExit(f"⛔ Footer art {os.path.basename(path)} is not solid: {soft:.0%} of its interior and {soft_col:.0%} of the "
                         f"inside of its green shapes are see-through (ghosted proof row). Rebuild the pieces with "
                         f"`python core/tools/make_footer_assets.py` (from assets/footer/approved_row.jpg), then run again. "
                         f"Refusing to draw a ghosted Trustpilot row (Mitansh 2026-11-05).")
    _SOLID_OK[path] = True


def open_footer_art(path):
    """Open a footer piece or row as RGBA, refusing any that is not solid (see assert_solid_footer_art)."""
    assert_solid_footer_art(path)
    return Image.open(path).convert("RGBA")


def row_art(path):
    """The approved trust-row art (one image) at the standard width."""
    r = open_footer_art(path)
    return r.resize((ROW_W, round(r.height * ROW_W / r.width)), Image.LANCZOS)


# ---------- ONE Trustpilot badge, forever (Mitansh 2026-11-05: "use the same logo we have in the original footer and fix it forever") ----------
# assets/footer/badge_master.png = the Nov 3 badge (git 19907b5, badge_dark.png), never regenerated by make_footer_assets.py.
# Every image finisher gets the badge from badge_art(): dark backgrounds = the master as is; light backgrounds = the SAME pixels with
# only the white "Trustpilot" wordmark (box WORDMARK_BOX of the master) recoloured to dark ink. Stars, shield, 4.9 and EXCELLENT
# never change, so the count row and the trust row, light or dark, always show the identical logo.
BADGE_MASTER = os.path.join(os.path.dirname(FD), "footer", "badge_master.png")
WORDMARK_BOX = (64, 18, 236, 70)      # x0, y0, x1, y1 in the master's own pixels (358x145)
WORDMARK_INK = (24, 30, 48)
MASTER_NAVY = (30, 58, 44)            # the master's baked dark-green edge line (measured: edge median 30,58,44), invisible on dark, an outline on light


def _label(mask):
    """Connected components (4-neighbour) without scipy: returns (labels, count)."""
    try:
        from scipy.ndimage import label
        return label(mask)
    except Exception:
        lab = np.zeros(mask.shape, int); n = 0
        H, W = mask.shape
        for y in range(H):
            for x in range(W):
                if mask[y, x] and not lab[y, x]:
                    n += 1; st = [(y, x)]; lab[y, x] = n
                    while st:
                        cy, cx = st.pop()
                        for ny, nx in ((cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)):
                            if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and not lab[ny, nx]:
                                lab[ny, nx] = n; st.append((ny, nx))
        return lab, n


def badge_art(tone):
    im = open_footer_art(BADGE_MASTER)
    if tone == "dark":
        return im
    a = np.array(im)
    x0, y0, x1, y1 = WORDMARK_BOX
    box = a[y0:y1, x0:x1]
    rgb = box[..., :3].astype(int)
    light = (rgb.min(axis=2) > 120) & (box[..., 3] > 0)           # the white letters and their anti-aliased edges, not the green star
    box[light, 0], box[light, 1], box[light, 2] = WORDMARK_INK
    a[y0:y1, x0:x1] = box
    # Un-blend the master's edge from the navy it was cut on: an edge pixel C = t*F + (1-t)*NAVY, F = the shape's own colour
    # (the strongest neighbour within 2 px). Its alpha becomes alpha*t and its colour F: smooth, rim-free edges on any background.
    f = a.astype(float)
    on = f[..., 3] > 0
    near = ~on
    for _ in range(3):                                             # pixels within 3 px of transparency = the edge zone
        g = near.copy(); g[1:] |= near[:-1]; g[:-1] |= near[1:]; g[:, 1:] |= near[:, :-1]; g[:, :-1] |= near[:, 1:]; near = g
    edge = on & near
    edge[y0:y1, x0:x1] = False                                     # the inked wordmark is already right
    nv = np.array(MASTER_NAVY, float)
    dist = np.sqrt(((f[..., :3] - nv) ** 2).sum(-1)) * on
    best = dist.copy(); col = f[..., :3].copy()
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            sd = np.roll(np.roll(dist, dy, 0), dx, 1); sc = np.roll(np.roll(f[..., :3], dy, 0), dx, 1)
            m = sd > best; best[m] = sd[m]; col[m] = sc[m]
    v = f[..., :3] - nv; w = col - nv
    t = np.clip((v * w).sum(-1) / np.maximum((w * w).sum(-1), 1e-6), 0, 1)
    f[edge, 3] = f[edge, 3] * t[edge]
    f[edge, :3] = col[edge]
    a = np.clip(f + 0.5, 0, 255).astype(np.uint8)
    on = a[..., 3] > 0                                             # leftover specks: 1-px edge pixels that are near-black,
    inner = on.copy(); inner[1:] &= on[:-1]; inner[:-1] &= on[1:]; inner[:, 1:] &= on[:, :-1]; inner[:, :-1] &= on[:, 1:]
    speck = on & ~inner & (a[..., :3].max(-1) < 70)               # (the art's darkest real colour, the shield's teal corner, is lighter)
    speck[y0:y1, x0:x1] = False
    a[speck, 3] = 0
    lab, n = _label(a[..., 3] > 0)                                 # and detached crumbs smaller than 30 px
    if n:
        sizes = np.bincount(lab.ravel())
        small = (sizes < 30); small[0] = False
        a[small[lab], 3] = 0
    return Image.fromarray(a, "RGBA")


# ---------- proof split (bible 2026-11-02, Standards 01 + 02 · 06; Mitansh's reading, 2026-11-02) ----------
# "do 30% without anything and 70% with footer with 40% having trustpilot + 100k customers". So, of all creatives,
# images AND videos:
#   trust  ~42%  the Trustpilot / Doctor Prescribed / Ships Free row
#   count  ~28%  the Trustpilot 4.9 badge + "Over 100,000 happy customers"
#   none   ~30%  no proof element (the logo and the verbatim disclaimer stay on every creative)
COUNT_LINE = "Over 100,000 happy customers"   # locked proof string (bible)
COUNT_PX = 34                                 # reads at story size for 50+ (the trust row's art is ~100 px tall)
PROOFS = ("trust", "count", "none")
SHARE = {"trust": 0.7 * 0.6, "none": 0.3, "count": 0.7 * 0.4}
LEDGER = os.path.join(os.path.expanduser(os.environ.get("EVERLIFE_HOME", "~/Everlife-Creative")), "proof-ledger.jsonl")


COUNT_BADGE_H = 96   # Trustpilot badge height beside the count line (Mitansh 2026-11-02)
COUNT_GAP = 28       # badge → divider → text spacing


COUNT_STYLE = os.environ.get("EVERLIFE_COUNT_STYLE", "badge")   # badge (default) | serif (variation, Mitansh 2026-11-02)


def count_row_serif(tone, fw=ROW_W):
    """Variation: no badge, the locked count line set alone in Instrument Serif Italic, large, with thin hairlines either side."""
    f = ImageFont.truetype(os.path.join(FD, "InstrumentSerif-Italic.ttf"), 60)
    d0 = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    tw = int(d0.textlength(COUNT_LINE, font=f))
    asc, desc = f.getmetrics()
    h = COUNT_BADGE_H
    row = Image.new("RGBA", (fw, h), (0, 0, 0, 0))
    col = (246, 240, 226, 255) if tone == "dark" else (24, 30, 48, 255)
    d = ImageDraw.Draw(row)
    x = (fw - tw) // 2
    d.text((x, (h - asc - desc) // 2), COUNT_LINE, font=f, fill=col)
    cy, rl = h // 2 + 2, 70
    d.line([(x - 28 - rl, cy), (x - 28, cy)], fill=col[:3] + (150,), width=2)
    d.line([(x + tw + 28, cy), (x + tw + 28 + rl, cy)], fill=col[:3] + (150,), width=2)
    return row


def count_row(tone, fw=ROW_W):
    if COUNT_STYLE == "serif":
        return count_row_serif(tone, fw)
    return count_row_badge(tone, fw)


def count_row_badge(tone, fw=ROW_W):
    """The customer-count line with the approved Trustpilot 4.9 Excellent badge beside it, centred together in an RGBA
    strip `fw` wide (takes the trust row's place). Mitansh 2026-11-02: "over 100k customers should at least have the
    trustpilot logo besides it". Badge art = the same approved art as the trust row (assets/footer/badge_<tone>.png)."""
    f = ImageFont.truetype(os.path.join(FD, "Inter.ttf"), COUNT_PX)
    try:
        f.set_variation_by_name("SemiBold")
    except Exception:
        pass
    badge = badge_art(tone)   # the ONE master badge (Nov 3), wordmark inked on light backgrounds
    badge = badge.resize((round(badge.width * COUNT_BADGE_H / badge.height), COUNT_BADGE_H), Image.LANCZOS)
    d0 = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    tw = int(d0.textlength(COUNT_LINE, font=f))
    asc, desc = f.getmetrics()
    total = badge.width + 2 * COUNT_GAP + 2 + tw
    row = Image.new("RGBA", (fw, COUNT_BADGE_H), (0, 0, 0, 0))
    x = (fw - total) // 2
    row.alpha_composite(badge, (x, 0))
    col = (246, 240, 226, 255) if tone == "dark" else (24, 30, 48, 255)
    d = ImageDraw.Draw(row)
    dx = x + badge.width + COUNT_GAP
    d.line([(dx, 18), (dx, COUNT_BADGE_H - 18)], fill=col[:3] + (110,), width=2)   # thin divider, like the trust row
    d.text((dx + 2 + COUNT_GAP, (COUNT_BADGE_H - asc - desc) // 2), COUNT_LINE, font=f, fill=col)
    return row


def _pick(counts, n):
    """The proof whose share is furthest behind after n creatives (largest remainder; ties: trust, none, count)."""
    return max(PROOFS, key=lambda k: (SHARE[k] * n - counts.get(k, 0), -PROOFS.index(k)))


def proof_plan(n):
    """Which ads of an n-ad batch get the trust row, the badge + count line, or no proof (~42 / 28 / 30%)."""
    counts, out = {}, []
    for i in range(1, n + 1):
        k = _pick(counts, i)
        counts[k] = counts.get(k, 0) + 1
        out.append(k)
    if "trust" in out:                       # open every batch on the trust row (a one-ad "batch" = trust)
        i = out.index("trust"); out = out[i:] + out[:i]
    return ["trust"] if n == 1 else out


def proof_row(proof, trust_art, tone="dark"):
    """The proof element for a creative: the trust-row art, the count row, or None (no proof)."""
    if proof == "none":
        return None
    return row_art(trust_art) if proof == "trust" else count_row(tone)


def _ledger(product):
    import json
    try:
        rows = [json.loads(l) for l in open(LEDGER) if l.strip()]
    except OSError:
        return []
    return [r for r in rows if r.get("product") == product]


def next_proof(product):
    """For creatives made one at a time (videos): the proof that keeps this product's running split nearest 42/28/30."""
    rows = _ledger(product)
    counts = {k: sum(r.get("proof") == k for r in rows) for k in PROOFS}
    return _pick(counts, len(rows) + 1)


def log_proof(product, proof, tag):
    import json, time
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "a") as fh:
        fh.write(json.dumps({"product": product, "proof": proof, "tag": tag, "at": time.strftime("%Y-%m-%dT%H:%M:%S")}) + "\n")


def proof_of(C):
    """A video job's proof from its copy.json ("proof": "trust" | "count"); missing → trust, with a reminder."""
    p = (C.get("proof") or "").strip()
    if p in PROOFS:
        return p
    if p:
        raise SystemExit(f"❌ copy.json \"proof\" must be one of {PROOFS}, not {p!r}")
    print("ℹ️  copy.json has no \"proof\": trust row. Split 2026-11-02: trust ~42%, badge + count ~28%, none ~30% "
          "(core/scripts/proof_next.py --product <id>).")
    return "trust"


# ---------- footer text colour without a haze (Mitansh 2026-11-04: no more "blurry area behind the Trustpilot footer") ----------
# The footer sits straight on the art/footage, so its text colour has to come from what is behind it.
TEXT_T = float(os.environ.get("EVERLIFE_TEXT_T", "150"))   # mean luminance 0-255; above = light background -> dark text


def tone_of(img, y0, y1):
    """'dark' (light text) or 'light' (dark text) for the band y0..y1 of an RGB/RGBA PIL image."""
    g = img.convert("L").crop((0, max(0, y0), img.width, min(img.height, y1))).resize((64, 16))
    v = sum(g.getdata()) / (64 * 16)
    return "dark" if v < TEXT_T else "light"


def video_tone(clip, ff, times=(1.0, 4.0, 8.0), y0=1100, y1=1920):
    """Footer tone for a 9:16 video: sample a few frames, scaled like the finisher scales them. EVERLIFE_FOOTER_TONE overrides."""
    forced = os.environ.get("EVERLIFE_FOOTER_TONE")
    if forced in ("dark", "light"):
        return forced
    import subprocess, tempfile
    votes = []
    for t in times:
        with tempfile.NamedTemporaryFile(suffix=".png") as f:
            r = subprocess.run([ff, "-v", "error", "-y", "-ss", str(t), "-i", clip, "-frames:v", "1", "-vf",
                                "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920", f.name])
            if r.returncode == 0 and os.path.getsize(f.name):
                votes.append(tone_of(Image.open(f.name), y0, y1))
    return "light" if votes and votes.count("light") > len(votes) / 2 else "dark"


def text_rgb(tone, alpha=255):
    return (236, 236, 232, alpha) if tone == "dark" else (24, 30, 48, alpha)


def trust_art(assets_dir, tone):
    """The approved trust row: white text for dark backgrounds, dark text (badge untouched) for light ones."""
    dark_txt = os.path.join(assets_dir, "proof_row_clear_dark.png")
    return dark_txt if tone == "light" and os.path.exists(dark_txt) else os.path.join(assets_dir, "proof_row_clear.png")
