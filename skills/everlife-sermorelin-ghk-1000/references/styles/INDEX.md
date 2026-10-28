# Style system — index (Sermorelin GHK 1000)

Source: the team's style library "Everlife Ad Style Examples" (Drive folder `1aQv40GQ3vwsF2EkJ_L41vnvZDYInTckF`), condensed into 6 categories. Same structure as the Restora-Z skill; the fit and recipes are rewritten for Sermorelin GHK. Example boards (library thumbnails, all products) are in `../style-boards/board_1..6.jpg`:

| Board | Rows (library folders) |
|---|---|
| board_1 | Winners · Advertorial · AI Avatar · Article · Billboard · Breaking News |
| board_2 | Cause & Effect · Clinical-Research · Comparison · Conversational · Dad Bod · Elite/Celebrity Secret |
| board_3 | Female Glow Up · Fighter UFC · Hero Fitness Guy · Life Cell · Minimalist · Movie-Peg |
| board_4 | NEW from Jeremy · New Year · No More Needles · Open Letter · Pill-Product Focused · Podcast |
| board_5 | Polaroid · Product Highlight · Product-as-Hero · Retro · Side-by-Side · Sports |
| board_6 | Talking Head Avatar · Trustpilot Reviews · UGC · Versus fighting · Voice Over · Wild-Creative/Surreal |

Boards show library ads as they ran, including some that break today's rules ("Dad Bod", "Breaking News", "No More Needles"). Show them for *look and layout* only.

## The 6 categories (Sermorelin GHK priority order)

| # | Category | File | Sub-styles | Fit | Formats |
|---|---|---|---|---|---|
| 6 | **Lifestyle & Identity** | `6-lifestyle-identity.md` | 6A Prime-time training · 6B Still in the game · 6C Glow + strength (women) · 6D GLP-1 complement | ⭐⭐⭐ | Video + image |
| 1 | **Real People Talking** | `1-real-people.md` | 1A Creator to camera · 1B Training partner POV · 1C Friends chatting · 1D Podcast set · 1E Voice-over lifestyle | ⭐⭐⭐ | Video (+ stills) |
| 4 | **Product as Hero** | `4-product-hero.md` | 4A Premium still life · 4B Tablet in hand · 4C Minimal bold · 4D Ad in a frame · 4E Morning routine ASMR | ⭐⭐⭐ | Image + video |
| 2 | **Authority & Proof** | `2-authority-proof.md` | 2A Doctor moment · 2B Review spotlight (gated) · 2C Open letter · 2D Article · 2E Mechanism map | ⭐⭐ | Image first |
| 3 | **Cinematic Big Idea** | `3-cinematic-big-idea.md` | 3A Movie-peg · 3B Comedic contrast · 3C Animated ingredients · 3D Retro film · 3E Seasonal | ⭐⭐ | Video + image |
| 5 | **Contrast & Comparison** | `5-contrast.md` | 5A Old routine vs 3-in-1 checklist · 5B Versus battle (vs a problem) | ⭐ | Image + video |

## How to ask (minimal clicks)
1. **"Pick a style direction"** (single select): "✨ Recommend for me" (you pick 1–3 sub-styles with one line why) · "Lifestyle & Real People" (Marketing Studio, ~75 cr/video) · "Product as Hero" (statics ~1 Creatify cr, video Seedance ~45 cr) · "Authority & Big Idea".
2. **"Which one?"**: the sub-styles of that category (≤ 4 options, look + cost). Add "👀 Show me examples first" → Read the board, show it, ask again.
3. Batches: "Mix it up (different sub-style per concept)" is the default.

## Routing
| Need | Engine | Cost |
|---|---|---|
| Realistic humans talking / acting | Higgsfield Marketing Studio UGC (720p) | ~75 / 15 s |
| One locked slow shot, talking head, simple product hero | Boreal-style (Creatify Ad Agent) | see `composer_billing_state` |
| Multi-scene, camera moves, fast motion, animation | Seedance 2.0 (+ bottle & tablet `--image`) | ~45 / 15 s (67.5 at 720p) |
| Statics | GPT Image 2.5 via Creatify, renders attached | ~1 Creatify credit |
| ALL words, numbers, logos, review text | finishing only (`finish_batch.py`, `full_layout.py`) | 0 |

## Library compliance traps (never copy)
"Breaking News" · "Dad Bod", "new 40", "50 is the new 30" for this product (those are plain-Sermorelin lines and body framing) · shirtless/bodybuilder heroes, UFC cage bodies · split-face or body before/after · "No More Needles" / needle imagery · celebrity names · $ prices · old proof (4.8 / 50,000 / 70,000) · named competitors · "GHK-Cu" / copper peptide · "GH".
