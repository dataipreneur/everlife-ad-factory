#!/usr/bin/env python3
"""The creative bible as data. ONE parser for core/claude/creative-bible.md (the repo copy written by bible_sync.py), used by
build_product_bibles.py, build_product_briefs.py, skill_lint.py, bible_sync.py and new_product.py.

    import bible_model as bm
    model = bm.load()                      # {"version", "globals", "pages": {heading: page}, "order": [headings]}
    pages = bm.pages_for(model, product_json)   # the product's page(s) (Men + Women for the Sermorelins)
    merged = bm.merge(pages)               # one dict of lists (union, page order) + who/truth/disclaimer/landing
    offer = bm.offer_of(merged, model["globals"], product_json["name"])

A page: {"heading", "category", "who", "truth", "direction": [str], "headlines": [item], "quick_hits": [item],
         "more_benefits": [item], "ctas": [item], "offers": [item], "proof": [item], "hard_nos": [item],
         "ingredient_claims": {ingredient: [item]}, "extra": {heading: [str]}, "field_badges": {field: [badge]},
         "disclaimer", "landing_page", "last_verified"}; an item = {"text", "badges": [str]}.
Nothing here writes a file.
"""
import json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BIBLE = os.path.join(REPO, "core", "claude", "creative-bible.md")
BADGES = ("Pending approval", "Weak headline", "Weak benefit", "Hard NO conflict", "Approved by JL", "PLACEHOLDER", "VERIFY CURRENT", "Product")
GLOBAL_HEADINGS = ("global hard nos", "creative direction guidelines", "creative & page standards", "safe zones")
FIELDS = {"who it's for": "who", "creative direction": "direction", "headlines & hooks": "headlines", "headlines": "headlines",
          "new headline options": "headlines", "quick-hit benefits": "quick_hits", "more approved benefits": "more_benefits",
          "more approved benefits (continued)": "more_benefits", "ctas": "ctas", "proof & value props": "proof",
          "offers & conversion": "offers", "hard nos": "hard_nos", "more claims": "more_benefits"}
CONTAINERS = ("headline bank", "headlines, benefits & claims", "benefits & claims")
INGREDIENT_HEADS = ("approved ingredient claims", "ingredient claims", "3-in-1 formula")
LIST_ITEM = re.compile(r"^(?:\d+\.|-|•)\s+")


def norm(t):
    """Loose compare key: curly quotes/dashes folded, whitespace collapsed, lowercase."""
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t.replace("—", "-").replace("–", "-")).strip().lower()


def key(t):
    """Tighter key for names: letters and digits only (so 'GLP1' == 'GLP-1', 'Titan-rx' == 'Titan-Rx')."""
    return re.sub(r"[^a-z0-9]+", "", norm(t))


def split_badges(text):
    """'Line [Weak headline]' or the glued 'LineWeak benefit' → ('Line', ['Weak headline'])."""
    badges = []
    def take(m):
        badges.append(m.group(1).strip()); return ""
    text = re.sub(r"\s*\[([^\]]+)\]", take, text)
    m = re.search(r"(?<=\S)(Weak benefit|Weak headline|Pending approval|Hard NO conflict)$", text)
    if m:
        badges.append(m.group(1)); text = text[:m.start()]
    return text.strip(), badges


def version_of(md):
    m = re.search(r"\(version ([^)]+)\)", md.splitlines()[0] if md else "")
    return m.group(1) if m else "unknown"


def sections(md):
    """[(heading_clean, heading_badges, [lines], category)] in page order; '## ' splits, comment lines dropped, the bare line
    right before a '## ' is the next section's category label (eyebrow) and is removed from the previous section."""
    out, cur = [], None
    lines = [l for l in md.splitlines() if not l.startswith("<!--")]
    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            head, badges = split_badges(ln[3:].strip())
            category = ""
            if cur is not None and cur[2]:
                prev = cur[2]
                j = len(prev) - 1
                while j >= 0 and not prev[j].strip():
                    j -= 1
                if j >= 0 and not prev[j].startswith(("#", "-", "•", "Ad disclaimer", "Landing page")) and not LIST_ITEM.match(prev[j]) \
                        and len(prev[j]) < 60:
                    category = prev[j].strip(); del prev[j:]
            cur = [head, badges, [], category]
            out.append(cur)
        elif cur is not None:
            cur[2].append(ln.rstrip())
        else:
            if ln.strip():
                out.append(["(top)", [], [ln.rstrip()], ""]) if not out else out[0][2].append(ln.rstrip())
                cur = None if out[0][0] != "(top)" else None
    return [tuple(s) for s in out if s[0] != "(top)"]


