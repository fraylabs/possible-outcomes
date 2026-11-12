# ROUNDS.md: look-match loop

There are no reference shorts. Each still is scored beside a STYLE_BIBLE target card (palette swatches and rules) instead of a reference frame.

## Round 0: pre-render checks (no browser)
- `tsc --noEmit`: pass. Webpack bundle: pass.
- Framing check (`scripts/framing_check.ts`, pure math): the first pass found S2b with the car behind the camera, S4b showing only the twist node at midspan, S7 and S9 with the model cut off at the frame edge, and S6b showing the card edges. All of these were re-keyed and re-checked.

## Round 1: waiting for stills (see RENDER.md)
- Rendered 34 stills at 540x960 in 71.4 s on the render machine (ANGLE). Exit 0.
- Seekability: f0770 and f1300, rendered twice, are pixel-identical (max diff 0). **PASS**.
- Sheets: `sheets/r1_sheet1-4.jpg`, each the bible target card beside 8 stills. Every sheet was scored by a fresh subagent that saw only the sheet and STYLE_BIBLE.md.

| Sheet (frames) | colour | lighting | ink | textures | characters | depth | composition | readability |
|---|---|---|---|---|---|---|---|---|
| 1 (30-500) | 6 | 5 | 6 | 6 | N/A | 6 | 5 | 5 |
| 2 (590-840) | 6 | 5 | 5 | 6 | 7 | 4 | 4 | 4 |
| 3 (905-1235) | 5 | 4 | 4 | 5 | 4 | 4 | 3 | 3 |
| 4 (1300-1760) | 5 | 6 | 6 | 7 | 5 | 6 | 5 | 4 |

Main fixes, merged and assigned to one owner file each:
- **world/env.ts**
  - Long wind ribbons read as contrails or scratches (all four sheets): removed outdoors.
  - Water: unlit palette colour with no cast shadows. The deck shadow read as a floating slab (260, 340).
  - Far range ink: the outline read as a wire or chart line.
  - Clouds: flat, inked and unbloomed. The cropped one read as a glowing orb (645).
  - Car seat lightened so Tubby separates from it.
- **post.ts**
  - Ink inked through character cards, drawing the tree cone over the kid's face (940-1080). Fixed: cards now write a flat normal through their alpha.
  - Ink now fades to 0 with fog.
  - Bloom threshold raised.
- **materials.ts**: cel contrast was invisible because the hemisphere fill was too strong. Fill lowered, shadow ramp to 0.48, so the shadow side lands about 0.55 of the lit side. Concrete is now cream.
- **story.ts (camera)**: every wide re-keyed for 9:16.
  - Hook: shows the twisted deck surface.
  - Twist and break: shot near the antinodes and close enough to read.
  - Water held to 35 % of the frame or less.
  - Push-ins doubled, because pairs read as identical.
  - Tubby close-up tighter; the engineer kept inside the frame.
  - Tunnel shots moved to a 3/4 view.
- **characters.ts**
  - Grass close-up redrawn as a head-and-hands portrait with eyes. It no longer reads as "hot dogs".
  - Brow logic was asymmetric and read angry on Tubby and the engineer.
  - Breath lines kept off the skin, the arrow made smaller, and the kid given a contact shadow.
- **world/tunnel.ts**: black stands read as monoliths, so they're now steel and thin. Walls are pale. Streamlines are thinner and smoother. Twist amplitude raised.
- **Captions.tsx**
  - Caption band lowered to a centre near 0.24 H.
  - Arrow drawn as an inked SVG.
  - End card: heavier blur and fade, placed higher.

## Round 2
- Rendered 34 stills in 51.9 s (ANGLE). Seekability: f0770 and f1300 are pixel-identical again. **PASS**.
- Sheets: `sheets/r2_sheet1-4.jpg`, scored by four fresh subagents (sheet plus bible only).

| Sheet (frames) | colour | lighting | ink | textures | characters | depth | composition | readability |
|---|---|---|---|---|---|---|---|---|
| 1 (30-500) | 7 | 4 | 6 | 7 | N/A | 6 | 5 | 5 |
| 2 (590-840) | 7 | 5 | 5 | 7 | 7 | 6 | 5 | 4 |
| 3 (905-1235) | 5 | 5 | 6 | 6 | 6 | 6 | 5 | 4 |
| 4 (1300-1760) | 7 | 5 | 6 | 6 | 7 | 6 | 6 | 6 |

