"""Before/after check for the shared toolkit: renders a fixed set of jobs with one copy of core/ and compares
the outputs with another run, pixel by pixel. No generation, no credits.

  run:      python regression.py run <core_dir> <out_dir>      (core_dir = a core/ folder: the repo's, or an export of main)
  compare:  python regression.py compare <baseline_out> <new_out>
  smoke:    python regression.py smoke <core_dir> <out_dir>    (every product: renders what it should, refuses what it must)

Run it with the toolkit venv (Pillow, numpy, imageio-ffmpeg). Fixtures live in tests/fixtures/<product>/.
Restora-Z must come out identical after any change that isn't meant to change its look.
"""
import hashlib, json, os, shutil, subprocess, sys
from PIL import Image, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SKILLS = os.path.join(REPO, "skills")
FIX = os.path.join(HERE, "fixtures")
PY = sys.executable

RZ_DISC = ("AI-generated depictions and simulated portrayals used for illustrative advertising purposes. Not actual "
           "patients or medical providers. Disclaimer: Individual results may vary. Doctor-prescribed compounded sleep medication.")
RZ_VIDEO = {
    "product": "restora-z",
    "head": ["UP AT 3 A.M. AGAIN?", "MEET RESTORA-Z"], "sub": "Three prescription ingredients, one capsule",
    "end_head": ["GET YOUR 3-IN-1", "SLEEP SOLUTION"],
    "benefits": ["Supports Falling + Staying Asleep", "Helps Reduce Nighttime Wake-Ups", "3-in-1 Sleep Formula"],
    "ingredients_label": "3-IN-1 SLEEP FORMULA",
    "ingredients": [["TRAZODONE", "Aids in falling asleep"], ["HYDROXYZINE", "Supports deep relaxation"],
                    ["DOXEPIN", "Reduces early awakenings"]],
    "cta": "EXPLORE RESTORA-Z", "kicker": "3 A.M. CLUB", "disclaimer": RZ_DISC,
    "bottle": "rz_bottle.png", "pill": "rz_capsule.png", "vocab": "Restora-Z.",
}
RZ_CAPS = [[0.4, 2.1, "UP AT 3 A.M. AGAIN?", [[0.4, 0.7], [0.7, 1.0], [1.0, 1.5], [1.5, 2.0]]],
           [2.3, 4.6, "MEET RESTORA-Z TONIGHT.", [[2.3, 2.7], [2.7, 3.8], [3.8, 4.5]]],
           [5.0, 7.2, "DOCTOR PRESCRIBED, SHIPPED FREE.", [[5.0, 5.6], [5.6, 6.3], [6.3, 6.8], [6.8, 7.1]]]]
RZ_STATIC = {"product": "restora-z", "m_head": "Struggling to relax|*at night?*", "m_sub": "Supports nighttime calm",
             "notify": {"title": "Lights out", "body": "Restora-Z: 3-in-1 sleep support"},
             "toggles": [["3:00 am", "Wide awake", False], ["7:00 am", "Rested", True]],
             "chips": ["Hydroxyzine · Calms the nervous system", "Trazodone · Aids in falling asleep",
                       "Doxepin · Non-addictive sleep aid"],
             "head": ["SLEEP EASIER TONIGHT"], "ingredients": RZ_VIDEO["ingredients"],
             "ingredients_label": "3-IN-1 SLEEP FORMULA", "cta": "EXPLORE RESTORA-Z", "dek": "Doxepin reduces early awakenings.",
             "checklist": [["x", "Another gummy"], ["x", "Random sleep hacks"], ["check", "Restora-Z — 3-in-1, doctor prescribed"]],
             "quote": "Restora Z has helped me sleep better for sure", "quote_name": "Kathleen",
             "disclaimer": RZ_DISC}


def sh(cmd, env, log):
    r = subprocess.run(cmd, env=env, capture_output=True, text=True)
    log.append({"cmd": " ".join(os.path.basename(c) if os.path.isabs(c) else c for c in cmd[1:3]) + " " + " ".join(cmd[3:]),
                "rc": r.returncode, "out": (r.stdout + r.stderr).strip()[-600:]})
    return r.returncode


