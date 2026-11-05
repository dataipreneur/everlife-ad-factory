#!/usr/bin/env python3
"""Sync the repo copy of the creative bible from the live bible artifact.

The live bible is a claude.ai artifact (https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG, visible to the Everlife org).
Claude reads it with its Artifact tool, which saves the page's HTML locally; this script turns that HTML into
core/claude/creative-bible.md (one "##" section per product, badges kept) and reports what changed.

  python3 core/scripts/bible_sync.py <saved.html> [--write] [--check]
    (no flag)  print the changes against the current core/claude/creative-bible.md; change nothing
    --write    also overwrite core/claude/creative-bible.md
    --check    verify every product skill's product.json disclaimer appears, verbatim, in its bible section
    --out F    also write the converted bible to F (a preview; the repo copy is untouched unless --write)
    --repo-version   print the repo copy's version (for the every-session check against the live page's version)

  --write refuses on `main` (make a branch) and refuses a weak parse (fewer than 20 product pages, a skill whose section is
  missing or has no disclaimer / CTAs, no discount table). After --write run build_product_bibles.py + build_product_briefs.py
  (`bible_pipeline.py regen`): every skill's references/bible.json, product-bible.md, product-brief.md and product.json
  disclaimer are GENERATED from the repo copy; nothing is edited by hand.

Compliance-relevant changes (claims, disclaimers, approvals) go through a PR with Jeremy's sign-off.
"""
import html.parser, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(REPO, "core", "claude", "creative-bible.md")
LIVE = "https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bible_model as bm  # noqa: E402   (the one parser; product skills map to sections via product.json "bible_sections")
MIN_PRODUCT_PAGES = 20


class Md(html.parser.HTMLParser):
    HEAD = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "### ", "h5": "#### "}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.buf, self.skip, self.lists, self.spans = [], [], 0, [], []

    def flush(self, prefix=""):
        t = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf = []
        if t:
            self.out.append(prefix + t)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if self.skip or tag in ("script", "style", "nav") or cls.startswith("nav"):
            self.skip += 1
            return
        if tag in self.HEAD or tag in ("p", "li", "div", "tr"):
            self.flush(self._prefix())
        if tag in self.HEAD:
            self.out.append("")
            self._head = self.HEAD[tag]
        if tag in ("ul", "ol"):
            self.lists.append([tag, 0])
        if tag == "li" and self.lists:
            self.lists[-1][1] += 1
        if tag == "span":
            self.spans.append("bdg" in cls)
            if "bdg" in cls:
                self.buf.append(" [")
        if tag == "span" and cls == "cta":
            self.flush(self._prefix())
            self._cta = True

    def _prefix(self):
        if getattr(self, "_head", None):
            h, self._head = self._head, None
            return h
        if getattr(self, "_cta", False):
            self._cta = False
            return "- CTA: "
        if getattr(self, "_li", False):
            self._li = False
            kind, n = self.lists[-1] if self.lists else ("ul", 0)
            return f"{n}. " if kind == "ol" else "- "
        return ""

    def handle_endtag(self, tag):
        if self.skip:
            self.skip -= 1
            return
        if tag == "li":
            self._li = True
            self.flush(self._prefix())
        elif tag == "span":
            if self.spans and self.spans.pop():
                self.buf.append("]")
            elif getattr(self, "_cta", False):
                self.flush(self._prefix())
        elif tag in self.HEAD or tag in ("p", "div", "tr", "td", "th"):
            self.flush(self._prefix())
        if tag in ("ul", "ol") and self.lists:
            self.lists.pop()
            self.out.append("")

    def handle_data(self, data):
        if not self.skip:
            self.buf.append(data)


def convert(path):
    p = Md()
    p.feed(open(path, encoding="utf-8").read())
    p.flush()
    text = "\n".join(p.out)
    # the artifact prints some badges as plain text glued to the line ("…SignalingWeak benefit"): bracket them like the others
    text = re.sub(r"(?<=\S)(Weak benefit|Weak headline|Pending approval|Hard NO conflict)$", r" [\1]", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    ver = re.search(r"artifact-[0-9a-f]+-(\d+-[0-9a-f]+)\.html$", os.path.basename(path))
    head = (f"<!-- Synced from the live creative bible {LIVE} (version {ver.group(1) if ver else 'unknown'}) by "
            f"core/scripts/bible_sync.py. Do not edit by hand: update the live bible, then re-sync. -->\n\n")
    return head + text


def norm(t):
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t.replace("—", "-").replace("–", "-")).strip().lower()


def sections(md):
    """{section: [lines]} via the shared parser (badges off the heading, the next page's category label kept with that page)."""
    return {head: [l.strip() for l in lines if l.strip()] for head, badges, lines, cat in bm.sections(md)}


def skill_sections():
    """skill folder -> [bible section headings] from product.json "bible_sections"."""
    out = {}
    for skill in sorted(os.listdir(os.path.join(REPO, "skills"))):
        pj = os.path.join(REPO, "skills", skill, "product.json")
        if os.path.exists(pj):
            out[skill] = bm.sections_of(json.load(open(pj)))
    return out


