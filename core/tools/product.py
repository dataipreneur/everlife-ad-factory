"""Product settings for the shared tools.

Everything that differs between products (name, renders, verbatim disclaimer, name casing, review highlight, legacy
layout defaults, the colours finish_modern uses to find the product) lives in skills/everlife-<id>/product.json, never
in tool code. A job names its product in copy.json ("product": "<id>"). Tools stop when the product or its file is
missing: they never fall back to another product.

Skills are looked up in $EVERLIFE_SKILLS_DIR (default ~/.claude/skills, where install.sh links them).
"""
import json, os

SKILLS_DIR = os.path.expanduser(os.environ.get("EVERLIFE_SKILLS_DIR", "~/.claude/skills"))


def load(pid):
    path = os.path.join(SKILLS_DIR, f"everlife-{pid}", "product.json")
    if not os.path.exists(path):
        raise SystemExit(f"❌ No product.json for '{pid}' at {path} (install the skill, or set EVERLIFE_SKILLS_DIR)")
    P = json.load(open(path))
    P["_dir"] = os.path.dirname(path)
    return P


def for_copy(C, where="copy.json"):
    """The product named in a job's copy.json. Its disclaimer, if present, must be the product's verbatim text."""
    pid = C.get("product")
    if not pid:
        raise SystemExit(f'❌ {where} has no "product" (e.g. "product": "restora-z"); tools never guess the product')
    P = load(pid)
    if C.get("disclaimer") and C["disclaimer"] != P["disclaimer"]:
        raise SystemExit(f"❌ {where}: disclaimer differs from {pid}'s product.json (it must be the bible text, verbatim)")
    return P


def asset(P, name):
    return os.path.join(P["_dir"], "assets", name)


def path(P, rel):
    return os.path.join(P["_dir"], rel)
