---
name: resizing
description: Resize finished Everlife static ads between 4:5 (1080x1350) and 9:16 (1080x1920) by regenerating each ad on Creatify (GPT Image 2.5, ~1 credit each) and re-finishing it with the house logo, proof row and verbatim disclaimer. Use whenever the user says resize, "make the 9:16s", "make 4:5 versions", "convert these to 4:5 / 9:16", "fix these" for a folder of finished ads, or points at a folder of statics that only exist in one size. Works for every everlife-* product. Not for videos.
---

# Resizing skill (4:5 ⇄ 9:16 for finished statics)

> **⛔ PROMPT LAYOUT ZONES = `core/references/prompt-layout-zones.md` (via the skill's core link) (HARD, 2026-11-04):** every resize prompt carries that file's STRICT LAYOUT block with its numbers; it overrides every layout number below.

Approved 2026-11-04 on Nomel (Sermorelin, 4:5→9:16), Wolverine (9:16→4:5) and Spartan. User: "amazing!! keep on going!".
The user wants SPEED: batch everything, show side-by-side sheets fast, never ask per-ad questions.

**Never do these (all rejected):** paste the old ad onto an AI background plate (visible seams, disclaimer mid-frame: "bullshit");
crop a finished ad (cuts logo/headline/disclaimer); convert old ads the user didn't point at.

## How it works
The finished ad is fed to `gpt-image-2.5-sunburst/edit` on Creatify, which re-lays the SAME design (same person, product,
colours, text) for the new ratio WITHOUT logo, proof row or disclaimer. Then `finish_batch.py` adds the Everlife logo,
the same proof style the source had, and the verbatim disclaimer at the very bottom. Text is re-drawn by the model, so
every line is spelled out in the prompt and checked on the sheet.

Scripts: `~/.claude/skills/resizing/scripts/` (setup.py, put.sh, finish.sh, sheet.py, pack.sh). Python: `~/Everlife-Creative/tools/venv/bin/python`.

## Steps
1. **Inspect** the folder: `setup.py <folder> ~/Everlife-Creative/output/_<Product>-<target> <prefix>`. Trust the PIXEL size,
   not the filename (Spartan files named 1080x1920 were 4:5). Direction = the size they are NOT. Product id = the
   `everlife-<id>` skill (sermorelin, wolverine, spartan, …); check its `product.json` has a disclaimer.
2. **Read every ad** (`read_N.jpg`): write down each text line exactly, and its proof style: `trust` (Trustpilot · Doctor
   Prescribed · Ships Free), `count` (Trustpilot + Over 100,000 happy customers) or `none` (disclaimer only).
   Fix on the way: "Get Started Now" is banned → use the ad family's own CTA ("Build Your Plan", "Start Your Stack",
   "Explore the Spartan Stack"); fix source typos (e.g. "Activty"). Say what you changed in the report.
3. **Cost**: ~1 Creatify credit per ad + ~10-15% re-rolls. State it; the user's "go"/"do it" is the approval. Creatify only, never Higgsfield.
4. **Upload**: `mcp__creatify__upload_file` (filename, image/png) per ad → `put.sh <work> <id> '<upload_url>'` (expect 200;
   on 400 get a fresh link). Request links in parallel batches of 5-7; links live 1 h.
5. **Generate** (`mcp__creatify__model_playground_generate`, model `gpt-image-2.5-sunburst/edit`, `quality: high`,
   `output_format: png`, keep one `project_id` for the batch). `image_size`: 9:16 → `portrait_16_9`; 4:5 → `portrait_5_4`
   (returns 832x1040, finisher upscales). Append `id<TAB>asset_id<TAB>proof` to `<work>/assets.tsv` right away.
