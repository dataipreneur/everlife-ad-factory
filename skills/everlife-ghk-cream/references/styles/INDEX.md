# Style system — index (GHK Peptide Cream)

Source: the team's style library "Everlife Ad Style Examples" (Drive folder `1aQv40GQ3vwsF2EkJ_L41vnvZDYInTckF`), condensed into 6
categories. Same structure as the other product skills; the fit and recipes are rewritten for GHK Peptide Cream (topical peptide skin
support, women 30–55, beauty-and-fitness register, pinks/tans/beige, the pump bottle as hero). Example boards (library thumbnails,
all products) are in `../style-boards/board_1..6.jpg`:

| Board | Rows (library folders) |
|---|---|
| board_1 | Winners · Advertorial · AI Avatar · Article · Billboard · Breaking News |
| board_2 | Cause & Effect · Clinical-Research · Comparison · Conversational · Dad Bod · Elite/Celebrity Secret |
| board_3 | Female Glow Up · Fighter UFC · Hero Fitness Guy · Life Cell · Minimalist · Movie-Peg |
| board_4 | NEW from Jeremy · New Year · No More Needles · Open Letter · Pill-Product Focused · Podcast |
| board_5 | Polaroid · Product Highlight · Product-as-Hero · Retro · Side-by-Side · Sports |
| board_6 | Talking Head Avatar · Trustpilot Reviews · UGC · Versus fighting · Voice Over · Wild-Creative/Surreal |

Boards show library ads as they ran, including some that break today's rules. Show them for *look and layout* only.

## The 6 categories (GHK cream priority order)

| # | Category | File | Sub-styles | Fit | Formats |
|---|---|---|---|---|---|
| 4 | **Product as Hero** | `4-product-hero.md` | 4A Vanity still life · 4B Pump macro · 4C Minimal bold · 4D Ad in a frame · 4E Morning-routine ASMR | ⭐⭐⭐ | Image + video |
| 6 | **Lifestyle & Identity** | `6-lifestyle-identity.md` | 6A One step, busy morning · 6B After the run · 6C Her glow | ⭐⭐⭐ | Video + image |
| 1 | **Real People Talking** | `1-real-people.md` | 1A Creator to camera · 1B Friend-to-friend · 1C AI avatar · 1D Voice-over lifestyle | ⭐⭐⭐ | Video (+ stills) |
| 2 | **Authority & Proof** | `2-authority-proof.md` | 2A Clinician moment · 2B Review spotlight (gated) · 2C Open letter · 2D Article (on white) · 2E The peptide step, explained | ⭐⭐ | Image first |
| 3 | **Cinematic Big Idea** | `3-cinematic-big-idea.md` | 3A Object metaphor (ribbon, linen, light) · 3B The cleared shelf · 3C Retro film · 3D Seasonal | ⭐⭐ | Video + image |
| 5 | **Contrast & Comparison** | `5-contrast.md` | 5A "Ten-step shelf" vs one peptide step (no skin, no brands) | ⭐ | Image |

## How to ask (minimal clicks)
1. **"Pick a style direction"** (single select): "✨ Recommend for me" (you pick 1–3 sub-styles with one line why) · "Product as Hero"
   (statics ~1 Creatify cr, video Seedance ~45 cr) · "Lifestyle & Real People" (Marketing Studio, ~75 cr/video; needs registration) ·
   "Authority & Big Idea".
2. **"Which one?"**: the sub-styles of that category (≤ 4 options, look + cost). Add "👀 Show me examples first" → Read the board, show it.
3. Batches: "Mix it up (different sub-style per concept)" is the default.

## Routing
| Need | Engine | Cost |
|---|---|---|
| Realistic humans talking / acting | Higgsfield Marketing Studio UGC (720p; product must be registered: still to do) | ~75 / 15 s |
| AI avatar (Jeremy: ≥ 2 per video batch) | `core/references/ai-avatar-video.md` | ~52.5 Higgsfield + ~3.6 Creatify / 15 s |
| One locked slow shot, simple product hero | Boreal-style (Creatify Ad Agent) or Seedance 480p | see `composer_billing_state` / ~45 |
| Multi-scene, camera moves | Seedance 2.0 (+ bottle and cast still `--image`) | ~45 / 15 s (67.5 at 720p) |
| Statics | GPT Image 2.5 via Creatify, render attached | ~1 Creatify credit |
| ALL words, numbers, logos, review text | finishing only (`finish_batch.py`, `full_layout.py`) | 0 |

## Library compliance traps (never copy)
"Breaking News" · "Female Glow Up" before/after faces and bodies · side-by-side skin · body shots, "Dad Bod"/"Hero Fitness" physiques,
anything bodybuilding or "huge" · "Clinical-Research" claims ("clinically proven") · "No More Needles" / needle imagery · celebrity
names or look-alikes · $ prices · old proof (4.8 / 50,000 / 70,000) · named competitors or treatments · "GHK-Cu" / "copper" (except the H2
product name) · oranges and greens.
