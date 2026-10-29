# Style system — index (PT-141)

Source: the team's style library "Everlife Ad Style Examples" (Drive folder `1aQv40GQ3vwsF2EkJ_L41vnvZDYInTckF`), condensed into 6 categories. Same structure as the Restora-Z and Sermorelin GHK skills; the fit and recipes are rewritten for PT-141 (intimate wellness: tasteful, product-led, shoulder-up, no beds). Example boards (library thumbnails, all products) are in `../style-boards/board_1..6.jpg`:

| Board | Rows (library folders) |
|---|---|
| board_1 | Winners · Advertorial · AI Avatar · Article · Billboard · Breaking News |
| board_2 | Cause & Effect · Clinical-Research · Comparison · Conversational · Dad Bod · Elite/Celebrity Secret |
| board_3 | Female Glow Up · Fighter UFC · Hero Fitness Guy · Life Cell · Minimalist · Movie-Peg |
| board_4 | NEW from Jeremy · New Year · No More Needles · Open Letter · Pill-Product Focused · Podcast |
| board_5 | Polaroid · Product Highlight · Product-as-Hero · Retro · Side-by-Side · Sports |
| board_6 | Talking Head Avatar · Trustpilot Reviews · UGC · Versus fighting · Voice Over · Wild-Creative/Surreal |

Boards show library ads as they ran, including some that break today's rules. Show them for *look and layout* only.

## The 6 categories (PT-141 priority order)

| # | Category | File | Sub-styles | Fit | Formats |
|---|---|---|---|---|---|
| 4 | **Product as Hero** | `4-product-hero.md` | 4A Marble still life (the bible image) · 4B Spray / tablet macro · 4C Minimal bold · 4D Ad in a frame · 4E Getting-ready ASMR (counter, never a bed) | ⭐⭐⭐ | Image + video |
| 6 | **Lifestyle & Identity** | `6-lifestyle-identity.md` | 6A Unplanned evening (dinner, terrace, car) · 6B Your body changed (30–55 identity) · 6C Her glow (women) · 6D Date night, clothed and daytime-lit | ⭐⭐⭐ | Video + image |
| 1 | **Real People Talking** | `1-real-people.md` | 1A Creator to camera · 1B Friend-to-friend · 1C Podcast set · 1D Voice-over lifestyle | ⭐⭐⭐ | Video (+ stills) |
| 3 | **Cinematic Big Idea** | `3-cinematic-big-idea.md` | 3A Switch / match / spark metaphor · 3B Comedic contrast (calendar vs moment) · 3C Animated brain-signal · 3D Retro film · 3E Seasonal | ⭐⭐ | Video + image |
| 2 | **Authority & Proof** | `2-authority-proof.md` | 2A Clinician moment (shoulder-up, white coat, AI disclosure) · 2B Review spotlight (gated) · 2C Open letter · 2D Article · 2E Mechanism map (brain → desire) | ⭐⭐ | Image first |
| 5 | **Contrast & Comparison** | `5-contrast.md` | 5A Old assumption vs brain-based checklist · 5B Versus a feeling (never a body or brand) | ⭐ | Image + video |

## How to ask (minimal clicks)
1. **"Pick a style direction"** (single select): "✨ Recommend for me" (you pick 1–3 sub-styles with one line why) · "Product as Hero" (statics ~1 Creatify cr, video Seedance ~45 cr) · "Lifestyle & Real People" (Marketing Studio, ~75 cr/video) · "Authority & Big Idea".
2. **"Which one?"**: the sub-styles of that category (≤ 4 options, look + cost). Add "👀 Show me examples first" → Read the board, show it, ask again.
3. Batches: "Mix it up (different sub-style per concept)" is the default.

## Routing
| Need | Engine | Cost |
|---|---|---|
| Realistic humans talking / acting | Higgsfield Marketing Studio UGC (720p) | ~75 / 15 s |
| One locked slow shot, talking head, simple product hero | Boreal-style (Creatify Ad Agent) | see `composer_billing_state` |
| Multi-scene, camera moves, fast motion, animation | Seedance 2.0 (+ the form's renders `--image`) | ~45 / 15 s (67.5 at 720p) |
| Statics | GPT Image 2.5 via Creatify, renders attached | ~1 Creatify credit |
| ALL words, numbers, logos, review text | finishing only (`finish_batch.py`, `full_layout.py`) | 0 |

## Library compliance traps (never copy)
"Breaking News" · beds, bedrooms, lingerie, undressing, couples in bed · body shots, split-face or body before/after · "ED", "erectile", "Viagra", "performance", "instant" · "No More Needles" / needle imagery · celebrity names · $ prices · old proof (4.8 / 50,000 / 70,000) · named competitors · "Dad Bod".
