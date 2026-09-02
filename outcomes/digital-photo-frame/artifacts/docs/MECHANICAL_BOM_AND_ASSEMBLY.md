# Mechanical BOM and assembly instructions

## Hardware BOM

| Qty | Item | Specification / status |
|---:|---|---|
| 1 | Front bezel | Printed prototype from `front_bezel.stl` |
| 1 | Rear chassis | Printed prototype from `rear_chassis.stl` |
| 1 | Service cover | Printed prototype from `service_cover.stl` |
| 1 | Folding stand | Printed prototype from `folding_stand.stl` |
| 4 | M3 heat-set insert | Brass, nominal 4.6-5.0 mm OD x 4-6 mm; exact vendor not selected |
| 4 | M3 service-cover screw | M3 x 8 mm, low-profile pan/button head; verify grip length |
| 4 | PCB standoff screw | M3 x 6 mm nylon or metal with insulating washer; exact stack unverified |
| 1 | Hinge pin | 5 mm nominal diameter x 140 mm max; exact retention hardware not selected |
| 1 set | Display pads/gasket | Replaceable closed-cell compliant pads, 0.5-1.0 mm |
| as needed | Strain relief | Serviceable USB-C cable clip or tie mount; not yet modelled |

The hardware list is a prototype selection guide, not a released procurement
BOM. Insert hole size, screw length, hinge-pin tolerance and polymer material
must be resolved with the chosen print process.

## Assembly sequence

1. Inspect printed parts and chase support material from the service-cover,
   connector and hinge openings. Install four M3 heat-set inserts without
   distorting the chassis bosses.
2. Apply compliant pads only to the display module's metal frame. Seat the
   display against the front ledge without contacting active glass.
3. Install the controller PCB on its four mapped standoffs. This step is blocked
   for the current digital result because no DRC-clean populated PCB STEP exists;
   first validate real connector reach and underside solder clearance.
4. Mate J2 and provide service slack/strain relief. Verify USB-C and microSD
   insertion before closing the cover.
5. Align the three button plungers/light openings; confirm the ambient sensor is
   optically exposed and the LED points rearward.
6. Fit the service cover using four reusable M3 screws. Do not glue the cover.
7. Install the hinge pin, verify the folded detents engage, and verify the two
   stand tabs land on the chassis hard stops at the deployed angle.
8. Perform low-voltage electrical bring-up with the cover removed, then repeat
   thermal and insertion checks with the enclosure assembled.

All four manufactured parts fit a stated 220 x 140 x 30 mm flat-oriented build
envelope. No statement is made about slicer settings, warping, strength,
tolerance stack, cycle life or print quality.
