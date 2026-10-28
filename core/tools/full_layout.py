"""EverlifeMD post-generation edit for a 9:16 video ad (the approved house layout).

  full frame  the whole generated video stays visible; no boxes over the talent
  top         Everlife logo + headline + subline over a soft fade
  lower third one word-timed caption line (from the clip's own voice, via whisper)
  bottom      Trustpilot 4.9 Excellent / Doctor Prescribed / Ships Free row on a transparent
              background + the product's verbatim disclaimer; stays on through the end card
  end card    from end_t: headline, real bottle + pill renders, 3 benefits, 100,000+ line, CTA

usage:
  venv/bin/python -I full_layout.py <project_dir> <clip.mp4> <tag> [--end 12.8] [--mirror-until 6.46]

<project_dir>/copy.json holds the product copy (all of it must come from the bible / brief):
  {"product": "<id, e.g. restora-z>", "head": ["LINE 1", "LINE 2"], "sub": "...", "end_head": ["...", "..."],
   "benefits": ["..", "..", ".."], "cta": "EXPLORE ...", "vocab": "product names to help whisper"}
Everything product-specific (verbatim disclaimer, renders, name casing, review highlight, reviews file) comes from the
product's skills/everlife-<id>/product.json (see product.py). copy.json may repeat the disclaimer only verbatim, and may
name other renders with "bottle"/"pill".
<project_dir>/source/ holds the bottle and pill renders; missing ones are copied from the product's skill assets.
Output: <project_dir>/out/<tag>_15s_9x16.mp4
"""
import argparse, json, os, shutil, subprocess, sys
from PIL import Image, ImageDraw

T = os.path.dirname(os.path.abspath(__file__))
import imageio_ffmpeg  # noqa: E402  (bundled ffmpeg, works on any Mac/Python)
FF = imageio_ffmpeg.get_ffmpeg_exe()

ap = argparse.ArgumentParser()
ap.add_argument("project")
ap.add_argument("clip")
ap.add_argument("tag")
ap.add_argument("--end", type=float, default=12.8, help="end card start (s)")
ap.add_argument("--mirror-until", type=float, default=0, help="un-mirror selfie shots before this time (s)")
ap.add_argument("--zoom", type=float, default=1.0, help="punch in, anchored to the top (hides junk at the bottom of frame)")
ap.add_argument("--reviews", default="", help="review-burst insert: comma list of review ids from reviews.json, e.g. R1,R3,R4,R2")
ap.add_argument("--reviews-at", type=float, default=9.5, help="review burst start (s)")
ap.add_argument("--reviews-dur", type=float, default=2.4, help="review burst length (s)")
ap.add_argument("--reviews-json", default="", help="default: the product's reviews file (product.json \"reviews\")")
a = ap.parse_args()
P = os.path.abspath(a.project)

# shared brand assets -> project source/
os.makedirs(f"{P}/source", exist_ok=True)
for f in ("logo_cream.png", "proof_row_clear.png"):
    if not os.path.exists(f"{P}/source/{f}"):
        shutil.copy(f"{T}/assets/{f}", f"{P}/source/{f}")

sys.argv = [sys.argv[0], P]
sys.path.insert(0, T)
import build_layers as bl  # noqa: E402
import product  # noqa: E402

C = json.load(open(f"{P}/copy.json"))
PR = product.for_copy(C, f"{P}/copy.json")
C["disclaimer"] = PR["disclaimer"]
C.setdefault("bottle", PR["renders"]["bottle"])
C.setdefault("pill", PR["renders"]["pill"])
C["keep_case"] = PR["keep_case"]
for f in (C["bottle"], C["pill"]):
    if not os.path.exists(f"{P}/source/{f}"):
        shutil.copy(product.asset(PR, f), f"{P}/source/{f}")
bl.END_HEAD, bl.BENEFITS, bl.CTA_TEXT = C["end_head"], C["benefits"], C["cta"]
bl.DISCLAIMER, bl.BOTTLE, bl.PILL = C["disclaimer"], C["bottle"], C["pill"]
REVIEWS_JSON = os.path.expanduser(a.reviews_json or product.path(PR, PR["reviews"]))

