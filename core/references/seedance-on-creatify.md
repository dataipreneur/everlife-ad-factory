# ⛔ HARD RULE: every Seedance video runs on Creatify; Higgsfield is only for Marketing Studio (Mitansh, 2026-11-03)

> Mitansh, 2026-11-03: "Alright, this should be the new rule for videos! All Seedance videos goes to Creatify, remove higgs!
> Higgs would only go for marketing studio!"

Applies to **every Everlife video in every product skill** (all `everlife-*` skills, including new ones built by
`everlife-new-product`). It **overrides** every older line that says `higgsfield generate create seedance_2_5 …`,
`seedance_2_0 …`, "Seedance on Higgsfield", "Seedance ~45 / 67.5 cr", "Unlimited mode in Chrome", or that routes
any Seedance, image-to-video, animated-still or start-frame step through Higgsfield.

## The rule
1. **Seedance (any version, any mode) = the Creatify Model Playground**, never the Higgsfield CLI, MCP or web UI.
2. **Higgsfield = Marketing Studio only** (`marketing_studio_video`: UGC, ugc_how_to, ugc_unboxing, product_review, with or
   without a `--hook_id`). Nothing else spends Higgsfield credits: no Seedance, no stills, no Soul, no upscales.
3. Hook stills, start frames and image batches also go to Creatify (GPT Image 2.5 Sunburst edit, or Nano Banana via the
   Playground). Music = Creatify `composer_generate_music` (Lyria). Boreal-H3 = Creatify. The AI Avatar Video route was already
   all-Creatify.
4. Spend approval is unchanged: quote the cost (Creatify credits) and get the user's OK first; report the real `credits_cost` the
   moment a job is submitted. Show a running total.

## How (proven 2026-11-03 on Wolverine V3 "Breakthrough" and V4 "Run-Through")
1. Upload each reference (the product render, the hook still): `creatify.upload_file(filename, content_type)` → PUT the bytes to
   `upload_url` with `curl -X PUT -H "Content-Type: …" --data-binary @file` → use `cdn_url`.
2. Start still (~1 cr): `model_playground_generate("gpt-image-2.5-sunburst/edit", {image_urls:[render cdn_url], image_size:
   "portrait_16_9", quality:"high", prompt})`. Download the output, LOOK at it, show it.
3. Video: `model_playground_generate("bytedance/seedance-2.5/reference-to-video", {image_urls:[start still, product render],
   duration:"15", aspect_ratio:"9:16", resolution:"720p", generate_audio:true, prompt})`. Refer to the images in the prompt as
   `@image1` (start / look) and `@image2` (the product, "reproduce it EXACTLY"); "The video OPENS EXACTLY on @image1" locks frame 0.
   Single-image alternative: `bytedance/seedance-2.5/image-to-video` (`image_url` = the start frame, optional `end_image_url`).
4. Poll `model_playground_get(asset_id)` (wait ~4 min for 15 s; never leave the user waiting without an update), download
   `outputs[0].url` to `<job>/out/raw.mp4`, run the skill's QA, and show the raw right away (open it + a contact sheet).

**Team logs (every video made with this recipe, `core/team-logs/TEAM-LOGS.md`):** before writing the script, read this product's Copy Ledger rows (never reuse a logged hook, line or CTA). Log every paid generation (still, clip, music) to the Prompt & Outcome Log **the moment its job is submitted** (inputs, exact prompt, refs, model, credits), then update that record after QA (pass/fail, reasons, re-takes), the final video's spoken lines, captions, CTA and proof to the Copy Ledger, and the run's spend to the Activity & Spend Log. Unreachable → the pending file, never block. Build every record with `core/scripts/teamlog.py` (it saves the exact prompt and checks the record; TEAM-LOGS §6) and send the file it prints. `teamlog.py close <job>` ✅ before SESSION.md.

**Costs seen (Creatify credits):** Seedance 2.5 reference-to-video 15 s 720p = **34.25** · Seedance 2.5 image-to-video 10 s 480p
≈ 10.25 · GPT Image 2.5 still = 1 · Lyria music = 0.8. Roughly half the credits of the old Higgsfield Seedance route
(≈ 67.5 for 15 s 720p), but the two are different currencies: compare dollars only with each plan's price per credit.

## Where the old routes used to be
Skills' `video-prompting.md`, `animated-still.md`, `styles/INDEX.md` routing tables, `SKILL.md` model lists and the Hook Engine
mentioned Higgsfield Seedance commands. Read every such line as "the same Seedance call on the Creatify Model Playground". Animated
stills: `bytedance/seedance-2.5/image-to-video` with the raw static as `image_url`, `duration:"8"`, `generate_audio:false`
(or the 0-credit `animate_code.py` route).
