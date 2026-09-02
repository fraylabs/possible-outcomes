$burr

Design a durable, fold-flat travel clothes hanger for adult shirts, trousers and lightweight jackets. It must open to a normal full-size hanger, fold into a compact package without loose pieces, and positively lock when deployed so garment weight cannot collapse it. Treat this as a complete mechanical product concept, not merely a recognizable hanger-shaped model.

Use Burr as the project environment and the installed mechanical CAD provider for authoritative parametric source, STEP generation and validation. Keep all source, models and evidence inside one portable project folder. Do not add electronics.

## Product requirements

Use millimetres.

Design targets:

- Deployed shoulder width: 430–450 mm.
- Folded envelope: no larger than approximately 230 × 90 × 30 mm.
- Hook must accept closet rods up to 38 mm diameter and retain the hanger during ordinary handling.
- Design intent: carry up to 3 kg of clothing without relying on visibly thin, flexible plates. This is a geometry target only, not a validated load rating.
- Every prototype part must fit within a 256 × 256 mm FDM build area in a sensible print orientation.
- No detachable pieces during normal folding, deployment or use.

Use a symmetrical articulated structure with named left and right components. Load-bearing shoulder links must have credible beam depth, ribs or box-like sections; do not use flat decorative strips that would obviously flex. Round garment-contact edges, avoid sharp corners, and include practical strap notches without weakening the primary load path.

## Locking and folding mechanism

The deployed hanger must use a positive mechanical lock. Friction, hinge tightness or a weak detent alone is not an acceptable deployed lock.

Design the mechanism so that:

- Downward garment loads react through hard stops and positive blocking faces.
- A deliberate thumb action is required to release the deployed lock.
- The release cannot be triggered by the normal downward or inward load of clothing.
- Both sides are locked, either through one central locking control or two mechanically linked locks.
- Locking engagement is visible and inspectable in the CAD.
- Locking faces have at least 3 mm of modeled positive engagement unless a stronger documented geometry is used.
- The arms also have a light folded-position retention feature so they do not swing open in luggage.
- Hinge pins are captive after assembly. Prefer standard metal dowel or shoulder pins where appropriate; printable substitutes may be included but must be clearly identified as prototype-only.
- Pin, bore and axial clearances are explicit source parameters. Choose credible prototype clearances and explain them.
- Fingers are protected from obvious pinch points during the final part of deployment and folding.

The deployed hard stops—not the release tab or a flexible snap feature—must carry the primary garment load. Do not hide an impossible latch inside overlapping solids.

## Authoritative CAD and deliverables

Create editable parametric CAD source with named dimensions, joints, mating datums and component labels.

Deliver:

1. Individual editable part sources.
2. Individual STEP files for every manufactured part.
3. STL or 3MF prototype exports for printable parts.
4. A complete deployed STEP assembly.
5. A complete folded STEP assembly.
6. Intermediate 25%, 50% and 75% fold-pose STEP assemblies for clearance inspection.
7. An exploded assembly showing pins, links, lock components and assembly order.
8. A close-up lock-detail assembly in both engaged and released states.
9. A concise BOM and assembly note identifying printed parts and purchased pins or springs.
10. A `.burr/config.toml` that scopes the final model folder and configures a named Fold hanger motion between the deployed and folded assemblies.

The deployed and folded Burr motion endpoints must contain the same uniquely named components with unchanged geometry and only different rigid transforms. Keep the motion assembly below Burr’s component limit.

## Validation

Validate all final STEP artifacts as closed, positive-volume solids. Report component counts, overall bounds and individual part envelopes.

Programmatically verify:

- Deployed and folded target envelopes.
- Hook opening and throat clearance.
- Pin-to-bore and axial clearances.
- Positive lock-face engagement.
- Hard-stop contact geometry.
- Clearance around the release control.
- Every printable part fits the stated build area.
- No unintended positive-volume intersections in the deployed, folded and three intermediate poses.
- The deployed and folded assemblies contain identical named component geometry for Burr motion playback.

Open the project in Burr, verify the named motion loads and plays, and inspect both endpoints in Solid and X-ray modes. Run Burr’s supported interference check on the deployed and folded assemblies. If detailed STEP tessellation prevents a clean result, report `Incomplete` honestly; a documented simplified collision envelope may be added only as secondary evidence and must never be described as the exact design.

Save reviewed snapshots of:

- Deployed isometric and front views.
- Folded isometric view.
- Exploded assembly.
- Lock engaged.
- Lock released.
- One intermediate fold pose.
- Burr Solid and X-ray views.

Repair source-level geometric or visual failures and regenerate affected outputs before finishing.

## Limits and physical test plan

This is a digital pre-build. Do not purchase parts, fabricate the hanger or claim that strength, fatigue life, creep, impact resistance, latch reliability, print quality or garment safety has been physically validated.

State the physical tests required before use, including:

- Progressive static load testing at the hook and both shoulders.
- Asymmetric one-arm loading.
- Repeated folding and locking cycles.
- Lock-release force and accidental-release testing.
- Hinge and pin-retention testing.
- Drop testing in the folded state.
- Warm-environment creep testing.
- Pinch-point and garment-contact edge inspection.

Return the authoritative source paths, generated models, Burr version and URLs, validation results, screenshots, remaining failures and unsupported claims. A visually attractive result is not complete unless the lock and load path are mechanically understandable.
