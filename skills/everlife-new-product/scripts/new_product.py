#!/usr/bin/env python3
"""Scaffold a new Everlife product skill from the synced creative bible (the plan doc's recipe, automated).

  new_product.py list                      products in the bible that have no skill yet (+ disclaimer / approval status)
  new_product.py inspect "<Product>"       the summary card: bible facts, readiness, renders, reference ads, winners, gaps
  new_product.py create "<Product>" --template <skill> [--id <id>] [--form capsule|tablet|vial|spray]
                                           [--bottle <file>] [--pill <file>]
                                           copy the template skill, strip its product files, write product.json/env (verbatim
                                           disclaimer), the bible extract, the renders, the copy-log seed; print what to adapt next

Reads only local files: core/claude/creative-bible.md (sync it first with core/scripts/bible_sync.py), the asset library
(~/Everlife-Creative/asset-library), reference ads (~/Everlife-Creative/reference-ads) and the Meta export in ~/Downloads.
Never spends credits, never pushes. `create` refuses a product with no ad disclaimer on file.
"""
import argparse, glob, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.realpath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BIBLE = os.path.join(REPO, "core", "claude", "creative-bible.md")
SKILLS = os.path.join(REPO, "skills")
HOME = os.path.expanduser("~")
ASSETS = os.path.join(HOME, "Everlife-Creative", "asset-library")
REFS = os.path.join(HOME, "Everlife-Creative", "reference-ads")
META = os.path.join(HOME, "Downloads", "Everlife_All-Time_Top_Ads_by_Account.xlsx")
NOT_PRODUCTS = {"Global Hard NOs", "Creative direction guidelines", "Creative & page standards", "Safe zones"}
TEMPLATE_HINT = [  # (words in the bible category or name, template skill, why)
    (("intimate", "desire", "libido", "sexual"), "everlife-pt-141", "intimate wellness: tasteful, product-led, no bedrooms"),
    (("stack", "recovery", "bpc", "tb-500", "tb500", "peptide", "metabolic", "mots"), "everlife-bpc-157", "peptide / recovery: vial, men's direction"),
    (("sermorelin", "growth hormone", "longevity"), "everlife-sermorelin", "tablet with strengths, men + women pages"),
    (("sleep",), "everlife-restora-z", "never edit Restora itself; copy only with Priestley's OK"),
]
BOTTLE_WORDS = ("BOTTLE", "VIAL", "SPRAY", "DROPPER", "JAR", "CREAM", "TUBE", "BOX")
PILL_WORDS = ("TABLET", "CAPSULE", "PILL", "SOFTGEL", "GUMMY")


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def sections():
    """{heading: (category, [lines])} for every '## ' section of the synced bible."""
    if not os.path.exists(BIBLE):
        sys.exit(f"❌ {BIBLE} missing: sync the bible first (core/scripts/bible_sync.py)")
    lines = open(BIBLE).read().split("\n")
    out, i = {}, 0
    while i < len(lines):
        if lines[i].startswith("## "):
            head = lines[i][3:].strip()
            j = i - 1
            while j > 0 and not lines[j].strip():
                j -= 1
            cat = lines[j].strip() if j > 0 and not lines[j].startswith(("#", "-", "Ad disclaimer", "Landing page")) else ""
            k = i + 1
            while k < len(lines) and not lines[k].startswith("## "):
                k += 1
            body = lines[i + 1:k]
            if body and body[-1].strip() and not body[-1].startswith(("-", "#", "Ad disclaimer", "Landing page")):
                body = body[:-1]          # the next section's category label
            out[head] = (cat, body)
            i = k
        else:
            i += 1
    return out


def find_section(secs, name):
    n = norm(name)
    for h in secs:
        if norm(h) == n or norm(h.split("(")[0]) == n or norm(h).startswith(n):
            return h
    return None