def affected(names):
    """Print which product skills each changed section touches (regenerated by build_product_bibles.py); the global
    sections touch every skill (lint checks the gates' numbers against them)."""
    if not names:
        return []
    secs = skill_sections()
    touched = []
    print("\nSections changed → skills regenerated by the pipeline:")
    for name in names:
        hit = [sk for sk, lst in secs.items() if any(bm.key(name) == bm.key(x) or bm.key(name.split("(")[0]) == bm.key(x.split("(")[0]) for x in lst)]
        if hit:
            print(f"  {name}  →  {', '.join(hit)}"); touched += hit
        elif bm.norm(name) in bm.GLOBAL_HEADINGS or any(name.startswith(p) for p in ("Standards", "(top)", "Creative Bible")):
            print(f"  {name}  →  GLOBAL: every skill (lint checks the gates and global-rules numbers)")
        else:
            print(f"  {name}  →  no skill yet (a product without a skill)")
    return sorted(set(touched))


def repo_version():
    head = open(OUT, encoding="utf-8").readline() if os.path.exists(OUT) else ""
    m = re.search(r"\(version ([^)]+)\)", head)
    return m.group(1) if m else "unknown"


def report(old, new):
    o, n = sections(old), sections(new)
    changed = False
    names = []
    for name in sorted(set(o) | set(n)):
        a, b = {norm(x) for x in o.get(name, [])}, {norm(x) for x in n.get(name, [])}
        add = [x for x in n.get(name, []) if norm(x) not in a]
        rem = [x for x in o.get(name, []) if norm(x) not in b]
        if name not in o:
            print(f"+ NEW SECTION: {name} ({len(n[name])} lines)")
            changed = True; names.append(name)
        elif name not in n:
            print(f"- REMOVED SECTION: {name}")
            changed = True; names.append(name)
        elif add or rem:
            changed = True; names.append(name)
            print(f"~ {name}")
            for x in add:
                print(f"    + {x}")
            for x in rem:
                print(f"    - {x}")
    if not changed:
        print("No changes: the repo copy matches the live bible.")
    affected(names)
    return changed


def guard(md):
    """Refuse a weak parse before anything is written: every product skill must resolve to a page with a disclaimer."""
    model = bm.parse(md)
    problems = []
    if len(model["order"]) < MIN_PRODUCT_PAGES:
        problems.append(f"only {len(model['order'])} product pages parsed (expected ≥ {MIN_PRODUCT_PAGES})")
    if model["version"] == "unknown":
        problems.append("no version in the converted page (the saved HTML file name must be artifact-<id>-<version>.html)")
    for skill, lst in skill_sections().items():
        for sec in lst:
            h = bm.find_page(model, sec)
            if not h:
                problems.append(f"{skill}: no bible section named '{sec}'")
            elif not model["pages"][h]["disclaimer"]:
                problems.append(f"{skill}: section '{h}' has no 'Ad disclaimer' line")
            elif not model["pages"][h]["ctas"]:
                problems.append(f"{skill}: section '{h}' has no CTAs")
    if not model["globals"].get("discount_to_feature"):
        problems.append("the global 'Discount to feature, by product' table was not found")
    return model, problems


def check(md):
    """Every product skill's product.json disclaimer must be the bible's, verbatim (the generator rewrites it; this reports)."""
    model, problems = guard(md); ok = not problems
    for pr in problems:
        print(f"❌ {pr}")
    for skill, lst in skill_sections().items():
        pj = json.load(open(os.path.join(REPO, "skills", skill, "product.json")))
        pages = [model["pages"][bm.find_page(model, s_)] for s_ in lst if bm.find_page(model, s_)]
        if not pages:
            continue
        disc = bm.norm(pages[0]["disclaimer"]); mine = bm.norm(pj.get("disclaimer", ""))
        if disc and disc == mine:
            print(f"✅ {skill}: disclaimer matches the bible ({', '.join(lst)})")
        else:
            print(f"❌ {skill}: product.json disclaimer differs from the bible ({', '.join(lst)}); build_product_bibles.py rewrites it (tell Jeremy)")
            ok = False
    return ok


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--repo-version" in argv:
        print(repo_version())
        sys.exit(0)
    if "--write" in argv:   # the repo copy changes only on a branch, through a PR (a local edit on main blocks update.sh)
        import subprocess
        br = subprocess.run(["git", "-C", REPO, "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True).stdout.strip()
        if br in ("main", "master"):
            sys.exit("❌ --write refuses on main: make a branch first (git checkout -b bible-sync-<date>), sync there, then open a PR.\n"
                     "   See core/references/bible-sync.md. Nothing was written.")
    out = argv[argv.index("--out") + 1] if "--out" in argv else None
    args = [a for a in argv if not a.startswith("--") and a != out]
    if not args:
        sys.exit(__doc__)
    new = convert(args[0])
    if out:
        open(out, "w", encoding="utf-8").write(new)
        print(f"preview written to {out}")
    old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
    report(old, new)
    if "--write" in sys.argv:
        model, problems = guard(new)
        if problems:
            sys.exit("❌ refusing to write: the converted page looks wrong:\n  " + "\n  ".join(problems))
        open(OUT, "w", encoding="utf-8").write(new)
        print(f"✅ wrote {OUT} (version {model['version']})")
    if "--check" in sys.argv:
        check(new)
