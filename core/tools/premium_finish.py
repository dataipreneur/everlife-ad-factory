"""EverlifeMD premium post-edit for a 9:16 video ad: 4 approved styles (Mitansh, 2026-11-02). 0 credits.

  champagne   bold  · centred · Avenir Next Heavy, tracked · champagne gold · navy wash end card, cream CTA pill
  blacklabel  bold  · centred · Helvetica Neue Condensed Black caps · bottle-label red (women: deep rose) · black end card
  subtle      calm  · left    · Futura Medium, one line · ice blue · bright frosted end card, outline CTA
  quietluxe   calm  · centred · Helvetica Neue Light tracked caps · warm sand · smoked-glass end card, outline CTA

usage (from the toolkit folder, $T):
  venv/bin/python -I premium_finish.py <job_dir> <clip.mp4> --style <name> [--out <file.mp4>] [--caps-auto]

<job_dir>/premium.json (all copy from the bible; the disclaimer is NEVER written here, it comes from product.json):
  {"product": "sermorelin-ghk", "audience": "men|women", "end": 11.0,
   "head": "SERMORELIN GHK", "sub": "DOUBLE STRENGTH" (optional),
   "end_label": "SERMORELIN GHK  ·  DOUBLE STRENGTH", "end_head": "Power Your Prime", "end_sub": "3-in-1 Sermorelin GHK",
   "benefits": ["..", "..", ".."], "cta": "EXPLORE SERMORELIN GHK",
   "bottle": "<render in the skill's assets/ or job source/>" (optional), "pill": "..." (optional, "" = none),
   "audio": "<job-relative audio file>" (optional; default = the clip's own audio),
   "caps": [[start, end, "Sentence case caption."], ...]}
--caps-auto: no "caps" yet → transcribe the clip (faster-whisper, product name as vocabulary), write sentence captions into
premium.json and STOP so they can be hand-checked (whisper misspells product names). Run again without the flag to render.
Layout: every element inside the 9:16 safe band y 144-1385 (x 156-924, minus the Reels profile notch); proof row 1290-1385; verbatim disclaimer at the bottom.
Output: <job_dir>/FINAL_<style>_9x16.mp4 unless --out.
"""
import argparse, json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, T)
import product as product_mod  # noqa: E402
import safezones as sz  # noqa: E402
import standard_footer as sf  # noqa: E402  (one trust-row + disclaimer size for every creative)
import imageio_ffmpeg  # noqa: E402

FF = imageio_ffmpeg.get_ffmpeg_exe()
STYLES = ("champagne", "blacklabel", "subtle", "quietluxe")
ap = argparse.ArgumentParser()
ap.add_argument("job"); ap.add_argument("clip")
ap.add_argument("--style", required=True, choices=STYLES)
ap.add_argument("--out", default="")
ap.add_argument("--caps-auto", action="store_true")
a = ap.parse_args()
J = os.path.abspath(a.job); CFG = os.path.join(J, "premium.json")
C = json.load(open(CFG))
P = product_mod.load(C["product"])
DISCLAIMER = P["disclaimer"]
WOMEN = C.get("audience", "men") == "women"


def clip_duration(p):
    s = subprocess.run([FF, "-i", p], capture_output=True, text=True).stderr.split("Duration: ")[1].split(",")[0]
    h, m, sec = s.split(":"); return float(h) * 3600 + float(m) * 60 + float(sec)


