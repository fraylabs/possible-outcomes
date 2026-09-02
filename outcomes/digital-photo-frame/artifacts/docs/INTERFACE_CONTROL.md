# Shared mechanical/electrical interface control

Status: digital pre-build, incomplete. KiCad and CAD remain independent
authorities. Only exported geometry is copied into `models/assembly/exports`.

## Product and display

| Interface | Controlled value |
|---|---|
| Product axes | Origin at front-face centre; +X right, +Y up, +Z rear |
| Product front envelope | 216 x 138 mm |
| Nominal enclosure rear | Z=29 mm |
| Display MPN/configuration | ER-TFTM070-4V3, 5 V, 8-bit 8080, no touch |
| Display outer/max envelope | 180 x 100 x 12.8 mm |
| Display active area | 154.08 x 85.92 mm, centred on product origin |
| Display front/back | Z=4.5 to 17.3 mm; active-area plate is immediately forward |
| Display mounting holes | Four 3.2 mm holes on 174 x 98 mm centres per selected module documentation; not modelled as product fasteners in this first result |
| Display connection | J2, 2x20 2.54 mm vertical pin header on controller PCB |
| Touch | No-touch configuration; pins 33-38 intentionally unconnected |

The CAD ledge clears the 180 x 100 mm display frame by 0.6 mm total in X and Y
and leaves a 2 mm perimeter allowance around the active area. A replaceable
0.5-1.0 mm compliant gasket is required between the ledge/clamp system and
module frame during physical build; no load may be applied to active glass.

## PCB mapping

| Interface | KiCad coordinates | Product coordinates |
|---|---:|---:|
| Board outline | X=20..132, Y=20..90 | X=-14..98, Y=-35..35 |
| Board centre | (76,55) | (42,0) |
| Mount 1 | (24,24) | (-10,-31) |
| Mount 2 | (128,24) | (94,-31) |
| Mount 3 | (24,86) | (-10,31) |
| Mount 4 | (128,86) | (94,31) |
| Board thickness | 1.6 mm | Z=18.5..20.1 |
| Modelled top envelope | 4.5 mm above board | Z=20.1..24.6 |
| Allowed bottom components | None in this revision | Board-to-display gap is 1.2 mm |

Coordinate transform: `product_x = kicad_x - 34`, `product_y = kicad_y - 55`.
The standoff centres exactly use this mapping in the CAD source. Edge clearance
to the inner cavity is at least 5 mm at the right board edge and 29 mm at the Y
edges. Top-envelope clearance to the service-cover underside at Z=27 is 2.4 mm.
The 1.2 mm board-bottom gap is an explicit local exception valid only because
the current PCB places no bottom-side components; solder protrusion and assembly
tolerance remain a physical bring-up check.

## External and service interfaces

| Item | KiCad anchor | Product opening/axis | Status |
|---|---:|---:|---|
| USB-C J1 | (130,32), rotated 90 deg | right wall, Y=-23 | Y aligned; exact shell protrusion unverified without populated PCB STEP |
| microSD J3 | (126,70), rotated 90 deg | right wall, Y=15 | Y aligned; insertion reach unverified without populated PCB STEP |
| Previous SW1 | (86,74) | (52,19) | coordinate-aligned |
| Next SW2 | (96,74) | (62,19) | coordinate-aligned |
| Menu/wake SW3 | (106,74) | (72,19) | coordinate-aligned |
| Ambient sensor U3 | (63,80) | (29,25) | coordinate-aligned |
| Status LED LED1 | (75,76) | (41,21) | coordinate-aligned after source repair |
| Debug J4 | (39,74) | internal, (5,19) | rear cover removal required; not externally exposed |

Keep at least 12 mm unobstructed outside the USB-C opening for plug overmould
and bend, and at least 20 mm outside the microSD slot for finger/card insertion.
The display module uses a rigid pin-header connection in the selected
configuration; there is no FPC bend region. Maintain a 6 mm insertion corridor
above and around J2 until exact mating hardware is validated.

## Stand and service envelope

- Hinge: X-axis, Y=35, Z=29.
- Deployed pose: -18 degrees from folded/rear plane.
- Folded pose: 0 degrees, stand plate substantially flush; final folded product
  bounds are approximately 216 x 139 x 35.2 mm including the stand barrel.
- Deployed product bounds are approximately 216 x 138 x 67.34 mm.
- Retention: spherical folded detents and two deployed stop tabs are modelled;
  retention force and cycle life are not verified.
- Service cover: four M3 reusable fasteners into heat-set inserts; display, PCB,
  controls and cover are intended to be replaceable after cover removal.

## Known failed interfaces

Burr reports positive-volume overlaps between enclosure pieces, display and PCB
envelope, and open component meshes. The deployed integrated assembly has six
reported interfering pairs, folded has seven, and exploded has three. Therefore
no-fit/no-interference claim is made. USB-C/microSD X alignment, all connector
insertion volumes, and mechanical clearances to real populated components remain
unverified because DRC prevented populated PCB STEP export.
