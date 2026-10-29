#!/usr/bin/env python3
"""animate_code.py: turn an approved static RAW into an 8 s "animated still" with code only (0 credits).

Effects (all on the RAW, before the finisher lays logo + footer with animate_still.py):
  * slow 5 % push-in (ease in-out)                       -> the Seedance "camera creeps in" look
  * a wide soft light sweep across the environment       -> warm or cool, low amplitude
  * a glint that slides across the headline text          -> text pixels brighten + soft bloom
  * optional twinkle on bright specks (ice / chalk)      -> --twinkle
  * a thin analog clock whose second hand sweeps one full turn in the clip, minute hand creeping -> --clock X,Y,R
The vial, label and every word stay pixel-locked: nothing is warped, only light is added.

usage: animate_code.py RAW.png out.mp4 [--seconds 8] [--fps 30] [--size 1080x1920]
         [--tone warm|cool] [--text-region y0,y1] [--clock X,Y,R] [--clock-color R,G,B] [--twinkle y0,y1,x0,x1 ...]
         [--push 0.05] [--ffmpeg PATH]
"""
import argparse, math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def ease(t):  # smoothstep
    return t * t * (3 - 2 * t)


def gauss_band(xx, yy, cx, angle_deg, width):
    """soft diagonal band centred on x = cx (at y = 0), returns 0..1 float array"""
    a = math.radians(angle_deg)
    d = (xx - cx) * math.cos(a) + yy * math.sin(a)
    return np.exp(-(d * d) / (2 * (width / 2.355) ** 2))


def draw_clock(size_px, t, color, hour=10, minute0=10):
    """returns an RGBA PIL tile with a minimalist analog clock, supersampled 2x"""
    S = 2
    D = size_px * S
    tile = Image.new("RGBA", (D, D), (0, 0, 0, 0))
    dr = ImageDraw.Draw(tile)
    c = D / 2
    r = D / 2 - 3 * S
    col = tuple(color) + (int(255 * 0.78),)
    dim = tuple(color) + (int(255 * 0.45),)
    dr.ellipse([c - r, c - r, c + r, c + r], outline=col, width=2 * S)
    for i in range(12):
        a = math.radians(i * 30)
        ln = (9 if i % 3 == 0 else 5) * S
        x0, y0 = c + (r - 6 * S) * math.sin(a), c - (r - 6 * S) * math.cos(a)
        x1, y1 = c + (r - 6 * S - ln) * math.sin(a), c - (r - 6 * S - ln) * math.cos(a)
        dr.line([x0, y0, x1, y1], fill=col if i % 3 == 0 else dim, width=(2 if i % 3 == 0 else 1) * S)
    # hands: hour fixed, minute creeps 45 deg over the clip, second hand one full turn with a tick feel
    sec_turn = t  # 0..1 over the clip
    tick = math.floor(sec_turn * 60)
    frac = sec_turn * 60 - tick
    sec_ang = (tick + ease(min(1.0, frac * 3))) / 60 * 360
    min_ang = minute0 * 6 + 45 * ease(t)
    hr_ang = hour * 30 + min_ang / 12
    for ang, length, w, a_ in ((hr_ang, 0.5, 3, col), (min_ang, 0.74, 2, col), (sec_ang, 0.86, 1, col)):
        a = math.radians(ang)
        dr.line([c, c, c + r * length * math.sin(a), c - r * length * math.cos(a)], fill=a_, width=w * S)
    dr.ellipse([c - 3 * S, c - 3 * S, c + 3 * S, c + 3 * S], fill=col)
    return tile.resize((size_px, size_px), Image.LANCZOS)


def _font(px, bold=True):
    from PIL import ImageFont
    here = os.path.dirname(os.path.abspath(__file__))
    for path in (os.path.join(here, "assets", "fonts", "Inter.ttf"), "/System/Library/Fonts/Supplemental/Arial Bold.ttf"):
        if os.path.exists(path):
            f = ImageFont.truetype(path, px)
            try:
                f.set_variation_by_name("Bold" if bold else "Regular")
            except Exception:
                pass
            return f
    return ImageFont.load_default()


