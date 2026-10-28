"""Put the REAL product renders into an AI-generated EMPTY scene (the image model never draws the product).
usage: composite.py <scene.png> <out.png> [--ratio 4:5|1:1|9:16] [--x 0.5] [--base 0.78] [--height 0.34]
                    [--capsule right|left|none] [--light left|right] [--bottle PNG] [--pill PNG]
  --base    where the bottle's base sits (fraction of frame height: the tabletop/surface line)
  --height  bottle height as a fraction of frame height
Adds a contact shadow, a soft cast shadow away from the light, a light colour/brightness match and grain,
so the product sits in the scene. Label pixels stay exactly the approved render."""
import argparse, os
import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
# renders default to the product skill named by EVERLIFE_SKILL_DIR (its product.env BOTTLE/PILL); else Restora-Z
SKILL_DIR = os.path.expanduser(os.environ.get("EVERLIFE_SKILL_DIR", "~/.claude/skills/everlife-restora-z"))
SKILL_ASSETS = f"{SKILL_DIR}/assets"
ENV = {}
if os.path.exists(f"{SKILL_DIR}/product.env"):
    for ln in open(f"{SKILL_DIR}/product.env"):
        k, _, v = ln.split("#")[0].partition("=")
        if v.strip():
            ENV[k.strip()] = v.strip().strip('"')
SIZES = {"1:1": (1080, 1080), "4:5": (1080, 1350), "9:16": (1080, 1920)}


def match(prod, scene_rgb, strength=0.10):
    """Nudge the product toward the scene's light: brightness ratio (clamped) + a light colour cast."""
    a = prod.split()[-1]
    p = np.asarray(prod.convert("RGB"), np.float32)
    s = np.asarray(scene_rgb, np.float32).reshape(-1, 3)
    s_mean = s.mean(0)
    s_l = float((s_mean * [0.299, 0.587, 0.114]).sum())
    k = np.clip(s_l / 150.0, 0.86, 1.06)
    cast = s_mean / max(1.0, s_mean.mean())
    p = p * k * (1 - strength + strength * cast)
    out = Image.fromarray(np.clip(p, 0, 255).astype(np.uint8)).convert("RGBA")
    out.putalpha(a)
    return out


def grain(img, sigma=3.0):
    a = img.split()[-1]
    p = np.asarray(img.convert("RGB"), np.float32)
    p += np.random.default_rng(7).normal(0, sigma, p.shape[:2])[..., None]
    out = Image.fromarray(np.clip(p, 0, 255).astype(np.uint8)).convert("RGBA")
    out.putalpha(a)
    return out


def shadows(canvas, obj, x, y, light):
    """Contact shadow under the base + soft cast shadow falling away from the light."""
    W, H = canvas.size
    w, h = obj.size
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # contact shadow: flat dark ellipse at the base
    cs = Image.new("L", (W, H), 0)
    ImageOps.expand  # noqa
    from PIL import ImageDraw
    d = ImageDraw.Draw(cs)
    d.ellipse([x + w * 0.04, y + h - h * 0.035, x + w * 0.96, y + h + h * 0.03], fill=150)
    cs = cs.filter(ImageFilter.GaussianBlur(max(4, w * 0.04)))
    # cast shadow: the silhouette squashed onto the surface, sheared away from the light
    sil = obj.split()[-1].resize((w, max(2, int(h * 0.22))))
    sh = Image.new("L", (W + w * 2, H), 0)
    shear = 0.9 if light == "left" else -0.9
    sil = sil.transform((int(w * 1.9), sil.height), Image.AFFINE,
                        (1, shear, -w * 0.45 if light == "left" else w * 0.45, 0, 1, 0), Image.BICUBIC)
    sil = ImageOps.flip(sil).point(lambda v: int(v * 0.45))
    sh.paste(sil, (int(x + w), int(y + h - 2)))
    sh = sh.crop((w, 0, W + w, H)).filter(ImageFilter.GaussianBlur(max(6, w * 0.06)))
    m = ImageChops.lighter(cs, sh)
    layer.putalpha(m)
    canvas.alpha_composite(layer)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scene"); ap.add_argument("out")
    ap.add_argument("--ratio", default="4:5", choices=SIZES)
    ap.add_argument("--x", type=float, default=0.5)
    ap.add_argument("--base", type=float, default=0.78)
    ap.add_argument("--height", type=float, default=0.34)
    ap.add_argument("--capsule", default="right", choices=["right", "left", "none"])
    ap.add_argument("--light", default="right", choices=["left", "right"])
    ap.add_argument("--bottle", default=f"{SKILL_ASSETS}/{ENV.get('BOTTLE', 'rz_bottle.png')}")
    ap.add_argument("--pill", default=f"{SKILL_ASSETS}/{ENV.get('PILL', 'rz_capsule.png')}")
    a = ap.parse_args()
    W, H = SIZES[a.ratio]
    scene = ImageOps.fit(Image.open(a.scene).convert("RGB"), (W, H), Image.LANCZOS).convert("RGBA")
    b = Image.open(a.bottle).convert("RGBA")
    b = b.crop(b.getbbox())
    bh = int(H * a.height); bw = int(b.width * bh / b.height)
    b = b.resize((bw, bh), Image.LANCZOS)
    bx, by = int(W * a.x - bw / 2), int(H * a.base - bh)
    region = scene.crop((max(0, bx - bw), max(0, by), min(W, bx + 2 * bw), min(H, by + bh))).convert("RGB")
    b = grain(match(b, region))
    shadows(scene, b, bx, by, a.light)
    scene.alpha_composite(b, (bx, by))
    if a.capsule != "none":
        c = Image.open(a.pill).convert("RGBA"); c = c.crop(c.getbbox())
        cl = int(bh * 0.30)
        s = cl / max(c.width, c.height)
        c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.LANCZOS)
        c = grain(match(c, region))
        cx = bx + bw + int(bw * 0.12) if a.capsule == "right" else bx - c.width - int(bw * 0.12)
        cy = int(H * a.base - c.height * 0.92)
        shadows(scene, c, cx, cy, a.light)
        scene.alpha_composite(c, (cx, cy))
    scene.convert("RGB").save(a.out, quality=95)
    print("done", a.out, "bottle box", (bx, by, bx + bw, by + bh))


if __name__ == "__main__":
    main()
