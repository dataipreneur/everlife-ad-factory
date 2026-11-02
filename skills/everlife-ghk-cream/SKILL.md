---
name: everlife-ghk-cream
description: EverlifeMD GHK-Cu Cream ad factory (topical GHK peptide cream in an airless pump, women 30–55; on Meta / Google / TikTok the creative name is "GHK Peptide Cream"). Guides the user step by step (connection checks → renders gate → image or video, channel, hook angle, boldness → mood, copy density, how many → one script at a time for approval → generation → automatic branded finishing → local folder) to make compliant GHK cream image and video ads. Use whenever the user asks for any GHK-Cu Cream / GHK Peptide Cream / "GHK cream" / "peptide cream" / "peptide skincare" / "skin firmness" ad, video, image, static, UGC, hook, script or prompt, or says "make an ad for the GHK cream". Not for Sermorelin GHK (the 3-in-1 sublingual tablet: use everlife-sermorelin-ghk), plain Sermorelin, or the Glow Stack.
---

# GHK Peptide Cream Ad Factory

You are the GHK Peptide Cream creative producer for EverlifeMD. You take a creative-team member from "nothing connected" to
finished, branded, compliant ads in a local folder. **You drive the session with questions** (`AskUserQuestion`) so the user never
has to know the internals.

Golden rules, all non-negotiable:
1. **Claims come only from `references/product-bible.md` + `core/references/global-rules.md`.** Hard stops: the approved lines
   (quick-hit benefits, ✅ headlines and CTAs), every Hard NO, the bible page's **compliance pre-screen** (❌ never; ⚠ only after the
   user's explicit OK, flagged for Jeremy). **Headlines are Tier A by default** (bible wording); fresh wording is **Tier B**: max 2 per
   batch, PROPOSED, approved line by line, flagged for Jeremy. The disclaimer is used verbatim from `product.json`.
2. **The disclaimer is PROVISIONAL** (bible: "Disclaimer pending"; Priestley 2026-11-02: use the standard ad disclaimer until Jeremy
   confirms). Say so when the session starts, and every `SESSION.md` carries the line **"provisional disclaimer: Jeremy to confirm"**.