Gain over round 1: colour +1.5, ink +0.5, textures +0.5, characters +1.7, depth +1, composition +1, readability +0.75. Lighting is flat.

One scorer claim was wrong. "The 7 Nov sky equals the day sky" isn't true: pixels measure #609DDB against #2A8DE5. Since the difference doesn't read, though, the morning preset is pushed greyer anyway.

Main fixes:
- **story.ts (camera)**
  - Twist was invisible: a 12 m deck seen from 200 m barely moves on screen. Every twist shot (hook, 4a, 4b, 8a) now sits 40-65 m from an antinode. Amplitude goes up to the true 28° maximum.
  - The break is shot from beside the west tear.
  - The opening wide includes a tower.
  - S3 tower moved clear of the caption, and the S6c eyes moved out from under it.
  - Tubby framed so the caption sits over sky.
  - Tunnel cameras at deck height.
  - End card: the tower panned off the text, a real push-in, and focus forced near so the whole background reaches the 0.012 H blur. Before, the tower sat closer than the focus distance and stayed sharp.
- **materials.ts**
  - The sun now comes from the -x side, so one visible face of every box sits in shadow tone. Before, both visible faces were lit, so the cel split never showed.
  - Morning preset greyer.
  - Concrete blotches at 12 % contrast or less.
  - Water strokes softer.
- **world/tunnel.ts**: the ceiling and walls cast shadow over the whole set, which is why it rendered dead grey. They no longer cast shadows. Other changes:
  - Cool palette walls and a lighter floor.
  - Streamlines bend over and under the section, and pass through the open truss.
  - Twist phase pinned so a peak lands on "flutter".
- **world/bridge.ts**: splash spheres read as balls, so they're replaced with drawn splash-crown cards.
- **world/env.ts**: cloud underside drawn as a lobe, not a band. Car interior lightened.
- **characters.ts**
  - Grass close-up: wider blade with ends sticking out, slimmer thumbs, lips visible. The orange arrow is replaced by blade bend plus motion ticks, and the shirt is cropped and shaded.
  - Kid wide: swooshes removed, bigger blade, visible ground shadow.
  - Card ink brought to 0.0035 H base, so the visible outer line lands at about 0.0045 H.
- **Captions.tsx**: stroke thinned to 0.0045 H so "a.m." counters stay open.

## Round 3
- Rendered 34 stills in 65.2 s. Seekability: f0770 and f1300 are pixel-identical. **PASS**.

| Sheet (frames) | colour | lighting | ink | textures | characters | depth | composition | readability |
|---|---|---|---|---|---|---|---|---|
| 1 (30-500) | 7 | 5 | 5 | 7 | N/A | 5 | 6 | 5 |
| 2 (590-840) | 6 | 5 | 5 | 7 | 7 | 6 | 4 | 3 |
| 3 (905-1235) | 6 | 5 | 6 | 6 | 6 | 6 | 5 | 5 |
| 4 (1300-1760) | 6 | 5 | 6 | 6 | 5 | 6 | 5 | 6 |

Gain over round 2: none. Average colour 6.25 (was 6.5), lighting 5.0 (4.75), ink 5.5 (5.75), textures 6.5, characters 6.0 (6.67), depth 5.75 (6.0), composition 5.0 (5.25), readability 4.75 (4.75). **This is the first round with no gain.** If round 4 also gains nothing, the loop stops.

Scorer disagreements:
- One scorer wants the car orange; the round-2 scorer wanted less orange. Kept cream.
- One scorer reads the light as coming from +x, but the code sets it from -x.
- The tunnel shadow direction comes from the tunnel's own preset (+x). Fixed by raising it nearly overhead.

Root cause behind the repeated "no twist visible" (sheet 2 at 3/10) and "hook shows no bridge":
- A 12 m deck at 170-200 m is about 7 % of a 9:16 frame's width, so an 18-28° roll barely moves on screen.
- Fix: long-lens (11-14°) shots straight down the roadway at the antinode. The tilting deck fills about 35 % of the width against the horizon.
- The framing checker now prints the deck's on-screen tilt and width.
- The twist phase is pinned so that peaks land on "twist" and "bigger".

## Round 4
- Rendered 37 stills in 55.6 s, including the new f0632/f0677 (twist peaks) and f0785 (mid-fall). Seekability: pixel-identical. **PASS**.

