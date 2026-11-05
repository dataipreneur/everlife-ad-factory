# Everlife World Deck (v1, 2026-11-05)

Source: the Restora-Z 2nd batch (2026-10-29, 235 ads). A WORLD is the universe an ad lives in. Dealt per slot by
`core/scripts/deal_worlds.py`; this file is the readable version of `worlds.json` (generated, edit the json).
Rules live in the gates + code, not here. Translate every world to the product; take the idea, never another product's theme.

## Families
- **PRINT**: paper and print objects: newspapers, tickets, memos, posters, books
- **COMIC**: illustrated and stylised worlds: comic, pop art, clay, pixel, knit, stained glass
- **MATERIAL**: one material carries the whole ad: marble, glass, liquid, clouds, chrome, feathers
- **SCENE**: a real place with real light: bus shelter, pharmacy, porch, gallery, elevator
- **UI**: screens and interfaces: phone article, search bar, forecast, notes, switch, waveform
- **PERSON**: a real person leads: holdout, hug, UGC selfie, lamp reader, b/w portrait
- **TYPE**: typography is the picture: brutalist, swiss, knockout, type ring, scribble, repeat
- **INFOGRAPHIC**: the formula explained visually: exploded view, blueprint, numbered, orbit, podium
- **SURREAL**: impossible but photoreal: moon, cloud bank, capsule sofa, dreamcore hall, levitation
- **METAPHOR**: one clever object idea: yarn, switch, ticket, hourglass, lineup, mini-bed

## Worlds

