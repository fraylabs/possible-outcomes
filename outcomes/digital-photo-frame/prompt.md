$burr

Design a complete digital pre-build for a compact, premium-looking, seven-inch tabletop digital photo frame. The result must include both the mechanical product and its actual electronic design: enclosure CAD, display integration, schematic, PCB layout and the populated board’s mechanical integration. An enclosure containing placeholder rectangles is not a complete result.

Use Burr as the project environment. Use the installed mechanical CAD provider for the enclosure and assembly, and the installed KiStack/KiCad skills for schematic, PCB, BOM, validation and populated STEP export. Preserve CAD and KiCad as separate authoritative sources and combine only their exported geometry for the final product assembly.

If either required provider is unavailable, stop and report the experiment as incomplete. Do not silently omit the PCB or replace it with an invented board.

## Product definition

Design an indoor, landscape-oriented photo frame for a desk, shelf or bedside table.

Target characteristics:

- Approximately seven-inch IPS display.
- Overall front envelope no larger than approximately 230 × 165 mm.
- Enclosure depth approximately 22–30 mm, excluding the deployed stand.
- Wide, stable folding easel stand with a hard viewing-angle stop around 15–20 degrees from vertical.
- Stand folds substantially flush for packing and has a credible retention feature in both folded and deployed positions.
- Removable rear service cover secured with reusable fasteners and inserts; do not permanently glue the product closed.
- Display, PCB and controls must be individually replaceable without destroying the enclosure.
- Rounded, restrained exterior suitable for a home rather than a development-board enclosure.
- Landscape operation is required; portrait operation, touch input, audio, camera and battery operation are out of scope.

Power the product from an external certified 5 V USB-C adapter. Do not include mains circuitry, a lithium battery or charging circuitry.

## Electronics architecture

Create a real KiCad project around an ESP32-S3 module with sufficient flash and PSRAM for a display framebuffer and Wi-Fi photo transfer. You are explicitly authorized to select exact electronic parts, packages and footprints for this digital pre-build.

Select a real, currently documented seven-inch display or display module that is electrically compatible with the controller architecture. Prefer a module with an integrated display timing or backlight solution when that materially reduces risk. Record the exact manufacturer, part number, datasheet URL, active area, outer dimensions, mounting geometry, connector and pinout.

Do not invent a display pinout, FPC connector, footprint, component rating or package. If the required public manufacturer documentation cannot be obtained, choose a different supported component or mark the result incomplete.

The electronics must include:

- ESP32-S3 module with Wi-Fi, flash and PSRAM.
- Selected display connector and required interface circuitry.
- Backlight power and brightness control appropriate to the selected display.
- USB-C 5 V power-only input with correct sink configuration.
- Input protection appropriate to a low-voltage prototype, including fuse or current limiting and ESD protection.
- Required regulated rails with documented current budgets and component derating.
- MicroSD storage.
- Three accessible user buttons for previous, next and menu or wake.
- Reset and boot access for development.
- Ambient-light sensing for automatic brightness.
- Status LED that does not shine directly through the display.
- Programming and debugging access plus labeled test points for major power rails and critical signals.

Use a four-layer PCB unless verified routing and return-path requirements justify another stack-up. Keep the PCB compact enough to sit behind the display without blocking the stand hinge, ventilation or service access.

Base the schematic on manufacturer datasheets and reference designs. Include decoupling, pull-ups or pull-downs, protection, boot strapping and unused-pin treatment. Record every consequential design choice and every unresolved assumption.

## Mechanical and electronic integration

Create one shared interface-control document defining:

- Product coordinate system and origins.
- Display active area, outer envelope, thickness and mounting features.
- PCB outline, board thickness and mounting-hole coordinates.
- Maximum component-height envelopes on both PCB sides.
- USB-C, microSD, button and programming-port locations.
- Cable and FPC bend or insertion keepouts.
- Stand hinge axis and folded/deployed envelopes.
- Minimum clearances used between electronics and enclosure.

Export the populated PCB from KiCad as STEP with component models wherever available. Missing critical component models must be documented and represented by conservative named envelopes rather than omitted.

Use the populated PCB STEP, selected display model or documented display envelope, and enclosure parts in the final mechanical assembly.

The enclosure must include:

