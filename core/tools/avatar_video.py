"""AI Avatar Video toolkit (core/references/ai-avatar-video.md): presenter on green, keyed over animated B-roll stills.

  avatar_video.py broll     <job> <plan.json>            stills in <job>/gen -> <job>/broll_track.mp4 (push-ins, crossfades)
  avatar_video.py bgvideo   <job> <clip.mp4> [...] [--len S] [--dx PX]   Boreal-H3 background clip(s) -> broll_track.mp4 (default route)
  avatar_video.py shift     <in.png> <out.png> [--scale 0.86 --dx 0 --dy 0]   feathered reposition of a still (0 cr)
  avatar_video.py animatic  <job> <presenter_still.png>  free format preview: keyed still over the B-roll
  avatar_video.py key       <job> [--width 580 --fade 0.40 0.66]   <job>/out/presenter_raw.mp4 -> RGBA frames
  avatar_video.py composite <job> [--x -50 --y 620]       B-roll + keyed presenter + presenter audio -> <job>/out/raw.mp4
  avatar_video.py caps      <job> <Tag> <phrases.json>    regroup full_layout captions into clean phrases
  avatar_video.py sheet     <out.jpg> <img> [<img> ...]   side-by-side contact sheet

plan.json: [{"name": "01_hook", "img": "a.png", "dur": 2.6, "z0": 1.0, "z1": 1.1, "img2": "b.png"?}, ...]
           (img2 = crossfade img -> img2 inside the segment, for before/after pairs made with an "identical, change only X" edit).
phrases.json: ["YOUR BRAIN JUST BOOKED", "A MEETING.", ...]; a phrase may end in "|n" to force n whisper words.
"""
import argparse, json, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()  # same binary the other tools use, on any machine
FPS = 30
W, H = 1080, 1920


def run(cmd):
    subprocess.run(cmd, check=True)


def probe(path):
    """(width, height, duration) of a video, parsed from ffmpeg's banner."""
    err = subprocess.run([FF, "-i", path], capture_output=True, text=True).stderr
    w, h = map(int, re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", err).groups())
    hh, mm, ss = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err).groups()
    return w, h, int(hh) * 3600 + int(mm) * 60 + float(ss)


def matte(rgb, fade0, fade1):
    """Green-dominance key (ffmpeg chromakey made cream/teal clothes see-through) + despill + bottom fade -> RGBA array."""
    a = rgb.astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    d = g - np.maximum(r, b)
    al = np.clip(1 - (d - 30) / 50, 0, 1)
    m = Image.fromarray((al * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.0))
    al = np.asarray(m).astype(np.float32) / 255
    h = a.shape[0]
    al *= np.clip((h * fade1 - np.arange(h)) / (h * (fade1 - fade0)), 0, 1)[:, None]
    a[..., 1] = np.where(d > 0, np.maximum(r, b) + np.clip(d, 0, 8), g)
    return np.dstack([a, al * 255]).astype(np.uint8)


