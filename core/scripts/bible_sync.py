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

Compliance-relevant changes (claims, disclaimers, approvals) go through a PR with Jeremy's sign-off.
"""
import html.parser, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(REPO, "core", "claude", "creative-bible.md")
LIVE = "https://claude.ai/artifact/PB9jBD5zHk1sueXcNTXuKG"
# product skill → its bible section heading (the women's / plain pages share the product's disclaimer)
SKILL_SECTION = {"restora-z": "Restora-Z", "sermorelin-ghk": "Sermorelin GHK \u2014 Men", "sermorelin": "Sermorelin \u2014 Men",
                 "pt-141": "PT-141", "bpc-157": "BPC-157"}


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
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    ver = re.search(r"artifact-[0-9a-f]+-(\d+-[0-9a-f]+)\.html$", os.path.basename(path))
    head = (f"<!-- Synced from the live creative bible {LIVE} (version {ver.group(1) if ver else 'unknown'}) by "
            f"core/scripts/bible_sync.py. Do not edit by hand: update the live bible, then re-sync. -->\n\n")
    return head + text


def norm(t):
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t.replace("—", "-").replace("–", "-")).strip().lower()


def sections(md):
    out, name = {}, "(top)"
    for ln in md.splitlines():
        if ln.startswith("## "):
            name = re.sub(r"\s*\[[^\]]*\]", "", ln[3:]).strip()   # drop badges such as [Approved by JL]
        elif ln.strip() and not ln.startswith("<!--"):
            out.setdefault(name, []).append(ln.strip())
    return out


def report(old, new):
    o, n = sections(old), sections(new)
    changed = False
    for name in sorted(set(o) | set(n)):
        a, b = {norm(x) for x in o.get(name, [])}, {norm(x) for x in n.get(name, [])}
        add = [x for x in n.get(name, []) if norm(x) not in a]
        rem = [x for x in o.get(name, []) if norm(x) not in b]
        if name not in o:
            print(f"+ NEW SECTION: {name} ({len(n[name])} lines)")
            changed = True
        elif name not in n:
            print(f"- REMOVED SECTION: {name}")
            changed = True
        elif add or rem:
            changed = True
            print(f"~ {name}")
            for x in add:
                print(f"    + {x}")
            for x in rem:
                print(f"    - {x}")
    if not changed:
        print("No changes: the repo copy matches the live bible.")
    return changed


def check(md):
    secs, ok = sections(md), True
    for skill in sorted(os.listdir(os.path.join(REPO, "skills"))):
        pj = os.path.join(REPO, "skills", skill, "product.json")
        if not os.path.exists(pj):
            continue
        prod = json.load(open(pj))
        sec = SKILL_SECTION.get(prod.get("id"), prod.get("name"))
        body = norm(" ".join(secs.get(sec, [])))
        disc = norm(prod.get("disclaimer", ""))
        if not body:
            print(f"⚠️  {skill}: no bible section named '{sec}'")
            ok = False
        elif disc and disc in body:
            print(f"✅ {skill}: disclaimer matches the bible ({sec})")
        else:
            pend = "disclaimer pending" in body
            print(f"❌ {skill}: product.json disclaimer not in the bible ({sec}{', bible says: Disclaimer pending' if pend else ''})")
            ok = False
    return ok


if __name__ == "__main__":
    argv = sys.argv[1:]
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
        open(OUT, "w", encoding="utf-8").write(new)
        print(f"✅ wrote {OUT}")
    if "--check" in sys.argv:
        check(new)
