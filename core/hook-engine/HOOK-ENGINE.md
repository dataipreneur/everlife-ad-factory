# Everlife Hook Engine (v1, 2026-10-30)

Applies to every Everlife VIDEO (all everlife-* skills: Restora-Z, Sermorelin, Sermorelin GHK, BPC-157, PT-141, and future products).
Not for statics. Animated stills: motion starts at frame 0 (the push-in or glint is already moving in the first frame).

**Precedence:** CLAUDE.md Creative Gates → the product skill's own rules and bible → this engine. If a hook breaks any of
them, the hook is dropped. Where a skill says "Hook (0–2 s)", use this engine's stricter timing. Copy (headers, claims, CTAs)
still comes only from the bible. This engine decides the opening ACTION, not new claims.

## 1. The hook contract (pass/fail, checked on every script AND on every raw video)
1. **Frame 0 is already mid-action.** No fade-in, no establishing shot, no logo, no still product, no person about to start.
   The first frame alone should look like a screenshot someone would send a friend.
2. **Timing:** motion or impact by 0.5 s · the hook lands by 1.5 s · the product (or its name) on screen by 3 s. Products that
   require speech from the first second (Sermorelin, Sermorelin GHK) keep that rule: the hook happens WHILE they talk.
3. **Sound-first:** one sharp, real sound at 0.0–0.3 s (thud, alarm, crash, catch-slap, cork pop, laugh). Written into the AUDIO block.
4. **One idea:** explainable in 5 words ("bottle flies, he dodges it").
5. **Bridge in one cut:** the chaos connects to ONE bible pain point or benefit (chaos → calm, stuck → comeback). Random shock that
   doesn't connect fails.
6. **Same-frame payoff preferred:** the team's favourite winner is comedic chaos → the SAME framing goes calm.
7. **Real people, real rooms, photoreal.** No surreal 3D, floating beds or cinematic fantasy (the team rejected these). 45+ talent
   unless the skill says otherwise.