def cmd_broll(job, plan_path):
    plan = json.load(open(plan_path))
    gen, bdir = os.path.join(job, "gen"), os.path.join(job, "broll")
    os.makedirs(bdir, exist_ok=True)
    outs = []
    for p in plan:
        dur, z0, z1 = p["dur"], p.get("z0", 1.0), p.get("z1", 1.08)
        n = int(round(dur * FPS))
        zp = (f"scale={W*2}:{H*2},zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              f":d={n}:s={W}x{H}:fps={FPS}")
        out = os.path.join(bdir, f"{p['name']}.mp4")
        if p.get("img2"):
            fc = f"[0]{zp}[a];[1]{zp}[b];[a][b]xfade=transition=fade:duration={dur*0.5:.2f}:offset={dur*0.25:.2f}[v]"
            run([FF, "-y", "-loglevel", "error", "-loop", "1", "-t", str(dur), "-i", os.path.join(gen, p["img"]),
                 "-loop", "1", "-t", str(dur), "-i", os.path.join(gen, p["img2"]), "-filter_complex", fc, "-map", "[v]",
                 "-frames:v", str(n), "-pix_fmt", "yuv420p", out])
        else:
            run([FF, "-y", "-loglevel", "error", "-loop", "1", "-i", os.path.join(gen, p["img"]), "-vf", zp,
                 "-frames:v", str(n), "-pix_fmt", "yuv420p", out])
        outs.append(out)
    lst = os.path.join(bdir, "list.txt")
    open(lst, "w").write("".join(f"file '{o}'\n" for o in outs))
    run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", os.path.join(job, "broll_track.mp4")])
    print(f"broll_track.mp4: {sum(p['dur'] for p in plan):.2f} s, {len(plan)} shots")


def cmd_bgvideo(job, clips, length, dx=0):
    """Boreal-H3 background clip(s) -> <job>/broll_track.mp4 at 1080x1920/30 fps, last frame held to `length` s
    (default: the presenter take's length, so the background runs under the end card)."""
    if not length:
        raw = os.path.join(job, "out", "presenter_raw.mp4")
        length = probe(raw)[2] if os.path.exists(raw) else sum(probe(c)[2] for c in clips)
    ins, fc = [], ""
    for i, c in enumerate(clips):
        ins += ["-i", c]
        fc += f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1[v{i}];"
    # dx > 0 slides the picture right by zooming in slightly and cropping from the left edge (a black pad showed as a bar)
    z = 1 + 2 * dx / W
    shift = f",scale={int(W*z)//2*2}:{int(H*z)//2*2},crop={W}:{H}:0:{(int(H*z)//2*2 - H)//2}" if dx > 0 else ""
    fc += "".join(f"[v{i}]" for i in range(len(clips))) + f"concat=n={len(clips)}:v=1:a=0{shift},tpad=stop_mode=clone:stop_duration=30[v]"
    out = os.path.join(job, "broll_track.mp4")
    run([FF, "-y", "-loglevel", "error", *ins, "-filter_complex", fc, "-map", "[v]", "-t", f"{length:.2f}",
         "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "16", out])
    print(f"broll_track.mp4: {length:.2f} s from {len(clips)} Boreal clip(s)")


def cmd_shift(src, dst, scale, dx, dy):
    im = Image.open(src).convert("RGB")
    w0, h0 = im.size
    # heavy blur + darkening: a light blur left a ghost copy of faces/tablets in the uncovered area (2026-10-30)
    bg = im.filter(ImageFilter.GaussianBlur(90)).point(lambda v: int(v * 0.28))
    sm = im.resize((int(w0 * scale), int(h0 * scale)), Image.LANCZOS)
    w, h = sm.size
    f = 160
    y = np.minimum(np.arange(h), h - 1 - np.arange(h))
    x = np.minimum(np.arange(w), w - 1 - np.arange(w))
    m = np.clip(np.minimum(y[:, None], x[None, :]) / f, 0, 1)
    bg.paste(sm, ((w0 - w) // 2 + dx, (h0 - h) // 2 + dy), Image.fromarray((m * 255).astype(np.uint8)))
    bg.save(dst)
    print("saved", dst)


def cmd_key(job, width, fade0, fade1):
    src = os.path.join(job, "out", "presenter_raw.mp4")
    outdir = os.path.join(job, "out", "presenter_rgba")
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir):
        os.remove(os.path.join(outdir, f))
    w0, h0, _ = probe(src)
    w, h = width, int(h0 * width / w0)
    p = subprocess.Popen([FF, "-loglevel", "error", "-i", src, "-vf", f"scale={w}:{h}:flags=lanczos", "-f", "rawvideo",
                          "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    i = 0
    while True:
        buf = p.stdout.read(w * h * 3)
        if len(buf) < w * h * 3:
            break
        Image.fromarray(matte(np.frombuffer(buf, np.uint8).reshape(h, w, 3), fade0, fade1)).save(f"{outdir}/f{i:04d}.png")
        i += 1
    print(f"keyed {i} frames at {w}x{h}")


def cmd_animatic(job, still, width, fade0, fade1, x, y):
    im = Image.open(still).convert("RGB")
    rgba = matte(np.asarray(im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)), fade0, fade1)
    keyed = os.path.join(job, "gen", "presenter_still_rgba.png")
    Image.fromarray(rgba).save(keyed)
    out = os.path.join(job, "ANIMATIC_format_preview.mp4")
    run([FF, "-y", "-loglevel", "error", "-i", os.path.join(job, "broll_track.mp4"), "-loop", "1", "-i", keyed,
         "-filter_complex", f"[0][1]overlay=x={x}:y={y}:shortest=1,format=yuv420p", out])
    print("saved", out)


def cmd_composite(job, x, y):
    raw = os.path.join(job, "out", "presenter_raw.mp4")
    _, _, dur = probe(raw)
    pfps = 24
    err = subprocess.run([FF, "-i", raw], capture_output=True, text=True).stderr
    m = re.search(r"(\d+(?:\.\d+)?) fps", err)
    if m:
        pfps = m.group(1)
    out = os.path.join(job, "out", "raw.mp4")
    run([FF, "-y", "-loglevel", "error", "-i", os.path.join(job, "broll_track.mp4"), "-framerate", str(pfps),
         "-i", os.path.join(job, "out", "presenter_rgba", "f%04d.png"), "-i", raw, "-filter_complex",
         f"[1]fade=t=out:st={dur-0.45:.2f}:d=0.4:alpha=1[p];[0][p]overlay=x={x}:y={y}:eof_action=pass,format=yuv420p[v];[2:a]apad[a]",
         "-map", "[v]", "-map", "[a]", "-t", f"{dur:.2f}", "-r", str(FPS), "-c:v", "libx264", "-crf", "17",
         "-c:a", "aac", "-b:a", "192k", out])
    print(f"saved {out} ({dur:.2f} s)")


def norm(s):
    return re.sub(r"[^A-Z0-9]", "", s.upper())


def cmd_caps(job, tag, phrases_path):
    p = os.path.join(job, "layers_full", f"{tag}_caps.json")
    caps = json.load(open(p))
    words = [(w, tm) for s, e, t, ws in caps for w, tm in zip(t.split(), ws)]
    phrases = json.load(open(phrases_path))
    out, i = [], 0
    for ph in phrases:
        text, _, n = ph.partition("|")
        if n:
            take = int(n)
        else:  # consume whisper words until their letters cover the phrase (tolerates "2 A .M." splits, spelling drift)
            target, acc, take = len(norm(text)), 0, 0
            while i + take < len(words) and acc < target - 1:
                acc += len(norm(words[i + take][0]))
                take += 1
        ws = [tm for _, tm in words[i:i + take]]
        if not ws:
            sys.exit(f"ran out of words at phrase {text!r}")
        out.append([ws[0][0], ws[-1][1] + 0.15, text, ws])
        i += take
    if i != len(words):
        sys.exit(f"phrases cover {i} of {len(words)} words: {[w for w, _ in words[i:]]} left; add or fix phrases (use |n)")
    for k in range(len(out) - 1):
        out[k][1] = min(out[k][1], out[k + 1][0])
    json.dump(out, open(p, "w"), indent=1)
    for o in out:
        print(f"  {o[0]:.2f}-{o[1]:.2f} {o[2]}")


def cmd_sheet(out, imgs):
    ims = [Image.open(f).convert("RGB").resize((432, 768)) for f in imgs]
    s = Image.new("RGB", (440 * len(ims), 768), "white")
    for i, im in enumerate(ims):
        s.paste(im, (i * 440, 0))
    s.save(out, quality=85)
    print("saved", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("broll"); a.add_argument("job"); a.add_argument("plan")
    a = sp.add_parser("bgvideo"); a.add_argument("job"); a.add_argument("clips", nargs="+"); a.add_argument("--len", type=float, default=0); a.add_argument("--dx", type=int, default=0)
    a = sp.add_parser("shift"); a.add_argument("src"); a.add_argument("dst")
    a.add_argument("--scale", type=float, default=0.86); a.add_argument("--dx", type=int, default=0); a.add_argument("--dy", type=int, default=0)
    for name in ("key", "animatic", "composite"):
        a = sp.add_parser(name); a.add_argument("job")
        if name == "animatic":
            a.add_argument("still")
        if name in ("key", "animatic"):
            a.add_argument("--width", type=int, default=580); a.add_argument("--fade", type=float, nargs=2, default=[0.90, 1.0])  # solid presenter; only the bottom edge softens (Mitansh 10-30: "should be solid")
        if name in ("animatic", "composite"):
            a.add_argument("--x", type=int, default=-50); a.add_argument("--y", type=int, default=620)
    a = sp.add_parser("caps"); a.add_argument("job"); a.add_argument("tag"); a.add_argument("phrases")
    a = sp.add_parser("sheet"); a.add_argument("out"); a.add_argument("imgs", nargs="+")
    g = ap.parse_args()
    job = os.path.abspath(os.path.expanduser(getattr(g, "job", "") or "."))  # concat lists need absolute paths
    if g.cmd == "broll": cmd_broll(job, g.plan)
    elif g.cmd == "bgvideo": cmd_bgvideo(job, [os.path.abspath(c) for c in g.clips], g.len, g.dx)
    elif g.cmd == "shift": cmd_shift(g.src, g.dst, g.scale, g.dx, g.dy)
    elif g.cmd == "key": cmd_key(job, g.width, *g.fade)
    elif g.cmd == "animatic": cmd_animatic(job, g.still, g.width, g.fade[0], g.fade[1], g.x, g.y)
    elif g.cmd == "composite": cmd_composite(job, g.x, g.y)
    elif g.cmd == "caps": cmd_caps(job, g.tag, g.phrases)
    elif g.cmd == "sheet": cmd_sheet(g.out, g.imgs)
