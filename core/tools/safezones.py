"""EverlifeMD safe zones (Creative Messaging Reference · Standards 03 · Meta 9:16 placements, 1080×1920).

Keep the logo, headline, offer, CTA, captions, proof and disclaimer OUT of these areas:
  Stories:  top 144 px (profile name + progress bar); centre-bottom 664×248 (reply bar + CTA sticker)
  Reels:    left & right 156 px; bottom 535 px (caption, audio, CTA button); lower-left 219×169 (profile + follow)

One asset serves both placements, so we use the INTERSECTION as the safe area:
  x 156–924, y 144–1385, minus the lower-left notch x 156–375 × y 1216–1385.
Feed ratios (4:5, 1:1) have no Meta overlay; we still keep a 60 px margin.
"""

import os

W, H = 1080, 1920
SAFE = (156, 144, 924, 1385)               # x0, y0, x1, y1 for 9:16
NOTCH = (156, 1216, 375, 1385)             # Reels profile + follow (inside SAFE's bounds, still unsafe)
STORIES_REPLY = (208, 1540, 872, 1788)     # outside SAFE already; listed for overlays
SAFE_W = SAFE[2] - SAFE[0]                 # 768
FEED_MARGIN = 60

# Where the proof block (Trustpilot row + disclaimer) and captions live on 9:16.
#   "bottom" (default; creative lead 2026-10-27: "have it at the bottom!"): footer anchored at the bottom of the frame,
#            captions just above it. Top + side margins still apply. NOTE: in Reels the bottom ~535 px sits under
#            Meta's caption/CTA UI, so the disclaimer can be partly covered there (flagged for Jeremy).
#   "safe":  everything above y 1206 (Standards 03 intersection), as before.
PROOF_AT = os.environ.get("EVERLIFE_PROOF_AT", "bottom")
BOTTOM_MODE = PROOF_AT == "bottom"
FOOTER_BOTTOM = H - 48 if BOTTOM_MODE else NOTCH[1] - 10
FOOT_W = W - 80 if BOTTOM_MODE else SAFE_W        # bottom mode = the approved full-width footer (matches the 10-26 videos)
FOOT_X0 = (W - FOOT_W) // 2


def safe_box(w, h):
    """Safe content box for a canvas size (9:16 → Meta zones; feed → margin)."""
    if (w, h) == (W, H):
        return SAFE
    return (FEED_MARGIN, FEED_MARGIN, w - FEED_MARGIN, h - FEED_MARGIN)


def violations(box, w=W, h=H, label="element"):
    """List of problems if `box` (x0,y0,x1,y1) leaves the safe area or touches the notch."""
    x0, y0, x1, y1 = box
    s = safe_box(w, h)
    if BOTTOM_MODE and (w, h) == (W, H):
        s = (s[0], s[1], s[2], H - 40)
        if label.startswith(("proof", "disclaimer", "footer")):   # the approved full-width footer (40 px margins)
            s = (FOOT_X0 - 1, s[1], W - FOOT_X0 + 1, H - 40)
    out = []
    if x0 < s[0] - 1 or y0 < s[1] - 1 or x1 > s[2] + 1 or y1 > s[3] + 1:
        out.append(f"{label} {tuple(int(v) for v in box)} is outside the safe area {s}")
    if (w, h) == (W, H) and not BOTTOM_MODE and not (x1 <= NOTCH[0] or x0 >= NOTCH[2] or y1 <= NOTCH[1] or y0 >= NOTCH[3]):
        out.append(f"{label} {tuple(int(v) for v in box)} overlaps the Reels profile area {NOTCH}")
    return out


def overlay(img):
    """Debug/QA view: shade the unsafe areas on a 9:16 frame (returns a new RGBA image)."""
    from PIL import Image, ImageDraw
    im = img.convert("RGBA").copy()
    if im.size != (W, H):
        return im
    sh = Image.new("RGBA", im.size, (255, 0, 80, 0))
    d = ImageDraw.Draw(sh)
    red = (255, 0, 80, 70)
    d.rectangle([0, 0, W, SAFE[1]], fill=red)
    d.rectangle([0, SAFE[3], W, H], fill=red)
    d.rectangle([0, SAFE[1], SAFE[0], SAFE[3]], fill=red)
    d.rectangle([SAFE[2], SAFE[1], W, SAFE[3]], fill=red)
    d.rectangle(NOTCH, fill=red)
    d.rectangle(STORIES_REPLY, outline=(255, 0, 80, 200), width=3)
    im.alpha_composite(sh)
    return im
