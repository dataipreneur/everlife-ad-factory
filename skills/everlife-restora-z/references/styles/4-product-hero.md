# Category 4 — Product as Hero

Library folders: Product Highlight · Pill-Product Focused · Minimalist · Product-as-Hero (Avatar) · Polaroid · Billboard (boards 1, 3, 4, 5).
What the library shows: premium still lifes (bottle on wet stone with a water splash, linen and leaves, a spotlit plinth), a big serif product name, 3 icon benefits, a Trustpilot + Doctor Prescribed footer; a hand holding the pill up close; dark minimal posters with one bold headline and a 3-benefit strip; the ad shown inside an Instagram post, polaroid or city billboard.
Why it works for Restora-Z: the creative bible says "the pill/tablet is the hero"; our real renders make product fidelity easy.

**Statics: GPT Image 2.5** with BOTH renders attached (`--image rz_bottle.png --image rz_capsule.png`), `--quality high --resolution 2k`, ~2.75 credits. If the label comes out wrong, re-roll or composite the real render in finishing. **Video: Seedance 2.0** (45 cr) with the same references.

---

## 4A — Premium still life
- **Looks like (Product Highlight):** the bottle large on a textured surface (wet slate, river stone, linen, warm oak nightstand), ONE capsule in front, a moonlit-to-amber mood, a soft water splash or drifting mist for motion.
- **Image prompt core:** "luxury product photography, the attached bottle large and sharp at center-left, one attached capsule in the foreground on a wet dark slate stone, cool moonlight rim light + warm amber key, drifting mist, deep navy background with texture; top 22% and bottom 25% clean."
- **Video:** a slow orbit or push-in, the capsule dropping into frame in slow motion, mist rolling (no text).
- **Finishing:** `standard` (headline + 3 ingredient cards + CTA + proof).
- **Starter:** headline *Unlock Deep, Restorative Sleep Every Night* (check the copy log first).

## 4B — Capsule in hand
- **Looks like (Pill-Product Focused, Product-as-Hero):** an extreme close-up of fingers (a 50+ hand, real skin) holding the ONE capsule up to warm lamp light; a person softly out of focus behind (bed, window).
- **Video:** the hand rotates the capsule, the light catches it, a rack focus to the person who smiles and turns the lamp off.
- **Guardrails:** exactly one capsule; never show swallowing multiple pills.
- **Finishing:** `standard` or the video `editorial` look.

## 4C — Minimal bold
- **Looks like (Minimalist):** black or deep-navy background, dramatic single key light on the bottle, one huge headline, a 3-benefit strip.
- **Image:** "dark minimalist studio, single hard key light, the attached bottle on a matte plinth, one capsule leaning against it, deep shadows."
- **Finishing:** `standard` with a short header (≤ 4 words, e.g. *Non-Addictive. No Grogginess.*) and 3 quick-hit benefits as cards (use `benefits` instead of `ingredients`).

## 4D — Ad in a frame (Polaroid / phone / billboard mockup)
- **Looks like:** a real-world object holding the ad: a hand holding a polaroid or an Instagram post, a city billboard, a bus-stop poster at dusk.
- **How:** generate the SCENE with a blank frame (GPT Image 2.5: "a hand holding a blank white polaroid card, cosy bedroom at night, the frame area plain white"), then finishing places a finished 4:5 ad inside the frame (`--layout frame` with `frame_box` x,y,w,h measured on the raw image).
- **Guardrails:** no fake social handles, likes counts or brand names on the frame.

## 4E — ASMR night routine
- **Looks like:** top-down nightstand, crisp foley, a whispered VO, the lamp click → the same frame in morning sun. Made once (visual OK, copy was rejected as repetitive). Write NEW copy.
- **Engine:** Seedance 2.0 (stylised hands only) or Marketing Studio if a face is shown.
- **Guardrails:** exactly ONE capsule into the palm (the earlier render tipped two); plain props with no text (the book cover came out garbled).
- **Finishing:** `editorial`.
