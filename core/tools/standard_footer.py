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


# ---------- proof split (bible 2026-11-02, Standards 01 + 02 · 06) ----------
# Trust callouts (the Trustpilot / Doctor Prescribed / Ships Free row) on ~60% of creatives, "Over 100,000 happy customers" on
# ~40%: images AND videos (Priestley 2026-11-02: "it's for videos too"). Each creative carries exactly ONE of the two.
COUNT_LINE = "Over 100,000 happy customers"   # locked proof string (bible)
COUNT_PX = 34                                 # reads at story size for 50+ (the trust row's art is ~100 px tall)
PROOFS = ("trust", "count")
LEDGER = os.path.join(os.path.expanduser(os.environ.get("EVERLIFE_HOME", "~/Everlife-Creative")), "proof-ledger.jsonl")


def count_row(tone, fw=ROW_W):
    """The customer-count line, centred in an RGBA strip `fw` wide (takes the trust row's place)."""
    f = ImageFont.truetype(os.path.join(FD, "Inter.ttf"), COUNT_PX)
    try:
        f.set_variation_by_name("SemiBold")
    except Exception:
        pass
    tw = int(ImageDraw.Draw(Image.new("RGB", (4, 4))).textlength(COUNT_LINE, font=f))
    row = Image.new("RGBA", (fw, COUNT_PX + 12), (0, 0, 0, 0))
    col = (246, 240, 226, 255) if tone == "dark" else (24, 30, 48, 255)
    ImageDraw.Draw(row).text(((fw - tw) // 2, 2), COUNT_LINE, font=f, fill=col)
    return row


def proof_plan(n):
    """Which ads of an n-ad batch get the trust row and which the customer count (~60% / ~40%, the first ad trust)."""
    k = round(0.4 * n + 1e-9) if n > 1 else 0
    return ["count" if (i * k) // n != ((i - 1) * k) // n else "trust" for i in range(1, n + 1)]


def _ledger(product):
    import json
    try:
        rows = [json.loads(l) for l in open(LEDGER) if l.strip()]
    except OSError:
        return []
    return [r for r in rows if r.get("product") == product]


def next_proof(product):
    """For creatives made one at a time (videos): the proof that keeps this product's running split nearest 60/40."""
    rows = _ledger(product)
    n, c = len(rows), sum(r.get("proof") == "count" for r in rows)
    return "count" if c < round(0.4 * (n + 1) + 1e-9) else "trust"


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
    print("ℹ️  copy.json has no \"proof\": trust row. Bible 2026-11-02: trust row on ~60% of creatives, customer count on ~40% "
          "(core/scripts/proof_next.py --product <id>).")
    return "trust"