def draw_urgency(R, ts, seconds, red, text_lines, width=None):
    """SUPER aggressive urgency block: thick pulsing countdown ring with glow, second hand one turn per second,
    fit-to-width type, offer flashing red/white. Returns (RGBA tile, pulse, clock_cy)."""
    S = 2
    pad = int(R * 0.9)
    tw = int(width or (2 * R + 2 * pad))
    th = int(2 * R + 2 * pad + R * 2.4)
    tile = Image.new("RGBA", (tw * S, th * S), (0, 0, 0, 0))
    dr = ImageDraw.Draw(tile)
    cx, cy = tw * S / 2, (pad + R) * S
    beat = ts % 1.0
    pulse = math.exp(-beat / 0.14)
    glow = Image.new("RGBA", tile.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gr = R * S * (1.35 + 0.6 * pulse)
    gd.ellipse([cx - gr, cy - gr, cx + gr, cy + gr], fill=red + (int(90 + 140 * pulse),))
    glow = glow.filter(ImageFilter.GaussianBlur(R * S * 0.4))
    tile.alpha_composite(glow)
    r = R * S
    w = int(R * 0.17) * S
    dr.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255, 90), width=w)
    remaining = 1 - ts / seconds
    if remaining > 0.002:
        dr.arc([cx - r, cy - r, cx + r, cy + r], start=-90, end=-90 + 360 * remaining, fill=red + (255,), width=w)
    for i in range(12):
        a = math.radians(i * 30)
        r0, r1 = r - w - 6 * S, r - w - (20 if i % 3 == 0 else 11) * S
        dr.line([cx + r0 * math.sin(a), cy - r0 * math.cos(a), cx + r1 * math.sin(a), cy - r1 * math.cos(a)],
                fill=(255, 255, 255, 240), width=(4 if i % 3 == 0 else 2) * S)
    hr = 300 + 60 * ts / seconds
    mn = 360 * 2 * ts / seconds
    sc = (360 * ts) % 360
    for ang, ln, wd, col in ((hr, 0.48, 8, (255, 255, 255, 255)), (mn, 0.7, 6, (255, 255, 255, 255)), (sc, 0.84, 4, red + (255,))):
        a = math.radians(ang)
        dr.line([cx, cy, cx + r * ln * math.sin(a), cy - r * ln * math.cos(a)], fill=col, width=wd * S)
    dr.ellipse([cx - 7 * S, cy - 7 * S, cx + 7 * S, cy + 7 * S], fill=red + (255,))
    # text block: kicker in a red pill, lead-in, offer flashing red/white every half second
    y = cy + r + pad * 0.55 * S
    flash = int(ts * 2) % 2 == 0
    offer_col = red + (255,) if flash else (255, 255, 255, 255)
    maxw = tw * S * 0.94
    specs = ((text_lines[0], int(R * 0.30), (255, 255, 255, 255), 0.14, True),
             (text_lines[1], int(R * 0.36), (255, 255, 255, 255), 0.03, False),
             (text_lines[2], int(R * 1.0), offer_col, -0.02, False))
    for txt, px, col, track, pill in specs:
        px_s = px * S
        while True:
            f = _font(px_s)
            widths = [dr.textlength(ch, font=f) for ch in txt]
            gap = track * px_s
            total = sum(widths) + gap * (len(txt) - 1)
            if total <= maxw or px_s < 12 * S:
                break
            px_s = int(px_s * 0.94)
        x = cx - total / 2
        if pill:
            ph = px_s * 1.5
            dr.rounded_rectangle([x - px_s * 0.7, y - ph * 0.17, x + total + px_s * 0.7, y - ph * 0.17 + ph],
                                 radius=ph / 2, fill=red + (255,))
        for ch, wch in zip(txt, widths):
            dr.text((x, y), ch, font=f, fill=col)
            x += wch + gap
        y += px_s * (1.5 if pill else 1.12)
    return tile.resize((tw, th), Image.LANCZOS), pulse, pad + R