- Display ledge or bracket that locates the display without loading the active glass.
- Replaceable compliant-pad or gasket allowance.
- PCB standoffs aligned to the KiCad mounting holes.
- Accessible and correctly aligned USB-C, microSD and button openings.
- Connector insertion space and cable strain relief.
- Ventilation near the controller and power circuitry.
- At least 1.5 mm nominal side clearance around PCB edges and at least 2 mm above the tallest modeled component, unless a documented local exception is required.
- A stable stand footprint and hard stop that cannot pass through the rear cover.
- No fastener, standoff or rib intersecting the PCB, display, connectors or cable paths.

Treat the detailed populated PCB as one named subsystem occurrence in the simplified Burr product-motion assembly so the folding stand animation remains below Burr’s component limit. Preserve the detailed board STEP separately for inspection.

## Deliverables

Produce one portable Burr project containing:

### KiCad authority

- `.kicad_pro`, `.kicad_sch` and `.kicad_pcb` sources.
- Any project-local symbols, footprints and 3D models.
- Exact-part BOM with manufacturer part numbers and datasheet links.
- Schematic PDF.
- ERC report.
- DRC report with schematic parity.
- PCB top and bottom renders.
- Populated PCB STEP export.
- A concise power-budget and interface report.
- Firmware pin map and bring-up requirements. Production firmware implementation is out of scope.

### Mechanical authority

- Editable parametric CAD source.
- Individual enclosure-part STEP files.
- STL or 3MF exports for prototype-printable enclosure parts.
- Rear-cover-open exploded assembly.
- Complete product STEP with the populated PCB and display installed.
- Stand-folded and stand-deployed STEP assemblies with identical named rigid components.
- Interface-control document shared with the KiCad design.
- BOM and assembly instructions for enclosure hardware.

### Burr project

- Organize viewable files under clear `models/cad`, `models/kicad` and `models/assembly` folders.
- Add a portable `.burr/config.toml` with those stable model roots.
- Configure a named Fold stand motion between the stand-deployed and stand-folded product assemblies.
- Include final Burr snapshots and check evidence.

Do not generate or present fabrication outputs as production-ready. Gerbers and drill files may be generated only for design review after clean ERC and DRC results, and must remain clearly marked as unverified prototype outputs.

## Validation

Run KiCad CLI validation and preserve the exact reports:

- Schematic ERC with error-level violations treated as failure.
- PCB DRC with error-level violations treated as failure.
- Schematic-to-PCB parity.
- BOM generation from the schematic rather than hand-edited CSV.
- Populated PCB STEP export and top/bottom renders.
- Confirmation that critical components have exact footprints and documented pinouts.

Run CAD validation:

- Every manufactured enclosure part is a closed, positive-volume solid.
- Overall product dimensions match the stated envelope.
- Display active area is centered and unobstructed.
- KiCad mounting holes align with CAD standoffs.
- External openings align with their actual connectors and controls.
- Board-edge, component-height and insertion clearances meet the documented values.
- Stand folded and deployed poses use unchanged rigid component geometry.
- No unintended positive-volume intersections exist between the display, PCB subsystem, enclosure, cover, fasteners and stand.
- Prototype-printable enclosure parts fit within a stated build volume.

Open all final STEP outputs in Burr. Inspect the complete product in Solid and X-ray modes, verify the stand motion plays, and run Burr’s supported interference check on the integrated assembly. An `Incomplete` Burr result must remain incomplete; do not convert it into a pass based on appearance.

Save and review:

- Front product view.
- Rear stand-deployed view.
- Stand-folded view.
- Rear-cover-open exploded view.
- X-ray view showing display, populated PCB and enclosure.
- USB-C and microSD alignment details.
- PCB top and bottom renders.
- Readable schematic overview.
- Burr motion and check evidence.

Repair source-level problems, regenerate affected outputs and rerun the failed validations before finishing.

## Limits

This is a digital pre-build, not a proven working or production-ready product. Do not purchase parts, order boards, fabricate the enclosure, power hardware or claim verified display operation, radio performance, EMC compliance, thermal safety, electrical safety, firmware completeness, print quality or manufacturability.

If exact datasheets, footprints, component models, providers or validation tools are unavailable, preserve the partial work and report the result as incomplete rather than inventing evidence.

Return the authoritative CAD and KiCad source paths, generated artifacts, selected exact parts, Burr and KiCad versions, ERC and DRC outcomes, CAD and Burr results, reviewed images, unresolved warnings and the physical bring-up tests still required.
