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
- **No body-composition or "fat and skinny" claims on any product.**
- No targeted fat loss; never name a body area (FTC). No "melting belly fat" style. Avoid melt, burn, ripped, shred.
- No unsupported medical-style claims, no exaggerated transformation claims, no claims outside the product's approved benefit scope.
- Never call a sublingual "all natural". Peptides support the body's own production — that is the limit.
- Say "supports", never "builds". No "high circulation". No vague inference phrasing ("one better night's sleep", not "one better night").
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
- Proof split (bible 2026-11-02, Standards 02 · 06): applied as (Mitansh 2026-11-02): 30% of creatives carry no proof; 70% carry one footer proof, of which 60% the trust row (Trustpilot, Doctor Prescribed, Ships Free From Pharmacy) and 40% the Trustpilot 4.9 badge + "Over 100,000 happy customers" (images: `finish_batch.py --proof-plan N`; videos: `core/scripts/proof_next.py`). Logo + verbatim disclaimer on every creative.
  **HARD, no conflicts (Mitansh 2026-11-02: "This should be followed without any conflicts!"):** ≈ 42% trust / 28% badge + count / 30% none, per batch and per ratio; replaces every "every ad carries visible social proof" line. Compose proof ads with a clean shelf for the row (9:16: product + CTA end above y 1150); never swap a planned proof to "none" on your own (re-roll with cost shown, or ask); `finish_batch.py --proof-check <batch folder>` must pass before a batch is shown.
- Authority = sourced trust signals only (100,000+, Trustpilot, Doctor Prescribed / "Dr. Prescribed, Direct From Pharmacy", Ships Free From Pharmacy). No adjectives as authority.
Disclaimers & AI disclosure:
- Use the product's **Ad disclaimer verbatim** — from the bible, or from the product skill's `product.json` when the bible has none (e.g. BPC-157). Never written, paraphrased or invented. Don't stop over a missing bible disclaimer when the skill has one.
- Every AI-generated image/video carries the AI disclosure; nothing AI-generated goes live without it. Wording is "AI depictions", never "AI deceptions". Global line: "ADVERTISEMENT: AI-generated depiction and simulated portrayal. Not an actual patient or medical provider." (Differs from product disclaimers' wording — open question for Jeremy; flag until resolved.)

## 3. Creative standards gate
- The pill/tablet is the hero, not the bottle. If a bottle appears it is large, foreground and legible.
- Product and benefit identifiable in under 2 seconds; product names run big.
- Texture and depth behind the product — never flat color. No shadows or outlines on type.
- Bullet type readable at story size; don't over-bullet. Text legible for age **50+**; spelling checked.
- Must hold up in square and vertical. Never end on a passive frame — last frame is benefits + a clear, specific CTA.
- **Everlife logo on every ad.**
- Imagery: warm, sun-lit, candid, real people, calm moments; pharmacy framing as a trust cue (45+). No generic stock-style couples.
- Women's creative (incl. GHK cream): pinks, tans, beige — no oranges or greens.
  **Exception: Sermorelin and Sermorelin GHK** follow Justin's direction (product owner, 2026-10-29): pinks, tans, neutrals and warm tones preferred; white and teal welcome (white backgrounds for advertorials); these are preferences, not limits — keep exploring trends. Their skills' rules apply.
- Intimate wellness (Lovara, PT-141, Spark): tasteful, product-led, no beds/bedroom scenes; PT-141 video stays shoulder-up.
- Sermorelin: frame around muscle, fitness, performance — not the bedroom. Male talent: rugged, unmistakably masculine, hardcore training feel.
- **Hardcore men (Jeremy, 2026-11-02):** bodybuilding / men's-muscle products (Sermorelin, Sermorelin GHK, BPC-157, Wolverine, Spartan; later TRT, Tesamorelin) lean intense: shirtless or stringer, 40–45, flawless muscular condition, hard gym light; random/Surprise-me batches make 40% of men's slots HARDCORE. Overrides any "clothed / no shirtless / no flexing / not bodybuilders" line. Rule: `core/references/hardcore-men.md`. Copy still never ties the body to the product (no before/after, body comparison or body-composition claims).
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
- The hook or key benefit is both **said** (voiceover or talent) **and shown on screen** within the first 2–3 seconds (bible 2026-11-02). Copy minimal; motion carries emotion, text carries information.
- Every video carries on-screen captions for all spoken audio (bible 2026-11-02, Standards 02).
- The product is always in focus whenever it's on screen: never soft, blurred or racked out of focus (bible 2026-11-02).

## 6. Production gate
- Model routing: single locked slow shot / talking head / simple product hero → Boreal-style; multi-scene, camera moves, fast motion, transitions → Seedance.
- 9:16 safe zone (bible "Safe zones", Meta): **x 156–924, y 144–1385 on 1080×1920, minus the Reels profile corner x 156–375 × y 1216–1385**. Footer exception: the proof row may run x 39–1041 and cross the corner. Feed (4:5, 1:1): 60 px margin. Logo, headline, offer, CTA, disclaimer **and captions** stay inside it (bible 2026-11-02).
- AI expand 1:1→9:16 OK for photo ads; flat infographics are rebuilt.

## 7. Approval gate (hard)
- Explicit approval of the master (Frame.io / Asana Review Status = Approved) before ANY other sizes. Compliance sign-off by Jeremy before anything goes live.

## 8. Pre-review checklist
Concept direction · approved benefits/subheaders · full section 2 pass · section 3 standards · legibility 50+ and spelling · product correctness · ratio/safe zone · disclaimer verbatim + AI disclosure · logo · proof per the 42/28/30 split (`--proof-check` passes).

## 9. Delivery gate
- Base 1:1 and 9:16 to Drive; tell Emily.
- Log in Master Creative Library (sheet 1CJfWo81wqhqx7SX8b_dkxOtlsidSzRGZbtTgLZ_UgT4), correct product tab.
- Update the Asana task (Review Status, links).

## Spend gate
Higgsfield uses shared Everlife team credits: run a cost estimate and get the user's OK before any paid generation.

## Known gaps (flag when touched)
- NAD+ (non-Optima) product page not imported.
- No ad disclaimers on file for Parts B/C products.
- AI disclosure wording mismatch (global vs product disclaimer).
- Bible source: Claude Design project 8cc4e3fe-5189-436d-aaba-6eb2320f14c6 (standalone Claude Design closes 14 Dec 2026). Re-import when it changes.

## Hook Engine (every video, all products)
Every Everlife video starts from the Hook Engine: `core/hook-engine/HOOK-ENGINE.md` (rules) and `core/hook-engine/HOOK-BANK.md` (per-product hooks), imported into CLAUDE.md by install.sh. Pick three scored hooks before each script, run the hook QA on every raw, and log the result. Not used for statics.