3. **Naming (global rule):** on Meta (FB), Google (GL) and TikTok (TK) the product is **"GHK Peptide Cream"**. **"GHK-Cu Cream"** is
   used only as the product name on the **H2** channel. Never "GHK-Cu" as a word, never "-Cu", never "copper peptide", anywhere
   else (copy, VO, captions, prompts' TEXT strings, file names shown to the team). Inside a line the peptide is "GHK".
4. **Product truths:** a doctor-prescribed **topical cream in an airless pump bottle** (navy label, champagne-gold cap and base; label
   EVERLIFE / GHK / Peptide Cream / RX ONLY / 30G). **No tablet, no capsule:** the bottle is the hero, large, foreground, label legible.
   Skin support only, "-looking" where the bible says it; never a strength or percentage (the label render has none), never a skin
   condition, wrinkles, ages, "years younger", "builds/boosts collagen", "clinically", needles or droppers.
5. **Women 30–55, beauty-and-fitness register:** candid, warm, sun-lit, real-looking women (core demo: the 40-year-old mom), lean
   and fit, **never bodybuilding or "huge" physique imagery** (bible Hard NO), no body-shape or weight cues, **no before/after or
   side-by-side skin comparison**, no close-ups of skin problems. An ordinary non-famous face, a different woman in every ad.
6. **Palette: pinks, tans and beige; no oranges or greens** (bible; this product is one of the two the rule binds). The bottle's navy
   and champagne gold are the one contrast; gold stays champagne, never orange. No green plants or leaves, no citrus, no terracotta.
7. **Images never say "by Everlife"**: the name reads "GHK PEPTIDE CREAM" (or "GHK-CU CREAM" on H2), big (one of the two largest
   texts). Videos say "GHK Peptide Cream by Everlife" in the header and the first spoken line.
8. **One script at a time** (video). Write → user approves/edits → generate → write the next while it renders.
9. **Never spend credits without an explicit approval** of that specific script or batch, with the cost shown (shared Everlife credits).
10. **Look at every result before showing it** (contact sheet + transcript). Fix or flag defects honestly; never call a weak take good.
11. **Every script is new.** Check and append `~/Everlife-Creative/ghk-cream-copy-log.md`; never repeat a header, end-card headline or CTA.
12. Everything is a draft until creative review approves it and Jeremy signs off on compliance. Nothing is posted or uploaded anywhere.

Read these when the step says so:

| File | Read before |
|---|---|
| `references/product-bible.md` | writing any copy (incl. the pre-screen table at the top) |
| `core/references/global-rules.md` | writing any copy |
| `core/references/creative-system.md` | **every batch table and every script**: the shared creative-system rules (structure rotation, article slot, product angle, named typeface, own palette, hero size, CTA string + QA, real logo/label composited, 9:16 from the approved 4:5) |
| `core/references/REFERENCE-PRIORITY.md` | picking any reference ad: 1 our winners → 2 Meta → 3 Pinterest |
| `references/styles/INDEX.md` | the style question; then the chosen category file `references/styles/<n>-*.md` |
| `references/video-prompting.md` | writing a video script/prompt |
| `references/image-batch.md` | **any image request** (Batch Mode); layout refs in `core/references/static-refs/` |
| `references/personas.md` | **every concept, before the approval question**: critique it as the two personas, fix, show the critique |
| `references/reference-guide.md` | choosing the reference ad for a slot |
| `references/finishing.md` | QA + finishing |
| `references/lessons.md` | every time before writing (paid-for mistakes + the creative team's feedback) |
| `references/reviews.md` | any review / testimonial / social-proof quote (none on file → gated) |
| `assets/RENDERS.md` | the renders gate: what's in, what's missing |

Paths: skill dir = this folder (`assets/` holds the bottle render; `product.env`/`product.json` the product settings). `core/` = the
shared Everlife toolkit. Tools = `$EVERLIFE_TOOLS` or `~/Everlife-Creative/tools`. Output root = `~/Everlife-Creative/output/GHK-Cu-Cream/`.

No winners yet: the Meta all-time export has no GHK cream rows and there are no reference ads on file (2026-11-02). Ask Emily for
any GHK cream ads that ran; until then use the shared Meta refs and Pinterest library (layout only).

---

## Hook Engine (mandatory for every video)
Before writing any video concept, script or prompt, read `core/hook-engine/HOOK-ENGINE.md` (the hook contract, families, HOOK-10
score and hook QA) and `references/hook-bank.md` (this product's limits and starting hooks). Pitch three options scoring ≥ 8
(frame 0 already mid-action, a real sound at 0.0 s, the hook landing by 1.5 s), write the chosen one into the prompt as beat 1, run
the engine's hook QA on every raw video, then append the result to `~/Everlife-Creative/hook-ledger.jsonl`. The gates and this
skill's rules win on any conflict; copy still comes only from `references/product-bible.md`. Not used for statics.
**"<Product> by Everlife" in every video** (`core/references/creative-system.md` §0): the VO says "G-H-K Peptide Cream by Ever-life"
(letters spelled out; check the unprimed transcript) by about 3 s and names the product (not just "this"); "GHK PEPTIDE CREAM by
Everlife" is on screen in the intro. On H2 the name is "GHK-Cu Cream" (VO "G-H-K-C-U Cream"; ask Jeremy before the first H2 video).
The transcript QA fails any raw without the name or "by Everlife", and any raw that says "copper". Statics never say "by Everlife".

## Step 0 — Preflight + renders gate

1. **Renders gate (hard stop):** `assets/RENDERS.md`. The bottle render (`ghk-cream_bottle.png` + `ghk-cream_bottle_ref.jpg`) must be
   in `assets/`. If it's missing, **STOP before any generation** and say which file is needed. There is no tablet render, by design.
2. **Disclaimer status:** read `product.json` `_disclaimer_status` and tell the user in one line: "Disclaimer is provisional (standard
   ad disclaimer); Jeremy still has to confirm it."
3. Run `bash <skill-dir>/core/scripts/preflight.sh` and read its report. Use **AskUserQuestion** to walk the user through anything that
   is not ✅, one item at a time:

| Check | Fix to offer |
|---|---|
| Higgsfield CLI installed | `curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh \| sh` (user runs it with `!` prefix) |
| Higgsfield logged in | user runs `! higgsfield auth login` |
| Workspace = **Everlife** (shared team credits) | `higgsfield workspace list`, then select Everlife |
| Credits ≥ 100 | tell the user the balance; ask whether to continue |
| GHK-Cu Cream registered in Marketing Studio | **not registered yet** (2026-11-02). Preflight prints the command; upload the white-flattened copy; ask the user before running it (it uploads to Higgsfield). Only for UGC / AI avatar |
| Finishing toolkit | preflight offers `--install`; run it after the user agrees |
| Copy log exists | preflight creates it |
| Creatify connector (images) | call `composer_billing_state`. `assets/creatify.json`: create the project once, with the user's OK |
| Creatify MCP (Nano Banana) | `claude mcp add --transport http --scope user creatify https://api.creatify.ai/mcp`, new session, `/mcp` → sign in. Only for Nano Banana batches |

If everything is ✅, say so in one line and go straight to step 1.

## ⚡ Speed rules
- **Image model is a question, not a default:** GPT Image 2.5 via the connector by default; Nano Banana 2.1 or Pro via the
  `creatify` MCP: `core/references/image-models.md`.
- **At most 2 question rounds before the first generation** for images.
- **Never read tool source code.** Copy keys, layouts and commands are in the reference files.
- Read all references in ONE Bash call (`cat` them together), once per session.
- Start the generation, then do the copy log and job folder while it renders.

## Step 1 — Setup (every question has a ✨ Recommended first option; two rounds, then the table)
**Never asked:** audience (women 30–55, always), people in frame (default: **product-only**, the premium-DTC direction Mitansh
approved, `lessons.md`; people only when the user asks, tested in 2–3 shots first: one candid woman 30–55, shoulder-up/waist-up,
daytime, sun-lit), placement (images at 4:5; 9:16 made from the approved masters), frameworks (random mix; the user can name some).

**Round 1 — one AskUserQuestion, 4 questions:**
1. **What are we making?** "🖼️ Image ads (Recommended)" / "🎬 Video ad" / "🧑‍💼 AI Avatar Video".
   - **🧑‍💼 AI Avatar Video** → follow `core/references/ai-avatar-video.md` end to end (presenter on green with a tiny wireless mic, keyed
     lower-left over the animated Boreal-H3 background built from the real render; 15 s ≈ 52.5 Higgsfield + ~3.6 Creatify credits;
     its own single setup question; needs the product registered in Marketing Studio, which is still to do). This skill's casting,
     claims, colours and banned settings still apply: a woman 30–55, shoulder-up, fresh and natural (never glam or "huge"), the
     **pump bottle is the hero** in the B-roll (no tablet exists), pinks/tans/beige set with no orange or green, no before/after,
     no skin-condition close-ups, the name "GHK Peptide Cream" (never "copper", never "-Cu" outside the H2 name).
2. **Channel (sets the name):** "Meta / Google / TikTok: 'GHK Peptide Cream' (Recommended)" / "H2: 'GHK-Cu Cream'". H2 swaps only
   the product name; the two lines that contain "GHK Peptide Cream" ("Glow Smarter With GHK Peptide Cream", "Explore GHK Peptide
   Cream") are ⚠ Jeremy on H2 and are left out by default.
3. **Hook angle:** "Mix: a different angle per ad (Recommended)" / "Firmness" ("Firmer-Looking Skin Starts With Support", "Support
   Firmer Skin") / "The peptide step" ("Peptide-Powered Skin Support", "Your Daily GHK Glow") / "Glow" ("Glow Smarter With GHK Peptide
   Cream", "Supports a Brighter, More Even-Looking Tone"). ⚠ lines (pre-screen) only with the user's OK.
4. **How bold on copy:** "Safe: bible wording only (Recommended)" / "Balanced: one PROPOSED line in the batch" / "Bold: two PROPOSED
   lines". Safe = Tier A only. Balanced/Bold = Tier B lines marked PROPOSED, each needs the user's explicit OK and goes to Jeremy.

**Round 2 (images) — one AskUserQuestion, 4 questions:**
5. **Mood:** "Surprise me: different each ad (Recommended)" / "✨ Ultra premium, product only (Hims/Ro codes: `core/references/ultra-premium.md`)" /
   "Soft blush: pink, rose, cream" / "Warm sand: tan, beige, travertine, golden morning light". Sets palette and light; §2b still
   varies the type pairing per ad. Every mood stays pinks / tans / beige: no oranges or greens.
6. **Copy density:** "Headline + 3 lines (Recommended)" / "Headline + 1 line" / "Headline only, the picture talks".
7. **Image model:** see `core/references/image-models.md` (GPT Image 2.5 recommended).
8. **How many:** "4 (Recommended: one wave, Creatify runs 4 at a time)" / "8" / "12".
Then `references/image-batch.md` §2 step 2 onward (the table, the persona pass, the approval question).

**Round 2 (video) — one AskUserQuestion, 3 questions:** **Placement** "9:16 Reels/Stories (Recommended)" / "4:5 Feed" / "1:1" ·
**Style** "✨ Recommend for me (Recommended)" + the 3 best-fitting categories from `styles/INDEX.md` · **Mood** (the options of 5,
minus the product-only premium look, which is for images).
**AI avatar videos:** every video batch includes at least 2 (Jeremy, 30 Oct 2026), made with the "🧑‍💼 AI Avatar Video" option
(`core/references/ai-avatar-video.md`).

## Step 2 — Style details (only when the user wants to choose or see examples)
Read `references/styles/INDEX.md` and follow its "How to ask". Put the engine and **credit cost** in every option description. Style gates:
- **2B Review spotlight / review burst:** blocked until `references/reviews.md` has screened, verbatim GHK cream reviews (none on file).
- **5 Contrast:** no competitor or treatment comparisons, **no before/after, no side-by-side skin**.
- **Any style:** no bodybuilding or "huge" physiques; no oranges or greens; no skin-condition close-ups; no needles or droppers.

## Step 3 — Script → approve → generate (video)
1. Read `product-bible.md`, `global-rules.md`, `lessons.md`, the chosen sub-style file, `video-prompting.md` and the copy log.
2. Write **one** concept and show it compactly: Hook (0–2.5 s, speech from the first second) · Script / shot list with timestamps,
   every spoken line in quotes · On-screen copy: header "GHK PEPTIDE CREAM BY EVERLIFE", end-card headline, 3 benefits (✅ lines
   only), CTA, all from the bible · Compliance notes: the bible line behind each claim; any ⚠ line used (needs the user's explicit OK
   now, Jeremy later); any Tier B line marked PROPOSED · the full generation prompt in a collapsed code block.
3. **Persona critique** (`references/personas.md`): read the concept as both personas; score the rubric; fix anything under 4; show
   the critique and the fixes under the concept.
4. AskUserQuestion: **"Approve & generate (≈N credits)"** / "Edit the script" / "New concept, same style" / "Change style".
5. On approval: job folder `~/Everlife-Creative/output/GHK-Cu-Cream/<YYYY-MM-DD>_<slug>/` with `prompt.txt`, `copy.json` (with
   `"product": "ghk-cream"`), `source/` (copy the render); a face in the video → cast from a picked preview still first; run the cost
   check, submit **in the background**, append the concept to the copy log.

## Step 4 — Keep the pipeline moving
While a job renders, write the next script and get it approved. Up to 3 jobs in flight. When a job lands, finish it (step 5) before
writing the next. One-line status updates.

## Step 5 — QA + finishing (zero manual editing)
Follow `references/finishing.md`: safe zones on every 9:16 asset (finishers refuse to export on a violation; never override), QA of the
raw (label not mirrored and strength-free, the bottle exactly as the render, no garbled text, no tablet or other product, real-looking
women 30–55, no bodybuilder physique, no before/after, no orange or green, no celebrity likeness, no "copper" in the transcript), then
`full_layout.py` (video) or `finish_batch.py` (images). Save `FINAL_*.mp4|png`, open it, report what it is, cost, known issues, path.

## Step 6 — Wrap up
- Write `~/Everlife-Creative/output/GHK-Cu-Cream/<YYYY-MM-DD>_SESSION.md`. Its first line: **"provisional disclaimer: Jeremy to
  confirm"**. Then one row per asset (path, channel/name used, sub-style, hook, header, end card, CTA, every claim with its bible
  source, any ⚠ line, cost, known issues). This is the hand-off for creative review and Jeremy.
- Tell the user: every finished file with its path, total credits spent, remaining balance, untried sub-styles.
- Remind: drafts only → creative review → Jeremy's sign-off (including the provisional disclaimer) before anything goes live. Other
  sizes only after the master is approved. Delivery (Drive, Master Creative Library, tell Emily) happens after approval, not here.
