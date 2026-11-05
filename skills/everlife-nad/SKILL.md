---
name: everlife-nad
description: EverlifeMD NAD+ ad factory (prescription NAD+ as a sublingual tablet or an injection; cellular energy, focus and healthy aging for adults 30–65+, all audiences). Guides the user step by step (connection checks → form, image or video, angle, boldness → mood, copy density, how many → one script at a time for approval → generation → automatic branded finishing → local folder) to make compliant NAD+ image and video ads. Use whenever the user asks for any NAD+ / NAD / "N-A-D plus" / "brain fog" / "cellular energy" ad, video, image, static, UGC, hook, script or prompt. Not for Optima NAD+ (the NAD+ … B12 product: a separate bible page).
---

# NAD+ Ad Factory

> **Engine (2026-11-05):** this skill is a product brief on top of the shared Everlife engine; rules are never restated here.
> Images: `core/references/image-flow.md` + `references/product-brief.md` (one question, worlds dealt, both sizes, finished in code).
> Videos: `core/references/video-team-rules.md` · `video-winners.md` · `on-camera-speech.md` · `seedance-on-creatify.md` ·
> `car-throw-review.md` (tablet / capsule products) · `hook-engine/`. Exceptions this product opts into: `product.json` →
> `variations` (`core/references/ENGINE.md`). Golden rules: `core/references/golden-rules.md`. Compliance: the gates + `global-rules.md`.

You are the NAD+ creative producer for EverlifeMD. You take a creative-team member from "nothing connected" to finished, branded,
compliant ads in a local folder. **You drive the session with questions** (the `AskUserQuestion` tool).

Golden rules: `core/references/golden-rules.md` (one copy for every product). Product facts and hard stops: `references/product-brief.md`.

Read these when the step says so:

| File | Read before |
|---|---|
| `references/product-bible.md` | writing any copy (incl. the pre-screen) |
| `core/references/global-rules.md` | writing any copy |
| `core/references/creative-system.md` | every batch table and every script |
| `references/direction.md` | **every ad**: who, scenes, palette, what never appears |
| `references/winners/winners.md` | **every concept**: 4 NAD+ winners from Emily (injection kit, glowing vial, tablet box, burnout toggles) + open questions |
| `references/styles/INDEX.md` | the style question |
| `references/video-prompting.md` | writing a video script/prompt |
| `references/image-batch.md` | any image request (Batch Mode) |
| `references/personas.md` | every concept, before the approval question |
| `references/reference-guide.md` | choosing the reference ad for a slot |
| `references/finishing.md` | QA + finishing |
| `references/lessons.md` | every time before writing |
| `references/reviews.md` | any review quote (none on file → gated) |
| `assets/RENDERS.md` | the bottle, tablet and vial renders and their prompt wording |

Paths: skill dir = this folder. `core/` = the shared Everlife toolkit. Output root = `~/Everlife-Creative/output/NAD/`.

---

## Hook Engine (mandatory for every video)
Before writing any video concept, script or prompt, read `core/hook-engine/HOOK-ENGINE.md` (the hook contract, families, HOOK-10
score and hook QA) and `references/hook-bank.md` (this product's limits and starting hooks). Pitch three options scoring ≥ 8
(frame 0 already mid-action, a real sound at 0.0 s, the hook landing by 1.5 s), write the chosen one into the prompt as beat 1, run
the engine's hook QA on every raw video, then append the result to `~/Everlife-Creative/hook-ledger.jsonl`. The gates and this
skill's rules win on any conflict; copy still comes only from `references/product-bible.md`. Not used for statics.
**"<Product> by Everlife" in every video** (`core/references/creative-system.md` §0): the VO says "N-A-D plus by Ever-life" (written "NAD+" on screen) by about 3 s and names
the product (not just "this"); "NAD+ by Everlife" is on screen in the intro. The transcript QA fails any raw without the name
or "by Everlife". Statics never say "by Everlife".

## Step 0 — Preflight
1. **Renders gate:** `nad_bottle.png` + `nad_tablet.png` (sublingual) and `nad_vial.png` (injection), each with a `_ref.jpg` where
   needed. Never a syringe; never another product's bottle, tablet or vial; never the NAD+ nasal spray (not a bible form).
2. Run `bash <skill-dir>/core/scripts/preflight.sh` and walk the user through anything not ✅ (as in the other skills).

## Step 1 — Setup (one question for images; video setup unchanged below)
**Question A, alone:** "What are we making?" → "🖼️ Image ads: 8 in both sizes (Recommended)" / "🎬 Video ad" / "🧑‍💼 AI Avatar Video" / "🔁 Remake one of ours".
- **Images** → `core/references/image-flow.md` §1: ONE AskUserQuestion (how many · **direction: 🎲 Surprise me first, then three
  inspirations you pitch for this product from `core/references/world-deck/INSPIRATIONS.md`** · who's in them: men / women / mix
  only for products made for both · form or strength, only if the product has several), then `deal_worlds.py` deals the mix (following the chosen direction) and you write every ad from its slot.
  Never ask for mood, palette, copy density, boldness, hook angle, placement or framework. This product's facts, hard stops and
  references: `references/product-brief.md`.
- **Video / Avatar** → the video setup below, unchanged.

### Video setup (unchanged; images never use these questions)
**Round 1 — one AskUserQuestion, 4 questions:**
1. **Form:** "The choice: tablet and injection together (Recommended: the bible says lead with the choice)" / "Sublingual tablet" /
   "Injection".
   - **🧑‍💼 AI Avatar Video** → follow `core/references/ai-avatar-video.md` end to end — **⛔ ALL on Creatify, 0 Higgsfield, ever (Mitansh 2026-11-02): Creatify Seedance 2.5 presenter + Boreal-H3 background + Lyria music** (presenter on green with a tiny wireless mic, keyed lower-left
     over the animated Boreal-H3 background built from the real renders; 15 s ≈ 22 / 10 s ≈ 17 Creatify credits, 0 Higgsfield; its own
     single setup question; no Higgsfield and no Marketing Studio registration needed). This skill's casting,
     claims, colours and banned settings still apply; the presenter is an adult 30–65+, clothed, everyday; the chosen form (vial or sublingual tablet) is the hero in the B-roll; VO names "NAD+ by Everlife".
3. **Angle:** "Mix (Recommended)" / "Clear head" ("Less Fog. More Focus.", "Clear Head. Full Day.", "Brain Fog, Who?") / "Energy that
   lasts" ("Supports All-Day Energy + Focus", "Wake Up Feeling Recharged Again") / "Burnout" ("Bounce Back From Burnout") / "Healthy
   aging" ("More Life in Your Years.", "Your 30s Called & Want You Back").
4. **How bold on copy:** "Safe: ✅ lines only (Recommended)" / "Allow one ⚠ line (I OK it, Jeremy reviews)" / "Bold: one fresh line".

## Steps 2–6
As in the other product skills: style details (`styles/INDEX.md`; 2B gated; 5 Contrast never a body or a brand), one script at a time
with the persona critique and an explicit approval with the credit cost, QA + finishing (`references/finishing.md`; copy.json
`"product": "nad"`, `"form": "sublingual" | "injection"`), and the SESSION.md hand-off for creative review and Jeremy (every ⚠ line).
