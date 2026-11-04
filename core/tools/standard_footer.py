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


def row_art(path):
    """The approved trust-row art (one image) at the standard width."""
    r = Image.open(path).convert("RGBA")
    return r.resize((ROW_W, round(r.height * ROW_W / r.width)), Image.LANCZOS)


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
    badge = Image.open(os.path.join(os.path.dirname(FD), "footer",
                                    "badge_dark.png" if tone == "dark" else "badge_light.png")).convert("RGBA")
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
TEXT_T = float(os.environ.get("EVERLIFE_TEXT_T", "118"))   # mean luminance 0-255; above = light background -> dark text


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
