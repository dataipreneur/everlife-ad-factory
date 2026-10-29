"""Creatify Asset Generator: generate an image with a Creatify image model other than the connector's GPT Image 2.5.
The skills offer three models (Mitansh, 2026-10-29): GPT Image 2.5 (connector), Nano Banana 2.1 and Nano Banana Pro (this tool).
Any other Creatify model still works here by exact model_name, but is not offered in the batch question.

Creatify REST API (https://docs.creatify.ai/api-documentation/ai-generation/ai-generation): the caller picks `model_name`; models and
their input schemas come from GET /api/asset_generator/schemas/. Credentials: X-API-ID + X-API-KEY from the Creatify settings page,
stored OUTSIDE git in ~/Everlife-Creative/creatify.env as two lines:
    CREATIFY_API_ID=...
    CREATIFY_API_KEY=...
(or exported in the environment). Nothing here is cached from memory: the model list is read live and saved to ~/Everlife-Creative/creatify-models.json.

usage:
  creatify_gen.py models [--refresh]                      list image models (text_to_image / image_to_image) with their input fields
  creatify_gen.py schema <model_name>                     print one model's input schema
  creatify_gen.py create --model <model_name> --prompt "<text>" [--image <url> ...] [--aspect 9:16] [--resolution 2k] \
                         --out gen/x.png [--param key=value ...] [--timeout 600]
      Picks the right field names from the model's schema (prompt / image URL(s) / aspect ratio / resolution), creates the task,
      polls until done, downloads the first asset to --out, prints the credits used. Costs Creatify credits: get the user's OK first.
  creatify_gen.py get <task_id>                           show a task
Image references must be URLs (the API fetches them): upload the render once with the Ad Agent connector's upload_file and keep
the URL in the skill's assets/creatify.json ("render_url").
"""
import argparse, json, os, sys, time, urllib.request, urllib.error

BASE = "https://api.creatify.ai"
HOME = os.path.expanduser("~/Everlife-Creative")
ENV = os.path.join(HOME, "creatify.env")
CACHE = os.path.join(HOME, "creatify-models.json")
IMAGE_TYPES = ("text_to_image", "image_to_image")
# menu names the skills use → exact Creatify model_name (image_to_image: the render is attached). Prices: core/references/image-models.md
MENU = {
    "gpt image 2.5": "gpt-image-2.5-sunburst/edit", "gpt-image-2.5": "gpt-image-2.5-sunburst/edit",
    "nano banana 2.1": "nano-banana-2.1/edit", "nano banana pro": "nano-banana-pro/edit", "nano banana 2": "nano-banana-2/edit",
    "nano banana 2 lite": "nano-banana-2-lite/edit", "nano banana": "nano-banana/edit",
    "seedream 5": "bytedance/seedream/v5/pro/edit", "seedream 5.0 pro": "bytedance/seedream/v5/pro/edit", "seedream 4": "bytedance/seedream/v4/edit",
    "flux 2 pro": "flux-2-pro/edit", "flux kontext": "flux-pro/kontext/max/multi",
    "grok image 2": "grok-imagine-image/v2.0/edit", "recraft v3": "recraft/v3/image-to-image",
    "wan 2.7": "wan2.7-image/image-to-image", "wan 2.7 pro": "wan2.7-image/pro/image-to-image",
}
PRICE = {"gpt-image-2.5-sunburst/edit": "0.5 (quality low/medium) · 1.0 high · 1.5 xhigh · 2.5 max (default!)",
         "nano-banana-2.1/edit": "1.0 at 1K · 1.5 at 2K · 2.0 at 4K", "nano-banana-pro/edit": "1.5 at 1K/2K · 3.0 at 4K",
         "nano-banana-2/edit": "from 1.0", "nano-banana-2-lite/edit": "0.5", "nano-banana/edit": "0.5",
         "bytedance/seedream/v5/pro/edit": "from 0.5", "bytedance/seedream/v4/edit": "0.5", "flux-2-pro/edit": "0.5",
         "flux-pro/kontext/max/multi": "1.0", "grok-imagine-image/v2.0/edit": "from 0.5", "recraft/v3/image-to-image": "0.5",
         "wan2.7-image/image-to-image": "0.5", "wan2.7-image/pro/image-to-image": "1.0"}


