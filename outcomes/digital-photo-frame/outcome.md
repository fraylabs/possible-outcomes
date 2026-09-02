# Seven-Inch Digital Photo Frame Pre-Build

This one-shot cleanroom result combines a parametric enclosure, folding easel stand, exact-part KiCad schematic and four-layer PCB source, shared mechanical/electrical interfaces, and a named Burr motion in one inspectable project. It is published as an incomplete, repair-required digital pre-build because the PCB does not pass DRC/parity and the populated board could not truthfully be integrated.

An isolated Codex agent received only the exact prompt in `prompt.md`, the Burr skill, its routed CAD provider, the referenced KiStack skills, and an empty workspace. It did not see the hanger run, and the parent agent did not steer it after execution began.

## What the run produced

- A 216 × 138 mm seven-inch frame enclosure with front bezel, rear chassis, removable service cover, ventilation, connector openings, and folding stand.
- Deployed, folded, and rear-cover-open exploded STEP assemblies.
- Four printable STL parts and editable parametric Python source.
- KiCad project, schematic, four-layer PCB source, grouped BOM, schematic PDF/SVG, and an interface-control document.
- Exact selections for the display, ESP32-S3 module, 3.3 V buck, USB-C receptacle, microSD socket, ambient-light sensor, and protection parts.
- A portable Burr project with a 1.2-second `Fold easel stand` motion.

## What is actually verified

- All nine final mechanical CAD targets passed topology, closure, and positive-volume validation.
- Burr loaded an eight-instance integrated assembly and generated a 61-frame rigid fold motion.
- KiCad ERC exits 0 with zero errors and zero warnings.
- The generated schematic PDF and grouped BOM are present and inspectable.

The electronics are **not fabrication-ready**. The saved KiCad DRC receipt exits 5 with 742 violations and 295 schematic-parity issues. Independent reruns reproduced the same failure and 295 parity issues, while the DRC violation count varied from 740 to 784 after zone refill. No populated PCB STEP, PCB renders, Gerbers, or drill files were generated after that failed gate. The CAD assembly therefore contains an explicitly named conservative PCB envelope rather than an invented populated board.

Burr's integrated checks also remain failed/incomplete: six deployed pairs, seven folded pairs, and three exploded pairs, all with an open-component-mesh caveat.

## Repair-required boundary

This project does not claim working display operation, correct routing, fabrication readiness, connector engagement, power integrity, radio performance, EMC, thermal or electrical safety, manufacturability, fit, stand stability, durability, or production readiness. The next design pass must repair routing, planes, keepouts, footprint parity, exact component 3D coverage, board/enclosure integration, and Burr findings before fabrication outputs are considered.

Publication review identified additional source-level blockers: the stand barrel has no hinge-pin bore and is offset from the chassis hinge axis; the stated display mounting-hole pattern exceeds the stated display envelope; the USB-C sink does not detect or limit itself to the source-advertised current; schematic-to-PCB footprint parity is not fail-closed; and the electronics generator contains host-specific KiCad and Python paths. These defects are preserved rather than silently repaired so the outcome remains an authentic one-shot result; see `artifacts/docs/PUBLICATION_REVIEW.md`.

Extract the project archive, change into the extracted project root, and run `burr .`. The electronics sources can be inspected with KiCad 10.0.6 or a compatible release.