| Sheet (frames) | colour | lighting | ink | textures | characters | depth | composition | readability |
|---|---|---|---|---|---|---|---|---|
| 1 (30-500) | 6 | 6 | 6 | 7 | N/A | 5 | 5 | 5 |
| 2 (590-770) | 6 | 4 | 5 | 5 | N/A | 6 | 4 | 4 |
| 3 (785-1080) | 7 | 6 | 7 | 7 | 6 | 6 | 5 | 4 |
| 4 (1120-1540) | 6 | 6 | 7 | 6 | 7 | 6 | 5 | 5 |
| 5 (1620-1760) | 7 | 6 | 6 | 7 | N/A | 7 | 6 | 7 |

Averages: colour 6.4, lighting 5.6, ink 6.2, textures 6.4, characters 6.5, depth 6.0, composition 5.0, readability 5.0. **Small gain over round 3** (lighting +0.6, ink +0.7, characters +0.5, depth +0.25, readability +0.25), so the loop continues.

The twist now reads in the hook and in S4b: the road banks against the horizon at peaks.

Must-fix readability items, whatever the score:
- Grass close-up: two upright thumbs around a dark slit can read as rude. Redrawn as a tilted clasp with short thumbs and the gap filled by the blade.
- Golden sky: interpolating #4A86D0 to #FFD9A8 passes through a grey-lilac band, which falls under the banned purple. A warm mid stop was added.
- Tubby close-up: the car's B-pillar ran into his head. The dog was moved into the clear front window.

Also fixed:
- Shadows: near-black, soft-edged cast shadows (tunnel, deck) were replaced by hard shadows at 45 % strength, so shadowed areas land at about 0.55 like the cel ramp.
- Tunnel: a bug put the streamlines for the 1950 model at floor height (ym used MODEL_Y - 0.5, not + 0.5). Model truss members thickened and reduced in number.
- Hangers and main cables: dark steel #24493A, not pure ink, so long-lens shots stop reading as cage bars.
- Snapped hangers now dangle instead of vanishing.
- Break framed with the west tower in shot.
- Morning fog pushed back so the hook's hills keep their greens.
- End card: fade raised to 0.75, longer push, smaller type, kept to 75 % width.
- "=" moved to the end of the line above "FLUTTER" (the approved words are unchanged).

## Round 5
- Rendered 37 stills in 158.8 s (slower render-machine load). Seekability: pixel-identical. **PASS**.

| Sheet (frames) | colour | lighting | ink | textures | characters | depth | composition | readability |
|---|---|---|---|---|---|---|---|---|
| 1 (30-500) | 7 | 6 | 6 | 7 | N/A | 5 | 6 | 6 |
| 2 (590-770) | 6 | 5 | 5 | 6 | N/A | 6 | 4 | 4 |
| 3 (785-1080) | 6 | 7 | 6 | 7 | 6 | 6 | 5 | 5 |
| 4 (1120-1540) | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 |
| 5 (1620-1760) | 7 | 5 | 6 | 7 | N/A | 7 | 5 | 6 |

Averages: colour 6.4, lighting 5.6, ink 5.8, textures 6.4, characters 6.0, depth 5.8, composition 5.0, readability 5.2 (overall 5.78 against 5.89 in round 4). **No gain.** This is the first no-gain round after round 4's small gain. If round 6 also gains nothing, the loop stops by rule.

Bugs found by inspecting the full-size frames:
- **f0800 "black pole":** slicePose classified the middle piece's first slice (u = 0.25) as stub, so one quad spanned from the standing stub down to the fallen deck. Pieces now pass their own identity.
- **S8b soft dog:** a leftover `focus: 6` override from round 1 put the focal plane 4 m behind Tubby. Removed.
- **Ragged centre-line ink:** the lane line was a raised strip whose side faces caught normal edges. The slab is now split into three coplanar strips.
- **Dashed double hangers:** hangers at 0.16 m are sub-pixel at distance. Now 0.3 m, and cables and hangers no longer cast shadows (they made the pothole-like blob on the road).
- **Grass close-up:** the round-4 clasp read as two raised fingers. Redrawn as a blade stretched sideways between two fists in front of the lips; it shakes up and down with ghost copies, and the whisker-like ticks are gone. The kid's wide pose matches, with arms rooted at the shoulders.
- **S6 light:** the cut from the 7 Nov morning to a saturated day sky jumped. S6 is now on the morning set.
- **Smaller:** contact shadows lightened. Golden sun less orange, so the far hills stop going khaki. End-card tower panned clear of the text.