def parse(body):
    """Headlines / benefits / CTAs with their status, offer, proof, disclaimer, landing page, creative direction, audience."""
    d = {"headlines": [], "benefits": [], "more_benefits": [], "ctas": [], "offer": [], "proof": [], "direction": [],
         "hard_nos": [], "ingredients": [], "audience": "", "disclaimer": "", "landing": ""}
    cur, block_status = None, ""
    for raw in body:
        ln = raw.strip()
        if not ln:
            continue
        if ln.startswith("### ") or ln.startswith("#### "):
            h = ln.lstrip("#").strip()
            block_status = "pending" if "[Pending approval]" in h else ""
            hl = h.lower()
            cur = ("headlines" if "headline" in hl else "benefits" if "quick-hit" in hl else
                   "more_benefits" if "more approved" in hl else "ctas" if hl.startswith("ctas") else
                   "offer" if "offer" in hl else "proof" if "proof" in hl else "direction" if "creative direction" in hl else
                   "hard_nos" if "hard no" in hl else "audience" if "who it" in hl else
                   "ingredients" if ("ingredient" in hl or h.istitle()) and cur in ("ingredients", "more_benefits", None) and "claim" in hl else cur)
            continue
        if ln.startswith("Ad disclaimer"):
            d["disclaimer"] = ln[len("Ad disclaimer"):].strip(); cur = None; continue
        if ln.startswith("Landing page"):
            d["landing"] = ln[len("Landing page"):].strip(); cur = None; continue
        item = re.sub(r"^(\d+\.|-)\s*", "", ln)
        if cur == "audience" and not d["audience"]:
            d["audience"] = item; continue
        if cur not in d or not isinstance(d.get(cur), list) or not (ln.startswith("-") or re.match(r"^\d+\.", ln)):
            continue
        status = block_status
        for tag, st in (("[Pending approval]", "pending"), ("[Weak headline]", "weak"), ("Weak headline", "weak"),
                        ("Weak benefit", "weak"), ("Hard NO conflict", "hard_no")):
            if tag in item:
                status, item = st, item.replace(tag, "").strip()
        if "[PLACEHOLDER]" in item:
            status = "placeholder"
        item = re.sub(r"^CTA:\s*", "", item)
        d[cur].append((item, status or "approved"))
    return d


def find_files(product):
    n = norm(product.split("(")[0])
    hits = []
    for root in (ASSETS, os.path.join(HOME, "Downloads")):
        for p in glob.glob(os.path.join(root, "**", "*"), recursive=True):
            if os.path.isfile(p) and p.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".avif")) and n and n in norm(p):
                if "/reference-ads/" in p or "everlife-ad-factory" in p:
                    continue
                hits.append(p)
    bottles = [p for p in hits if any(w in os.path.basename(p).upper() for w in BOTTLE_WORDS)]
    pills = [p for p in hits if any(w in os.path.basename(p).upper() for w in PILL_WORDS)]
    form = next((w.lower() for w in ("CAPSULE", "TABLET", "SOFTGEL", "GUMMY") if any(w in os.path.basename(p).upper() for p in pills)), None)
    if not form:
        form = next((w.lower() for w in ("VIAL", "SPRAY", "DROPPER", "CREAM") if any(w in os.path.basename(p).upper() for p in bottles)), None)
    return sorted(set(bottles)), sorted(set(pills)), form


def ref_ads(product):
    n = norm(product.split("(")[0])
    return [p for p in glob.glob(os.path.join(REFS, "**", "*"), recursive=True)
            if os.path.isfile(p) and n in norm(os.path.dirname(p) + os.path.basename(p))]


def winners(product, top=5):
    if not os.path.exists(META):
        return None, []
    try:
        import openpyxl
    except ImportError:
        return None, []
    n, rows = product.split("(")[0].strip().lower(), []
    wb = openpyxl.load_workbook(META, read_only=True, data_only=True)
    for ws in wb.worksheets:
        for r in ws.iter_rows(values_only=True):
            cells = [c for c in r if c is not None]
            if cells and n in "|".join(str(c) for c in cells).lower():
                nums = [c for c in cells if isinstance(c, (int, float))]
                rows.append((ws.title, " | ".join(str(c) for c in cells if isinstance(c, str))[:90], nums))
    rows.sort(key=lambda x: -(x[2][1] if len(x[2]) > 1 else 0))   # 2nd number = purchases in the export's layout
    return len(rows), rows[:top]


def suggest_template(head, cat):
    t = (head + " " + cat).lower()
    for words, skill, why in TEMPLATE_HINT:
        if any(w in t for w in words):
            return skill, why
    return "everlife-bpc-157", "default: the newest product skill"