def job(out, name, copy, renders_from):
    d = os.path.join(out, name)
    os.makedirs(os.path.join(d, "source"), exist_ok=True)
    for f in ("rz_bottle.png", "rz_capsule.png"):
        shutil.copy(os.path.join(renders_from, f), os.path.join(d, "source", f))
    json.dump(copy, open(os.path.join(d, "copy.json"), "w"), indent=1)
    return d


def run(core, out):
    core, out = os.path.abspath(core), os.path.abspath(out)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    T = os.path.join(core, "tools")
    env = dict(os.environ, EVERLIFE_TOOLS=T, EVERLIFE_SKILLS_DIR=SKILLS, PYTHONHASHSEED="0")
    env.pop("EVERLIFE_SKILL_DIR", None)
    rz_assets = os.path.join(SKILLS, "everlife-restora-z", "assets")
    log = []
    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    clip = os.path.join(out, "clip.mp4")
    subprocess.run([ff, "-v", "error", "-y", "-f", "lavfi", "-i", "testsrc2=size=1080x1920:rate=24:duration=15",
                    "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", "15", "-c:v", "libx264", "-pix_fmt",
                    "yuv420p", "-c:a", "aac", "-threads", "1", clip], check=True)

    # video: three looks; the house look also gets the review burst
    for style in ("default", "tiktok", "editorial"):
        d = job(out, f"video_{style}", dict(RZ_VIDEO, style=style), rz_assets)
        os.makedirs(os.path.join(d, "layers_full"), exist_ok=True)
        cache = os.path.join(d, "layers_full", "T_caps.json")
        json.dump(RZ_CAPS, open(cache, "w"))
        os.utime(cache, (os.path.getmtime(clip) + 10,) * 2)  # newer than the clip, so whisper is skipped
        extra = ["--reviews", "R1,R3,R2", "--reviews-at", "9.0"] if style == "default" else []
        sh([PY, "-I", os.path.join(T, "full_layout.py"), d, clip, "T", "--end", "12.8"] + extra, env, log)

    # statics: modern templates, batch footer, legacy layouts
    for raw in sorted(os.listdir(os.path.join(FIX, "restora-z"))):
        src = os.path.join(FIX, "restora-z", raw)
        tag = raw[4:-4]
        d = job(out, f"static_{tag}", RZ_STATIC, rz_assets)
        cp = os.path.join(d, "copy.json")
        for tpl in ("hero", "strip", "notify", "toggle", "chips"):
            sh([PY, "-I", os.path.join(T, "finish_modern.py"), src, cp, os.path.join(d, f"modern_{tpl}.png"),
                "--ratio", "4:5", "--template", tpl], env, log)
        sh([PY, "-I", os.path.join(T, "finish_modern.py"), src, cp, os.path.join(d, "modern_hero_916.png"),
            "--ratio", "9:16", "--template", "hero"], env, log)
        sh([PY, "-I", os.path.join(T, "finish_batch.py"), src, os.path.join(d, "batch.png"), "--ratio", "4:5",
            "--disclaimer", RZ_DISC], env, log)
        if tag == "yarn":
            for lay in ("standard", "checklist", "article", "quote"):
                sh([PY, "-I", os.path.join(core, "scripts", "finish_image.py"), src, cp, os.path.join(d, f"legacy_{lay}.png"),
                    "--ratio", "4:5", "--layout", lay], env, log)
            sh([PY, "-I", os.path.join(T, "composite.py"), src, os.path.join(d, "composite.png"),
                "--bottle", os.path.join(rz_assets, "rz_bottle.png"), "--pill", os.path.join(rz_assets, "rz_capsule.png")], env, log)
    json.dump(log, open(os.path.join(out, "log.json"), "w"), indent=1)
    files = {}
    for root, _, names in os.walk(out):
        for n in names:
            if n.endswith(".png") and "/source" not in root:
                p = os.path.join(root, n)
                files[os.path.relpath(p, out)] = hashlib.sha256(open(p, "rb").read()).hexdigest()
    json.dump(files, open(os.path.join(out, "manifest.json"), "w"), indent=1, sort_keys=True)
    bad = [x for x in log if x["rc"] not in (0,)]
    print(f"rendered {len(files)} images from {len(log)} runs into {out}; non-zero exits: {len(bad)}")
    for x in bad:
        print(f"  rc={x['rc']}: {x['cmd']}\n     {x['out'][-200:]}")


