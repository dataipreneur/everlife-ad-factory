# EverlifeMD Creative Gates — MANDATORY

> **⛔ Proof row ALWAYS inside the Meta safe area (Mitansh, 2026-11-02, HARD, every product, every skill, image AND video):** the Trustpilot / Doctor Prescribed / Ships Free / 100,000+ proof row ends at or above y 1385 on 1080×1920 (`safezones.py`). Never move it lower or outside the safe area by any means (env `EVERLIFE_PROOF_AT`, copy.json `proof_at`, flags, manual edits); the tools refuse. If the product or text collides with the proof row: re-roll the raw (cost approved) or ask the user. Never move the footer. The disclaimer alone may sit at the very bottom.

These gates apply to ALL creative work for EverlifeMD: scripts, prompts, images, videos, statics, landers, copy, on-screen text. A gate is pass/fail. If any gate fails, STOP, report which gate and why, and do not proceed, generate, upload or hand off. When a brief conflicts with a gate, follow the gate and flag the conflict.

**Precedence:** (1) Creative bible global rules (section 2–3 below; full text in `~/.claude/everlife/creative-bible.md`, Part A) → (2) the product's bible page → (3) the Asana brief → (4) everything else. Compliance questions route to **Jeremy**; nothing goes live without his approval.

**Before any product work, read that product's section of `~/.claude/everlife/creative-bible.md`.** It holds the approved positioning, headlines, benefits, ingredient claims, CTAs, proof, offers, product Hard NOs and the verbatim ad disclaimer.

## 1. Claims sources
- No Asana brief is required to start work: never ask about one or stop for a missing one. The product skill's own flow decides what to make.
- Benefits, headlines, CTAs, offers come ONLY from the brief's approved list or the product's bible page — and must also pass sections 2–3. Never invent new claims.
- Headline status in the bible: lines marked **Hard NO conflict** → never use. **Pending approval** (and every "PROPOSED FOR APPROVAL" hook in Parts B/C) → only with explicit approval. **Weak headline / Weak benefit** → avoid unless the brief asks for it.
- Offers marked [PLACEHOLDER] are not usable — flag.