| id | World | Family | Look | Type | Product | Translate | Flags |
|---|---|---|---|---|---|---|---|
| `magazine` | **Magazine cover** | PRINT | editorial cover: masthead-size product name, cover lines down one side, a calm portrait or still life as the cover photo, cream or white paper | high-contrast serif masthead + small-caps cover lines | bottle as the cover 'object', pill beside the barcode area | men: fitness magazine cover, hard light, stringer or shirtless lifter as cover star; intimacy: lifestyle magazine cover, shoulder-up smiling portrait, warm daylight; metabolic: wellness magazine cover, bright kitchen light; skin: beauty magazine cover, blush paper, dewy portrait |  |
| `newspaper` | **Newspaper front page** | PRINT | broadsheet front page on a table, headline across columns, 'Morning Edition' style nameplate, product resting on the paper | heavy serif headline, column body text | bottle on the fold, pill on the headline | generic: nameplate uses the product's benefit world (e.g. 'The Training Edition', 'The Morning Edition') | no-breaking-news |
| `classifieds` | **Classified ad circled** | PRINT | newspaper classifieds page, one ad circled in blue pen: 'WANTED: ...', product lying on the paper | typewriter / classifieds serif | bottle on the page, the circled ad is the headline | generic: WANTED line = the approved pain point phrased as a want ('Wanted: a full night of sleep' -> 'Wanted: mornings with energy') |  |
| `wanted` | **Western wanted poster** | PRINT | aged parchment poster, saloon-town night behind, star badge, torn edges | slab western wood type | bottle as the 'outlaw' photo, pill as the badge | men: 'The gym has a new sheriff'; generic: 'The night/morning has a new sheriff' |  |
| `public-notice` | **Public notice poster** | PRINT | red-and-cream civic notice pasted on a wall, bold stacked lines, stamp marks | condensed poster grotesque, red + cream | bottle leaning on the poster | generic: 'NOTICE: <benefit> resumes tonight/today' |  |
| `ticket` | **Admit-one ticket** | PRINT | vintage cinema ticket on velvet seats: 'ADMIT ONE: a full night's sleep' | ticket serif + perforation | bottle beside the ticket | men: 'Admit one: the 5 a.m. session'; intimacy: 'Admit one: an unplanned evening'; metabolic: 'Admit one: a steady afternoon' |  |
| `boarding-pass` | **Boarding pass** | PRINT | airline boarding pass on a blanket: FROM tossing & turning TO deep sleep, boards 10:30 PM, arrives 6:30 AM | airline mono + sans | bottle on the pass | men: FROM sore TO back on the bar; metabolic: FROM 3 p.m. slump TO steady; generic: the FROM/TO pair is the approved pain -> benefit | no-readable-times-in-video |
| `order-ticket` | **Restaurant order ticket** | PRINT | thermal receipt on a kitchen pass: 'Tonight's order: ingredient ✓ ingredient ✓ TOTAL: 1 capsule' | receipt mono | bottle beside the ticket | generic: lines = the product's ingredients or forms; total = one dose / one tablet / one vial |  |
| `memo` | **Office memo** | PRINT | paper-clipped memo on a desk: 'TO: The Racing Mind, RE: Bedtime', fountain pen | typewriter + serif headline | pill clipped to the memo, bottle at the corner | generic: TO: the pain point personified; RE: the benefit |  |
| `letter` | **Handwritten letter** | PRINT | cream letter with wax seal: 'Dear restless nights, your lease is up.' | script + small serif | pill on the seal, bottle in the corner | generic: 'Dear <pain point>, ...' pronoun-free |  |
| `dictionary` | **Dictionary entry** | PRINT | open dictionary page: 'sleep-through /slēp-thrü/ noun: ...' with 'see also' lines | dictionary serif + italics | pill on the page, bottle on the book | generic: coin a word for the benefit ('bounce-back', 'steady-state') |  |
| `sticky-notes` | **Sticky notes** | PRINT | yellow stickies on a mirror or fridge: 'Tonight's to-do: sleep.' | handwriting marker | bottle on the shelf below | men: on a gym locker; metabolic: on the fridge door |  |
| `collage` | **Ransom collage** | PRINT | torn-paper collage, cut-out letters, Polaroid scraps, 'Pieced together for sleep' | ransom letters + typewriter | bottle taped into the collage | generic: the torn pieces are the ingredients or benefits |  |
| `leaflet` | **Pharmacy leaflet** | PRINT | folded white leaflet 'in large print', pharmacy shelves soft behind | large clean sans, red accents | bottle in front of the leaflet | generic: pharmacy trust cue; 50+ legibility built in |  |
| `longread` | **Long-read article** | PRINT | white page, drop cap, two pull-quotes, product photo inset, byline area | editorial serif body, bold sans headline | bottle as the article photo | generic: advertorial family; byline needs Jeremy (gates) | byline-pending |
| `blueprint` | **Blueprint** | INFOGRAPHIC | white lines on blueprint blue, the capsule/bottle drawn as a technical plan with callouts | drafting mono | the product IS the drawing, real bottle in the corner | generic: callouts = ingredients or the three approved benefits |  |
| `chalkboard` | **Chalkboard math** | PRINT | blackboard, chalk: 'ingredient + ingredient + ingredient = product', crossed-out old habits | chalk handwriting | bottle on the chalk tray | generic: cross out the myths, chalk in the formula |  |
| `typewriter` | **Typewriter page** | PRINT | vintage typewriter, a sheet half typed with the headline, warm desk lamp | typewriter mono | bottle beside the machine, pill on the keys |  |  |
| `comic-strip` | **Comic strip** | COMIC | 4-panel vintage comic: the problem at 2 a.m., the doctor, bedtime, the payoff; halftone paper | comic lettering, caption boxes | real bottle composited into the last panel | men: 4 panels: alarm, gym, the tablet, the lift; intimacy: panels stay shoulder-up, kitchen/dinner, no bed | no-faces-compared |
| `pop-art` | **Pop art** | COMIC | Ben-Day dots, bold outlines, speech bubble 'SLEEP. AT LAST.', a hand holding the pill | comic display caps in a yellow banner | real bottle in the frame, pill in the hand | men: 'LIFT. AGAIN.'; metabolic: 'STEADY. ALL DAY.' | hand-held |
| `superhero-cover` | **Superhero comic cover** | COMIC | explosive comic cover, city skyline, 'THE NIGHT HAS A NEW HERO', burst shapes | chunky comic title | bottle as the hero figure, pill flying | men: 'THE SESSION HAS A NEW HERO' |  |
| `ingredient-team` | **Ingredient team cards** | COMIC | trading-card trio: each ingredient as a character card with one approved claim; 'MEET THE 3-IN-1 TEAM' | comic caps on card frames | bottle centre, cards around | generic: stack products: one card per peptide (lists every peptide, gates); single-ingredient products: cards = three benefits |  |
| `noir` | **Film noir case file** | COMIC | black-and-white detective office, venetian-blind light, 'THE CASE OF THE 3 A.M. WAKE-UP', product in colour | typewriter case-file labels | the only colour object on the desk | men: 'The case of the missing recovery'; metabolic: 'The case of the 3 p.m. crash' |  |
| `western-saloon` | **Western night street** | COMIC | moonlit saloon town, painterly, product standing in the street | wood type | bottle as the gunslinger |  |  |
| `retro-futurism` | **Retro-futurism** | COMIC | 1960s space-age lounge, egg chair, Earth in the window, 'Tomorrow's bedtime, today' | atomic-age script + sans | bottle on the console | metabolic: 'Tomorrow's energy, today' |  |
| `pixel` | **8-bit game** | COMIC | pixel-art room, 'PLAYER 1 IS ASLEEP', dialogue box, pixel moon | pixel font dialogue box | real bottle composited as the item pickup | men: 'POWER-UP UNLOCKED', pixel gym; metabolic: 'ENERGY BAR: FULL' |  |
| `claymation` | **Claymation** | COMIC | stop-motion clay figure, tired in bed or at a desk, soft studio light | rounded friendly sans | real bottle beside the clay figure | men: clay lifter at a clay rack; intimacy: clay couple at a kitchen table, shoulder-up |  |
| `clay-blob` | **Clay blob character** | COMIC | a grumpy clay blob yawning with coffee, pastel backdrop, 'Zero energy all day' | bold humanist sans | bottle next to the blob | metabolic: the blob is the slump |  |
| `mascot` | **Product mascot** | COMIC | the capsule/bottle as a friendly 3D character with eyes, nightcap or headband, interacting with a real room | playful rounded display | mascot = product; real bottle also present | men: mascot with a headband spotting a lifter; intimacy: avoid; use a different world | not-intimacy |
| `knit` | **Knitted world** | COMIC | everything knitted: pills as yarn balls, 'Woven into one', chunky wool texture | soft rounded sans | real bottle nested in wool | skin: cashmere tones, blush and cream |  |
| `embroidered` | **Embroidered headline** | COMIC | headline stitched into linen, 'Sleep, sewn up.' | embroidery serif | bottle on the linen |  |  |
| `papercut` | **Paper-cut layers** | COMIC | layered paper landscape at night, hills and a cabin, 'Night, layer by layer' | clean sans | bottle standing in the paper scene | men: paper-cut mountain trail; metabolic: paper-cut sunrise |  |
| `stained-glass` | **Stained glass** | COMIC | cathedral window with the ingredients as glass motifs, 'Three in harmony' | gothic-lite serif | bottle on the sill |  |  |
| `art-nouveau` | **Art nouveau poster** | COMIC | Mucha-style border, botanical frame, 'A nightcap, prescribed' | nouveau display | bottle in the medallion | skin: ideal for GHK cream |  |
| `vintage-pharma` | **Vintage pharmacy label** | COMIC | 1920s apothecary ad, mortar and pestle, ornate frame, ingredient medallions | Victorian display + script | bottle centre on an oval | generic: pharmacy trust cue |  |
| `marble` | **Set in stone** | MATERIAL | headline carved into a marble block, dark stone studio | carved Roman caps | bottle on the block | men: black granite, chalk dust |  |
| `glass` | **Crystal glass type** | MATERIAL | headline rendered in refracting glass on a bright surface | glass 3D display | bottle in front of the glass word |  |  |
| `fluted` | **Fluted glass** | MATERIAL | product behind ribbed glass, cool pale light | thin editorial serif | bottle sharp through a gap in the glass | skin: blush light |  |
| `holo` | **Holographic foil** | MATERIAL | iridescent foil backdrop, capsules scattered sharp | clean sans | bottle angled on foil |  | pills-max-one-in-video |
| `prism` | **Prism light** | MATERIAL | a diagonal rainbow refraction across a white scene | serif + small caps | bottle in the light beam |  |  |
| `cascade` | **Capsule cascade** | MATERIAL | capsules tumbling in a blue glossy cascade, 'Stacked in your favor' | italic display | bottle at the base |  | pills-max-one-in-video |
| `liquid` | **Liquid sim** | MATERIAL | three coloured liquids swirl into one; 'Three flows, one formula' | bold sans | bottle where the flows meet | generic: flows = ingredients or forms |  |
| `ink` | **Ink bloom** | MATERIAL | navy ink blooming in water around the product, 'Let sleep spread' | serif italic | bottle in the bloom | metabolic: gold ink |  |
| `splash` | **Liquid-smooth splash** | MATERIAL | chrome-blue liquid splash frozen around the bottle | chrome display | bottle in the splash |  |  |
| `burst` | **Capsule cracked open** | MATERIAL | a capsule bursts into its three ingredients mid-air | bright sans | the capsule is the hero | generic: only for multi-ingredient tablets/capsules | pill-products-only |
| `chrome` | **Chrome type** | MATERIAL | liquid-chrome product name, dark studio | chrome 3D caps | bottle under the word | men: strong fit |  |
| `light-paint` | **Light painting** | MATERIAL | long-exposure light ribbons orbit the product | neon script | bottle centre |  |  |
| `pearl` | **Hidden gem** | MATERIAL | oyster or geode opened to reveal the pill | elegant serif | pill in the shell, bottle beside | skin: pearl tones |  |
| `feathers` | **Feathers** | MATERIAL | white feathers drifting, 'Light as a feather' | light serif italic | bottle among feathers | skin: blush feathers |  |
| `clouds` | **Cloud bank** | MATERIAL | product on a bank of real clouds at sunrise | warm display | bottle on the clouds |  |  |
| `puffy` | **Puffy type** | MATERIAL | inflated cushion letters spelling the name | puffy 3D | bottle leaning on a letter |  |  |
| `extruded` | **Extruded type** | MATERIAL | the product name extruded as a solid block on sand or stone | extruded 3D sans | bottle on the block | men: concrete |  |
| `emboss` | **Embossed paper** | MATERIAL | white-on-white embossed moon or symbol, minimal | thin serif | bottle, tiny shadow |  |  |
| `lava` | **Lava lamp blobs** | MATERIAL | golden glossy blobs float around a podium | rounded display | bottle on the podium |  |  |
| `waveform` | **Waveform** | UI | a sound wave flattening to a line: 'turned quiet' | clean sans | bottle on the line | metabolic: a spike flattening to steady |  |
| `switch` | **The switch** | METAPHOR | a big physical toggle: OFF restless, ON sleep; concrete wall | industrial caps | bottle beside the switch | generic: OFF = pain point, ON = benefit, pronoun-free |  |
| `bus-shelter` | **Bus shelter poster** | SCENE | a lit bus-shelter ad on a rainy night street, the ad is our ad | any, inside the poster | bottle inside the poster frame |  |  |
| `billboard` | **Billboard break-out** | SCENE | highway billboard at dusk, the product bursts out of the board | billboard caps | bottle breaking the frame |  |  |
| `neon` | **Neon sign** | SCENE | neon product name on a brick wall, shelf below | neon tube script | bottle on the shelf | men: gym brick wall |  |
| `gallery` | **Gallery plinth** | SCENE | white museum room, the product on a plinth, small wall label | museum caption sans | bottle on the plinth |  |  |
| `elevator` | **Elevator** | SCENE | elevator doors opening on a bed / a gym / a sunrise: 'Next floor' | brass elevator caps | bottle on the floor indicator shelf | men: doors open on the squat rack; intimacy: doors open on a kitchen dinner, no bed |  |
| `doorway` | **Doorway light** | SCENE | warm light through a half-open door, 'Right this way' | serif italic | bottle on the threshold | intimacy: door opens on a living room, never a bedroom |  |
| `cabinet` | **Medicine cabinet** | SCENE | a small lit cabinet on a flat blue wall, doodled moon and stars | friendly sans | bottle inside the cabinet |  |  |
| `pharmacy` | **Pharmacy counter** | SCENE | a pharmacist's hands (no face) slide the bottle across the counter | clean sans | bottle centre, hands only | generic: trust cue for 45+ | hands-only |
| `desk` | **Morning desk flat lay** | SCENE | overhead desk: laptop corner, coffee, glasses, notebook, product | clean sans | bottle in the flat lay | men: gym bag flat lay: chalk, wraps, shaker |  |
| `nightstand-lineup` | **Shelf lineup** | SCENE | a wooden shelf with small labelled bowls of the ingredients and the bottle | label serif | bottle at the end of the line | generic: bowls = ingredients, or the forms |  |
| `dark-academia` | **Dark academia** | SCENE | candle, old books, library at night, 'Study hall is closed' | book serif | bottle on the desk | men: 'Gym's closed. Recover.' |  |
| `golden-hour` | **Golden-hour porch** | SCENE | a real person on a porch at first light with coffee, 45–65, candid | warm serif | bottle on the rail | men: porch after a run, towel on shoulder | person |
| `cinematic-window` | **Cinematic window** | SCENE | rain on a window, a man in a dark room looking out, moody | spaced caps | bottle on the sill |  | person |
| `split-time` | **Same room, two hours** | SCENE | left: the room at 3 a.m. blue; right: same room at 7 a.m. warm. No people compared. | big time stamps (analog or soft) | bottle on the nightstand in both halves | men: left: cold garage pre-dawn; right: same garage, bar loaded; metabolic: left: 3 p.m. desk; right: same desk, 6 p.m. | no-bodies-compared |
| `fog-mirror` | **Fogged mirror** | SCENE | product name written in a fogged bathroom mirror | finger-written | bottle on the sink |  |  |
| `blinds` | **Through the blinds** | SCENE | a hand parting blinds, morning light | bold sans | bottle on the sill |  | hands-only |
| `tv` | **Retro TV** | SCENE | a 1970s TV showing the night sky, 'Now showing: a full night' | TV title serif | bottle on the TV |  |  |
| `phone-article` | **Phone article** | UI | a phone screen with an article headline, product beside the phone | iOS article type | bottle beside the phone |  | no-call-screens |
| `search` | **Search bar** | UI | a big search field: 'waking up at 3 a.m. every night' -> 'Search no further.' | search UI sans | bottle below the field | generic: the query is a pronoun-free pain point |  |
| `forecast` | **Weather forecast** | UI | a weather-app card: 'Tonight: Calm', icons for 10 PM / 2 AM / 6 AM | weather UI | bottle under the card | metabolic: 'Today: Steady' |  |
| `notes` | **Notes app** | UI | a Notes page with a checklist of benefits | iOS notes | bottle beside the phone |  |  |
| `reply-comment` | **Reply to comment** | UI | UGC selfie with a 'Reply to comment' bubble: 'What's actually in it?' | comment bubble UI | bottle held up to camera | generic: the comment is a pronoun-free question | person, hand-held |
| `tiles` | **Photo tiles** | UI | a 2x2 grid of calm photos, one tile is the product | caption sans | one tile |  |  |
| `hud` | **Sci-fi HUD** | UI | holographic dashboard, hexagon callouts, the product on a light ring | HUD mono | capsule on the ring, bottle beside | men: strong fit |  |
| `poll` | **Poll card** | UI | a poll: 'Up at 3 a.m. again?' YES / ALSO YES, handwritten 'real question' | poll UI + marker | bottle below | generic: question stays pronoun-free |  |
| `holdout` | **Hold-out** | PERSON | a real person holds the bottle to camera, label sharp, tight crop | stacked bold caps beside | bottle in hand, label readable | men: hardcore lifter, hard light; intimacy: shoulder-up, daylight, kitchen | person, hand-held |
| `big-hug` | **Giant bottle hug** | PERSON | a person hugs a person-sized bottle, white studio, joyful | friendly bold | the giant bottle | intimacy: avoid; pick another | person, not-intimacy |
| `ugc-selfie` | **UGC selfie** | PERSON | phone-shot selfie, natural light, product in frame, caption bar | caption sans with highlight | bottle held or on the table |  | person, hand-held |
| `lamp-reader` | **Lamp reader** | PERSON | a person reading in a warm armchair at night, lamp on | serif italic | bottle on the side table |  | person |
| `bw-portrait` | **B/W portrait** | PERSON | black-and-white studio portrait, the product the only colour | elegant serif | bottle in colour | men: strong fit | person |
| `capsule-sofa` | **Capsule sofa** | SURREAL | a person reclines on a giant capsule like a sofa in a living room | serif italic | the giant capsule + real bottle | intimacy: avoid reclining; pick another | person, not-intimacy, pill-products-only |
| `drop-the-day` | **Drop the day** | PERSON | a person falls back onto a mattress while laptop, phone and papers float away | bold sans | bottle on the mattress | intimacy: no mattress; use 'drop the day' onto a couch | person |
| `mini-bed` | **Pocket-sized** | SURREAL | a tiny bed inside an open capsule in a palm, 'Pocket-sized' | serif | the capsule in the palm, bottle beside | men: a tiny squat rack in the capsule | hand-held, pill-products-only |
| `moon` | **Moon cradle** | SURREAL | a crescent moon as a hammock in the clouds, 'Sleep on cloud nine' | display caps | bottle floating by the moon | metabolic: a sunrise crest |  |
| `dreamcore` | **Dreamcore hall** | SURREAL | an endless pastel hall of doors and clouds, 'Where good nights live' | airy serif | bottle at the vanishing point |  |  |
| `levitate` | **Levitation** | SURREAL | product and pills floating in gold light, 'Gravity optional' | gold display | bottle floating |  | pills-max-one-in-video |
| `moon-stairs` | **Moon stairs** | SURREAL | stone steps into a giant moon, 'Step by step' | serif italic | bottle on a step |  |  |
| `harbor` | **Harbor light** | SURREAL | a lighthouse at dusk, product as the lamp, 'Finds its harbor' | serif italic | bottle as the lantern |  |  |
| `ocean` | **Deep ocean** | SURREAL | product sinking slowly through deep blue water, light shafts | serif italic | bottle mid-water |  |  |
| `bubble` | **Soap bubble** | SURREAL | product inside a giant soap bubble on a sunlit bed of grass | clean sans | bottle in the bubble |  |  |
| `sheep` | **Sheep clocked out** | SURREAL | cartoon-real sheep asleep on a giant capsule, 'Even the sheep clocked out' | playful display | giant capsule + bottle | men: gym mascot bulls asleep? no: use another world | restora-only |
| `sheet-ghost` | **Sheet ghost** | SURREAL | a sleeping bedsheet ghost, Halloween warm, 'Boo-tifully' | playful display | bottle on the nightstand |  | seasonal |
| `orbit` | **Orbit ring** | INFOGRAPHIC | a thin gold ring orbits the bottle with three benefit callouts | serif italic + small sans | bottle centre |  |  |
| `exploded` | **Exploded view** | INFOGRAPHIC | the bottle's parts float apart vertically: cap, capsule, ingredients, with thin leader lines | technical sans | the bottle exploded | generic: vials: cap, vial, label as the parts |  |
| `numbered` | **Numbered one to three** | INFOGRAPHIC | big numerals 1 2 3 down the page, one approved line each, sky backdrop | giant serif numerals | bottle beside the list |  |  |
| `giant-numeral` | **Giant numeral** | INFOGRAPHIC | a huge '3' or '1' fills the page, 'Ingredients. 1 Capsule.' | display numeral | bottle in the counter of the numeral | generic: the number = ingredients, forms or peptides |  |
| `thirds` | **Engineered in thirds** | INFOGRAPHIC | a capsule drawn as three chambers on blueprint blue | drafting | capsule as diagram, bottle real |  | pill-products-only |
| `podium` | **Podium spotlight** | INFOGRAPHIC | the capsule upright on a lit podium, three ingredient orbs around | bold sans | capsule centre |  |  |
| `pillar` | **Vertical pillar** | INFOGRAPHIC | a tall glowing pillar with the product name running vertically, three nodes | vertical caps | bottle at the base |  |  |
| `ingredient-bar` | **Ingredient bar** | INFOGRAPHIC | three ingredient chips in a row with a + between, sunrise behind | clean sans | bottle below the bar | generic: stacks: one chip per peptide |  |
| `team-cards` | **Flashcards** | INFOGRAPHIC | three index cards pinned on cork, one ingredient each | handwriting + print | bottle on the desk |  |  |
| `macro` | **Macro capsule** | INFOGRAPHIC | extreme close-up of the pill with water droplets, bottle soft-free behind (still sharp) | small caps | pill hero |  | pill-products-only |
| `brutalist` | **Brutalist** | TYPE | concrete wall, huge condensed black caps, one yellow bar | ultra-condensed grotesque | bottle on a concrete block | men: best fit |  |
| `swiss` | **Swiss** | TYPE | white page, red block, strict grid, 'Sleep. Simplified.' | Helvetica-style grotesque | bottle right, grid-aligned |  |  |
| `knockout` | **Knockout type** | TYPE | the product name cut out of a navy page revealing a night sky | heavy caps, image-filled | bottle in front | men: name filled with gym light |  |
| `typering` | **Type ring** | TYPE | a glowing ring of text circles the bottle on cobalt | caps on a path | bottle centre |  |  |
| `typestack` | **Type stack** | TYPE | huge stacked words 'SLEEP THAT ACTUALLY SHOWS UP' with a cut-out portrait | stacked bold caps, one word in colour | bottle held by the portrait | men: 'STRENGTH THAT SHOWS UP' hardcore portrait | person, hand-held |
| `scribble` | **Scribble** | TYPE | a giant marker scribble headline, a person sits on a huge bottle | marker handwriting | giant bottle + real bottle |  | person |
| `repeat` | **Repeat pattern** | TYPE | the product name repeated as a wall pattern, one line highlighted | repeated caps | bottle in front |  |  |
| `bauhaus` | **Bauhaus** | TYPE | primary shapes, circle and bar, vertical name | geometric sans | bottle on the bar |  |  |
| `vertical` | **Vertical name** | TYPE | the product name runs vertically down one edge in deep red | tall serif | pill held between fingers |  | hand-held |
| `wall` | **Type wall** | TYPE | cobalt wall of outline letters, finger pressing the pill | outline caps | bottle + pill |  | hand-held |
| `lineup` | **Clock vs capsule** | METAPHOR | a grumpy brass alarm clock faces off against the capsule mascot | bold caps | capsule + bottle | metabolic: a coffee cup faces the tablet |  |
| `no-coffee` | **Skip the extra** | METAPHOR | a crossed-out coffee cup beside the bottle, 'Skip the extra espresso' | bold sans | bottle | metabolic: crossed-out snack |  |
| `restock` | **Restock the shelf** | METAPHOR | a hand places bottles on a bathroom shelf, 'Restock your nights' | condensed caps | bottles | men: restock the gym bag | hands-only |
| `beam-split` | **Dark/light beam** | METAPHOR | half the frame in night blue, half in morning gold, the bottle on the seam | serif italic | bottle on the seam |  |  |
| `alarm-clock` | **Two clocks** | METAPHOR | two digital clocks 3:07 and 7:00 on a nightstand, 'Sleep through 3:07' | LED digits + serif | bottle between |  | no-readable-times-in-video |
| `yarn` | **Untangled yarn** | METAPHOR | a tangle of yarn resolving into one neat ball, 'untangled' | serif italic | bottle beside |  |  |
| `setdesign` | **Set design** | METAPHOR | a tan studio set with a circular cut-out and a row of pills on a ledge, 'Neatly arranged' | serif italic | bottle on the ledge |  |  |
| `leatherbook` | **Leather book** | SCENE | the bottle on an embossed leather book, 'the premium edition' | gold-foil serif | bottle on the book |  |  |
| `walnut` | **Walnut tray** | SCENE | the name carved into a walnut tray, warm lamp | carved serif | bottle on the tray |  |  |
| `chairs` | **Director's chairs** | SCENE | two director's chairs: 'RESTLESS NIGHTS' empty, 'RESTFUL NIGHTS' with a person; 'Now starring' | movie serif | bottle on the chair | generic: the two chair labels are pain point / benefit, no bodies compared | person |
| `collage-photo` | **Photo collage** | PRINT | a grid of evening-routine photos: tea, candle, book, product | serif italic | one frame |  |  |
| `social-proof` | **Social proof hero** | TYPE | 'Over 100,000 happy customers' as the headline over a sparkling night, bottle hero | bold sans | bottle | generic: counts as the badge+count proof; dealer gives it proof=count | proof-count |
| `review` | **Review card** | PRINT | a verbatim Trustpilot review on a card, 5 stars, bottle beside | quote serif | bottle | generic: only reviews from the skill's reviews.md | needs-review |
| `ambien-switch` | **Switch comparison** | INFOGRAPHIC | two-column product vs the approved competitor with the real pill | clean sans | bottle vs pill |  | restora-only |