def compare(a, b):
    ma, mb = (json.load(open(os.path.join(x, "manifest.json"))) for x in (a, b))
    la, lb = (json.load(open(os.path.join(x, "log.json"))) for x in (a, b))
    same = diff = 0
    for k in sorted(set(ma) | set(mb)):
        if k not in ma or k not in mb:
            print(f"ONLY IN {'baseline' if k in ma else 'new'}: {k}"); diff += 1; continue
        if ma[k] == mb[k]:
            same += 1; continue
        ia, ib = Image.open(os.path.join(a, k)).convert("RGBA"), Image.open(os.path.join(b, k)).convert("RGBA")
        if ia.size != ib.size:
            print(f"DIFF {k}: size {ia.size} -> {ib.size}"); diff += 1; continue
        dd = ImageChops.difference(ia, ib)
        n = sum(1 for p in dd.getdata() if max(p) > 2)
        if n == 0:
            same += 1; continue
        print(f"DIFF {k}: {100 * n / (ia.width * ia.height):.2f}% of pixels changed (max {max(max(p) for p in dd.getdata())})")
        diff += 1
    for x, y in zip(la, lb):
        if x["rc"] != y["rc"]:
            print(f"EXIT CODE changed {x['rc']} -> {y['rc']}: {x['cmd']}"); diff += 1
    print(f"identical: {same}   different: {diff}")
    return diff


SG_DISC = ("AI-generated depictions and simulated portrayals used for illustrative advertising purposes. Not actual "
           "patients or medical providers. Disclaimer: Individual results may vary. Doctor-prescribed compounded prescription.")