def is_product(lines):
    low = [norm(l.lstrip("#").strip()) for l in lines if l.startswith("### ")]
    low = [split_badges(l)[0] for l in low]
    return "who it's for" in low or "ctas" in low


def parse_page(heading, badges, lines, category=""):
    page = {"heading": heading, "heading_badges": badges, "category": category, "who": "", "truth": "", "direction": [],
            "headlines": [], "quick_hits": [], "more_benefits": [], "ctas": [], "offers": [], "proof": [], "hard_nos": [],
            "ingredient_claims": {}, "extra": {}, "field_badges": {}, "disclaimer": "", "landing_page": "", "last_verified": ""}
    field, ingredient, in_ingredients, extra_head = None, None, False, None
    for raw in lines:
        ln = raw.strip()
        if not ln:
            continue
        if ln.startswith("#"):
            level = len(ln) - len(ln.lstrip("#"))
            h, hb = split_badges(ln.lstrip("#").strip())
            hl = norm(h)
            if level >= 4 and in_ingredients:
                ingredient = h; page["ingredient_claims"].setdefault(ingredient, []); field = "ingredient"; continue
            in_ingredients = hl in INGREDIENT_HEADS
            if in_ingredients:
                field, ingredient, extra_head = "ingredient", None, None; continue
            if hl in CONTAINERS:
                field, extra_head = None, None; continue
            guess = FIELDS.get(hl) or ("headlines" if re.search(r"headline|hook option", hl) else
                                       "more_benefits" if re.search(r"benefit|claim", hl) and "ingredient" not in hl else None)
            if guess:
                field, extra_head = guess, None
                if hb: page["field_badges"].setdefault(field, []).extend(hb)
                continue
            field, extra_head = "extra", h; page["extra"].setdefault(h, []); continue
        if ln.startswith("Ad disclaimer"):
            page["disclaimer"] = ln[len("Ad disclaimer"):].strip(); field = None; continue
        if ln.startswith("Landing page"):
            rest = ln[len("Landing page"):].strip()
            m = re.match(r"(.*?)\s*Last verified\s*(.*)$", rest)
            page["landing_page"], page["last_verified"] = (m.group(1).strip(), m.group(2).strip()) if m else (rest, "")
            field = None; continue
        if re.match(r"^More headlines on page \d+", ln) or re.match(r"^\d+ more headlines? beyond", ln):
            continue
        is_item = bool(LIST_ITEM.match(ln))
        item = LIST_ITEM.sub("", ln)
        item = re.sub(r"^CTA:\s*", "", item)
        text, ib = split_badges(item)
        if field == "who":
            if not page["who"]: page["who"] = text
            continue
        if field == "direction":
            if is_item: page["direction"].append(text)
            elif not page["truth"]: page["truth"] = text
            continue
        if field == "ingredient":
            if ingredient and is_item: page["ingredient_claims"][ingredient].append({"text": text, "badges": ib})
            elif not ingredient and is_item: page["ingredient_claims"].setdefault("(formula)", []).append({"text": text, "badges": ib})
            continue
        if field == "extra":
            page["extra"][extra_head].append(ln); continue
        if field in page and isinstance(page[field], list):
            if is_item:
                page[field].append({"text": text, "badges": ib})
            elif field in ("headlines", "quick_hits", "more_benefits", "ctas", "offers", "proof", "hard_nos") and not page["truth"] \
                    and field == "headlines" and not page["headlines"]:
                page["truth"] = text
            continue
        if not page["truth"] and field is None and not is_item and not page["who"] == text:
            page["truth"] = text
    return page