8. **Compliance applies to visuals too:** nobody gets hurt (no hit to the face, no fall by 50+ talent, no injury or medical
   emergency); pills never spill, scatter or get shared (exactly one pill/tablet/capsule on screen); no needles or syringes, ever; no
   bedrooms or beds for intimate products; no shirtless, no flexing (EXCEPT the hardcore-men products in `core/references/hardcore-men.md`:
   shirtless, flexing and bodybuilder casts are allowed and recommended there, Jeremy 2026-11-02), no body before/after or body comparison; no "Breaking News";
   no named competitors (except the skill's approved ones); dialogue has no I/me/my and no "Are you…?"; no readable text in the
   generated video except the real label (headers are added in finishing).
9. **Safe zone:** the hook action happens inside the skill's 9:16 COMPOSITION block (central column, top 8% to 63% of height).
10. **Model-feasible:** fast throws make objects morph, so every hook has a **landing moment**: the real product, still and
    label-readable for ≥ 0.6 s inside the safe column. QA checks the product there.

## 2. Hook families (rotate; never the same family twice in a row for one product)
- **IMPACT**: throw, catch, drop, dodge, slam, slide down the counter.
- **INTERRUPTION**: camera bump, doorbell, whistle, someone barges into frame mid-sentence.
- **ABSURD ESCALATION**: a small everyday problem blown up comically.
- **SAME-FRAME FLIP**: chaos → identical framing, calm.
- **POV / ODD ANGLE**: from inside the mailbox, drawer, fridge, gym bag; locked overhead.
- **SOUND-FIRST**: a huge sound at 0.0 s, snap zoom to the source.
- **STREET / INTERVIEW**: an ambush question, a mix-up, a reveal (answers pronoun-free, bible lines only).
- **MISDIRECTION**: opens like another genre (cooking show, nature doc, sports replay) and swerves into ours by 2 s.
- **SPEED**: speed ramp, freeze-frame mid-air (the header is added in finishing), rewind.
- **CONTRAST SPLIT**: two realities in one frame (chaos side / calm side). Never bodies.

## 3. Marketing Studio built-in hooks (Higgsfield `--hook_id`)
At the start of every video session run `higgsfield marketing-studio hooks list --json` (free). Match hooks **by name**; never
reuse an old id. Rules: works only with `marketing_studio_video` in modes `ugc`, `ugc_how_to`, `ugc_unboxing`, `product_review`;
the hook text is PREPENDED to our prompt; can't be combined with an ad-reference video; always pass `--product_ids`; if the CLI
says `Unknown params: hook_id`, use the Seedance route instead.

| MS hook | Use | Everlife adaptation (write it in our prompt) |
|---|---|---|
| Product Dodge | ✅ all | The flying object is the sealed bottle/box/pharmacy bag; they come up holding it, label to camera |
| Product Hit | ✅ all | Soft hit to the shoulder only, surprise not pain; never the face |
| Random Object Mic | ✅ all | On-theme object (see the bank) |
| Camera Bump | ✅ all | Light bump, a laugh, no injury reaction |
| Interview | ✅ all | Answers pronoun-free, only bible lines |
| Product Crash | ⚠️ adapt | The pharmacy bag or shipping box falls and bursts. The Rx bottle/vial never smashes, pills never scatter |
| Blizzard | ⚠️ rare | Only grounded and photoreal; never surreal |
| Epic Fail | ⚠️ | Men under 50, Sermorelin/Sermorelin GHK only, pure comedy, never next to a recovery claim, never BPC-157 or PT-141 |
| Spicy | ❌ | Not for Everlife (body close-ups) |

## 4. The Hook Ladder: why every batch gets better
**Ledger:** `~/Everlife-Creative/hook-ledger.jsonl`, one JSON line per hook used:
`{"date","product","family","mechanic","route","job","score","rating","meta_hook_rate","status"}`, where status is active, winner or retired.

**HOOK-10 score:** 1 point each: ① frame-0 stop power ② motion + sound by 0.5 s ③ curiosity gap ④ bridge to a bible pain point
⑤ product visible/named by 3 s ⑥ novelty (0 if the same family+mechanic appears in this product's last 10 ledger lines) ⑦ easy to
follow for a 50+ viewer ⑧ model-feasible with a clean landing moment ⑨ safe-zone fit ⑩ compliance (any doubt = drop the hook).

**The bar rises:**
- Pitch only hooks scoring **≥ 8**.
- The top pitched hook must score **above the median of this product's last 5 ledger scores**.
- At least one option is from a family this product hasn't used in its last 3 videos.
- **Winners breed:** a hook rated 5, or with this product's best Meta hook rate, becomes `winner`. Winners are never repeated as-is:
  mutate exactly ONE variable (object, angle, cast, room, speed or sound). Once a winner exists, one of the 3 options is always a winner mutation.
- **Losers retire:** rated ≤ 2, or bottom-quarter hook rate → `retired`; never pitched again for that product unless asked.
- **Data beats opinion:** when anyone pastes Meta results (hook rate / thumb-stop %, 3-s views, hold rate, CTR, CPA) for a video,
  update its ledger line and re-rank.

## 5. Step: "Pick the opening hook" (runs before EVERY video script, inside the skill's script step)
1. Read this file, `HOOK-BANK.md` (the product's section), the product's last 15 ledger lines (create the ledger if missing), and
   the live MS hook list.
2. Silently brainstorm **8** hooks across ≥ 5 families: winner mutations, bank hooks, adapted MS hooks, and ≥ 2 brand-new
   inventions. Bank hooks are starting points; vary them (room, object, cast, angle) so no two teammates' ads look identical.
3. Score each with HOOK-10. Drop anything < 8, anything with a compliance doubt, and anything repeating the ledger.
4. AskUserQuestion, one question "Opening hook for this video?": 3 options, label `<FAMILY> · <5-word mechanic>`, description =
   frame-0 description + sound + score + route (MS hook name or Seedance) + credit cost; the best one first, marked "(Recommended)".
   4th option: "Show 3 different hooks". A hook typed by the user goes through the contract; say plainly if it fails and why.
5. The chosen hook is beat 1 of the script; the rest of the skill's script structure continues as normal. The last frame is still
   benefits + a clear CTA. In the script summary show: `Hook (0–1.5 s): family · mechanic · score · route · frame 0 · sound`.

## 6. Writing the hook into the generation prompt
**Route A: Marketing Studio UGC** (a real talking human): `--mode ugc` (or `ugc_unboxing` / `product_review`),
`--hook_id <id matched by name>`, `--product_ids`. Our prompt starts with:
"Continuing straight from the opening hook: <the Everlife adaptation from §3>. The hook is light comedy; nobody is hurt; no pills
spill. All dialogue is third-person or pronoun-free; nobody says I, me or my." Then all of the skill's normal prompt blocks, unchanged.

**Route B: Seedance** (physics, camera moves, chaos): put this block first, before the skill's normal blocks:
"HOOK 0.0–1.5 s: Frame 0 starts mid-action: <exact action>. <camera move>. Sound at 0.0 s: <sound>. At ~1.2 s <landing/catch>:
the product (attached reference, exact) is still and label-readable for 0.6 s inside the central safe column. No slow fade-in,
no establishing shot, no static opening frame."
**Start frame (mandatory for physical hooks, learned 2026-10-30):** text-only Seedance ignores "frame 0 mid-action" (it opened on a
still glass). First make a ~0.25 cr still of the exact hook moment (GPT Image 2.5, 9:16, the product references attached, faces below
the top 25%), show it to the user, then pass it as the video's START image. Put the 0.0 s sound in the HOOK block AND as the first
AUDIO item. Write dialogue to end by ~11 s ("all dialogue ends by 11 seconds"). Prefer non-alcoholic props near an Rx product.

Model routing stays as in the gates: talking UGC → Marketing Studio; multi-scene/camera moves/chaos → Seedance; a single locked
product hero → Boreal. Always quote the cost and get approval before generating.

## 7. Hook QA on every raw (free, before finishing, before showing the user)
Contact sheet of frames at 0.0 / 0.25 / 0.5 / 1.0 / 1.5 / 3.0 s (ffmpeg). Check: frame 0 mid-action · sound at the start ·
correct real product and readable label at the landing · safe zone · nothing non-compliant. If the action starts late, offer a
free trim (`ffmpeg -ss <t>`). Otherwise show the raw honestly and offer a re-roll with its cost; never pay for a fix the user hasn't picked.
Optional, paid, only with approval: Higgsfield Virality Predictor on the finished video, with its score added to the ledger.

## 8. After each video
1. AskUserQuestion "Rate the hook": 5 Banger / 4 Good / 3 OK / 2 Weak / 1 Kill.
2. Append the ledger line (score, rating, job folder).
3. Add the hook to the product's copy log and as a column in the session's SESSION.md
   (`family · mechanic · score · rating`).
4. At wrap-up, name the families this product hasn't tried yet.