def creds():
    cid, key = os.environ.get("CREATIFY_API_ID"), os.environ.get("CREATIFY_API_KEY")
    if (not cid or not key) and os.path.exists(ENV):
        for ln in open(ENV):
            if "=" in ln and not ln.strip().startswith("#"):
                k, v = ln.strip().split("=", 1); v = v.strip().strip('"').strip("'")
                if k == "CREATIFY_API_ID": cid = cid or v
                if k == "CREATIFY_API_KEY": key = key or v
    if not cid or not key:
        raise SystemExit(f"❌ Creatify API credentials missing. Put CREATIFY_API_ID and CREATIFY_API_KEY in {ENV} "
                         "(Creatify → Settings → API). Never commit them.")
    return cid, key


def api(method, path, body=None):
    cid, key = creds()
    req = urllib.request.Request(BASE + path, method=method, headers={"X-API-ID": cid, "X-API-KEY": key, "Content-Type": "application/json"},
                                 data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode() or "null")
    except urllib.error.HTTPError as e:
        raise SystemExit(f"❌ Creatify API {e.code} on {method} {path}: {e.read().decode()[:600]}")


def models(refresh=False):
    if not refresh and os.path.exists(CACHE) and time.time() - os.path.getmtime(CACHE) < 86400:
        return json.load(open(CACHE))
    data = api("GET", "/api/asset_generator/schemas/")
    items = data.get("results", data) if isinstance(data, dict) else data
    imgs = [m for m in items if m.get("generation_type") in IMAGE_TYPES]
    os.makedirs(HOME, exist_ok=True); json.dump(imgs, open(CACHE, "w"), indent=1)
    return imgs


def find(name, ms):
    """Exact model_name, else the single model whose name contains every word of `name` (case-insensitive)."""
    name = MENU.get(name.lower().strip(), name)
    for m in ms:
        if m["model_name"] == name: return m
    words = [w for w in name.lower().replace("-", " ").replace("/", " ").split() if w]
    hits = [m for m in ms if all(w in m["model_name"].lower().replace("-", " ").replace("/", " ") for w in words)]
    if len(hits) == 1: return hits[0]
    if not hits: raise SystemExit(f"❌ no Creatify image model matches '{name}'. Run: creatify_gen.py models")
    raise SystemExit("❌ ambiguous model name '" + name + "': " + ", ".join(h["model_name"] for h in hits))


def props(m):
    return (m.get("input_params_schema") or {}).get("properties") or {}