## 2. Compliance gate — global Hard NOs (every line, every image)
Claims:
- No disease claims (cure, treat, prevent). Structure-function only.
- No "clinically studied" or "clinically backed" for a compound/product — only a named ingredient may carry it.
- Never attribute an outcome to the compound. Mechanism first, then downstream benefit ("raises testosterone, and healthy testosterone levels support…").
- **Never use the phrase "body composition" anywhere** (rewrite it: "supports lean muscle"). **No "fat" or "skinny" claims anywhere**: no fat loss, "melting fat", "fat and skinny" (bible 2026-11-04, 1793832093-ced5).
- No targeted fat loss; never name a body area (FTC). No "melting belly fat" style. Avoid melt, burn, ripped, shred.
- No unsupported medical-style claims, no exaggerated transformation claims, no claims outside the product's approved benefit scope.
- Never call a sublingual "all natural". Peptides support the body's own production — that is the limit.
- Say "supports", never "builds". No "high circulation". No vague inference phrasing ("one better night's sleep", not "one better night").
- **Benefits only ever come from the product's Quick-hit benefits list, matched word for word: no paraphrasing, no new benefits** (bible 2026-11-04). "Dr. Prescribed" / "Doctor Prescribed" is never a benefit (it is a trust callout). ⚠ Interpretation until Justin confirms: benefit lines (bullets, checklists, "Supports…" lines) are Quick-hit wording only; an approved per-ingredient claim may still sit on its own ingredient callout.
- No named-competitor comparisons (Restora-Z vs Ambien is the only exception — use only the approved Ambien claims/phrasing on its bible page, with Ambien's actual pill). No guaranteed outcomes.
- No first person ("I tried", "my results"). No second-person health questions with a pronoun ("Are you…?"); pronoun-free elliptical questions are OK.
- No body-comparison / before-after imagery, male or female.
- No "Breaking News" framing (article style OK).
Naming:
- **GHK, never "GHK-Cu" / "-Cu" / "copper peptide"** in creative. Only exception: H2 channel product name "GHK-Cu Cream" (FB, GL, TK → "GHK Peptide Cream"). Data records may still say ghk-cu.
- Spell out **"growth hormone" — never "GH".**
- Sermorelin GHK: "Sermorelin GHK" or "Sermorelin + GHK"; ingredient list reads Sermorelin, GHK, Citrulline.
- Compounded GLP-1s always carry the word "compounded". "GLP-1" is the umbrella term in headers/titles.
- "Optima NAD+" — NAD+ listed first, B12 last.
- **No mention of needles, including "needle-free"** → say "easy sublingual delivery".
- Spark: never tie a benefit to one ingredient — PT-141, Apomorphine and Tadalafil together as a combo. Ingredient claims (3-in-1 formulas) attach only to their own ingredient.
Proof:
- Trustpilot always reads exactly **"Trustpilot rated 4.9 Excellent"**. Never "Trustpilot rating" alone.
- Customer count locked at **100,000+** ("Over 100,000 happy customers").
- Proof split (bible 2026-11-04, Standards 02 · 06): **42% trust row** (Trustpilot, Doctor Prescribed, Ships Free From Pharmacy), **28% Trustpilot bar + "Over 100,000 happy customers"** (always with the Trustpilot bar), **30% neither** (images: `finish_batch.py --proof-plan N`; videos: `core/scripts/proof_next.py`). The bible now states the same split Mitansh applied on 2026-11-02 (it used to say 60/40). Logo + verbatim disclaimer on every creative.
  **HARD, no conflicts (Mitansh 2026-11-02: "This should be followed without any conflicts!"):** ≈ 42% trust / 28% badge + count / 30% none, per batch and per ratio; replaces every "every ad carries visible social proof" line. Compose proof ads with a clean shelf for the row (9:16: product + CTA end above y 1150); never swap a planned proof to "none" on your own (re-roll with cost shown, or ask); `finish_batch.py --proof-check <batch folder>` must pass before a batch is shown.
- Authority = sourced trust signals only (100,000+, Trustpilot, Doctor Prescribed / "Dr. Prescribed, Direct From Pharmacy", Ships Free From Pharmacy). No adjectives as authority.
Disclaimers & AI disclosure:
- Use the product's **Ad disclaimer verbatim** — from the bible, or from the product skill's `product.json` when the bible has none (e.g. BPC-157). Never written, paraphrased or invented. Don't stop over a missing bible disclaimer when the skill has one.
- Every AI-generated image/video carries the AI disclosure; nothing AI-generated goes live without it. Wording is "AI depictions", never "AI deceptions". **Resolved 2026-11-04:** the bible removed the global "ADVERTISEMENT: AI-generated depiction…" line and now says "Product-specific: each ad uses the disclaimer from that product's page, not a shared global one" (Standards 02 · 04). The product's verbatim disclaimer IS the AI disclosure; do not add a second line.

## 3. Creative standards gate
- **Focal-point mix** (bible 2026-11-04, replaces 50/25/25 and "the pill is the hero"): **40% pill-focused · 30% bottle-focused · 30% person-focused** across a product's creatives (batch table Focal column; batch of 4 = 2/1/1, 5 = 2/2/1, 8 = 3/3/2, 10 = 4/3/3; videos follow the same split as statics, Justin). Products without a pill: 75% product-focused · 25% person-focused (Justin 3 Nov 2026) stays until Justin says the new split replaces it ⚠ ask. If a bottle appears it is large, foreground and legible.
- Product and benefit identifiable in under 2 seconds; product names run big.
- Texture and depth behind the product — never flat color. No shadows or outlines on type.
- Bottles, pills, CTAs and text are never covered by another element, including a footer gradient (bible 3 Nov 2026).
- Bullet type readable at story size; don't over-bullet. Text legible for age **50+**; spelling checked.
- Capitalization consistent within a headline set, benefit list or CTA row: never mix Title Case and sentence case (bible 3 Nov 2026).
- Must hold up in square and vertical. Never end on a passive frame — last frame is benefits + a clear, specific CTA.
- **Price CTAs** (bible 3 Nov 2026): each product's "<product> for $N/day" CTA from its bible page is an approved alternative CTA; the offer CTA ("Save Up to N%") stays the default. It is the only $ amount allowed in ads (the "percent-off, not dollar prices" default still holds for everything else). **Show the lowest price or the price per day on 10% of ALL ads** (bible 2026-11-04; e.g. "Starting at $95/month", "Sermorelin for $3.00/day"), using the product's price from its CTAs or Offers & conversion. Titan-Rx's $/day is held while its offer is [VERIFY CURRENT]; Spark's needs the user's OK (its CTA list is Pending approval); GHK cream on Meta/Google/TikTok: "GHK Peptide Cream for $1.50/day".
- **Advertorial bylines** (bible 3 Nov 2026): article-style ads carry a byline: men "Brian L.", women "Erika S.", unisex either. ⚠ Needs Jeremy before any byline ad runs (a named author on an AI-made advertorial); flag it in SESSION.md.
- **Peptide stacks list every peptide** (bible 3 Nov 2026, mandatory): every ad for a stack shows each peptide, legibly, as supporting copy, a subheadline or an ingredient callout, never overwhelming the headline or product; every concept, variation and format (4:5, 9:16; videos on screen, at least on the end card). Spartan = BPC-157 / TB-500 / KPV · Wolverine = BPC-157 / TB-500 · Klow = BPC-157 / GHK / KPV / TB-500 · Glow = [PLACEHOLDER]. The stack name alone fails.
- **Never "Get Started Now" as a CTA** (bible 3 Nov 2026): lead with the offer ("Save Up to N%", the product's current % from its bible page); "Ships Free From Pharmacy" is the bible CTA where the % is still a placeholder.
- **Everlife logo on every ad.** Size (bible Standards 02 · 03, 4:5 width changed 31% → 29% on 2026-11-04): 9:16 = 40% of the width, 4:5 = 29%, height 3.5%. Minimum on-screen text **24 px** (disclaimer 13 px). ⚠ The finisher's default logo is 311 px: right for 4:5, about 29% on 9:16 (spec 40%: pass `--logo-w 40%`).
- **Discount accuracy** (bible 2026-11-04, Standards 03 · 09): the % on the ad is the featured product + delivery method's own maximum, always "Save Up to X%" (never a fixed discount); several forms shown → the highest; product or form not confidently identified → flag for review, do not guess. Approved maximums: PT-141 nasal spray 23% · sublingual 59% · Sermorelin sublingual 65% · injection 59% · NAD+ sublingual 62% · injection 62% · GLP-1 semaglutide 83% · tirzepatide 70%.
- Imagery: warm, sun-lit, candid, real people, calm moments; pharmacy framing as a trust cue (45+). No generic stock-style couples.
- Women's creative (incl. GHK cream): pinks, tans, beige — no oranges or greens.
  **Exception: Sermorelin and Sermorelin GHK** follow Justin's direction (product owner, 2026-10-29): pinks, tans, neutrals and warm tones preferred; white and teal welcome (white backgrounds for advertorials); these are preferences, not limits — keep exploring trends. Their skills' rules apply.
- Intimate wellness (Lovara, PT-141, Spark): tasteful, product-led, no beds/bedroom scenes; PT-141 video stays shoulder-up.
- Sermorelin: frame around muscle, fitness, performance — not the bedroom. Male talent: rugged, unmistakably masculine, hardcore training feel.
- **Hardcore men (Jeremy, 2026-11-02):** bodybuilding / men's-muscle products (Sermorelin, Sermorelin GHK, BPC-157, Wolverine, Spartan; later TRT, Tesamorelin) lean intense: shirtless or stringer, 40–45, flawless muscular condition, hard gym light; random/Surprise-me batches make **up to 30%** of men's slots HARDCORE. **Bible 2026-11-04 caps shirtless male talent at 30% of creatives (static and video) for Sermorelin, Sermorelin GHK, TRT, BPC-157, TB-500, Spartan and Wolverine, and bans shirtless talent, male or female, on Lovara, PT-141, Spark and Titan-Rx.** (Was 40%.) Overrides any "clothed / no shirtless / no flexing / not bodybuilders" line, only up to that cap. Rule: `core/references/hardcore-men.md`. Copy still never ties the body to the product (no before/after, body comparison or body-composition claims).
- Reference top-performing, lowest-CPA creative before generating new iterations. Cap at five iterations per base concept.
- Landing pages: mobile first; build from the approved template; no hamburger, no login, no links to other products on a traffic page; test structurally (A/B, multivariate); default to percent-off, not dollar prices.

## 4. Product-correctness gate
- Product images only from the Product asset library, checked against the website. Drive folders: 1EJkg6ts2jwNWvVPgflHgxvsR3PquYfJF (per-product renders, e.g. "SERMORELIN GHK 500": bottle NOBG + tablet; "INGREDIENT TABLETS") and 1CYPd3P2vpjUkkQvD2WPOJ0P_kcmy7HvP (TABLETS/CAPSULES, GHK cream). Search these folders by parent before saying a render is missing.
- LOOK at every product image and every generated frame; confirm the right product (bottle, vial, tablet). Never infer from a filename.
- Tablet prompts: "use the attached tablet reference exactly; do not invent, alter, or substitute a different pill." Never describe the tablet's shape, colour or markings in text.
- Attach all three references: product bottle render, Trustpilot badge, tablet render.
- LDN and Sildenafil have no tablet/capsule render → flag; never substitute another product's pill.

## 5. Script gate (video)
- 7-beat spine: Hook → Authority → Emotion → Visual element → Structure → Connection → Payoff, with a throughline.
- The hook or key benefit is both **said** (by the on-screen talent; voiceover only in no-person videos) **and shown on screen** within the first 2–3 seconds (bible 2026-11-02). Copy minimal; motion carries emotion, text carries information.
- Every video carries on-screen captions for all spoken audio (bible 2026-11-02, Standards 02).
- **⛔ Humans speak on camera (Mitansh 2026-11-03, HARD):** in any video with a person, that person speaks every line on camera, lip-synced; never a background voiceover over a person (J-cut product cutaways inside the speaker's line are fine). Voiceover only in videos with no person. Rule: `core/references/on-camera-speech.md`.
- The product is always in focus whenever it's on screen: never soft, blurred or racked out of focus (bible 2026-11-02).
- **📋 Team video rules (Mitansh 2026-11-03, HARD):** scripts are a clear, connected mini-story (problem → why → product → what it does → offer → urgent CTA), never cryptic fragments; the problem is said in the first ~1–2 s; no specific ages in video scripts or captions (bible-approved image headlines with an age stay usable, Priestley); scripts are shown as plain chat text with no popup in the same turn; no paid re-take without an explicit "go" (free fix first; never speed up talking); men's music = trap-metal or walk-out, never taiko. Rule: `core/references/video-team-rules.md`.

## 6. Production gate
- **⛔ Prompt layout zones (Mitansh 2026-11-04, HARD, every image prompt, every product):** every 9:16 / 4:5 image prompt (new ads, resizes, re-rolls, edits, start frames, any model) carries the STRICT LAYOUT block from `core/references/prompt-layout-zones.md` with its numbers (9:16: ZONE A top 16% empty, ZONE B 16–56% all text + product, ZONE C plain calm surface, central 67% width; 4:5: top 14% empty, product last and lowest, bottom 33% plain). Raws that miss a zone are re-rolled; never shifted, padded, blurred or hazed. Proof rows are assigned to layouts with a natural shelf (content ends high on a plain surface); product-low and person-led layouts are planned as no-proof up front (same file, "Proof row ↔ layout").
- Model routing: single locked slow shot / talking head / simple product hero → Boreal-style; multi-scene, camera moves, fast motion, transitions → Seedance.
- **⛔ Seedance = Creatify, Higgsfield = Marketing Studio only (Mitansh 2026-11-03, HARD):** every Seedance video, animated still, hook still and start frame runs on the Creatify Model Playground; Higgsfield credits go ONLY to Marketing Studio. Rule: `core/references/seedance-on-creatify.md`.
- **AI avatar videos: everything on Creatify** (Mitansh, 2 Nov 2026: "AI Avatar videos always go to Creatify for everything!!! No Higgsfield needed at all!"): the presenter on Creatify Seedance, the animated background on Creatify Boreal-H3, music on Creatify; 0 Higgsfield credits (`core/references/ai-avatar-video.md`). This wins over the talking-head line above for avatar videos.
- 9:16 safe zone (bible "Safe zones", Meta): **x 156–924, y 144–1385 on 1080×1920, minus the Reels profile corner x 156–375 × y 1216–1385**. Footer exception: the proof row may run x 39–1041 and cross the corner. Feed (4:5, 1:1): 60 px margin. Logo, headline, offer, CTA, disclaimer **and captions** stay inside it (bible 2026-11-02).
- AI expand 1:1→9:16 OK for photo ads; flat infographics are rebuilt.

## 7. Approval gate (hard)
- Explicit approval of the master (Frame.io / Asana Review Status = Approved) before ANY other sizes. Compliance sign-off by Jeremy before anything goes live.

## 8. Pre-review checklist
Concept direction · approved benefits/subheaders · full section 2 pass · section 3 standards · legibility 50+ and spelling · product correctness (label orientation, realistic scale, no distortion: bible 2026-11-04) · ratio/safe zone · disclaimer verbatim + AI disclosure · logo · proof per the 42/28/30 split (`--proof-check` passes) · focal mix per 40/30/30 · discount = the featured form's maximum.

## 9. Delivery gate
- Base 1:1 and 9:16 to Drive; tell Emily.
- Log in Master Creative Library (sheet 1CJfWo81wqhqx7SX8b_dkxOtlsidSzRGZbtTgLZ_UgT4), correct product tab.
- Update the Asana task (Review Status, links).

## Spend gate
Higgsfield (Marketing Studio only) and Creatify (Seedance, stills, Boreal, music) both use shared Everlife team credits: run a cost estimate and get the user's OK before any paid generation.

## Known gaps (flag when touched)
- NAD+ (non-Optima) product page not imported.
- No ad disclaimers on file for Parts B/C products.
- Gate §7 (master approved before other sizes) still says so, while PT-141 (PR #50) and every product (PR #51) now generate both sizes in one run: Priestley to confirm the override stands.
- Non-pill products: 75/25 focal rule (Justin 3 Nov) vs the bible's 40/30/30 for all products: Justin to confirm.
- The bible's "benefits only from the Quick-hit list" vs approved per-ingredient claims: Justin to confirm what counts.
- Advertorial bylines ("Brian L." / "Erika S.", 3 Nov 2026): Jeremy to approve before use. Titan-Rx $1.50/day CTA held until its offer is verified.
- Klow Stack's bible page lists "GHK-Cu" (stack rule, 3 Nov 2026) but the global Hard NO says creative uses "GHK": Justin to confirm before any Klow ad. Glow Stack's peptides are [PLACEHOLDER].
- Bible source: Claude Design project 8cc4e3fe-5189-436d-aaba-6eb2320f14c6 (standalone Claude Design closes 14 Dec 2026). Re-import when it changes.

## Hook Engine (every video, all products)
Every Everlife video starts from the Hook Engine: `core/hook-engine/HOOK-ENGINE.md` (rules) and `core/hook-engine/HOOK-BANK.md` (per-product hooks), imported into CLAUDE.md by install.sh. Pick three scored hooks before each script, run the hook QA on every raw, and log the result. Not used for statics.