## Menus

**Type pairings:** heavy condensed grotesque, all caps + light humanist sans · elegant high-contrast serif, roman + clean geometric sans · serif with ONE italic word + small-caps sans · wide extended sans, bold + regular sans · slab serif, bold + light sans · chunky rounded sans + mono-spaced labels · brush or handwritten accent word inside a sans headline + regular sans · thin editorial sans, tracked out, all caps + serif body · typewriter mono headline + small serif · comic display caps + comic lettering

**Accents:** label red, brass gold, deep navy, charcoal on cream, cream on charcoal, ink on sand, forest, teal, sky, slate, mocha, rose, blush, burgundy, warm white, cobalt, amber, mint

**Placements:** headline top-left, product right · headline centred, product centred below · headline split either side of the product · headline bottom-third above the shelf, product above it · headline vertical down one edge · headline inside the world object (poster, screen, page)

**Lights:** morning window light, golden hour, overcast soft, studio hard key, night lamp pool, neon spill, blue hour

## Flags
- `person`: a real person leads (counts toward the 25% person focal) · `hand-held`: product in a hand (max 20% of a batch) · `hands-only`: hands, no face
- `not-intimacy`: never for PT-141 / Lovara / Spark / Titan-Rx · `restora-only` · `pill-products-only` · `needs-review`: only with a verbatim approved review
- `no-bodies-compared`, `no-faces-compared`: the split is rooms/hours/objects, never people · `no-breaking-news` · `no-call-screens` · `seasonal` · `byline-pending` (Jeremy)
