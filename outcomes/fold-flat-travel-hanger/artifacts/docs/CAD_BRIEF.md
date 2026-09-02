# CAD brief

- Model: symmetric fold-flat travel clothes hanger; five printed parts plus purchased shoulder screws, locknuts and compression springs.
- Task type: new fit-critical mechanical assembly with five static fold poses, exploded assembly and lock details.
- Units and axes: millimetres; X shoulder width, Y front/back thickness, Z vertical.
- Deployed target: 430–450 mm shoulder width; modeled nominal 442 mm.
- Folded target: at most approximately 230 × 90 × 30 mm.
- Load path: each thick shoulder beam has an 8 × 6 mm heel bearing on a rigid dual-ear lock bar. The bar presents 6 mm positive blocking engagement per side; it is spring-biased engaged and moves 7.5 mm axially under deliberate thumb action.
- Hook: 42 mm circular rod pocket, 40 mm modeled throat, folding on a captured M5 shoulder screw in a front-layer clevis.
- Parts: `center_yoke`, `left_shoulder_arm`, `right_shoulder_arm`, `folding_hook`, `dual_positive_lock_bar`.
- Purchased hardware: two M5 arm shoulder screws, one shorter M5 hook shoulder screw, three low-profile prevailing-torque locknuts, two small compression springs.
- Clearances: 5.0 mm pin in 5.6 mm bore (0.30 mm radial); arm axial clearance 1.0 mm each side; hook axial clearance 0.5 mm each side; released lock clearance 1.0 mm.
- Joints/datums: named left/right arm revolute axes, hook revolute axis and lock linear-release axis in `models/hanger_common.py`.
- Finger protection: both arm roots remain between 4 mm cheek plates; the thumb pad is recessed in an 8 mm-high guide slot; final arm movement occurs behind the cheek faces.
- Strap notches: shallow 9 mm-diameter transverse top grooves near both tips, leaving more than 12 mm of local beam depth.
- Manufacturing assumption: FDM PETG/PA-class prototype with layer direction selected to keep shoulder bending in the XY layer plane; rounded long edges are modeled where OCC permits. This is not a material or strength validation.
- Authoritative paths: `models/hanger_common.py`, individual `models/parts/*.step.py`, and pose `models/assemblies/*.step.py` generators.
- Validation targets: closed positive-volume occurrences; part build-area envelopes; deployed/folded envelopes; hook pocket/throat; pin and axial clearances; blocking-face engagement/contact; release clearance; component identity; pairwise positive-volume intersection for five poses; Burr motion and Burr interference outcomes.