def field(m, *cands, contains=None, types=None):
    """The schema field whose name matches a candidate (or contains a word), optionally filtered by JSON type."""
    P = props(m)
    for c in cands:
        if c in P: return c
    if contains:
        for k, v in P.items():
            if contains in k.lower() and (not types or v.get("type") in types): return k
    return None


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("models"); s.add_argument("--refresh", action="store_true")
    s = sub.add_parser("schema"); s.add_argument("model")
    s = sub.add_parser("get"); s.add_argument("task_id")
    s = sub.add_parser("create")
    s.add_argument("--model", required=True); s.add_argument("--prompt", required=True)
    s.add_argument("--image", action="append", default=[], help="reference image URL (repeatable)")
    s.add_argument("--aspect", default="9:16"); s.add_argument("--resolution", default=None)
    s.add_argument("--param", action="append", default=[], help="extra key=value for the model schema")
    s.add_argument("--out", required=True); s.add_argument("--timeout", type=int, default=600)
    a = ap.parse_args()

    if a.cmd == "models":
        ms = models(a.refresh)
        for m in sorted(ms, key=lambda x: x["model_name"]):
            P = props(m); req = (m.get("input_params_schema") or {}).get("required") or []
            print(f"{m['model_name']:48s} {m['generation_type']:15s} credits: {PRICE.get(m['model_name'], '?'):42s} fields: " + ", ".join(f"{k}{'*' if k in req else ''}" for k in P))
        print(f"\n{len(ms)} image models (cached in {CACHE}; --refresh to re-read)"); return
    if a.cmd == "schema":
        print(json.dumps(find(a.model, models()), indent=1)); return
    if a.cmd == "get":
        print(json.dumps(api("GET", f"/api/asset_generator/{a.task_id}/"), indent=1)); return

    ms = models(); m = find(a.model, ms); P = props(m)
    params = {}
    pf = field(m, "prompt", contains="prompt", types=("string",))
    if not pf: raise SystemExit(f"❌ {m['model_name']} has no prompt field: {list(P)}")
    params[pf] = a.prompt
    if a.image:
        imf = field(m, "image_urls", "image_url", "images", "image", "reference_image_urls", "reference_images", contains="image")
        if not imf: raise SystemExit(f"❌ {m['model_name']} takes no image reference (fields: {list(P)}); use a text_to_image prompt or another model")
        params[imf] = a.image if P[imf].get("type") == "array" else a.image[0]
    elif m["generation_type"] == "image_to_image":
        raise SystemExit(f"❌ {m['model_name']} is image_to_image: pass --image <url>")
    af = field(m, "aspect_ratio", contains="aspect")
    if af and a.aspect:
        enum = P[af].get("enum")
        if enum and a.aspect not in enum: raise SystemExit(f"❌ {m['model_name']} aspect ratios: {enum}")
        params[af] = a.aspect
    elif "image_size" in P and a.aspect:
        size = {"9:16": "portrait_16_9", "4:5": "portrait_4_3", "3:4": "portrait_4_3", "1:1": "square_hd", "16:9": "landscape_16_9"}.get(a.aspect)
        enum = P["image_size"].get("enum") or []
        if size and size not in enum and size == "square_hd": size = "square"
        if size and (not enum or size in enum): params["image_size"] = size
    if "quality" in P and not any(kv.startswith("quality=") for kv in a.param):
        params["quality"] = "high"      # GPT Image: the API default is "max" (2.5 cr); high = 1.0 cr, the connector's price class
    rf = field(m, "resolution", contains="resolution")
    if rf and a.resolution: params[rf] = a.resolution
    for kv in a.param:
        k, v = kv.split("=", 1)
        try: v = json.loads(v)
        except Exception: pass
        params[k] = v
    print(f"model {m['model_name']}  price: {PRICE.get(m['model_name'], 'see Creatify docs')} API credits per image", flush=True)
    t = api("POST", "/api/asset_generator/", {"model_name": m["model_name"], "input_params": params})
    tid = t["id"]; print(f"task {tid} created (status {t.get('status')})", flush=True)
    t0 = time.time()
    while True:
        t = api("GET", f"/api/asset_generator/{tid}/")
        st = t.get("status")
        if st == "done": break
        if st == "failed": raise SystemExit(f"❌ task {tid} failed: {t.get('failed_reason')}")
        if time.time() - t0 > a.timeout: raise SystemExit(f"❌ task {tid} still {st} after {a.timeout}s; check later: creatify_gen.py get {tid}")
        time.sleep(6)
    assets = t.get("assets") or []
    if not assets: raise SystemExit(f"❌ task {tid} done but no assets: {json.dumps(t)[:400]}")
    url = assets[0]["url"]
    os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
    urllib.request.urlretrieve(url, a.out)
    print(f"done {a.out}  model={m['model_name']}  credits_used={t.get('credits_used')}  url={url}")


if __name__ == "__main__":
    main()
