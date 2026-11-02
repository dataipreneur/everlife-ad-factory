# Everlife style library: 15 ad styles (shared by every product skill)

Source: the team's Drive folder "Ad styles" (`1lViskBTTmI756jcXE72IOcrGAxCMdQFT`, owner Justin), imported 2026-11-02 at Mitansh's
request: "These should be used as a reference for all the product skills." 14 style folders + **S15 Phone Screen**, built from the
`00_Products` folder (incoming-call and social-post examples). `00_Products` itself (GLP-1, NAD+ Injections, Restora-Z example
ads; Spark was empty) is in `product-examples/<product>/`: category inspiration, same "layout only" rule.

**How to use (all products):**
- The Mood question offers these styles (`MOOD-QUESTION.md`). "🎲 Surprise me" = `core/scripts/pick_styles.py` draws a random,
  non-repeating set every batch.
- For each slot: **Read the style's board** (`boards/<code>_<slug>.jpg`) or one file in `refs/<code>_<slug>/`, describe its
  LAYOUT in the prompt (structure, where the type and product sit, the UI chrome), then write this product's own words, palette and
  product. **Layout only: never copy a reference's words, brand, claims, prices, people or product.** Most references are other
  brands' ads and many break our rules (first person, $ prices, named competitors, "News Flash", weight-loss numbers, needles/pens,
  lips close-ups, body-on-a-scale). The product skill's rules, bible and the global gates always win.
- Our finishing still applies: the real Everlife logo, the proof footer and the verbatim disclaimer are added by `finish_batch.py`;
  never ask the image model for them. Product name big in every ad; type legible at 50+; product hero ≥ 35% width.
- Write the style code into `prompts.md`, the copy log and SESSION.md (e.g. "S02 crossed-out-words") so the ledger can rotate them.

| Code | Style | The layout (from the refs) | Everlife recipe | Never copy / gate |
|---|---|---|---|---|
| S01 | **Bold Headlines** | one huge condensed headline over a dark product shot, small kicker above, one CTA | one bible headline, very large, 2–3 lines; product hero under it; one kicker line | ref is BlueChew ("makes sex fun again"): layout only; no sex-performance language |
| S02 | **Crossed Out Words** | a centred stack of old habits each struck through, ending in one bold un-struck answer (Seed pill-stack, makeup list, our Restora-Z "I tried…") | 3 struck lines = habits/assumptions (never claims, never another product), then ONE approved benefit as the answer, then product | our own Restora-Z ref is **first person ("I tried…")**: never; write the struck lines as plain phrases |
| S03 | **Reasons Why** | "3 reasons to…" title, numbered rows with small icons or product swatches, product beside | "3 reasons to try <product>": three approved lines, numbered, big numerals | ref 3 is first person ("why I use"): never; no "3rd-party tested" unless the bible says it |
| S04 | **Benefit Stacks** | product hero with callout arrows / leader lines to 3–5 benefits (Seed, MaleMD, Purely, the runner with callouts) | product centred, 3–4 approved benefits on leader lines; optional person in motion with callouts | no $ prices ("$149/mo"), no "slows aging", no muscle/fat callouts, no body-area labels |
| S05 | **Myth vs. Fact** | title, two cards: ✗ MYTH / ✓ FACT, product under | a common belief (no brand, no disease) vs an approved claim; product + proof | never "hormone"/"balance hormones" outside the product's scope; no disease myths |
| S06 | **Us vs. Them** | two columns or a check table: our product vs "Others" (em, Seed, wellmedr) | "<Product>" vs "The usual way" / "Other options", ✓ rows from approved claims only | **no named competitors** (Restora-Z vs Ambien is the only exception, on its own page); **no $ price columns**: percent-off only |
| S07 | **What's Inside** | product or capsule at centre, ingredients radiating out on thin lines with labels | product centre, each ingredient on its own spoke with ONLY its own bible claim; single-ingredient products → mechanism map (product → signal → benefit) | Spark: never tie a benefit to one ingredient; no invented ingredients |
| S08 | **Search** | "the search:" + a search bar with a pain-point query, "the solution:" + product on texture | search bar with a pronoun-free query from an approved pain point ("energy for long runs"), then product + one approved line | no symptom/disease queries; no "you" questions |
| S09 | **Notes / Reminders** | iOS Notes list, Reminder alert (Options / Close), AirDrop card with product photo, over a textured photo | Notes checklist of approved benefits, or a Reminder alert carrying a bible headline, or an AirDrop card showing the product; product large beside it | GLP-1 pen ref = needles: never; lips close-up: never (intimate products especially) |
| S10 | **AMA (Ask Me Anything)** | Instagram story: question sticker ("AMA: Looking great, what have you been doing?") + creator answer text | question sticker with a pronoun-free question; the answer in **brand voice** (approved claims) beside the product | **refs are first-person creator testimonials + weight-loss / belly-fat claims: never**; no "I", no results claims, no selfies of bodies |
| S11 | **News** | editorial headline on a photo, a red tag, a highlighted phrase (Fridays, Novos) | article-style: a highlighted bible headline on a real photo, small "Everlife" section tag | **no "News Flash" / "Breaking News"**, no "clinical study" claims for the product, no $ prices, no competitor names |
| S12 | **Testimonial** | stars + a quoted review over product shots (Joi + Blokes) | a verbatim, screened review from the product's `reviews.md` + stars + product | **gated:** only when `reviews.md` has screened reviews for this product; never invent or edit a quote |
| S13 | **Whiteboard / Billboard** | a note on a whiteboard, a comparison chart on a board, a roadside or Times-Square billboard carrying the ad | a billboard in a real place (skyline, highway, wall) or a whiteboard with a handwritten approved line; product on the board | no $ prices; **no bathroom-scale / body imagery**; no weight numbers; no named competitors on the chart |
| S14 | **We're Sorry** | a bold "We're Sorry" apology letter on black; a tongue-in-cheek half-price post | brand voice apology: "We're sorry… <an approved claim / the offer>"; product small, type does the work | no profanity (Hume ref); no competitor digs; offer = the bible offer only |
| S15 | **Phone Screen (call / post)** | incoming-call screen ("Your vitamins are calling", Decline / Accept); a Reddit-style post + a promoted reply | incoming call: "<Product> is calling…" + the product as the caller photo; or a forum post title (a pronoun-free pain point) + a promoted brand reply with approved claims | posts in the refs are **first person ("I wake up exhausted")**: write the post as a pronoun-free question; no $ prices, no dose ("up to 1600mg") |

## Grouping (for the picker question; ≤ 4 per group)
- **Text-led:** S01 Bold Headlines · S02 Crossed Out Words · S03 Reasons Why · S04 Benefit Stacks
- **Compare:** S05 Myth vs. Fact · S06 Us vs. Them · S07 What's Inside · S08 Search
- **Phone & social:** S09 Notes / Reminders · S10 AMA · S11 News · S15 Phone Screen
- **Out loud:** S12 Testimonial (gated) · S13 Whiteboard / Billboard · S14 We're Sorry

## Product notes
- **Product-led intimate products (PT-141, Spark, Lovara):** S09 no lips; S10 / S15 never a sexual question; no beds anywhere.
- **Body-composition products (GLP-1, MOTS-c, Tesamorelin, Sermorelin):** S04 / S13 never a body, a scale, a waist or a number of pounds.
- **Vial products (BPC-157, GLP-1, MOTS-c, Spartan, Wolverine, NAD+ injection):** the vial is a still object; never a pen, syringe or needle (S09 ref 3).
- **Restora-Z:** S06 vs Ambien only with the approved Ambien claims and Ambien's real pill (not on file → skip).
