# Titan-Rx product renders (✅ all in)

Source: the local asset library `~/Everlife-Creative/asset-library/TABLETS-CAPSULES/TITAN-RX/` (Drive TABLETS/CAPSULES folder),
looked at one by one on 2026-11-02. Check against the website before the first paid batch.

| File | What it is | Made from |
|---|---|---|
| `titan-rx_bottle.png` | the Titan-Rx bottle, transparent background (721×1364) | `TITAN-RX BOTTLE_.webp` (already transparent; kept; fully transparent pixels set to white so no hidden colour shows through) |
| `titan-rx_bottle_ref.jpg` | the same bottle flattened on white: attach this one to image models | the PNG above |
| `titan-rx_capsule.png` | ONE capsule, transparent background (1145×452) | `TITAN-RX CAPSULE.jpg` (white background cut out by flood fill from the edges; checked on green: clean edges, no white fringe, highlights inside the capsule kept) |
| `titan-rx_capsule_ref.jpg` | the same capsule flattened on white: attach this one to image models | the PNG above |

Hidden-pixel check (2026-11-02): no coloured pixels under transparency in either PNG.

## Bottle label (exact text, top to bottom)
Matte black bottle, matte black screw cap with a ribbed band, a bright chrome ring under the cap and a chrome base ring; two
brushed-steel diagonal swooshes on the lower sides.
- `EVERLIFE®` (white, the Everlife logotype with the stylised E)
- `TITAN-RX` (very large, brushed-chrome letters; the A has a red chevron inside it)
- `TADALAFIL + VARDENAFIL + L-ARGININE` (white)
- a short white rule
- `3-IN-1 INTIMACY SUPPORT` (white, tracked caps) / `FOR MEN` (grey)
- a chrome male symbol (♂)
- `30 CAPSULES`
- `RX ONLY | PRESCRIPTION USE ONLY`

Prompt wording: "a matte black bottle with a black cap and chrome rings; the label reads EVERLIFE, then a large brushed-chrome
TITAN-RX with a red chevron in the A, then TADALAFIL + VARDENAFIL + L-ARGININE, 3-IN-1 INTIMACY SUPPORT FOR MEN, a chrome male
symbol and 30 CAPSULES". The label is the product's own text: fine in the picture. Our COPY never adds "30 capsules", a count or a
strength, and "3-in-1 Intimacy Support" is label text, not a bible claim (use the bible's "3-in-1 Performance Formula").

## Capsule
A mirror-chrome two-piece capsule (a fine seam in the middle) printed `TITAN-RX` in brushed silver letters, the A with the same red
chevron. Never describe it in prompts beyond "use the attached capsule reference exactly; do not invent, alter, or substitute a
different pill; exactly one capsule". It is the hero (gates §3): larger in frame than the bottle.

Reflective chrome picks up the scene: expect the model to tint it (warm light → gold). QA: still reads as chrome/silver, the
TITAN-RX print legible and not mirrored.

## Still missing
- Higgsfield Marketing Studio registration (title "Titan-Rx"): NOT done; preflight prints the command. Use the white-flattened copies.
- `assets/creatify.json` (Creatify project): created on the first image run (`composer_project_create`, then import
  `titan-rx_bottle_ref.jpg` + `titan-rx_capsule.png`), never with another product's assets.