L = f"{P}/layers_full"
os.makedirs(L, exist_ok=True)
os.makedirs(f"{P}/out", exist_ok=True)
W, H = 1080, 1920
HEAD = bl.font(bl.AV_COND, 66, "Heavy Italic")
SUB = bl.font(bl.AV_COND, 36, "Demi Bold Italic")
CAP = bl.font(bl.AV_COND, 48, "Heavy")
DISC = bl.font(bl.AV, 21, "Medium")


# --- 1. captions from the clip's own audio (max 4 words, break on punctuation)
def captions():
    cache = f"{L}/{a.tag}_caps.json"
    if os.path.exists(cache) and os.path.getmtime(cache) > os.path.getmtime(a.clip):
        return json.load(open(cache))
    wav = f"{L}/{a.tag}.wav"
    subprocess.run([FF, "-v", "error", "-y", "-i", a.clip, "-ac", "1", "-ar", "16000", wav], check=True)
    from faster_whisper import WhisperModel
    words = []
    for seg in WhisperModel("small", compute_type="int8").transcribe(
            wav, word_timestamps=True, initial_prompt=C.get("vocab", ""))[0]:
        words += seg.words
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) == 4 or w.word.strip()[-1:] in ".,?!":
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    caps = []
    for c in chunks:
        text = "".join(w.word for w in c).strip()
        s, e = c[0].start, c[-1].end + 0.15
        if caps:
            s = max(s, caps[-1][1])
        if a.end - s > 0.8:  # skip a line the end card would cut off
            wt = [[round(float(w.start), 2), round(float(w.end), 2)] for w in c]  # per-word timing
            caps.append([round(float(s), 2), round(float(min(e, a.end)), 2), text.upper(), wt])
    json.dump(caps, open(cache, "w"), indent=1)
    return caps


# --- 2. layers (every text element stays inside the Meta 9:16 safe area: see safezones.py)
import safezones as sz  # noqa: E402

SX0, SY0, SX1, SY1 = sz.SAFE
SAFE_W = sz.SAFE_W
BLOCK_BOTTOM = sz.FOOTER_BOTTOM          # proof row + disclaimer end (bottom of frame by default; see safezones.PROOF_AT)
SAFE_ISSUES = []


def note(box, label):
    SAFE_ISSUES.extend(sz.violations(box, label=label))


def fit(text, path, size, name, maxw):
    f = bl.font(path, size, name)
    d0 = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    while d0.textlength(text, font=f) > maxw and size > 20:
        size -= 2
        f = bl.font(path, size, name)
    return f


def block_layout():
    """Positions of the bottom proof block inside the safe area: (row_y, disc_y, block_top)."""
    d0 = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    lines = bl.wrap(d0, bl.DISCLAIMER, DISC, sz.FOOT_W)
    row = Image.open(f"{P}/source/proof_row_clear.png")
    rh = int(row.height * sz.FOOT_W / row.width)
    top = BLOCK_BOTTOM - (rh + 12 + 27 * len(lines))
    return top, top + rh + 12, top, lines, rh


def top_layer():
    img = bl.canvas()
    bl.gradient_band(img, 0, 520, 190, 0)
    bl.logo(img, SY0 + 8, 280)
    note(((W - 280) / 2, SY0 + 8, (W + 280) / 2, SY0 + 48), "logo")
    d = ImageDraw.Draw(img)
    y = 210
    for ln in C["head"]:
        f = fit(ln, bl.AV_COND, 66, "Heavy Italic", SAFE_W)
        bl.centered(d, y, ln, f, bl.GOLD)
        note(((W - d.textlength(ln, font=f)) / 2, y, (W + d.textlength(ln, font=f)) / 2, y + f.size), "headline")
        y += int(f.size * 1.03)
    if C.get("sub"):
        f = fit(C["sub"], bl.AV_COND, 36, "Demi Bold Italic", SAFE_W)
        bl.centered(d, y + 12, C["sub"], f, bl.CREAM)
        note(((W - d.textlength(C["sub"], font=f)) / 2, y + 12, (W + d.textlength(C["sub"], font=f)) / 2, y + 12 + f.size), "sub")
    return img