## Round 6
- Rendered 37 stills in 122.6 s. Seekability: pixel-identical. **PASS**.

| Sheet (frames) | colour | lighting | ink | textures | characters | depth | composition | readability |
|---|---|---|---|---|---|---|---|---|
| 1 (30-500) | 7 | 7 | 6 | 7 | N/A | 6 | 5 | 5 |
| 2 (590-770) | 6 | 4 | 5 | 5 | N/A | 6 | 4 | 4 |
| 3 (785-1080) | 5 | 4 | 5 | 6 | 4 | 6 | 4 | 4 |
| 4 (1120-1540) | 6 | 6 | 7 | 6 | 6 | 5 | 5 | 6 |
| 5 (1620-1760) | 7 | 6 | 5 | 7 | N/A | 7 | 6 | 7 |

Averages: colour 6.2, lighting 5.4, ink 5.6, textures 6.2, characters 5.0, depth 6.0, composition 4.8, readability 5.2 (overall 5.55 against 5.78 in round 5). **No gain for the second round in a row, so the loop stops here, as the skill requires.**

### Score history (averages across sheets)
| Round | colour | lighting | ink | textures | characters | depth | composition | readability | overall |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5.5 | 5.0 | 5.25 | 6.0 | 5.3 | 5.0 | 4.25 | 4.0 | 5.0 |
| 2 | 6.5 | 4.75 | 5.75 | 6.5 | 6.7 | 6.0 | 5.25 | 4.75 | 5.8 |
| 3 | 6.25 | 5.0 | 5.5 | 6.5 | 6.0 | 5.75 | 5.0 | 4.75 | 5.6 |
| 4 | 6.4 | 5.6 | 6.2 | 6.4 | 6.5 | 6.0 | 5.0 | 5.0 | 5.9 |
| 5 | 6.4 | 5.6 | 5.8 | 6.4 | 6.0 | 5.8 | 5.0 | 5.2 | 5.8 |
| 6 | 6.2 | 5.4 | 5.6 | 6.2 | 5.0 | 6.0 | 4.8 | 5.2 | 5.55 |

### Areas that fell short of 8 (all of them) and why
- **Composition (4.8) and readability (5.2)** are the weakest. Five causes:
  1. **The narrow frame.** A 9:16 frame cannot hold a 1.8 km suspension bridge and its towers at a readable size. Every wide either crops the towers or shrinks the deck to a line, and scorers marked both down.
  2. **Twist shots that don't show twist.** Wide twist shots read as "a camera off to one side", because a still can't separate a rolling deck from an angled camera. Shown in motion, the roll oscillates, which settles it; the stills can't.
  3. **Long-lens cages.** Long-lens road views stack the hangers into a cage, even in dark steel.
  4. **Hand poses.** Hand poses for the grass analogy took four redesigns to stop reading as something else.
  5. **Too much water.** Water above the 22 % target persists in most bridge wides, since the structure sits over water.
- **Lighting (5.4).** Scorers repeatedly read the cel split as missing. Stylised boxes viewed near-frontally show one face, and the -x sun works against cameras that look along -x (S10, S11).
- **Characters (5.0).** The flat drawn cards next to 3D geometry read as pasted on. The close-up anatomy (head, neck, arms) is simple, and proportions drifted between the wide and the close-up cards.
- **Ink (5.6).** Ink sits on thin members at distance (hangers, truss diagonals). The depth/normal pass draws both edges of sub-pixel members as dashed doubles.
- **Colour (6.2), textures (6.2), depth (6.0).** Closest to target. The remaining notes are golden-hour hills going beige, a pale morning sky, and a blur radius at the bible limit that scorers read as soft.
- **Scorer noise.** Fresh scorers often disagreed: car orange or not, light from +x or -x, whether "N/A" counts. Single-sheet scores swing by about ±1 between rounds with no code change in that area.

### Post-loop fixes (high-confidence readability only; checked on frames of the final render, not re-scored)
- Grass close-up read as "a head on poles": the shirt now sits right under the chin, with arms bending at the elbows. The translucent ghost ellipse (read as drool) and the white breath ticks are removed; the blade's shake is shown by its bend alone.
- S6b → S6c cut between nearly identical framings (a jump-cut). The two are now one continuous push-in.
- Kid wide (S6a): the blade read as a moustache, so it's thicker and its ends stick out past the fists.