def globals_of(secs):
    """The global sections as text plus the numbers the gates copy from them."""
    g = {"hard_nos": [], "text": {}, "discount_to_feature": {}, "variant_max": {}, "logo": {}, "focal": None, "proof_split": None,
         "min_text_px": None, "shirtless_cap": None}
    for head, badges, lines, cat in secs:
        if norm(head) not in GLOBAL_HEADINGS:
            continue
        g["text"][head] = [l for l in lines if l.strip()]
        body = "\n".join(lines)
        if norm(head) == "global hard nos":
            g["hard_nos"] = [split_badges(LIST_ITEM.sub("", l.strip()))[0] for l in lines if LIST_ITEM.match(l.strip())]
        m = re.search(r"#### Discount to feature, by product\n(.*?)(?:\n\n|\nVariant)", body, re.S)
        if m:
            for l in m.group(1).splitlines():
                mm = re.match(r"-\s*([^:]+):\s*Save Up to (\d+)%", l.strip(), re.I)
                if mm: g["discount_to_feature"][mm.group(1).strip()] = int(mm.group(2))
        m = re.search(r"Variant maximums for reference:(.*)", body)
        if m:
            for part in m.group(1).split(";"):
                mm = re.match(r"\s*(.+?)\s+((?:[a-z][a-z ]*?\d+%)(?:\s*/\s*[a-z][a-z ]*?\d+%)*)\s*\.?\s*$", part.strip().split(". ")[0])
                if mm:
                    g["variant_max"][mm.group(1)] = {v.strip(): int(p) for v, p in re.findall(r"([a-z][a-z ]*?)\s*(\d+)%", mm.group(2))}
        # the bible renders its logo table as a flat list: Logo / 9:16 / 4:5 / Width / 40% / 29% / Height / 3.5% / 3.5%
        mm = re.search(r"\nLogo\n9:16\n4:5\nWidth\n(\d+)%\n(\d+)%", body)
        if mm: g["logo"] = {"9:16": int(mm.group(1)), "4:5": int(mm.group(2))}
        # focal mix: "40%\nPill-focused … 30%\nBottle-focused … 30%\nPerson-focused"
        mm = re.search(r"(\d+)%\s*\nPill-focused.*?(\d+)%\s*\nBottle-focused.*?(\d+)%\s*\nPerson-focused", body, re.S | re.I)
        if mm: g["focal"] = [int(x) for x in mm.groups()]
        mm = re.search(r"(\d+)% of graphics.*?(\d+)%,? with the Trustpilot.*?(\d+)% show neither", body, re.S | re.I)
        if mm: g["proof_split"] = [int(x) for x in mm.groups()]
        mm = re.search(r"[Mm]inimum[^\n]*?(\d+)\s*px", body)
        if mm: g["min_text_px"] = int(mm.group(1))
        mm = re.search(r"up to (\d+)% of creatives", body)
        if mm: g["shirtless_cap"] = int(mm.group(1))
    return g


def parse(md):
    secs = sections(md)
    model = {"version": version_of(md), "globals": globals_of(secs), "pages": {}, "order": []}
    for head, badges, lines, cat in secs:
        if norm(head) in GLOBAL_HEADINGS or not is_product(lines):
            continue
        model["pages"][head] = parse_page(head, badges, lines, cat)
        model["order"].append(head)
    return model


def load(path=BIBLE):
    if not os.path.exists(path):
        raise SystemExit(f"❌ {path} missing: sync the bible first (core/scripts/bible_sync.py)")
    return parse(open(path, encoding="utf-8").read())


def find_page(model, name):
    n, k = norm(name), key(name)
    for h in model["order"]:
        if norm(h) == n or key(h) == k:
            return h
    for h in model["order"]:
        if key(h.split("(")[0]) == k:
            return h
    return None


def sections_of(prod):
    secs = prod.get("bible_sections") or ([prod["bible_section"]] if prod.get("bible_section") else [prod.get("name", "")])
    return [s for s in secs if s]


def pages_for(model, prod):
    """The product's page(s); raises SystemExit naming a missing heading."""
    out = []
    for s in sections_of(prod):
        h = find_page(model, s)
        if not h:
            raise SystemExit(f"❌ {prod.get('id', '?')}: no bible section named '{s}' (product.json bible_sections). "
                             f"Sections: {', '.join(model['order'])}")
        out.append(model["pages"][h])
    return out


def _union(lists):
    seen, out = set(), []
    for lst in lists:
        for it in lst:
            k = norm(it["text"] if isinstance(it, dict) else it)
            if k and k not in seen:
                seen.add(k); out.append(it)
    return out