6. **Prompt template** (fill per ad):
   ```
   Resize the attached <4:5|9:16> ad into a <9:16 vertical (1080x1920)|4:5 feed (1080x1350)> ad. Keep the SAME design:
   <scene, person, props, style> , same <label colour>-label Everlife <PRODUCT> <form> exactly as in the attachment (do not
   invent, alter or substitute the product or the pill), same <icons/cards>, fonts and colours (<colours>).
   TEXT (spell exactly, nothing else): Headline: "…" / Subhead: "…" / lines… / Button: "…"
   REMOVE completely: the EVERLIFE logo, the <proof row if any>, and the small disclaimer text. No logo, stars or small print.
   LAYOUT … (below) … Photoreal, sharp, label readable.
   ```
   - **LAYOUT = the STRICT LAYOUT block from `core/references/prompt-layout-zones.md` (via the skill's core link), pasted word for
     word with its numbers (HARD, Mitansh 2026-11-04).** 9:16: ZONE A y 0-330 of 2048 empty (name the surface), ZONE B 340-1150
     all text + product (product base ~y 800, CTA above y 950), ZONE C plain calm surface, everything inside x 190-960.
     4:5: top 14% empty, elements top-to-bottom with the product LAST and lowest (base ~63%), bottom 33% plain, 7% side margins.
     Always add "DO NOT draw any EVERLIFE logo or wordmark except on the product labels". (The old 12% / 70% numbers here were
     wrong: they put headlines under the logo.)
7. **Collect**: `model_playground_get` each asset (don't loop fast; 1-4 min each), `curl` the output URL to `raw/<id>.png`.
8. **Finish**: `finish.sh <work> <9:16|4:5> <product id>` (same proof as the source; finishes AS IS with `--shift 0`, never moves the image; a FAIL = re-roll with the zones block, or drop the footer).
9. **QA every ad** with `sheet.py <work> sheet_X.jpg <9x16|4x5> ids…` and LOOK: logo not doubled (model sometimes draws
   its own), products NOT under the proof row or footer scrim, no text cut, spelling, CTA swapped. Fail → re-roll once
   (1 credit, tell the user). Second fail → set aside in `rejected/` and list it; never ship it. Drop a proof row ONLY if the
   user asks (gate: never swap planned proof to none on your own). The user may also ask to ADD a footer to a none ad:
   change its proof in assets.tsv and re-run finish.sh (free).
10. **Show** the side-by-side sheets as soon as each batch is done (open them), then **pack**:
    `pack.sh <work> ~/Desktop/<Product>-All-Sizes <srcTag> <targetTag>` → `imageN_4x5.png` + `imageN_9x16.png` + key.txt.
    macOS can't use ":" in names, so 4x5 / 9x16 (say so once).
11. **Drive**: the Drive connector only takes base64 (too big for ~1.8 MB PNGs). Copy the requested size into its own Desktop
    folder, `open` it and the Drive folder URL, and tell the user to ⌘A + drag (10 s). Offer Chrome automation as a fallback.

## Report (short)
Folder path, N pairs, what was changed (CTA swaps, typos, footers), what's set aside and why, credits used. Remind: drafts
until creative review + Jeremy's compliance sign-off; headlines may run wider than Meta's 9:16 safe column (156-924) when the
source was full-width, so flag it once and offer a narrower re-roll.

Related memory: resize-45-to-916-regen.

## Standing rules from the user (2026-11-04)
- If the proof row/footer covers the product, button or text after finishing: **drop the footer** (`--proof none`, free) without asking. Only re-roll when dropping the footer doesn't fix it.
- Ads with a woman + intimacy wording (PT-141, Lovara) get blocked by GPT Image's filter ~30%: send those straight to `nano-banana-pro/edit` (aspect_ratio 9:16 / 4:5, resolution 2K, 1.5 cr) and resize the output to 1080 wide before finishing.
- Never stop between batches: keep uploading/generating the next batch while the previous one renders.
- **NEVER shrink/pad a raw onto a blurred copy of itself** (user, 11-04: "why the fuck did you have blurry backgrounds"). To add a footer where the CTA/product sits too low: re-roll with the CTA ending above 54%, never pad, never shift up.
