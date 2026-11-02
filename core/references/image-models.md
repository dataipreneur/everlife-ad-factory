# Image model choice per batch (every product skill, from 2026-10-29)

> **⛔ NEVER `reposition_916.py` / shrink / edge-stretch / blur a raw (Mitansh, 2026-11-02: "why the hell are these things blurry on the edges! Who told you to do that!").** This overrides every older line in this skill that calls `reposition_916.py` "the fix". Finish the raw AS IS: `finish_batch.py <raw> <out> --ratio 9:16 --product <id> --fit trusted --shift 0`. If its text or product runs into the footer, the raw is a FAIL: re-roll it with the LAYOUT block (ask for the lowest element at 40%, top 12% empty), with the cost approved. Never ship a smeared edge.

All images are made on Creatify, through two connectors that both sign in with the Creatify account (no API key anywhere):
- **Ad Agent connector** (`plugin:creatify-ad-agent`, tools `composer_*`): `composer_edit_image` is hard-wired to **GPT Image 2.5**.
  Tested 2026-10-29: a request naming another model still renders on `gpt-image-2.5-sunburst`. This is the batch default.
- **Creatify MCP server** (`creatify`, `https://api.creatify.ai/mcp`, added with `claude mcp add --transport http --scope user creatify
  https://api.creatify.ai/mcp`, then `/mcp` → sign in): its **Model Playground** tools run any Creatify image model and charge the SAME
  workspace credits: `model_playground_list_models(media_type="image", query)`, `model_playground_get_model_schema(model_name)`,
  `model_playground_generate(model_name, input_params, project_id)`, `model_playground_get(asset_id)`. This is how Nano Banana runs.
(The REST route via `core/tools/creatify_gen.py` + `~/Everlife-Creative/creatify.env` still works as a fallback for a machine without
the MCP; it bills Creatify API-plan credits instead.)

## The question (in the image setup round, one more question; Mitansh 2026-10-29: "keep these 3")
**Image model:** "GPT Image 2.5 via the connector (Recommended: proven on every batch so far, 1 workspace credit/image)" /
"Nano Banana 2.1 (1 API credit/image at 1K, 1.5 at 2K; strong product fidelity)" / "Nano Banana Pro (1.5 API credits/image at 1K or
2K; the top Google model)". No other options are offered (Creatify has more; they stay off the menu unless Mitansh adds one). One model
per batch (comparing models = two batches). Quote the batch from the price table below; the tool prints `credits_used` after each task.

## Setup once per machine (any non-default model)
1. Register the Creatify MCP once: `claude mcp add --transport http --scope user creatify https://api.creatify.ai/mcp`, start a new
   session, type `/mcp`, choose **creatify**, approve the sign-in in the browser. Preflight reports whether it is connected.
2. The Playground fetches reference images by URL. Upload each render once with `upload_file(filename, content_type="image/png")`
   (presigned: `curl -X PUT -H "Content-Type: image/png" --upload-file <render> "<upload_url>"`) and store the returned `cdn_url` in
   the skill's `assets/creatify.json` as `"render_urls": {"<render file>": "<cdn_url>"}`. Reuse forever.

## Generating with a non-default model (in the session, no shell needed)
1. `model_playground_get_model_schema(model_name="nano-banana-2.1/edit")` once per session: read the field names (expect `prompt`,
   `image_urls`, `aspect_ratio`, `resolution`, `num_images`, `output_format`; Nano Banana Pro is `nano-banana-pro/edit`). If the
   playground lists a different identifier, take it from `model_playground_list_models(media_type="image", query="nano banana")`.
2. `model_playground_generate(model_name=…, input_params={"prompt": <the slot's prompt>, "image_urls": [<render cdn_url>],
   "aspect_ratio": "9:16", "resolution": "1K"}, project_id=<the skill's Ad Agent project, optional>)` → `asset_id`. Up to 4 in flight.
3. `model_playground_get(asset_id)` until done → download the output URL with curl into `gen/b<date>_<n>.png`.
4. Same QA, same `finish_batch.py`. Log the model and the credits in `prompts.md` and SESSION.md.
Keep the prompt template unchanged; "use the attached product reference exactly" means the `image_urls` reference here.

## Prices (Creatify docs, "AI Image, Video and Audio Model API Pricing", read 2026-10-29; credits per output image)
One credit pool: the Ad Agent connector and the Model Playground both spend the **workspace** credits (`composer_billing_state`).
(Only the REST fallback bills a separate API plan.) Quote the batch from this table (image_to_image = reference attached):

| Model (image_to_image `model_name`) | 1K | 2K | 4K | Notes |
|---|---|---|---|---|
| GPT Image 2.5 via the connector (`composer_edit_image`) | 1.0 | | | the default; 2K output |
| `nano-banana-2.1/edit` | 1.0 | 1.5 | 2.0 | aspect_ratio 9:16 / 4:5 / 1:1; up to 7 references; default resolution 1K |
| `nano-banana-pro/edit` | 1.5 | 1.5 | 3.0 | same fields; default resolution 1K |

(Off the menu but reachable through the playground by exact model_name if Mitansh asks: Seedream 5 Pro 0.5, Flux 2 Pro 0.5,
GPT Image 2.5 via the API 0.5–2.5 by quality, Recraft 0.5, Wan 0.5/1.0.)

Text-to-image twins (no reference) cost the same; we never use them for product ads (the render must be attached).
So: a batch of 5 = 5 credits on GPT Image 2.5, 5 on Nano Banana 2.1 at 1K (7.5 at 2K), 7.5 on Nano Banana Pro. Confirm with the
playground's own `credits` field on the first generation and put the real number in prompts.md. The tool prints `credits_used` after every task; put the real number in prompts.md.

## Model notes (update as batches teach us)
All three models are reachable with NO API keys through the Creatify connector's model playground tools (`model_playground_generate`); the `creatify_gen.py` API route is optional.
| Model | Good for | Watch |
|---|---|---|
| GPT Image 2.5 (connector) | whole-ad layouts with clean type; the default | places the product 8–15% lower than asked |
| Nano Banana 2.1 | product fidelity from a reference, photoreal materials | type can drift: QA every string |
| Nano Banana Pro | the same, highest fidelity and texture; BPC-157 batch 1: best type + scenes so far, 4/5 labels perfect | 1.5× the price; via the connector playground (`nano-banana-pro/edit`, no API keys); content lands at 70-75% → `reposition_916.py`; its edit calls do NOT reposition (never pay for one) |

Log the model used in `prompts.md` and SESSION.md for every batch so winners can be traced to a model.
