# Hardcore men: the bodybuilding-product rule (Jeremy, via Mitansh, 2026-11-02)

> Mitansh, 2026-11-02: "strictly upload rules for all body building masculine products! And corely instruct them! To recommend
> more intense / shirtless / hardcore models and images for these masculine products! Also in random mode for these products, 40%
> of images should be hardcore manly! These are direct instructions from jeremy! So override anything that stops it!"

**This file OVERRIDES every older line in these skills that says "fully clothed", "no bare torso", "never shirtless", "no
flexing", "not a bodybuilder", "fit, mature, not bodybuilders", "natural build", or a winner's "Don't copy: shirtless
bodybuilder" note.** Where any of those lines disagree with this file, this file wins. That includes the gates
(`core/claude/everlife-gates.md` Sermorelin line) and the Hook Engine's no-shirtless / no-flexing rule (`HOOK-ENGINE.md` §8).

## Products (the bible's men's pages say "a serious gym-goer with a hardcore training feel")
Listed in `hardcore-men.json` (the picker reads it):
- **Sermorelin** (Men) · **Sermorelin GHK** (Men) · **BPC-157** (Men) · **Wolverine Stack** · **Spartan Stack**
- Future skills to opt in when built: **TRT / Enclomiphene**, **Tesamorelin**, **Tesamorelin/Ipamorelin** (men's slots).
- NOT these: Titan-Rx (men's intimate wellness, stays tasteful and product-led), MOTS-c, Epithalon, GHK-Cu Cream, Glow Stack,
  Lovara, PT-141, Spark, Restora-Z, NAD+, GLP-1. Women's slots on any product are never hardcore.

## The 40% rule (random mode)
In **🎲 Surprise me / Random**, **40% of the men's slots are HARDCORE** (exactly: floor(0.4 × N) plus a 40% chance of one more,
so it averages 40% every batch; 5 ads → 2 or 3). `core/scripts/pick_styles.py --product <id> --n <N> --audience <men|women|both>`
tags those slots `HARDCORE` in its output; write the slot as a HARDCORE slot. For "Both", only men's slots count. When the user
picks moods or styles by hand, still **recommend** hardcore first for men's slots (option 1 or in the description), and offer a
"💪 Hardcore shirtless" mood wherever the skill's mood question has room.

## A HARDCORE slot looks like this
- **Visual references (read first):** `core/references/hardcore-men-refs/REFS.md`: H1 (stringer-tank lifter on a box,
  dark gym, benefit-icon column) and H2 (shirtless 45–50 silver fox, low-key side light, check-list). Take the look, never the copy.
- **Cast:** a man **40–45** (Wolverine / Spartan / BPC-157 may use their own 25–55 / 30–45 range), flawless condition: lean,
  dense, visibly muscular shoulders, chest, arms and back, veins, defined but natural (not a stage bodybuilder in posing trunks,
  not a cartoon). Tattoos welcome. Beard or stubble, cropped or silver hair, rugged and confident, real skin, sweat, chalk.
- **Wardrobe:** **shirtless** (default) or a stringer / cut-off tank; training shorts or joggers, lifting belt, wrist wraps.
- **Action:** intense: mid-set on a loaded barbell, a heavy carry, rope climb, sled push, battle ropes, chin-ups, between sets
  breathing hard; a natural pump or flex in the moment is fine. Holding or presenting the product with intent.
- **Place and light:** a hardcore gym or garage gym (steel rack, iron plates, rubber floor, chalk), or a fight gym; hard side
  light or top light, deep shadows, real texture and depth.
- **Prompt line to use** (replace the skill's "fully clothed … no bare torso, no flexing poses" line in HARDCORE slots only):
  `a rugged man aged 40–45 in flawless physical condition: lean, dense and visibly muscular shoulders, chest, arms and back,
  veins, real skin texture and sweat, tattoos optional, stubble; shirtless (or a stringer tank), training shorts, lifting belt,
  chalked hands; intense and confident, mid-set or between sets in a hardcore gym under hard light; a real person, not a stage
  bodybuilder, not a celebrity look-alike.`
- **Video:** the same cast, waist-up or full-body; shirtless is allowed in the hook and every beat.

## Still applies to every slot, hardcore or not (compliance: Jeremy signs off on every ad anyway)
- The **product stays the hero** and in focus (tablet or vial per the skill; label legible; exactly one tablet).
- **Copy never says the product gave him that body.** No before/after, no "same man" splits, no body comparison, no
  "get this body", no "results in X weeks", no "ripped / shred / burn / melt", no naming a body area, no body-composition or
  fat claims. Headlines and benefits only from the bible (e.g. "Forge a Stronger Physique" is still ⚠ until approved).
- No needles, syringes or injecting; no bedroom; no blood or gore (Wolverine / Spartan); no celebrity look-alikes; no mirror
  selfies (they read cheap); disclaimer verbatim + AI disclosure, logo, social proof.
- Non-hardcore slots follow the skill's own direction as before (e.g. Sermorelin's fitted-tee silver fox, scene variety).