def bottom_layer():
    img = bl.canvas()
    row_y, disc_y, top, lines, rh = block_layout()
    bl.gradient_band(img, top - 380, H, 0, 225)
    row = Image.open(f"{P}/source/proof_row_clear.png").convert("RGBA")
    row = row.resize((sz.FOOT_W, rh), Image.LANCZOS)
    img.alpha_composite(row, (sz.FOOT_X0, row_y))
    note((sz.FOOT_X0, row_y, sz.FOOT_X0 + sz.FOOT_W, row_y + rh), "proof row")
    d = ImageDraw.Draw(img)
    ty = disc_y
    for ln in lines:
        bl.centered(d, ty, ln, DISC, (236, 236, 232))
        ty += 27
    note((sz.FOOT_X0, disc_y, W - sz.FOOT_X0, ty), "disclaimer")
    return img


def cap_y():
    return block_layout()[2] - 96   # caption line sits just above the proof block


def caption(text):
    img = bl.canvas()
    d = ImageDraw.Draw(img)
    f = fit(text, bl.AV_COND, 48, "Heavy", SAFE_W - 44)
    w = d.textlength(text, font=f)
    y = cap_y()
    d.rounded_rectangle([(W - w) / 2 - 22, y, (W + w) / 2 + 22, y + 66], 18, fill=(255, 255, 255, 240))
    bl.centered(d, y + 3, text, f, bl.NAVY)
    note(((W - w) / 2 - 22, y, (W + w) / 2 + 22, y + 66), f"caption '{text[:20]}'")
    return img


def end_layer():
    real = bl.proof_block
    bl.proof_block = lambda img, **k: 1040  # the proof row lives in the bottom layer instead
    try:
        return bl.endcard()
    finally:
        bl.proof_block = real


ING_T = bl.font(bl.AV_COND, 38, "Heavy")
ING_B = bl.font(bl.AV, 25, "Demi Bold")
ING_LABEL = bl.font(bl.AV_COND, 40, "Heavy Italic")