def draw_alarm(R, ts, color, text_lines, width):
    """classic twin-bell alarm clock in the ad's palette, vibrating hard. Line art, no fills, no glow.
    Returns (RGBA tile, clock centre y in tile px)."""
    S = 2
    pad = int(R * 0.75)
    tw, th = int(width), int(2 * R + 2 * pad + R * 1.6)
    tile = Image.new("RGBA", (tw * S, th * S), (0, 0, 0, 0))
    col = tuple(color) + (255,)
    soft = tuple(color) + (110,)
    # --- clock body drawn on its own layer so it can rotate about its feet
    body = Image.new("RGBA", (int(3.2 * R) * S, int(3.2 * R) * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(body)
    bc = body.width / 2
    cy = body.height * 0.56
    r = R * S
    w = max(3, int(R * 0.075)) * S
    d.ellipse([bc - r, cy - r, bc + r, cy + r], outline=col, width=w)
    d.ellipse([bc - r * 0.86, cy - r * 0.86, bc + r * 0.86, cy + r * 0.86], outline=soft, width=max(1, w // 3))
    for i in range(12):
        a = math.radians(i * 30)
        r0, r1 = r * 0.80, r * (0.66 if i % 3 == 0 else 0.73)
        d.line([bc + r0 * math.sin(a), cy - r0 * math.cos(a), bc + r1 * math.sin(a), cy - r1 * math.cos(a)],
               fill=col, width=(w if i % 3 == 0 else max(1, w // 2)))
    # hands: hour 10, minute at 2 (classic alarm pose), second hand racing one turn per second
    for ang, ln, wd in ((300, 0.42, w), (60, 0.62, w), ((360 * ts) % 360, 0.74, max(1, w // 2))):
        a = math.radians(ang)
        d.line([bc, cy, bc + r * ln * math.sin(a), cy - r * ln * math.cos(a)], fill=col, width=wd)
    d.ellipse([bc - w, cy - w, bc + w, cy + w], fill=col)
    # bells: two domes on top at +-35 deg, with stems; hammer between them
    for sgn in (-1, 1):
        a = math.radians(sgn * 35)
        bx, by = bc + r * 1.08 * math.sin(a), cy - r * 1.08 * math.cos(a)
        br = r * 0.30
        d.pieslice([bx - br, by - br, bx + br, by + br], start=180 + sgn * 35 - 10, end=360 + sgn * 35 + 10, outline=col, width=w)
        d.line([bc + r * 0.9 * math.sin(a), cy - r * 0.9 * math.cos(a), bx, by], fill=col, width=w)
        # bell cap
        ca = math.radians(sgn * 35)
        d.line([bx - br * 0.35 * math.cos(ca), by - br * 0.35 * math.sin(ca) - br * 1.0,
                bx + br * 0.35 * math.cos(ca), by + br * 0.35 * math.sin(ca) - br * 1.0], fill=col, width=w)
    hx = bc + r * 0.18 * math.sin(ts * 70)  # hammer whips left-right
    d.line([bc, cy - r * 1.02, hx, cy - r * 1.36], fill=col, width=w)
    d.ellipse([hx - w * 1.6, cy - r * 1.36 - w * 1.6, hx + w * 1.6, cy - r * 1.36 + w * 1.6], fill=col)
    # feet
    for sgn in (-1, 1):
        a = math.radians(sgn * 28)
        d.line([bc + r * 0.92 * math.sin(math.radians(180 - sgn * 28)), cy - r * 0.92 * math.cos(math.radians(180 - sgn * 28)),
                bc + r * 1.22 * math.sin(math.radians(180 - sgn * 28)), cy - r * 1.22 * math.cos(math.radians(180 - sgn * 28))],
               fill=col, width=w)
    # ring marks: short arcs beside the bells, flickering with the vibration
    if int(ts * 20) % 2 == 0:
        for sgn in (-1, 1):
            for k in (1.38, 1.52):
                d.arc([bc - r * k, cy - r * k, bc + r * k, cy + r * k],
                      start=(-90 + sgn * 40 - 14), end=(-90 + sgn * 40 + 14), fill=soft, width=max(1, w // 2))
    # --- vibration: fast rocking about the feet + horizontal jitter, with two ghost echoes
    ang = 9 * math.sin(ts * 2 * math.pi * 7.3) * (0.7 + 0.3 * math.sin(ts * 2 * math.pi * 0.9))
    pivot = (bc, cy + r * 1.1)
    layer = Image.new("RGBA", tile.size, (0, 0, 0, 0))
    cx_t = tw * S / 2
    top = pad * S
    for k, alpha in ((2, 60), (1, 110), (0, 255)):
        a_k = ang * (1 - 0.35 * k)
        rot = body.rotate(a_k, resample=Image.BICUBIC, center=pivot)
        if alpha < 255:
            al = rot.split()[3].point(lambda v: v * alpha // 255)
            rot.putalpha(al)
        jx = int(6 * S * math.sin(ts * 2 * math.pi * 11 + k))
        layer.alpha_composite(rot, (int(cx_t - body.width / 2 + jx), int(top)))
    tile.alpha_composite(layer)
    # --- text: one quiet line in the ad's own type and colour (no pill, no flash)
    f_px = int(R * 0.30) * S
    y = top + cy + r * 1.3 + pad * 0.6 * S
    dr = ImageDraw.Draw(tile)
    maxw = tw * S * 0.95
    for i, txt in enumerate(text_lines):
        px = int(f_px * (1.35 if i == len(text_lines) - 1 else 1.0))
        while True:
            f = _font(px); total = dr.textlength(txt, font=f)
            if total <= maxw or px < 12 * S: break
            px = int(px * 0.94)
        dr.text((cx_t - total / 2, y), txt, font=f, fill=col)
        y += px * 1.25
    return tile.resize((tw, th), Image.LANCZOS), (top + cy) / S


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw"); ap.add_argument("out")
    ap.add_argument("--seconds", type=float, default=8); ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--size", default="1080x1920"); ap.add_argument("--push", type=float, default=0.05)
    ap.add_argument("--tone", choices=["warm", "cool"], default="warm")
    ap.add_argument("--text-region", default="0,0.3", help="y0,y1 as fractions of height holding the headline")
    ap.add_argument("--text-thresh", type=int, default=140)
    ap.add_argument("--clock", default=None, help="X,Y,R in raw pixels")
    ap.add_argument("--clock-color", default="235,225,205")
    ap.add_argument("--urgency", default=None, help="X,Y,R: aggressive pulsing countdown clock + blinking offer instead of the calm clock")
    ap.add_argument("--urgency-text", default="LIMITED TIME|TAKE UP TO|40% OFF", help="kicker|lead-in|offer, '|' separated (offer must be an approved line)")
    ap.add_argument("--urgency-color", default="232,48,40")
    ap.add_argument("--urgency-width", type=int, default=None, help="block width in raw px (fit-to-width type)")
    ap.add_argument("--alarm", default=None, help="X,Y,R: vibrating twin-bell alarm clock in the ad's palette (line art, no red)")
    ap.add_argument("--alarm-color", default="205,175,125")
    ap.add_argument("--alarm-width", type=int, default=380)
    ap.add_argument("--alarm-text", default="LIMITED TIME|TAKE UP TO 40% OFF", help="'|' separated lines under the clock; '' for none")
    ap.add_argument("--twinkle", action="append", default=[], help="y0,y1,x0,x1 (raw px) box of bright specks to twinkle")
    ap.add_argument("--sweep-amp", type=float, default=16)
    ap.add_argument("--glint-amp", type=float, default=0.55)
    ap.add_argument("--anchor", choices=["center", "top"], default="center",
                    help="top keeps the top edge fixed so a headline near the logo never rises into it")
    ap.add_argument("--ffmpeg", default=os.environ.get("FF", "ffmpeg"))
    a = ap.parse_args()

    base = Image.open(a.raw).convert("RGB")
    W, H = base.size
    OW, OH = (int(v) for v in a.size.split("x"))
    N = int(round(a.seconds * a.fps))
    img = np.asarray(base).astype(np.float32)
    lum = img @ np.array([0.299, 0.587, 0.114], dtype=np.float32)

    # headline text mask (bright pixels inside the text band), plus a blurred halo for bloom
    y0f, y1f = (float(v) for v in a.text_region.split(","))
    tmask = np.zeros((H, W), np.float32)
    ys, ye = int(y0f * H), int(y1f * H)
    tmask[ys:ye] = (lum[ys:ye] > a.text_thresh).astype(np.float32)
    halo = np.asarray(Image.fromarray((tmask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(14))).astype(np.float32) / 255.0
    text_x0 = int(np.where(tmask.any(axis=0))[0].min()) if tmask.any() else 0
    text_x1 = int(np.where(tmask.any(axis=0))[0].max()) if tmask.any() else W

    # twinkle specks mask with per-pixel random phase
    twk = np.zeros((H, W), np.float32); phase = np.zeros((H, W), np.float32)
    rng = np.random.default_rng(7)
    for box in a.twinkle:
        by0, by1, bx0, bx1 = (int(v) for v in box.split(","))
        sub = (lum[by0:by1, bx0:bx1] > 150).astype(np.float32)
        twk[by0:by1, bx0:bx1] = np.maximum(twk[by0:by1, bx0:bx1], sub)
    if twk.any():
        phase = rng.uniform(0, 2 * math.pi, (H, W)).astype(np.float32)
        phase = np.asarray(Image.fromarray(((phase / (2 * math.pi)) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))).astype(np.float32) / 255 * 2 * math.pi

    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    tone = np.array([1.0, 0.82, 0.6] if a.tone == "warm" else [0.75, 0.85, 1.0], dtype=np.float32)
    clock = None
    if a.clock:
        cx, cy, cr = (int(v) for v in a.clock.split(","))
        ccol = tuple(int(v) for v in a.clock_color.split(","))

    cmd = [a.ffmpeg, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{OW}x{OH}", "-r", str(a.fps), "-i", "-",
           "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-movflags", "+faststart", a.out]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    for i in range(N):
        t = i / max(1, N - 1)
        frame = img.copy()
        # 1. environment light sweep: a wide band crossing the whole frame once
        cx_s = -0.3 * W + 1.6 * W * ease(t)
        band = gauss_band(xx, yy, cx_s, -35, 0.55 * W)
        frame += (band[..., None] * a.sweep_amp) * tone
        # 2. headline glint: a narrow band crossing the text twice (1.0-3.4 s and 5.2-7.6 s)
        ts = t * a.seconds
        for g0, g1 in ((1.0, 3.4), (5.2, 7.6)):
            if g0 <= ts <= g1:
                u = ease((ts - g0) / (g1 - g0))
                gx = (text_x0 - 0.25 * W) + (text_x1 - text_x0 + 0.5 * W) * u
                gb = gauss_band(xx, yy, gx, -25, 110)
                gain = gb * tmask * a.glint_amp
                frame += (255 - frame) * gain[..., None]
                frame += (gb * halo * 70)[..., None] * np.array([1, 1, 1], np.float32)
        # 3. twinkle
        if twk.any():
            tw = (0.5 + 0.5 * np.sin(phase + t * 2 * math.pi * 1.5)) * twk
            frame += (tw * 70)[..., None]
        np.clip(frame, 0, 255, out=frame)
        pil = Image.fromarray(frame.astype(np.uint8))
        # 4. clock (drawn in raw coords so it pushes in with the scene)
        if a.clock:
            tile = draw_clock(cr * 2, t, ccol)
            pil.paste(tile, (cx - cr, cy - cr), tile)
        if a.alarm:
            ax, ay, ar = (int(v) for v in a.alarm.split(","))
            acol = tuple(int(v) for v in a.alarm_color.split(","))
            lines = [l for l in a.alarm_text.split("|") if l]
            tile, ccy = draw_alarm(ar, ts, acol, lines, a.alarm_width)
            pil.paste(tile, (ax - tile.width // 2, ay - int(ccy)), tile)
        if a.urgency:
            ux, uy, ur = (int(v) for v in a.urgency.split(","))
            ured = tuple(int(v) for v in a.urgency_color.split(","))
            tile, pulse, ccy = draw_urgency(ur, ts, a.seconds, ured, a.urgency_text.split("|"), a.urgency_width)
            sc = 1 + 0.08 * pulse
            tile = tile.resize((int(tile.width * sc), int(tile.height * sc)), Image.LANCZOS)
            jx = int(round(4 * pulse * math.sin(ts * 90)))  # beat shake
            pil.paste(tile, (ux - tile.width // 2 + jx, uy - int(ccy * sc)), tile)
            # red edge pulse on every beat
            if pulse > 0.05:
                edge = Image.new("RGBA", pil.size, (0, 0, 0, 0))
                ed = ImageDraw.Draw(edge)
                m = int(min(W, H) * 0.06)
                ed.rectangle([0, 0, W, H], outline=ured + (int(170 * pulse),), width=m)
                edge = edge.filter(ImageFilter.GaussianBlur(m * 0.9))
                pil = pil.convert("RGBA"); pil.alpha_composite(edge); pil = pil.convert("RGB")
        # 5. push-in
        s = 1 + a.push * ease(t)
        cw, ch = W / s, H / s
        top = 0.0 if a.anchor == "top" else (H - ch) / 2
        box = ((W - cw) / 2, top, (W + cw) / 2, top + ch)
        out = pil.resize((OW, OH), Image.LANCZOS, box=box)
        proc.stdin.write(out.tobytes())
        if i % 30 == 0:
            print(f"  frame {i}/{N}", file=sys.stderr)
    proc.stdin.close()
    err = proc.stderr.read().decode(errors="ignore")
    if proc.wait() != 0:
        sys.exit("ffmpeg failed:\n" + err[-2000:])
    print("wrote", a.out)


if __name__ == "__main__":
    main()