def merge(pages):
    """Men + Women pages → one dict. Lists are the union in page order; disclaimer and CTAs must agree (exit 1 otherwise)."""
    if not pages:
        raise SystemExit("merge(): no pages")
    m = {"headings": [p["heading"] for p in pages], "who": pages[0]["who"], "truth": pages[0]["truth"],
         "category": pages[0]["category"], "landing_page": pages[0]["landing_page"], "last_verified": pages[0]["last_verified"],
         "disclaimer": pages[0]["disclaimer"], "field_badges": {}, "ingredient_claims": {}, "extra": {}}
    for f in ("direction", "headlines", "quick_hits", "more_benefits", "ctas", "offers", "proof", "hard_nos"):
        m[f] = _union([p[f] for p in pages])
    for p in pages:
        for f, b in p["field_badges"].items():
            m["field_badges"].setdefault(f, []).extend(x for x in b if x not in m["field_badges"][f])
        for ing, items in p["ingredient_claims"].items():
            m["ingredient_claims"][ing] = _union([m["ingredient_claims"].get(ing, []), items])
        for h, ls in p["extra"].items():
            m["extra"].setdefault(h, []).extend(x for x in ls if x not in m["extra"][h])
    discs = {norm(p["disclaimer"]) for p in pages if p["disclaimer"]}
    if len(discs) > 1:
        raise SystemExit(f"❌ {m['headings']}: the pages carry different disclaimers; Justin must align them before a sync")
    ctas = [{norm(c["text"]) for c in p["ctas"]} for p in pages]
    if len(pages) > 1 and any(c != ctas[0] for c in ctas[1:]):
        raise SystemExit(f"❌ {m['headings']}: the pages carry different CTA lists; Justin must align them before a sync")
    return m


SAVE = re.compile(r"save up to (\d+)\s*%", re.I)


def offer_of(merged, globals_, name):
    """{pct, status: ok|placeholder|verify|none, source, cta, lines, variants}. Highest-discount rule (bible rule 09): the global
    'Discount to feature' table wins when the product is listed; else the product's own 'Save Up to N%' CTA; badges decide status."""
    o = {"pct": None, "status": "none", "source": "", "cta": "", "lines": [i["text"] for i in merged["offers"]],
         "variants": {}}
    save_ctas = [c for c in merged["ctas"] if SAVE.search(c["text"]) or "[PLACEHOLDER]" in c["text"] or "PLACEHOLDER" in c["badges"]]
    offer_badges = [b for i in merged["offers"] for b in i["badges"]] + [b for i in merged["offers"] if "PLACEHOLDER" in i["text"] for b in ["PLACEHOLDER"]]
    cta_badges = [b for c in save_ctas for b in c["badges"]]
    k = key(name)
    for prod, pct in globals_.get("discount_to_feature", {}).items():
        if key(prod) == k:
            o["pct"], o["source"] = pct, "Discount to feature, by product"
    for prod, vs in globals_.get("variant_max", {}).items():
        if key(prod) == k:
            o["variants"] = vs
    cta_pct = next((int(SAVE.search(c["text"]).group(1)) for c in save_ctas if SAVE.search(c["text"])), None)
    if o["pct"] is None and cta_pct is not None:
        o["pct"], o["source"] = cta_pct, "CTA"
    if "PLACEHOLDER" in offer_badges + cta_badges or any("[PLACEHOLDER]" in c["text"] for c in save_ctas):
        o["status"] = "placeholder"
    elif "VERIFY CURRENT" in offer_badges + cta_badges:
        o["status"] = "verify"
    elif o["pct"] is not None:
        o["status"] = "ok"
    if o["status"] == "ok":
        o["cta"] = f"Save Up to {o['pct']}%"
    return o


def cta_default_of(merged, offer):
    texts = [c["text"] for c in merged["ctas"]]
    if offer["status"] == "ok":
        for t in texts:
            if norm(t) == norm(offer["cta"]):
                return t
        return offer["cta"]
    for t in texts:
        if norm(t) == "ships free from pharmacy":
            return t
    return texts[0] if texts else "Ships Free From Pharmacy"


def cta_price_of(merged):
    return next((c["text"] for c in merged["ctas"] if "/day" in c["text"] or "/month" in c["text"]), "")


if __name__ == "__main__":
    import sys
    m = load(sys.argv[1] if len(sys.argv) > 1 else BIBLE)
    print(json.dumps({"version": m["version"], "pages": m["order"], "globals": {k: v for k, v in m["globals"].items() if k != "text"}},
                     indent=1, ensure_ascii=False))
