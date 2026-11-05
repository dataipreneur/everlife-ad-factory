#!/usr/bin/env python3
"""Print a product's current bible copy as exact strings to paste into prompts (from references/bible.json, generated).

    product_copy.py pt-141            # offer, default CTA, all CTAs, quick-hits, more benefits, headlines, retired
    product_copy.py pt-141 --json     # the whole bible.json
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(HERE))


def find(pid):
    for root in (os.path.join(REPO, "skills"), os.path.expanduser("~/.claude/skills")):
        p = os.path.join(root, f"everlife-{pid}", "references", "bible.json")
        if os.path.exists(p):
            return p
    return None


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pid = sys.argv[1].replace("everlife-", "")
    p = find(pid)
    if not p:
        sys.exit(f"❌ no references/bible.json for {pid}: run bible_pipeline.py regen")
    b = json.load(open(p, encoding="utf-8"))
    if "--json" in sys.argv:
        print(json.dumps(b, indent=1, ensure_ascii=False)); return
    o = b.get("offer", {})
    print(f"{b['name']} · bible version {b['version']} · sections {', '.join(b['sections'])}")
    print(f"Who: {b.get('who')}")
    if b.get("truth"): print(f"What: {b['truth']}")
    if o.get("status") == "ok":
        print(f"OFFER: {o['cta']}   (highest discount; source: {o.get('source')})")
    else:
        print(f"OFFER: none usable ({o.get('status')}): no % and no price on this product")
    print(f"DEFAULT CTA: {b['cta_default']}")
    print("CTAs:        " + " · ".join(b["ctas"]))
    if b.get("cta_price"): print(f"PRICE CTA:   {b['cta_price']}  (the only $ amount allowed)")
    print("QUICK-HITS (word for word): " + " · ".join(b["benefits_quick"]))
    more = [x["text"] + (f" [{', '.join(x['badges'])}]" if x["badges"] else "") for x in b.get("benefits_more", [])]
    if more: print("MORE BENEFITS: " + " · ".join(more))
    heads = [x["text"] + (f" [{', '.join(x['badges'])}]" if x["badges"] else "") for x in b.get("headlines", [])]
    if heads: print("HEADLINES (references, not limits): " + " · ".join(heads))
    print("PROOF: " + " · ".join(b.get("proof", [])))
    if b.get("hard_nos"): print("PRODUCT HARD NOs: " + " · ".join(b["hard_nos"]))
    scr = {k: v for k, v in (b.get("screen") or {}).items() if not v["status"].startswith("✅")}
    if scr: print("FLAGGED: " + " · ".join(f"{k} → {v['status']}" for k, v in scr.items()))
    if b.get("retired"): print("RETIRED (never): " + " · ".join(r["line"] if isinstance(r, dict) else r for r in b["retired"]))
    print(f"DISCLAIMER (verbatim): {b.get('disclaimer')}")


if __name__ == "__main__":
    main()