# ---------- captions ----------
if not C.get("caps"):
    if not a.caps_auto:
        sys.exit('❌ premium.json has no "caps": run once with --caps-auto, check the spellings, then run again.')
    from faster_whisper import WhisperModel
    wav = os.path.join(J, "_premium_caps.wav")
    subprocess.run([FF, "-loglevel", "error", "-y", "-i", os.path.join(J, C["audio"]) if C.get("audio") else a.clip,
                    "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    segs, _ = WhisperModel("small", compute_type="int8").transcribe(
        wav, word_timestamps=True, initial_prompt=f'{P["name"]} by Everlife.')
    caps, cur, st = [], [], None
    for sg in segs:
        for w in sg.words:
            if st is None: st = w.start
            cur.append(w.word.strip())
            if w.word.strip()[-1:] in ".?!," or len(cur) >= 7:
                caps.append([round(st, 2), round(w.end + 0.15, 2), " ".join(cur)]); cur, st = [], None
    if cur: caps.append([round(st, 2), round(w.end + 0.15, 2), " ".join(cur)])
    caps = [c for c in caps if c[0] < float(C.get("end", 11.0))]
    C["caps"] = caps; json.dump(C, open(CFG, "w"), indent=1)
    print("captions written to premium.json — CHECK SPELLINGS (product name!), then run again without --caps-auto:")
    for c in caps: print("  ", c)
    sys.exit(0)

END = float(C.get("end", 11.0)); CAPS = C["caps"]; NC = len(CAPS)
L = os.path.join(J, f"layers_{a.style}"); os.makedirs(L, exist_ok=True)
OUT = a.out or os.path.join(J, f"FINAL_{a.style}_9x16.mp4")
A = os.path.join(T, "assets")
W, H = 1080, 1920
SX0, SX1 = sz.SAFE[0], sz.SAFE[2]          # 156-924: text column (Reels side margins)
SW = SX1 - SX0                              # 768
DISC_BOTTOM = P.get("disclaimer_at") == "bottom" and not sz.BOTTOM_MODE   # product opt-in (Sermorelin GHK, PT-141...)
PROOF_Y = 1290 if DISC_BOTTOM else 1206    # proof row; with the disclaimer in the footer both end by y 1385
CAP_BOTTOM = min(sz.NOTCH[1] - 10, PROOF_Y - 12)   # captions + end card end above the Reels profile notch / proof row
SAFE_BOTTOM = CAP_BOTTOM
AV = "/System/Library/Fonts/Avenir Next.ttc"; HN = "/System/Library/Fonts/HelveticaNeue.ttc"
FU = "/System/Library/Fonts/Supplemental/Futura.ttc"
AV_HEAVY, AV_DEMI, AV_MED = 8, 2, 5
HN_REG, HN_CBOLD, HN_LIGHT, HN_CBLACK, HN_MED = 0, 4, 7, 9, 10
FU_MED, FU_BOLD = 0, 2


# ---------- renders ----------
def find_render(name):
    for d in (os.path.join(J, "source"), os.path.join(P["_dir"], "assets")):
        if name and os.path.exists(os.path.join(d, name)): return os.path.join(d, name)
    return None


bottle_name, pill_name = product_mod.renders_for(P, C)
BOTTLE = find_render(C.get("bottle") or bottle_name)
PILL = None if C.get("pill") == "" else find_render(C.get("pill") or pill_name)
if not BOTTLE: sys.exit("❌ bottle render not found (job source/ or the skill's assets/)")


# ---------- drawing helpers ----------
def F(path, idx, size): return ImageFont.truetype(path, size, index=idx)
def canvas(): return Image.new("RGBA", (W, H), (0, 0, 0, 0))
def tw(d, t, f, track=0.0): return sum(d.textlength(c, font=f) for c in t) + f.size * track * max(0, len(t) - 1)


def text(d, x, y, t, f, fill, track=0.0, anchor="l"):
    if anchor == "c": x = x - tw(d, t, f, track) / 2
    for ch in t:
        d.text((x, y), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + f.size * track
    return x


def fit(d, t, path, idx, size, maxw, track=0.0, floor=30):
    while size > floor and tw(d, t, F(path, idx, size), track) > maxw: size -= 2
    return F(path, idx, size)


def vgrad(img, y0, y1, a0, a1, rgb):
    d = ImageDraw.Draw(img)
    for y in range(y0, y1):
        t = (y - y0) / max(1, y1 - y0); d.line([(0, y), (W, y)], fill=tuple(rgb) + (int(a0 + (a1 - a0) * t),))


def logo(img, x, y, w, color=None, anchor="c"):
    lg = Image.open(f"{A}/logo_cream.png").convert("RGBA")
    lg = lg.resize((w, int(lg.height * w / lg.width)), Image.LANCZOS)
    if color:
        solid = Image.new("RGBA", lg.size, color); solid.putalpha(lg.split()[3]); lg = solid
    img.alpha_composite(lg, (int(x - w / 2) if anchor == "c" else int(x), int(y)))
    return y + lg.height


def wrap(d, t, f, maxw):
    out, cur = [], ""
    for w in t.split():
        s = (cur + " " + w).strip()
        if d.textlength(s, font=f) <= maxw: cur = s
        else: out.append(cur); cur = w
    return out + [cur]


def product_group(img, cx, y, bh, pill_w, glow):
    """glow + bottle (+ pill in front-left, the hero). Returns the bottom y."""
    g = Image.new("RGBA", (W + 600, bh + 520), (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse([cx, 200, cx + 600, bh + 300], fill=glow)
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(70)).crop((300, 0, 300 + W, bh + 520)), (0, int(y - 200)))
    b = Image.open(BOTTLE).convert("RGBA"); b = b.crop(b.getbbox())
    b = b.resize((int(b.width * bh / b.height), bh), Image.LANCZOS)
    if PILL:
        img.alpha_composite(b, (int(cx + 10), int(y)))
        t = Image.open(PILL).convert("RGBA"); t = t.crop(t.getbbox())
        t = t.resize((pill_w, int(t.height * pill_w / t.width)), Image.LANCZOS)
        img.alpha_composite(t, (int(cx - pill_w - 20), int(y + bh - t.height + 10)))
    else:
        img.alpha_composite(b, (int(cx - b.width / 2), int(y)))
    return y + bh


def bottom_layers(scrim_rgb=(6, 10, 14)):
    scr = canvas(); vgrad(scr, 960, 1300, 0, 175, scrim_rgb); vgrad(scr, 1300, 1920, 175, 230, scrim_rgb)
    scr.save(f"{L}/scrim.png")
    bot = canvas(); pr = sf.row_art(f"{A}/proof_row_clear.png")   # standard trust-row width (Justin 2026-11-02)
    bot.alpha_composite(pr, ((W - pr.width) // 2, PROOF_Y))
    d = ImageDraw.Draw(bot); fd = sf.disc_font()                     # standard disclaimer: 18 px, exactly 2 lines
    lines = sf.disclaimer_lines(DISCLAIMER)
    base = 1884 if DISC_BOTTOM else sz.SAFE[3] - 2
    step = sf.DISC_LH
    for i, ln in enumerate(lines):
        d.text(((W - d.textlength(ln, font=fd)) / 2, base - step * (len(lines) - i)), ln, font=fd, fill=(255, 255, 255, 190))
    if not DISC_BOTTOM and base - step * len(lines) < PROOF_Y + pr.height:
        sys.exit("❌ disclaimer does not fit between the proof row and y 1385")
    bot.save(f"{L}/bottom.png")


def save_checked(bg, fg, name):
    """Refuse to export when text/logo/CTA (alpha > 120) leaves the 9:16 safe area or enters the Reels notch."""
    m = fg.split()[3].point(lambda v: 255 if v > 120 else 0); box = m.getbbox()
    if box:
        probs = sz.violations(box, label=name)
        nx = m.crop(sz.NOTCH).getbbox()
        if nx: probs.append(f"{name} enters the Reels profile notch {sz.NOTCH}")
        if box[3] > SAFE_BOTTOM + 1 and name != "top": probs.append(f"{name} ends at y {box[3]}, below {SAFE_BOTTOM}")
        if probs: sys.exit("❌ safe-zone violation (fix the copy/layout, never override):\n  " + "\n  ".join(probs))
    Image.alpha_composite(bg, fg).save(f"{L}/{name}.png")


def captions(draw_one):
    for i, (_, _, t) in enumerate(CAPS):
        c = canvas(); draw_one(ImageDraw.Draw(c), t); save_checked(canvas(), c, f"cap{i}")


def centred_caption(d, t, path, idx, size, fill, track=0.0, upper=False, accent=None):
    t = t.upper() if upper else t
    f = fit(d, t, path, idx, size, SW, track, floor=40)
    lines = [t] if tw(d, t, f, track) <= SW else wrap(d, t, f, SW - 20)[:2]
    for k, ln in enumerate(lines):
        y = CAP_BOTTOM - int(f.size * 1.25) - (len(lines) - 1 - k) * int(f.size * 1.15)
        if accent and k == len(lines) - 1 and " " in ln:
            head, last = ln.rsplit(" ", 1); x = W / 2 - tw(d, ln, f, track) / 2
            x = text(d, x, y, head + " ", f, fill, track); text(d, x, y, last, f, accent, track)
        else:
            text(d, W / 2, y, ln, f, fill, track, "c")


def benefits_centred(d, by, font_, fill, bullet, step=52):
    for k, t in enumerate(C["benefits"][:3]):
        f = font_ if d.textlength(t, font=font_) <= SW - 40 else ImageFont.truetype(font_.path, int(font_.size * (SW - 40) / d.textlength(t, font=font_)), index=font_.index)
        yy = by + k * step; x0 = (W - d.textlength(t, font=f) - 40) / 2
        bullet(d, x0, yy); d.text((x0 + 40, yy), t, font=f, fill=fill)


# =====================================================================================
CREAM = (246, 241, 230, 255); WHITE = (255, 255, 255, 255); NAVY = (12, 28, 40, 255)
if a.style == "champagne":
    ACC = (214, 168, 150, 255) if WOMEN else (217, 191, 140, 255)  # women: rose gold
    bottom_layers()
    top = canvas(); TG = canvas(); vgrad(TG, 0, 560, 170, 0, (8, 18, 24)); d = ImageDraw.Draw(top)
    y = logo(top, W / 2, 150, 280)
    text(d, W / 2, y + 22, C["head"], fit(d, C["head"], AV, AV_HEAVY, 86, SW, 0.06), CREAM, 0.06, "c")
    if C.get("sub"):
        d.line([(W / 2 - 70, y + 148), (W / 2 + 70, y + 148)], fill=ACC, width=2)
        text(d, W / 2, y + 162, C["sub"], F(AV, AV_DEMI, 30), ACC, 0.32, "c")
    save_checked(TG, top, "top")
    captions(lambda d, t: centred_caption(d, t, AV, AV_DEMI, 50, CREAM))
    e = canvas(); EW = canvas(); vgrad(EW, 0, H, 200, 235, (10, 24, 33)); d = ImageDraw.Draw(e)
    y = logo(e, W / 2, 150, 250)
    text(d, W / 2, y + 24, C["end_label"], fit(d, C["end_label"], AV, AV_DEMI, 26, SW, 0.22), ACC, 0.22, "c")
    fh = fit(d, C["end_head"], AV, AV_HEAVY, 96, SW); text(d, W / 2, y + 62, C["end_head"], fh, CREAM, 0, "c")
    text(d, W / 2, y + 180, C["end_sub"], fit(d, C["end_sub"], AV, AV_MED, 46, SW), (246, 241, 230, 225), 0, "c")
    py = product_group(e, W / 2, y + 262, 360, 270, ACC[:3] + (80,))
    by = py + 45
    def chk(d, x, yy): d.line([(x, yy + 24), (x + 10, yy + 34), (x + 28, yy + 12)], fill=ACC, width=4, joint="curve")
    benefits_centred(d, by, F(AV, AV_MED, 36), CREAM, chk, 54)
    t = "Over 100,000 happy customers"; fp = F(AV, AV_MED, 28)
    d.text(((W - d.textlength(t, font=fp)) / 2, by + 178), t, font=fp, fill=(246, 241, 230, 190))
    fc = fit(d, C["cta"], AV, AV_DEMI, 38, SW, 0.08); cw = tw(d, C["cta"], fc, 0.08) + 110; cy = by + 225; ch = 82
    d.rounded_rectangle([(W - cw) / 2, cy, (W + cw) / 2, cy + ch], radius=41, fill=CREAM)
    text(d, W / 2, cy + 16, C["cta"], fc, (14, 30, 40, 255), 0.08, "c")
    GRADE = "eq=contrast=1.06:saturation=1.06:gamma=0.98,colorbalance=rs=0.03:bs=-0.03,vignette=PI/5"

elif a.style == "blacklabel":
    ACC = (180, 62, 92, 255) if WOMEN else (206, 38, 46, 255)  # women: deep rose
    bottom_layers()
    top = canvas(); TG = canvas(); vgrad(TG, 0, 600, 190, 0, (6, 6, 8)); d = ImageDraw.Draw(top)
    y = logo(top, W / 2, 150, 230)
    f = fit(d, C["head"], HN, HN_CBLACK, 132, SW, 0.01); text(d, W / 2, y + 12, C["head"], f, WHITE, 0.01, "c")
    ry = y + 12 + f.size + 14; d.rectangle([W / 2 - 230, ry, W / 2 + 230, ry + 4], fill=ACC)
    if C.get("sub"): text(d, W / 2, ry + 18, C["sub"], F(HN, HN_MED, 30), WHITE, 0.42, "c")
    save_checked(TG, top, "top")
    captions(lambda d, t: centred_caption(d, t, HN, HN_CBOLD, 60, WHITE, 0.03, upper=True, accent=ACC))
    e = canvas(); EW = canvas(); vgrad(EW, 0, H, 225, 245, (8, 8, 10)); d = ImageDraw.Draw(e)
    y = logo(e, W / 2, 150, 210)
    text(d, W / 2, y + 22, C["end_label"].upper(), fit(d, C["end_label"].upper(), HN, HN_MED, 24, SW, 0.32), ACC, 0.32, "c")
    T_ = C["end_head"].upper(); f = fit(d, T_, HN, HN_CBLACK, 128, SW, 0.01)
    text(d, W / 2, y + 58, T_, f, WHITE, 0.01, "c")
    text(d, W / 2, y + 66 + f.size, C["end_sub"], fit(d, C["end_sub"], HN, HN_LIGHT, 44, SW), (255, 255, 255, 220), 0, "c")
    py = product_group(e, W / 2, y + 150 + f.size, 380, 280, ACC[:3] + (60,))
    by = py + 40
    def sq(d, x, yy): d.rectangle([x + 10, yy + 15, x + 22, yy + 27], fill=ACC)
    benefits_centred(d, by, F(HN, HN_MED, 35), WHITE, sq, 52)
    t = "Over 100,000 happy customers"; fp = F(HN, HN_REG, 27)
    d.text(((W - d.textlength(t, font=fp)) / 2, by + 168), t, font=fp, fill=(255, 255, 255, 190))
    fc = fit(d, C["cta"], HN, HN_CBOLD, 40, SW, 0.06); cw = tw(d, C["cta"], fc, 0.06) + 120; cy = by + 214; ch = 84
    d.rounded_rectangle([(W - cw) / 2, cy, (W + cw) / 2, cy + ch], radius=10, fill=ACC)
    text(d, W / 2, cy + 18, C["cta"], fc, WHITE, 0.06, "c")
    GRADE = "eq=contrast=1.10:saturation=0.92:gamma=0.97,colorbalance=rs=0.02:bs=0.01,vignette=PI/4.5"

elif a.style == "subtle":
    ICE = (232, 190, 190, 235) if WOMEN else (170, 222, 238, 235)  # women: blush
    ICE_D = (176, 96, 110, 255) if WOMEN else (40, 120, 150, 255)
    SUBC = (248, 226, 226, 255) if WOMEN else (225, 242, 248, 255)
    X = SX0
    bottom_layers()
    top = canvas(); TG = canvas(); vgrad(TG, 0, 470, 125, 0, (6, 14, 20)); d = ImageDraw.Draw(top)
    y = logo(top, X, 150, 200, anchor="l")
    head = C.get("head_display") or C["head"]
    if head.isupper():  # sentence/title case reads calmer; keep product casing from product.json
        head = head.title()
        for kc in P.get("keep_case", []): head = head.replace(kc.title(), kc)
    f = fit(d, head, FU, FU_MED, 68, SW, floor=52); hy = y + 20
    d.text((X, hy), head, font=f, fill=(255, 255, 255, 245))
    ly = hy + f.size + 22; d.rectangle([X, ly, X + 56, ly + 2], fill=ICE)
    if C.get("sub"): text(d, X + 74, ly - 12, C["sub"], F(FU, FU_MED, 25), SUBC, 0.32)
    save_checked(TG, top, "top")
    def cap_subtle(d, t):
        f = fit(d, t, FU, FU_MED, 42, SW - 38, floor=36)
        lines = [t] if d.textlength(t, font=f) <= SW - 38 else wrap(d, t, f, SW - 38)[:2]
        for k, ln in enumerate(lines):
            yy = CAP_BOTTOM - int(f.size * 1.3) - (len(lines) - 1 - k) * int(f.size * 1.2)
            if k == 0: d.rectangle([X, yy + 22, X + 22, yy + 24], fill=ICE)
            d.text((X + 38, yy), ln, font=f, fill=(255, 255, 255, 240))
    captions(cap_subtle)
    e = canvas(); EW = canvas(); vgrad(EW, 0, 1262, 212, 226, (240, 246, 248)); vgrad(EW, 1262, 1920, 225, 240, (10, 22, 30))
    ImageDraw.Draw(EW).rectangle([0, 1261, W, 1262], fill=ICE); d = ImageDraw.Draw(e)
    y = logo(e, X, 150, 180, color=NAVY, anchor="l")
    text(d, X, y + 24, C["end_label"].upper(), fit(d, C["end_label"].upper(), FU, FU_MED, 21, SW, 0.30), ICE_D, 0.30)
    f = fit(d, C["end_head"], FU, FU_MED, 76, SW); d.text((X, y + 58), C["end_head"], font=f, fill=NAVY)
    sy = y + 58 + f.size + 12; d.text((X, sy), C["end_sub"], font=fit(d, C["end_sub"], FU, FU_MED, 34, SW), fill=(12, 28, 40, 185))
    py = product_group(e, W / 2 + 40, sy + 80, 290, 200, ICE[:3] + (110,))
    by = py + 50; d.line([(X, by - 22), (SX1, by - 22)], fill=(12, 28, 40, 45), width=1)
    for k, t in enumerate(C["benefits"][:3]):
        yy2 = by + k * 50
        d.line([(X, yy2 + 20), (X + 8, yy2 + 28), (X + 24, yy2 + 10)], fill=ICE_D, width=3, joint="curve")
        d.text((X + 40, yy2), t, font=fit(d, t, FU, FU_MED, 32, SW - 40), fill=(12, 28, 40, 235))
    d.text((X, by + 160), "Over 100,000 happy customers", font=F(FU, FU_MED, 26), fill=(12, 28, 40, 170))
    fc = fit(d, C["cta"], FU, FU_MED, 30, SW - 90, 0.10); cw = tw(d, C["cta"], fc, 0.10) + 90; cy = by + 206; ch = 68
    d.rounded_rectangle([X, cy, X + cw, cy + ch], radius=34, outline=NAVY, width=2)
    text(d, X + 45, cy + 17, C["cta"], fc, NAVY, 0.10)
    GRADE = "eq=contrast=1.02:saturation=1.04:brightness=0.02,colorbalance=bs=0.02,vignette=PI/7"

elif a.style == "quietluxe":
    SAND = (218, 200, 170, 255); SAND_HI = (236, 222, 198, 255); SOFT = (255, 255, 255, 235)
    bottom_layers((10, 10, 12))
    top = canvas(); TG = canvas(); vgrad(TG, 0, 480, 130, 0, (10, 10, 12)); d = ImageDraw.Draw(top)
    y = logo(top, W / 2, 150, 190)
    f = fit(d, C["head"], HN, HN_LIGHT, 60, SW, 0.16, floor=52); text(d, W / 2, y + 22, C["head"], f, SOFT, 0.16, "c")
    ly = y + 22 + f.size + 22; d.rectangle([W / 2 - 34, ly, W / 2 + 34, ly + 1], fill=SAND)
    if C.get("sub"): text(d, W / 2, ly + 14, C["sub"].title(), F(HN, HN_MED, 28), SAND_HI, 0.10, "c")
    save_checked(TG, top, "top")
    captions(lambda d, t: centred_caption(d, t, HN, HN_REG, 44, SOFT, 0.01))
    e = canvas(); EW = canvas(); vgrad(EW, 0, H, 175, 215, (14, 14, 16)); d = ImageDraw.Draw(e)
    y = logo(e, W / 2, 150, 170)
    text(d, W / 2, y + 24, C["end_label"].upper(), fit(d, C["end_label"].upper(), HN, HN_REG, 21, SW, 0.30), SAND, 0.30, "c")
    f = fit(d, C["end_head"], HN, HN_LIGHT, 80, SW, 0.01); text(d, W / 2, y + 58, C["end_head"], f, SOFT, 0.01, "c")
    sy = y + 58 + f.size + 12; text(d, W / 2, sy, C["end_sub"], fit(d, C["end_sub"], HN, HN_REG, 32, SW), (255, 255, 255, 200), 0.02, "c")
    py = product_group(e, W / 2, sy + 80, 290, 200, SAND[:3] + (55,))
    by = py + 46
    def dot(d, x, yy): d.ellipse([x + 14, yy + 16, x + 22, yy + 24], fill=SAND)
    benefits_centred(d, by, F(HN, HN_REG, 32), SOFT, dot, 50)
    t = "Over 100,000 happy customers"; fp = F(HN, HN_REG, 26)
    d.text(((W - d.textlength(t, font=fp)) / 2, by + 160), t, font=fp, fill=(255, 255, 255, 175))
    fc = fit(d, C["cta"], HN, HN_MED, 30, SW, 0.14); cw = tw(d, C["cta"], fc, 0.14) + 96; cy = by + 206; ch = 68
    d.rounded_rectangle([(W - cw) / 2, cy, (W + cw) / 2, cy + ch], radius=34, outline=SAND, width=2)
    text(d, W / 2, cy + 17, C["cta"], fc, SOFT, 0.14, "c")
    GRADE = "eq=contrast=1.03:saturation=0.96:brightness=0.01,colorbalance=rs=0.025:gs=0.01:bs=-0.02,vignette=PI/6"

if cy + ch > SAFE_BOTTOM:
    sys.exit(f"❌ end card CTA ends at y {cy + ch}, below {SAFE_BOTTOM} (safe area / Reels notch). Shorten benefits/headline.")
save_checked(EW, e, "end")

# ---------- compose ----------
grade = f"scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,unsharp=5:5:0.6,{GRADE}"
AUD = C.get("audio")
inputs = ["-i", a.clip]
for p in ["bottom", "top"] + [f"cap{i}" for i in range(NC)] + ["end", "scrim"]:
    inputs += ["-loop", "1", "-i", f"{L}/{p}.png"]
if AUD: inputs += ["-i", os.path.join(J, AUD)]
fc = (f"[0:v]{grade},split[v][vb];[vb]boxblur=22:2[blur];[v][blur]overlay=enable='gte(t,{END})'[v1];"
      f"[1:v]format=rgba[bot];[{4 + NC}:v]format=rgba[scr];[2:v]format=rgba,fade=out:st={END - 0.3}:d=0.3:alpha=1[top];")
for i, (s, e_, _) in enumerate(CAPS):
    fc += f"[{3 + i}:v]format=rgba,fade=in:st={s}:d=0.2:alpha=1,fade=out:st={min(e_, END) - 0.2}:d=0.2:alpha=1[c{i}];"
fc += f"[{3 + NC}:v]format=rgba,fade=in:st={END}:d=0.4:alpha=1[end];[v1][scr]overlay[v2];[v2][top]overlay[k0];"
for i in range(NC): fc += f"[k{i}][c{i}]overlay[k{i + 1}];"
fc += f"[k{NC}][end]overlay=enable='gte(t,{END})'[e];[e][bot]overlay,format=yuv420p[out]"
D = clip_duration(a.clip)
subprocess.run([FF, "-loglevel", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[out]", "-map",
                (f"{5 + NC}:a" if AUD else "0:a"), "-t", f"{D:.2f}", "-c:v", "libx264", "-crf", "17", "-preset", "slow",
                "-r", "30", "-c:a", "aac", "-b:a", "192k", OUT], check=True)
print(f"done {OUT}  (style={a.style}, product={P['id']}, audience={'women' if WOMEN else 'men'}, end card at {END}s)")