def skill_id(head):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", head.split("(")[0].strip().lower())).strip("-")


def built_ids():
    return {d[len("everlife-"):] for d in os.listdir(SKILLS) if d.startswith("everlife-")}


def cmd_list(_):
    secs, built = sections(), built_ids()
    print("Products in the bible without a skill (✅ disclaimer on file / ⛔ pending):")
    for h, (cat, body) in secs.items():
        if h in NOT_PRODUCTS or skill_id(h) in built or any(skill_id(h).startswith(b) for b in built if len(b) > 4):
            continue
        d = parse(body)
        disc = "⛔ no disclaimer" if (not d["disclaimer"] or "pending" in d["disclaimer"].lower()) else "✅ disclaimer"
        appr = sum(1 for _, s in d["headlines"] if s == "approved")
        print(f"  {h:45s} {cat[:24]:24s} {disc:16s} headlines {appr}/{len(d['headlines'])} approved")


def card(product):
    secs = sections()
    head = find_section(secs, product)
    if not head:
        sys.exit(f"❌ No bible section matches '{product}'. Sections: " + ", ".join(h for h in secs if h not in NOT_PRODUCTS))
    cat, body = secs[head]
    d = parse(body)
    bottles, pills, form = find_files(head)
    nwin, top = winners(head)
    refs = ref_ads(head)
    tpl, why = suggest_template(head, cat)
    disc_ok = bool(d["disclaimer"]) and "pending" not in d["disclaimer"].lower()
    other = [h.split("(")[0].split("—")[0].strip() for h in secs if h not in NOT_PRODUCTS and h != head]
    flags = []
    for item, _ in d["ctas"] + d["headlines"]:
        for o in other:
            if len(o) > 3 and re.search(r"\b" + re.escape(o) + r"\b", item) and o.lower() not in head.lower():
                flags.append(f'"{item}" names another product ({o}): likely a copy error')
    return {"product": head, "id": skill_id(head), "category": cat, "audience": d["audience"], "data": d,
            "disclaimer_ok": disc_ok, "bottles": bottles, "pills": pills, "form": form, "winners": (nwin, top),
            "refs": refs, "template": (tpl, why), "flags": flags}


def cmd_inspect(a):
    c = card(a.product)
    d = c["data"]
    cnt = lambda xs: {s: sum(1 for _, t in xs if t == s) for s in ("approved", "pending", "weak", "hard_no", "placeholder") if any(t == s for _, t in xs)}
    print(f"== {c['product']} ==  ({c['category'] or 'no category label'})")
    print(f"Audience: {c['audience'] or '—'}")
    print(f"Disclaimer: {'✅ on file' if c['disclaimer_ok'] else '⛔ ' + (d['disclaimer'] or 'none')}")
    print(f"Headlines: {len(d['headlines'])} {cnt(d['headlines'])}")
    for h, s in d["headlines"]:
        print(f"   {'✅' if s == 'approved' else '⏳' if s == 'pending' else '·'} {h}  ({s})")
    print(f"Benefits: {len(d['benefits'])} quick-hit {cnt(d['benefits'])}, {len(d['more_benefits'])} more {cnt(d['more_benefits'])}")
    print(f"CTAs: {len(d['ctas'])} {cnt(d['ctas'])}: " + " · ".join(x for x, _ in d["ctas"]))
    print(f"Offer: " + (" · ".join(f'{x} ({s})' for x, s in d['offer']) or "—"))
    print(f"Creative direction: " + (" | ".join(x for x, _ in d['direction']) or "— (global rules only)"))
    print(f"Product Hard NOs: " + (" | ".join(x for x, _ in d['hard_nos']) or "—"))
    print(f"Landing page: {d['landing'] or '—'}")
    print(f"Renders ({ASSETS} + ~/Downloads): form {c['form'] or 'UNKNOWN (not in the bible, no render named it)'}")
    for p in c["bottles"]:
        print(f"   bottle: {p}")
    for p in c["pills"]:
        print(f"   pill:   {p}")
    if not c["bottles"]:
        print("   ⛔ no bottle/vial render found")
    nwin, top = c["winners"]
    print(f"Winners (Meta all-time export): {'export not in ~/Downloads' if nwin is None else f'{nwin} rows'}")
    for sheet, name, nums in top:
        print(f"   {sheet}: {name}  {nums[:4]}")
    print(f"Reference ads ({REFS}): {len(c['refs'])}")
    print(f"Suggested template: {c['template'][0]}  ({c['template'][1]})")
    for f in c["flags"]:
        print(f"⚠️  {f}")
    gaps = []
    if not c["disclaimer_ok"]: gaps.append("ad disclaimer (Jeremy) — BLOCKS the build")
    if not c["form"]: gaps.append("form (tablet / capsule / vial / spray)")
    if not c["bottles"]: gaps.append("bottle/vial render (asset library download)")
    if c["form"] in ("capsule", "tablet", "softgel", "gummy") and not c["pills"]: gaps.append("tablet/capsule render")
    if any(s == "placeholder" for _, s in d["offer"]) or not d["offer"]: gaps.append("offer (placeholder in the bible)")
    if not any(s == "approved" for _, s in d["headlines"]): gaps.append("approved headlines (all pending)")
    if any(s == "pending" for _, s in d["ctas"]): gaps.append("approved CTAs (pending)")
    if c["flags"]: gaps.append("answers on the flagged copy errors (Justin)")
    print("Gaps (human inputs): " + ("; ".join(gaps) if gaps else "none"))


def cut_out(src, dst):
    from PIL import Image, ImageFilter
    import numpy as np
    from collections import deque
    im = Image.open(src).convert("RGBA")
    if im.getchannel("A").getextrema()[0] < 250:      # already transparent
        im.crop(im.getbbox()).save(dst); return "kept transparency"
    a = np.asarray(im.convert("RGB")).astype(np.int16)
    h, w, _ = a.shape
    white = (a.min(axis=2) > 236) & ((a.max(axis=2) - a.min(axis=2)) < 14)
    bg = np.zeros((h, w), bool)
    q = deque([(y, x) for y in range(h) for x in (0, w - 1) if white[y, x]] + [(y, x) for x in range(w) for y in (0, h - 1) if white[y, x]])
    for y, x in q:
        bg[y, x] = True
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and white[ny, nx] and not bg[ny, nx]:
                bg[ny, nx] = True; q.append((ny, nx))
    from PIL import Image as I
    alpha = I.fromarray(np.where(bg, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    im.putalpha(alpha)
    im.crop(im.getbbox()).save(dst)
    return "cut out from a white background"


def cmd_create(a):
    c = card(a.product)
    if not c["disclaimer_ok"]:
        sys.exit(f"⛔ {c['product']}: no ad disclaimer on file in the bible. Nothing can be built until Jeremy adds it.")
    pid = a.id or c["id"]
    dest = os.path.join(SKILLS, f"everlife-{pid}")
    tpl = os.path.join(SKILLS, a.template)
    if os.path.exists(dest):
        sys.exit(f"❌ {dest} already exists")
    if not os.path.isdir(tpl):
        sys.exit(f"❌ template {tpl} not found")
    if a.template == "everlife-restora-z" and not a.allow_restora:
        sys.exit("⛔ copying Restora-Z needs Priestley's explicit OK (--allow-restora)")
    shutil.copytree(tpl, dest, symlinks=True)
    # strip the template's own product files: renders, Creatify project, winners, team refs, reviews, vial/pin refs
    for p in glob.glob(os.path.join(dest, "assets", "*")):
        (shutil.rmtree if os.path.isdir(p) else os.remove)(p)
    for sub in ("winners", "team-refs", "pinterest", "vial-refs", "meta-refs"):
        p = os.path.join(dest, "references", sub)
        if os.path.isdir(p):
            shutil.rmtree(p)
    for f in ("reviews.json",):
        p = os.path.join(dest, "references", f)
        if os.path.exists(p):
            os.remove(p)
    name = c["product"].split("(")[0].split("—")[0].strip()
    form = a.form or c["form"] or "tablet"
    bottle = a.bottle or (c["bottles"][0] if c["bottles"] else None)
    pill = a.pill or (c["pills"][0] if c["pills"] else None)
    bfile = f"{pid}_bottle.png"
    pfile = f"{pid}_{form}.png" if pill else None
    notes = []
    if bottle:
        notes.append(f"{bfile}: {cut_out(bottle, os.path.join(dest, 'assets', bfile))} (from {bottle})")
        from PIL import Image
        im = Image.open(os.path.join(dest, "assets", bfile)).convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255)); bg.alpha_composite(im)
        bg.convert("RGB").save(os.path.join(dest, "assets", f"{pid}_bottle_ref.jpg"), quality=92)
    if pill:
        notes.append(f"{pfile}: {cut_out(pill, os.path.join(dest, 'assets', pfile))} (from {pill})")
    # product.json: keep the template's generic keys, replace everything product-specific
    tp = json.load(open(os.path.join(tpl, "product.json")))
    for k in ("forms", "strengths", "product_zones", "pill_end_scale", "_disclaimer_status"):
        tp.pop(k, None)
    tp.update({
        "_about": f"Product settings read by the shared tools (core/tools/product.py). Data only. disclaimer = the bible's {name} ad "
                  f"disclaimer, verbatim. Scaffolded {__import__('datetime').date.today()} by everlife-new-product from {a.template}.",
        "id": pid, "name": name, "renders": {"bottle": bfile, "pill": pfile},
        "disclaimer": c["data"]["disclaimer"], "disclaimer_at": "bottom", "end_card_safe_shift": True,
        "keep_case": [f"{name} by Everlife", name], "review_highlight": re.escape(name), "reviews": "references/reviews.json",
        "notify_app": name, "compare_allowed": False,
    })
    tp.setdefault("hero", {})
    tp["hero"].update({"element": f"the {name} {form} (the bottle/vial is secondary, large and legible when shown)",
                       "never": "TODO: fill from the bible's Hard NOs + creative direction"})
    json.dump(tp, open(os.path.join(dest, "product.json"), "w"), indent=1, ensure_ascii=False)
    open(os.path.join(dest, "product.env"), "w").write(
        "# Product settings read by core/scripts/preflight.sh. One file per product skill.\n"
        f'PRODUCT_NAME="{name}"\nOUT_DIR="$HOME/Everlife-Creative/output/{name.replace(" ", "-")}"\n'
        f'COPY_LOG="$HOME/Everlife-Creative/{pid}-copy-log.md"\nBOTTLE="{bfile}"\nPILL="{pfile or ""}"\n'
        f'RENDERS="{bfile} {pid}_bottle_ref.jpg{(" " + pfile) if pfile else ""}"\n'
        f'DRIVE_FOLDER="{os.path.relpath(os.path.dirname(bottle), ASSETS) if bottle and bottle.startswith(ASSETS) else name.upper()}"\n')
    open(os.path.join(dest, "assets", "copy-log-seed.md"), "w").write(
        f"# {name} copy log — lines already used (do not reuse)\n\n| Ad | Audience | Header | VO lines | End head | CTA |\n|---|---|---|---|---|---|\n")
    status = "✅ all in" if bottle and (pill or form in ("vial", "spray", "cream", "dropper")) else "❌ MISSING: generation blocked"
    open(os.path.join(dest, "assets", "RENDERS.md"), "w").write(
        f"# {name} product renders ({status})\n\n" + ("\n".join(f"- {n}" for n in notes) or "- none yet") +
        "\n\nLOOK at every render before use (right product, label, strength, clean background); check against the website. "
        "Never use another product's render.\n")
    # the bible extract: verbatim section + a pre-screen to fill in
    secs = open(BIBLE).read().split("\n")
    s = secs.index(f"## {c['product']}")
    e = next((i for i in range(s + 1, len(secs)) if secs[i].startswith("## ")), len(secs))
    verb = "\n".join(secs[s:e]).rstrip()
    rows = "\n".join(f"| {x} | {k} | {'⚠ Jeremy' if st == 'pending' else 'Weak (bible)' if st == 'weak' else '❌' if st == 'hard_no' else 'TODO screen'} | |"
                     for k in ("headlines", "benefits", "more_benefits", "ctas", "offer") for x, st in c["data"][k])
    open(os.path.join(dest, "references", "product-bible.md"), "w").write(
        f"# {name} — creative bible (verbatim extract)\n\n> Source: the live creative bible, synced into `core/claude/creative-bible.md` "
        f"(section \"## {c['product']}\"), copied {__import__('datetime').date.today()} by everlife-new-product. Re-copy when the bible changes. "
        "Global rules: `core/references/global-rules.md` (they win).\n\n## Product facts for this skill\nTODO (see references/adapt-checklist.md §2).\n\n"
        "## Compliance pre-screen (Claude's reading against the GLOBAL Hard NOs — NOT bible text; confirm with Jeremy)\n\n"
        "| Line (bible) | Where | Status | Why |\n|---|---|---|---|\n" + rows +
        "\n\n---\n\n# VERBATIM (do not edit; re-copy from the bible)\n\n```text\n" + verb + "\n```\n")
    leftovers = {}
    old = json.load(open(os.path.join(tpl, "product.json"))).get("name", "")
    for dp, _, fs in os.walk(dest):                 # os.walk doesn't follow the core -> ../../core link
        for f in fs:
            if f.endswith(".md") and old:
                p = os.path.join(dp, f)
                n = open(p).read().count(old)
                if n:
                    leftovers[os.path.relpath(p, dest)] = n
    print(f"✅ scaffolded {dest} from {a.template}  (id {pid}, form {form})")
    for n in notes:
        print("   " + n)
    print(f"   renders: {status}")
    print(f"Next: adapt these files (template name '{old}' still appears): " +
          ", ".join(f"{k} ×{v}" for k, v in sorted(leftovers.items(), key=lambda x: -x[1])))
    print("Then: references/adapt-checklist.md §2–§5 (pre-screen, rules, tests).")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("list")
    i = sp.add_parser("inspect"); i.add_argument("product")
    c = sp.add_parser("create"); c.add_argument("product"); c.add_argument("--template", required=True)
    c.add_argument("--id"); c.add_argument("--form"); c.add_argument("--bottle"); c.add_argument("--pill")
    c.add_argument("--allow-restora", action="store_true")
    a = ap.parse_args()
    {"list": cmd_list, "inspect": cmd_inspect, "create": cmd_create}[a.cmd](a)


if __name__ == "__main__":
    main()
