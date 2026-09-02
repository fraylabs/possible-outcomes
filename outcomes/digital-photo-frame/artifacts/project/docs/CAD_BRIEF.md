# CAD brief

## Goal and scope

Create a landscape tabletop enclosure for a documented seven-inch display, a
compact controller PCB envelope, a reusable-fastener rear cover, and a folding
easel stand. The authoritative editable source is
`models/cad/source/photo_frame_parts.py`; STEP and STL files are generated
artifacts. The detailed PCB is not represented as validated populated geometry
because the KiCad PCB failed DRC and parity, so the assembly intentionally uses
a named conservative PCB envelope and is incomplete.

## Units and coordinates

- Units: millimetres and degrees.
- Origin: centre of the front product face.
- +X: landscape right; +Y: product up; +Z: toward the rear.
- Front exterior plane: Z=0.
- Rear-cover exterior plane: Z=29.
- Stand hinge axis: X direction through Y=35, Z=29.

## Objects and configuration

- `front_bezel`: 216 x 138 mm rounded outer form, 4 mm face, display-frame
  ledge and an unobstructed 158.08 x 89.92 mm window around the active area.
- `rear_chassis`: 216 x 138 mm, rear envelope ending at Z=29, service-cover
  insert bosses, PCB standoffs/ribs, connector openings, hinge blocks and hard
  stops.
- `service_cover`: 208 x 130 x 2 mm; four M3 clearances, controller/power vents,
  three button holes, ambient-sensor hole, and rear status-light opening.
- `folding_stand`: 140 x 105 x 4 mm plate with hinge barrel, folded detents, and
  stop tabs; deployed source angle -18 degrees and folded angle 0 degrees.
- `display_envelope`: EastRising ER-TFTM070-4V3 documented 180 x 100 x 12.8 mm
  maximum envelope plus 154.08 x 85.92 mm active-area plate.
- `pcb_unverified_envelope`: 112 x 70 x 1.6 mm board plus 4.5 mm conservative
  top-side component envelope. This is explicitly not a populated-PCB STEP.
- Product outputs: deployed, folded, and rear-cover-open exploded arrangements
  built from unchanged rigid component functions.

## Constraints and assumptions

- Outer front envelope must remain <=230 x 165 mm. Actual: 216 x 138 mm.
- Enclosure excluding stand must remain approximately 22-30 mm deep. Nominal
  exterior planes span 29 mm; the hinge/stop source is constrained to Z<=29.
- Display ledge locates the module by its outer frame, not active glass.
- Four product PCB standoff centres are (-10,-31), (94,-31), (-10,31),
  (94,31), mapped from KiCad holes (24,24), (128,24), (24,86), (128,86).
- Side openings share the KiCad connector Y coordinates; final X insertion and
  shell engagement require the missing validated populated-PCB STEP.
- No underside PCB components are allowed in the current integration envelope.
- Prototype parts require a build volume of at least 220 x 140 x 30 mm when
  oriented flat; this is an envelope statement, not a printability proof.

## Validation contract

All nine final STEP files were run through CAD `inspect refs --facts --planes
--positioning` and `inspect validate`; every final validation reported
`failureCount: 0`. Every primary STEP has at least one saved snapshot. These
checks prove closed positive-volume source geometry, but do not supersede
Burr's failed tessellated interference check or prove manufactured fit.
