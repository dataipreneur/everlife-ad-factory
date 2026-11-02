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
