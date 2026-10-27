# Style system — index (Restora-Z)

Source: the team's style library "Everlife Ad Style Examples" (Drive folder `1aQv40GQ3vwsF2EkJ_L41vnvZDYInTckF`, 37 style folders, reviewed 2026-10-27). The library was condensed into **6 categories → 28 sub-styles**. Each category file holds the full recipe for every sub-style in it.

Example boards (real thumbnails from the library, 4 per style) live in `../style-boards/board_1..6.jpg`. When a user wants to *see* a style, Read the board that contains it and show it:

| Board | Rows (library folders) |
|---|---|
| board_1 | Winners · Advertorial · AI Avatar · Article · Billboard · Breaking News |
| board_2 | Cause & Effect · Clinical-Research · Comparison · Conversational · Dad Bod · Elite/Celebrity Secret |
| board_3 | Female Glow Up · Fighter UFC · Hero Fitness Guy · Life Cell · Minimalist · Movie-Peg |
| board_4 | NEW from Jeremy · New Year · No More Needles · Open Letter · Pill-Product Focused · Podcast |
| board_5 | Polaroid · Product Highlight · Product-as-Hero · Retro · Side-by-Side · Sports |
| board_6 | Talking Head Avatar · Trustpilot Reviews · UGC · Versus fighting · Voice Over · Wild-Creative/Surreal |

## The 6 categories (in Restora-Z priority order)

| # | Category | File | Sub-styles | Restora-Z fit | Formats |
|---|---|---|---|---|---|
| 1 | **Real People Talking** | `1-real-people.md` | 1A Creator to camera · 1B Partner / family POV · 1C Friends chatting · 1D Podcast set · 1E Voice-over lifestyle | ⭐⭐⭐ | Video (+ image stills) |
| 2 | **Authority & Proof** | `2-authority-proof.md` | 2A Doctor moment · 2B Review spotlight · 2C Open letter · 2D Article / social post · 2E Problem → benefit map | ⭐⭐⭐ | Image first, video possible |
| 3 | **Cinematic Big Idea** | `3-cinematic-big-idea.md` | 3A Movie-peg ("Take the blue pill") · 3B Comedic chaos → calm · 3C Animated characters · 3D Surreal metaphor · 3E Retro film · 3F Seasonal moment | ⭐⭐⭐ | Video + image |
| 4 | **Product as Hero** | `4-product-hero.md` | 4A Premium still life · 4B Capsule in hand · 4C Minimal bold · 4D Ad-in-a-frame (polaroid / phone / billboard) · 4E ASMR night routine | ⭐⭐⭐ | Image + video |
| 5 | **Contrast & Comparison** | `5-contrast.md` | 5A Restora-Z vs Ambien (gated) · 5B Before another sleep fix checklist · 5C Night / morning split · 5D Versus battle | ⭐⭐ | Image + video |
| 6 | **Lifestyle & Identity** | `6-lifestyle-identity.md` | 6A Active 50+ mornings · 6B "Night shift" identity · 6C Couple wellness | ⭐ (mostly a Sermorelin / Optima territory) | Video + image |

## How to ask (keep the creative team's clicks minimal)

1. **Q: "Pick a style direction"** (AskUserQuestion, single select). Show these 4 options. "Other" lets them type any category or sub-style name:
   - "✨ Recommend for me": you pick the best 1–3 sub-styles for their angle and format, with one line on why each
   - "Real People Talking": realistic creators, couples, podcasts (Marketing Studio, ~75 cr/video)
   - "Cinematic Big Idea": movie-peg, comedy chaos → calm, animated characters (Seedance, ~45 cr)
   - "Authority & Proof / Product as Hero": doctor, reviews, article, premium product shots (mostly statics, ~3 cr)
2. **Q: "Which one?"**: the sub-styles of the chosen category (≤ 4 options, each with a one-line look description + cost). Add "👀 Show me examples first" when they hesitate → Read the board and show it, then ask again.
3. **Batch mode:** if they asked for 3–5 concepts, offer "Mix it up (different sub-style per concept)", which is the default for batches because variety tests better and avoids repetition.

## Routing summary (what generates what)

| Need | Engine | CLI | Cost |
|---|---|---|---|
| Realistic humans talking / acting | Higgsfield Marketing Studio UGC | `marketing_studio_video --mode ugc --resolution 720p` | 75 / 15s |
| Stylised, comedic, animated, cinematic, ASMR | Seedance 2.0 | `seedance_2_0 --resolution 480p` (+ bottle & capsule `--image`) | 45 / 15s (67.5 at 720p) |
| Statics: lifestyle, product, scenes | GPT Image 2.5 **via Creatify** (`composer_edit_image`, renders attached) | see image-prompting.md | ~1 Creatify credit (fallback: Higgsfield ~2.75) |
| Illustrated / 3D character stills | GPT Image 2.5 via Creatify (or Higgsfield Nano Banana 2) | — | ~1 Creatify credit |
| ALL words, numbers, logos, review text, tables | **Finishing only**: statics → `finish_modern.py` (modern brand look, default); legacy `finish_image.py` only for compare/quote/article/letter; video → `full_layout.py` | — | 0 |

## Library compliance traps (seen in the examples; never copy)
"BREAKING / Breaking News" banners · Dad-bod / "new 40" / body-composition claims · split-face before/after · celebrity names (e.g. Joe Rogan) · $ prices ("$69", "$2 a day") · old proof (4.8, 50,000, 70,000) · "The last sleep solution you'll ever need" (Hard NO) · named competitors other than Ambien · needles and injections imagery · first-person testimonials.