def smoke(core, out):
    """Product-neutral behaviour: a second product renders with its own settings, and the guards refuse
    what must be refused (no product named, wrong disclaimer, uncalibrated finish_modern, unapproved compare)."""
    core, out = os.path.abspath(core), os.path.abspath(out)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    T = os.path.join(core, "tools")
    env = dict(os.environ, EVERLIFE_TOOLS=T, EVERLIFE_SKILLS_DIR=SKILLS)
    env.pop("EVERLIFE_SKILL_DIR", None)
    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    clip = os.path.join(out, "clip.mp4")
    subprocess.run([ff, "-v", "error", "-y", "-f", "lavfi", "-i", "testsrc2=size=1080x1920:rate=24:duration=15",
                    "-t", "15", "-c:v", "libx264", "-pix_fmt", "yuv420p", clip], check=True)
    raw = os.path.join(FIX, "restora-z", "raw_yarn.png")
    sg = {"product": "sermorelin-ghk", "head": ["POWER YOUR PRIME", "WITH 3-IN-1 SERMORELIN GHK"],
          "sub": "Supports Lean Muscle + Performance", "end_head": ["2 NEXT-GEN PEPTIDES", "+ 1 LEAN MUSCLE POWERHOUSE"],
          "benefits": ["Supports Lean Muscle + Performance", "3-in-1 Peptide Support", "Supports Daily Energy + Healthy Blood Flow"],
          "ingredients_label": "3-IN-1 PEPTIDE SUPPORT", "ingredients": [["SERMORELIN", "Supports metabolism and lean muscle tone"],
          ["GHK", "Promotes radiant, firmer skin"], ["L-CITRULLINE MALATE", "Promotes healthy blood flow"]],
          "cta": "EXPLORE SERMORELIN GHK", "bottle": "sghk1000_bottle_ref.jpg", "vocab": "Sermorelin GHK."}
    checks = []

    def expect(name, cmd, want_ok, must_say=""):
        r = subprocess.run(cmd, env=env, capture_output=True, text=True)
        txt = r.stdout + r.stderr
        ok = (r.returncode == 0) == want_ok and (must_say in txt)
        checks.append((ok, name, r.returncode, txt.strip().splitlines()[-1][:160] if txt.strip() else ""))

    for style in ("default", "tiktok", "editorial"):
        d = os.path.join(out, f"sg_{style}")
        os.makedirs(os.path.join(d, "layers_full"))
        json.dump(dict(sg, style=style), open(os.path.join(d, "copy.json"), "w"))
        cache = os.path.join(d, "layers_full", "T_caps.json")
        json.dump([[0.4, 2.4, "AGE HITS GROWTH HORMONE.", [[0.4, 0.8], [0.8, 1.3], [1.3, 1.9], [1.9, 2.3]]]], open(cache, "w"))
        os.utime(cache, (os.path.getmtime(clip) + 10,) * 2)
        expect(f"Sermorelin video renders ({style})",
               [PY, "-I", os.path.join(T, "full_layout.py"), d, clip, "T", "--end", "12.8"], True)
    d = os.path.join(out, "sg_static"); os.makedirs(d)
    cp = os.path.join(d, "copy.json"); json.dump(dict(sg, m_head="Power your prime.|*3-in-1.*"), open(cp, "w"))
    expect("finish_batch takes the Sermorelin disclaimer from --product",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "batch.png"), "--product", "sermorelin-ghk"], True)
    expect("finish_batch refuses a disclaimer that isn't the product's",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "x.png"), "--product", "sermorelin-ghk",
            "--disclaimer", RZ_DISC], False, "differs")
    expect("finish_modern refuses an uncalibrated product",
           [PY, "-I", os.path.join(T, "finish_modern.py"), raw, cp, os.path.join(d, "x.png")], False, "product_zones")
    expect("finish_image refuses compare for a product without an approved comparison",
           [PY, "-I", os.path.join(core, "scripts", "finish_image.py"), raw, cp, os.path.join(d, "x.png"), "--layout", "compare"],
           False, "compare_allowed")
    expect("finish_image article uses the product's kicker default",
           [PY, "-I", os.path.join(core, "scripts", "finish_image.py"), raw, cp, os.path.join(d, "article.png"), "--layout", "article"], True)
    nop = os.path.join(d, "noproduct.json"); json.dump({"m_head": "x", "head": ["x"], "disclaimer": SG_DISC}, open(nop, "w"))
    expect("a copy.json without a product is refused",
           [PY, "-I", os.path.join(T, "finish_modern.py"), raw, nop, os.path.join(d, "x.png")], False, '"product"')
    bad = os.path.join(d, "baddisc.json"); json.dump(dict(sg, m_head="x", disclaimer=RZ_DISC), open(bad, "w"))
    expect("a copy.json with another product's disclaimer is refused",
           [PY, "-I", os.path.join(core, "scripts", "finish_image.py"), raw, bad, os.path.join(d, "x.png")], False, "differs")
    expect("composite refuses to guess the product",
           [PY, "-I", os.path.join(T, "composite.py"), raw, os.path.join(d, "x.png")], False, "--product")
    expect("composite takes Restora-Z renders from --product",
           [PY, "-I", os.path.join(T, "composite.py"), raw, os.path.join(d, "comp_rz.png"), "--product", "restora-z"], True)

    # Plain Sermorelin (not GHK): single ingredient, so tiktok/editorial end-card rows carry its approved benefits
    sp = {"product": "sermorelin", "head": ["DOUBLE STRENGTH", "SERMORELIN"], "sub": "Supports Energy + Stamina",
          "end_head": ["STRENGTH FOR TODAY,", "VITALITY FOR LIFE"],
          "benefits": ["Supports Energy + Stamina", "Supports Strength + Vitality", "Supports Natural Growth Hormone Activity"],
          "ingredients_label": "DOCTOR-PRESCRIBED SERMORELIN",
          "ingredients": [["ENERGY", "Supports Energy + Stamina"], ["STRENGTH", "Supports Strength + Vitality"],
                          ["GROWTH HORMONE", "Supports Natural Growth Hormone Activity"]],
          "cta": "EXPLORE SERMORELIN", "vocab": "Sermorelin."}
    for style in ("default", "tiktok", "editorial"):
        d = os.path.join(out, f"sp_{style}")
        os.makedirs(os.path.join(d, "layers_full"))
        job = dict(sp, style=style)
        if style == "tiktok":  # the long growth-hormone row collides in this look (see the skill's finishing.md)
            job["ingredients"] = sp["ingredients"][:2] + [["DELIVERY", "Easy sublingual delivery"]]
        json.dump(job, open(os.path.join(d, "copy.json"), "w"))
        cache = os.path.join(d, "layers_full", "T_caps.json")
        json.dump([[0.4, 2.4, "ENERGY FADING BY 3 P.M.?", [[0.4, 0.9], [0.9, 1.4], [1.4, 1.8], [1.8, 2.3]]]], open(cache, "w"))
        os.utime(cache, (os.path.getmtime(clip) + 10,) * 2)
        expect(f"plain Sermorelin video renders ({style})",
               [PY, "-I", os.path.join(T, "full_layout.py"), d, clip, "T", "--end", "12.8"], True)
    d = os.path.join(out, "sp_static"); os.makedirs(d)
    expect("finish_batch takes the plain Sermorelin disclaimer from --product",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "batch.png"), "--product", "sermorelin"], True)
    expect("plain Sermorelin refuses another product's disclaimer",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "x.png"), "--product", "sermorelin",
            "--disclaimer", RZ_DISC], False, "differs")
    expect("composite takes plain Sermorelin renders from --product",
           [PY, "-I", os.path.join(T, "composite.py"), raw, os.path.join(d, "comp_sp.png"), "--product", "sermorelin"], True)

    # MOTS-c: the bible's disclaimer is pending; product.json carries the provisional standard text (Priestley 2026-10-30)
    d = os.path.join(out, "mc_static"); os.makedirs(d)
    expect("finish_batch renders MOTS-c with its provisional disclaimer",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "batch.png"), "--product", "mots-c"], True)

    # NAD+ (sublingual tablet or injection): statics take its disclaimer; end cards render both forms
    d = os.path.join(out, "nad_static"); os.makedirs(d)
    expect("finish_batch takes the NAD+ disclaimer from --product",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "batch.png"), "--product", "nad"], True)
    expect("NAD+ refuses another product's disclaimer",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "x.png"), "--product", "nad",
            "--disclaimer", RZ_DISC], False, "differs")
    nd = {"product": "nad", "head": ["NAD+ BY EVERLIFE"], "head_always": True,
          "end_head": ["LESS FOG.", "MORE FOCUS."],
          "benefits": ["Supports All-Day Energy + Focus", "Supports Bounce-Back From Burnout", "Promotes Healthy Aging"],
          "ingredients_label": "SUBLINGUAL TABLET OR INJECTION",
          "ingredients": [["FOCUS", "Supports All-Day Energy + Focus"], ["BURNOUT", "Supports Bounce-Back From Burnout"],
                          ["AGING", "Promotes Healthy Aging"]],
          "cta": "CHOOSE YOUR FORM", "vocab": "NAD+."}
    for form, style in (("sublingual", "default"), ("injection", "tiktok")):
        d = os.path.join(out, f"nad_{form}")
        os.makedirs(os.path.join(d, "layers_full"))
        json.dump(dict(nd, style=style, form=form), open(os.path.join(d, "copy.json"), "w"))
        cache = os.path.join(d, "layers_full", "T_caps.json")
        json.dump([[0.4, 2.4, "LESS FOG. MORE FOCUS.", [[0.4, 0.9], [0.9, 1.4], [1.4, 1.8], [1.8, 2.3]]]], open(cache, "w"))
        os.utime(cache, (os.path.getmtime(clip) + 10,) * 2)
        expect(f"NAD+ video renders ({form}, {style})",
               [PY, "-I", os.path.join(T, "full_layout.py"), d, clip, "T", "--end", "11"], True)

    # GLP-1 (two vials): statics take its disclaimer; end cards render the semaglutide and the tirzepatide vial
    d = os.path.join(out, "glp_static"); os.makedirs(d)
    expect("finish_batch takes the GLP-1 disclaimer from --product",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "batch.png"), "--product", "glp-1"], True)
    expect("GLP-1 refuses another product's disclaimer",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "x.png"), "--product", "glp-1",
            "--disclaimer", RZ_DISC], False, "differs")
    gl = {"product": "glp-1", "head": ["GLP-1 BY EVERLIFE"], "head_always": True,
          "end_head": ["TURN DOWN THE", "FOOD NOISE"],
          "benefits": ["Supports Appetite Regulation", "Helps Reduce Food Noise", "One Price, No Surprise Increases"],
          "ingredients_label": "PROVIDER-GUIDED FROM HOME",
          "ingredients": [["APPETITE", "Supports Appetite Regulation"], ["FOOD NOISE", "Helps Reduce Food Noise"],
                          ["ONE PRICE", "No Surprise Increases"]],
          "cta": "EXPLORE GLP-1", "vocab": "GLP-1."}
    for form, style in (("semaglutide", "default"), ("tirzepatide", "tiktok")):
        d = os.path.join(out, f"glp_{form}")
        os.makedirs(os.path.join(d, "layers_full"))
        json.dump(dict(gl, style=style, form=form), open(os.path.join(d, "copy.json"), "w"))
        cache = os.path.join(d, "layers_full", "T_caps.json")
        json.dump([[0.4, 2.4, "TURN DOWN THE FOOD NOISE", [[0.4, 0.9], [0.9, 1.4], [1.4, 1.8], [1.8, 2.3]]]], open(cache, "w"))
        os.utime(cache, (os.path.getmtime(clip) + 10,) * 2)
        expect(f"GLP-1 video renders ({form}, {style})",
               [PY, "-I", os.path.join(T, "full_layout.py"), d, clip, "T", "--end", "11"], True)

    # Spartan Stack (vial): statics take its disclaimer; video end cards render the vial
    d = os.path.join(out, "st_static"); os.makedirs(d)
    expect("finish_batch takes the Spartan Stack disclaimer from --product",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "batch.png"), "--product", "spartan"], True)
    expect("Spartan Stack refuses another product's disclaimer",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "x.png"), "--product", "spartan",
            "--disclaimer", RZ_DISC], False, "differs")
    st = {"product": "spartan", "head": ["SPARTAN STACK BY EVERLIFE"], "head_always": True,
          "end_head": ["SUPPORTS JOINTS", "+ LIGAMENTS"],
          "benefits": ["Supports Joints + Ligaments", "Supports Mobility + Range of Motion", "Supports Muscle Recovery"],
          "ingredients_label": "RECOVERY STACK",
          "ingredients": [["JOINTS", "Supports Joints + Ligaments"], ["MOBILITY", "Supports Mobility + Range of Motion"],
                          ["RECOVERY", "Supports Muscle Recovery"]],
          "cta": "EXPLORE THE SPARTAN STACK", "vocab": "Spartan Stack."}
    for style in ("default", "tiktok"):
        d = os.path.join(out, f"st_{style}")
        os.makedirs(os.path.join(d, "layers_full"))
        json.dump(dict(st, style=style), open(os.path.join(d, "copy.json"), "w"))
        cache = os.path.join(d, "layers_full", "T_caps.json")
        json.dump([[0.4, 2.4, "SUPPORTS JOINTS AND LIGAMENTS", [[0.4, 1.1], [1.1, 1.6], [1.6, 1.9], [1.9, 2.3]]]], open(cache, "w"))
        os.utime(cache, (os.path.getmtime(clip) + 10,) * 2)
        expect(f"Spartan Stack video renders ({style})",
               [PY, "-I", os.path.join(T, "full_layout.py"), d, clip, "T", "--end", "11"], True)

    # Wolverine Stack (vial): statics take its disclaimer; video end cards render the vial
    d = os.path.join(out, "wv_static"); os.makedirs(d)
    expect("finish_batch takes the Wolverine Stack disclaimer from --product",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "batch.png"), "--product", "wolverine"], True)
    expect("Wolverine Stack refuses another product's disclaimer",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "x.png"), "--product", "wolverine",
            "--disclaimer", RZ_DISC], False, "differs")
    wv = {"product": "wolverine", "head": ["WOLVERINE STACK BY EVERLIFE"], "head_always": True,
          "end_head": ["SUPPORTS TENDONS", "+ LIGAMENTS"],
          "benefits": ["Supports Tendons + Ligaments", "Supports Mobility", "Supports Gut Lining Health"],
          "ingredients_label": "RECOVERY STACK",
          "ingredients": [["TENDONS", "Supports Tendons + Ligaments"], ["MOBILITY", "Supports Mobility"],
                          ["GUT LINING", "Supports Gut Lining Health"]],
          "cta": "EXPLORE THE WOLVERINE STACK", "vocab": "Wolverine Stack."}
    for style in ("default", "tiktok"):
        d = os.path.join(out, f"wv_{style}")
        os.makedirs(os.path.join(d, "layers_full"))
        json.dump(dict(wv, style=style), open(os.path.join(d, "copy.json"), "w"))
        cache = os.path.join(d, "layers_full", "T_caps.json")
        json.dump([[0.4, 2.4, "SUPPORTS TENDONS AND LIGAMENTS", [[0.4, 1.1], [1.1, 1.6], [1.6, 1.9], [1.9, 2.3]]]], open(cache, "w"))
        os.utime(cache, (os.path.getmtime(clip) + 10,) * 2)
        expect(f"Wolverine Stack video renders ({style})",
               [PY, "-I", os.path.join(T, "full_layout.py"), d, clip, "T", "--end", "11"], True)

    # Lovara (oral capsule): statics take its disclaimer; video end cards render the bottle + capsule
    d = os.path.join(out, "lv_static"); os.makedirs(d)
    expect("finish_batch takes the Lovara disclaimer from --product",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "batch.png"), "--product", "lovara"], True)
    expect("Lovara refuses another product's disclaimer",
           [PY, "-I", os.path.join(T, "finish_batch.py"), raw, os.path.join(d, "x.png"), "--product", "lovara",
            "--disclaimer", RZ_DISC], False, "differs")
    lv = {"product": "lovara", "head": ["LOVARA BY EVERLIFE"], "head_always": True,
          "end_head": ["FROM DISTANT TO", "DEEPLY CONNECTED"],
          "benefits": ["Supports Desire + Sensitivity", "Supports Comfort + Responsiveness", "Supports Intimate Readiness"],
          "ingredients_label": "3-IN-1 INTIMACY SUPPORT",
          "ingredients": [["DESIRE", "Supports Desire + Sensitivity"], ["COMFORT", "Supports Comfort + Responsiveness"],
                          ["READINESS", "Supports Intimate Readiness"]],
          "cta": "EXPLORE LOVARA", "vocab": "Lovara."}
    for style in ("default", "tiktok"):
        d = os.path.join(out, f"lv_{style}")
        os.makedirs(os.path.join(d, "layers_full"))
        json.dump(dict(lv, style=style), open(os.path.join(d, "copy.json"), "w"))
        cache = os.path.join(d, "layers_full", "T_caps.json")
        json.dump([[0.4, 2.4, "FROM DISTANT TO DEEPLY CONNECTED", [[0.4, 0.9], [0.9, 1.4], [1.4, 1.8], [1.8, 2.3]]]], open(cache, "w"))
        os.utime(cache, (os.path.getmtime(clip) + 10,) * 2)
        expect(f"Lovara video renders ({style})",
               [PY, "-I", os.path.join(T, "full_layout.py"), d, clip, "T", "--end", "11"], True)
    for ok, name, rc, last in checks:
        print(f"{'PASS' if ok else 'FAIL'}  {name}  (rc={rc}) {'' if ok else last}")
    print(f"{sum(c[0] for c in checks)}/{len(checks)} passed")
    return all(c[0] for c in checks)


if __name__ == "__main__":
    if sys.argv[1] == "run":
        run(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "smoke":
        sys.exit(0 if smoke(sys.argv[2], sys.argv[3]) else 1)
    else:
        sys.exit(1 if compare(sys.argv[2], sys.argv[3]) else 0)