def paste_render(img, name, size, box_center, by="height"):
    r = Image.open(f"{P}/source/{name}").convert("RGBA")
    r = r.crop(r.getbbox())
    if by == "height":
        r = r.resize((int(r.width * size / r.height), size), Image.LANCZOS)
    else:
        r = r.resize((size, int(r.height * size / r.width)), Image.LANCZOS)
    img.alpha_composite(r, (box_center[0] - r.width // 2, box_center[1] - r.height // 2))


def ingredient_end_layers():
    """End card that names the formula: product, '3-in-1' label, one card per ingredient with its own
    bible claim, proof line and CTA, all inside the 9:16 safe area. Returns (base, [card1, card2, card3])."""
    from PIL import ImageFilter
    base = bl.canvas()
    base.alpha_composite(Image.new("RGBA", (W, H), bl.NAVY + (246,)))
    glow = bl.canvas()
    ImageDraw.Draw(glow).ellipse([200, 300, 880, 720], fill=bl.TEAL + (120,))
    base.alpha_composite(glow.filter(ImageFilter.GaussianBlur(110)))
    d = ImageDraw.Draw(base)
    bl.logo(base, SY0 + 8, 260)
    y = 205
    for ln in C["end_head"]:
        f = fit(ln, bl.AV_COND, 70, "Heavy Italic", SAFE_W)
        bl.centered(d, y, ln, f, bl.GOLD)
        note(((W - d.textlength(ln, font=f)) / 2, y, (W + d.textlength(ln, font=f)) / 2, y + f.size), "end headline")
        y += int(f.size * 1.02)
    paste_render(base, C["bottle"], 300, (W // 2 + 100, y + 175))
    paste_render(base, C["pill"], 300, (W // 2 - 120, y + 235), by="width")
    ly = y + 350
    bl.centered(d, ly, C["ingredients_label"], ING_LABEL, bl.GOLD)
    cy0 = ly + 56
    ch = 150
    cust_y = cy0 + ch + 18
    bl.centered(d, cust_y, "Over 100,000 happy customers", bl.PROOF_S, bl.CREAM)
    cw2 = 560
    cta_y = cust_y + 42
    d.rounded_rectangle([(W - cw2) / 2, cta_y, (W + cw2) / 2, cta_y + 72], 36, fill=bl.GOLD)
    cf = fit(C["cta"], bl.AV_COND, 50, "Heavy", cw2 - 40)
    bl.centered(d, cta_y + (72 - cf.size) // 2 - 4, C["cta"], cf, bl.NAVY)
    note(((W - cw2) / 2, cta_y, (W + cw2) / 2, cta_y + 72), "CTA")
    if cta_y + 72 > block_layout()[2] - 8:
        SAFE_ISSUES.append(f"end card CTA ({cta_y + 72}) collides with the proof block ({block_layout()[2]})")

    cards = []
    gap = 12
    cw = (SAFE_W - 2 * gap) // 3
    nf = bl.font(bl.AV_COND, 32, "Heavy")
    for i, (name, claim) in enumerate(C["ingredients"]):
        img = bl.canvas()
        cd = ImageDraw.Draw(img)
        x = SX0 + i * (cw + gap)
        cd.rounded_rectangle([x, cy0, x + cw, cy0 + ch], 20, fill=(250, 249, 244, 246))
        cd.ellipse([x + cw // 2 - 8, cy0 + 14, x + cw // 2 + 8, cy0 + 30], fill=bl.TEAL)
        f = fit(name, bl.AV_COND, 32, "Heavy", cw - 20)
        cd.text((x + (cw - cd.textlength(name, font=f)) / 2, cy0 + 38), name, font=f, fill=bl.NAVY)
        ty = cy0 + 84
        for ln in bl.wrap(cd, claim, bl.font(bl.AV, 22, "Demi Bold"), cw - 22)[:2]:
            lf = bl.font(bl.AV, 22, "Demi Bold")
            cd.text((x + (cw - cd.textlength(ln, font=lf)) / 2, ty), ln, font=lf, fill=(70, 78, 92))
            ty += 28
        note((x, cy0, x + cw, cy0 + ch), f"ingredient card {i+1}")
        cards.append(img)
    return base, cards

caps = captions()
print("captions:", *[c[:3] for c in caps], sep="\n  ")
STYLE = C.get("style", "default")
bottom_layer().save(f"{L}/bottom.png")
if STYLE == "default":
    top_layer().save(f"{L}/top.png")
    end_layers = [("end.png", a.end, 99)]
    if C.get("ingredients"):
        base, cards = ingredient_end_layers()
        base.save(f"{L}/end.png")
        for i, c in enumerate(cards):
            c.save(f"{L}/end_ing{i}.png")
            end_layers.append((f"end_ing{i}.png", round(a.end + 0.25 + 0.3 * i, 2), 99))
    else:
        end_layer().save(f"{L}/end.png")
    cap_layers = []
    for i, c in enumerate(caps):
        caption(c[2]).save(f"{L}/cap_{a.tag}_{i}.png")
        cap_layers.append((f"cap_{a.tag}_{i}.png", c[0], c[1]))
else:
    import styles  # alternative looks: "tiktok", "editorial"
    st = styles.make(STYLE, bl, C, P, a.end)
    st.cap_y, st.block_top = cap_y(), block_layout()[2]
    st.top().save(f"{L}/top.png")
    end_layers = st.end_layers(L)
    cap_layers = st.caption_layers(caps, L, a.tag)
    SAFE_ISSUES.extend(st.issues)

# --- 3. composite
# keep the headline off faces: hide it while a head would sit under it (heads tracked with OpenCV)
top_segments = [(0.0, a.end)]
try:
    import faces
    import numpy as np
    _al = np.asarray(Image.open(f"{L}/top.png").split()[-1])
    _ys, _xs = np.where((_al > 200).sum(1) > 0)[0], np.where((_al > 200).sum(0) > 0)[0]
    if len(_ys):
        _box = (int(_xs.min()), int(_ys.min()), int(_xs.max()), int(_ys.max()))
        _blocked = [w for w in faces.blocked_windows(faces.heads(a.clip, FF, zoom=a.zoom), _box) if w[0] < a.end]
        for s0, e0 in _blocked:
            nxt = []
            for s1, e1 in top_segments:
                if e0 <= s1 or s0 >= e1:
                    nxt.append((s1, e1))
                else:
                    if s0 > s1: nxt.append((s1, s0))
                    if e0 < e1: nxt.append((e0, e1))
            top_segments = [(round(x, 2), round(y, 2)) for x, y in nxt if y - x > 0.3]
        if _blocked:
            print("headline hidden over faces:", _blocked)
except ImportError:
    print("NOTE: faces.py/opencv missing; headline not face-checked")
layers = [("top.png", s_, e_) for s_, e_ in top_segments] + cap_layers
burst = None
if a.reviews:
    # verbatim Trustpilot review cards slamming in (covers the video + captions for ~dur s; proof bar stays on top)
    import review_burst
    review_burst.HIGHLIGHT = PR["review_highlight"]
    R = json.load(open(REVIEWS_JSON))
    bdir = f"{L}/review_burst"
    shutil.rmtree(bdir, ignore_errors=True)
    nfr = review_burst.render(R, a.reviews.split(","), bdir, 1080, 1920, 24, a.reviews_dur)
    burst = ("@burst", a.reviews_at, a.reviews_at + nfr / 24)
    layers.append(burst)
# bottom mode: the end card was laid out for the old (higher) proof block, so move it down to sit centred
# between the logo and the proof block instead of leaving a dead gap above the footer
END_DY = int((BLOCK_BOTTOM - (sz.NOTCH[1] - 10)) * 0.5) if sz.BOTTOM_MODE else 0
end_names = {f for f, _, _ in end_layers}
END_BG = end_layers[0][0] if end_layers else None          # the opaque card background (+ logo + content)
LOGO_H = SY0 + 70                                         # logo strip stays pinned at the top
if END_DY and END_BG:
    # rebuild the card: logo strip unchanged, then the card's own background stretched to fill the gap, then the content
    _c = Image.open(f"{L}/{END_BG}").convert("RGBA")
    _n = _c.copy()
    # stretch a plain-background strip: the one under the logo unless type runs through it (a long end headline),
    # else the nearest clean strip below (a strip with letters in it would stretch into vertical bars)
    import numpy as np
    _a = np.asarray(_c.convert("RGB"), dtype=np.int16)
    _fy = next((y for y in range(LOGO_H, LOGO_H + 400) if np.abs(np.diff(_a[y:y + 6], axis=1)).max() <= 12), LOGO_H)
    _fill = _c.crop((0, _fy, W, _fy + 6)).resize((W, END_DY), Image.BILINEAR)
    _n.paste(_fill, (0, LOGO_H))
    _n.paste(_c.crop((0, LOGO_H, W, H - END_DY)), (0, LOGO_H + END_DY))
    _n.save(f"{L}/end_shifted.png")
    end_layers[0] = ("end_shifted.png",) + tuple(end_layers[0][1:])
    end_names = {f for f, _, _ in end_layers[1:]}       # the transparent pop-in layers just move down
layers += end_layers + [("bottom.png", 0, 99)]
cmd = [FF, "-v", "error", "-y", "-i", a.clip]
for f, s, _ in layers:
    if f == "@burst":
        cmd += ["-framerate", "24", "-itsoffset", str(s), "-i", f"{L}/review_burst/%03d.png"]
    else:
        cmd += ["-i", f"{L}/{f}"]
zw, zh = int(1080 * a.zoom) // 2 * 2, int(1920 * a.zoom) // 2 * 2
fc = f"[0:v]scale={zw}:{zh}:flags=lanczos,crop=1080:1920:(iw-1080)/2:0,unsharp=5:5:0.6,setsar=1[sc]"
if a.mirror_until:
    fc += f";[sc]split[x][y];[y]hflip[yf];[x][yf]overlay=0:0:enable='lt(t,{a.mirror_until})'[v0]"
else:
    fc += ";[sc]null[v0]"
for i, (f, s, e) in enumerate(layers, 1):
    extra = ":eof_action=pass" if f == "@burst" else ""
    src = f"[{i}:v]"
    oy = END_DY if f in end_names else 0
    fc += f";[v{i-1}]{src}overlay=0:{oy}:enable='between(t,{s},{e})'{extra}[v{i}]"
out = f"{P}/out/{a.tag}_15s_9x16.mp4"
cmd += ["-filter_complex", fc, "-map", f"[v{len(layers)}]", "-map", "0:a?", "-c:v", "libx264", "-crf", "18",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out]
if SAFE_ISSUES:
    print("SAFE-ZONE VIOLATIONS (not exported):", *sorted(set(SAFE_ISSUES)), sep="\n  ")
    raise SystemExit(3)
subprocess.run(cmd, check=True)
print("done", out)
