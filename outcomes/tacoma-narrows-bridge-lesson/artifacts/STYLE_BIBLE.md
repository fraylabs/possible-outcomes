# STYLE_BIBLE.md: Look B, "Bold flat toon"

There are no reference shorts. The buyer picked look B, so every number below is a target set by this bible, not measured from a reference. Everything that follows is built and checked against this file. Every pixel value is a fraction of the output height H (H = 1920 for the final, 960 for half-size stills).

## Format
- 1080x1920, 30 fps, about 59 s (1770 frames). Voice starts at 0.30 s and ends at 54.5 s; the silent end card runs from 55.0 to 59.0 s.
- Safe area for words: no text below 0.78 H (the platform UI sits there) and none in the right-hand 0.12 W strip below 0.55 H.

## Motion and camera
- Shot length 2.8-7.6 s (median about 4.5 s). Cut on sentence boundaries, 0-3 frames before the first word of the new sentence.
- Every hold has a push-in: FOV narrows 6-10 % over the shot plus a dolly of 6-12 % of subject distance (round 1: 3-6 % read as frozen pairs).
- Camera height: wide bridge shots at 25-60 m above the water (deck at 58 m), close deck shots at deck +1.5 to +4 m, character shots at eye level (1.2-1.6 m).
- FOV 28-50 degrees vertical. Roll limited to ±4 degrees, except a ±1.5 degree shake on impacts.
- Impact shake: amplitude 0.6 % of subject distance, decaying with a 0.35 s half-life, made from summed sines (seeded).

## Depth and lens blur (light: look B stays crisp)
- Subject plane sharp. Circle of confusion grows linearly with |depth - focus| / focus, up to a maximum radius of 0.0035 H at the far background and 0.006 H for foreground props closer than 0.4x the focus distance.
- Character shots: background blur max 0.006 H (round 1: 0.0035 H read as sharp).
- The end card uses heavy background blur, 0.010 H.

## Textures
- Flat colour plus painted Canvas2D detail at no more than 12 % contrast: water stroke bands, grass tufts on the hills, concrete blotches on the piers, road lane lines. Clouds are flat cards: white, with a #D6E3F2 underside and a #5C7FA6 outline.
- No photo textures and no noise grain.

## Characters
- Drawn in Canvas2D on camera-facing cards. Proportions: head = 1/2.6 of total height, eye height = 0.17 of head height, pupils solid ink, one white catch-light.
- Outline: variable width, 0.0045 H outer silhouette and 0.0022 H inner lines, tapered at stroke ends.
- Face library: neutral, puff (blowing), surprised, worried, sad, focused. Blink every 2.6-4.1 s (seeded), lasting 4 frames.
- Cast (all original): Kid (yellow cap, orange shirt), Tubby (black spaniel, cartoon), Engineer (cream shirt, green tie, clipboard).

## Lighting and colour (hex, with the target share of the frame on a typical bridge wide)
| Role | Hex | Share |
|---|---|---|
| Sky top | #2E8FE0 | 30 % |
| Sky horizon / fog | #BFE6FF | 12 % |
| Water deep | #1D6FB5 | 22 % |
| Water highlight strokes | #5FC0F5 | 4 % |
| Hills dark | #1F6B3A | 10 % |
| Hills light / grass | #5DBB63 | 6 % |
| Gertie steel (towers, girders) | #3A9A62 | 6 % |
| Road (base #454950, reads #3B414B after grade) | #3B414B | 3 % |
| Ink | #141619 | 2 % |
| Cables / hangers (dark steel) | #24493A | 2 % |
| Accent (car, key words) | #FF7A1A | <2 % |
| Cream (text, concrete) | #FFF3D9 | 3 % |
- Lights:
  - Day: sun #FFF6E6 from (-0.4, 0.75, 0.55), sky fill #9FD3FF.
  - Morning of 7 Nov: sun #F2F6FF, sky top #86A9C8, horizon #DCE6EE.
  - Golden: sun #FFD6A0 from (-0.7, 0.32, 0.6), sky top #4A86D0, horizon #FFD9A8.
  - The sun always comes from the -x side, so one visible face of every box reads in the shadow tone. In round 2, light from +x lit both visible faces.
- Cel shading in 2 tones: ramp lit 1.0 / shadow 0.48 at N·L = 0.35, with a low hemisphere fill (0.45-0.6), so the shadow side lands at about 0.55 of the lit side. The fill's ground colour #2B4A8C sets the shadow hue. Water is unlit palette colour and receives no cast shadows.

## Outlines (ink pass on the 3D world)
- Depth and normal edges: ink #141619, width 0.0026 H (5 px at 1920). Ink fades from full at 0.3x fog-far to 0 at 0.85x fog-far (round 1: far ridges inked through the sky read as wires).
- Character cards keep their own drawn outlines (described above).

## Grade (applied last)
- Saturation x1.12, contrast x1.06 around 0.5. Lift adds #000000 (no lifted blacks).
- Golden shots get a warm offset of +0.03 R and -0.02 B. Morning shots get a cool offset of -0.01 R and +0.02 B.
- Bloom: threshold linear luma 0.92 (only near-white highlights), strength 0.22, radius 0.012 H. No vignette beyond 6 % darkening at the corners. No grain.

## Captions (the brief asks for captions)
- Fredoka, weight 680. Cap height 0.026 H for body lines and 0.032 H for the hook and key words (font size = cap height / 0.72).
- Cream #FFF3D9 fill with a 0.0055 H ink #141619 stroke (paint-order stroke) and an ink drop shadow offset 0.003 H.
- Key words in accent #FF7A1A.
- The block starts at 0.17 H, so its centre falls at 0.20-0.28 H; never below 0.78 H. The end-card block starts at 0.27 H over a 0.012 H blur and a 66 % navy (#0E2A4A) fade.
- Lines pop in over 5 frames (scale 0.92 to 1.0, plus opacity), 0-3 frames before their spoken word.

## Shadows, sky and steel
- Cast shadows are hard-edged (basic shadow map) at 45 % strength, so a shadowed area lands near the 0.55 cel shadow tone and never goes black.
- The sky has three stops: horizon, mid (at 40 % of the ramp), top. Golden uses mid #A9D3EE so blue-to-peach never passes through grey-lilac (banned purple).
- Main cables and hangers are dark steel #24493A; the ink pass draws their edges. Pure-ink bars read as cages in long-lens shots.

## Twist and break
- The twist reads only within about 65 m of an antinode (u = 0.25 / 0.75). Twist amplitude rises to the true 28° maximum.
- The splash is drawn crown cards (white, #BFE6FF base, ink edge). Never spheres.

## Wind
- No long wind ribbons outdoors; they read as contrails. Wind is told by the captions and the sound. In the tunnel: 8 streamlines, 0.018 m wide, at 30-75 % alpha.

## Banned
Purple gradients, glowing orbs, decorative particles, eyebrow labels, watermark, film grain, AI or stock footage.
