# Publication review

This receipt records findings made after the one-shot cleanroom run. The generated archive, CAD, KiCad files, source, prompt, and original run report remain unchanged so the published pack is evidence of the actual run rather than a parent-edited redesign.

## Reproducibility

- Burr package: `@fraylabs/burr` version `0.31.0`, skill commit `3a1b8ebf17e178b28c6d65f67ad04fc97f009a55`, source: <https://github.com/fraylabs/burr/tree/3a1b8ebf17e178b28c6d65f67ad04fc97f009a55/skills/burr>.
- CAD skill commit: `fc4f7069fb31c131a55f1ecd334b505f031f486b`, source: <https://github.com/earthtojake/text-to-cad/tree/fc4f7069fb31c131a55f1ecd334b505f031f486b/skills/cad>.
- KiStack skill commit: `c5a25d1d0af7ae811666cab41d7952f41e310575`, source: <https://github.com/American-Embedded/kistack/tree/c5a25d1d0af7ae811666cab41d7952f41e310575/skills>.
- Archive CAD source: `models/cad/source/photo_frame_parts.py`.
- Archive electronics source: `tools/generate_electronics.py`.
- Archive mechanical endpoints: `models/assembly/exports/product_stand_deployed.step`, `models/assembly/exports/product_stand_folded.step`, and `models/assembly/exports/product_rear_cover_open_exploded.step`.
- Archive KiCad authority: `models/kicad/source/photo_frame.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`.
- Reviewed snapshots: `media/xray.png`, `media/deployed.png`, `media/exploded.png`, `media/schematic.png`, and `media/burr-checks.png`.

Paths beginning with `models/` or `tools/` are valid relative to the extracted archive root. Paths beginning with `artifacts/` or `media/` are valid relative to this outcome pack.

## Confirmed source blockers

1. The stand barrel is a solid cylinder: it has no clearance bore for the specified 5 mm hinge pin. Its local barrel centre is also 2 mm behind the hinge datum before placement. The documented hinge assembly cannot be completed from this geometry.
2. The interface control gives a 180 × 100 mm display envelope and four 3.2 mm holes on 174 × 98 mm centres. The vertical pattern plus hole diameters spans 101.2 mm, so those stated values are mutually incompatible. The exact selected-module drawing must resolve the interface before CAD placement.
3. The USB-C input has fixed 5.1 kΩ sink resistors but no detection or load limiting for the source-advertised Type-C current. The estimated 1.045 A load can exceed a source advertising default current; the 2 A resettable protector is not a precision current-control mechanism.
4. The KiCad project ignores or downgrades footprint/symbol identity mismatches, and the generator has no equivalent fail-closed schematic-to-PCB footprint comparison. The already failed parity result must be repaired and independently blocked before fabrication.
5. The electronics generator hard-codes one macOS KiCad 10.0.6 installation and a host-specific Python package path. The checked-in KiCad files are inspectable, but regeneration is not portable as generated.

The schematic date `2026-09-03` is not a future-dated receipt: the run and publication used Singapore time (UTC+08:00), as recorded by the outcome's `authoredAt` value.

These are repair blockers, not physical validation results. A future design pass must repair the sources, regenerate all affected CAD/KiCad artifacts, rerun ERC, DRC/parity, exact CAD validation and Burr checks, and then perform the specified physical bring-up. Until then, this pack remains incomplete and repair-required.
