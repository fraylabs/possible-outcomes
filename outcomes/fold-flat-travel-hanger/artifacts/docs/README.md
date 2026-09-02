# Fold-flat travel hanger cleanroom result

This directory contains a complete, self-contained one-shot design result.

## Designed model

- `../source/travel_hanger.py` — authoritative parametric geometry and both source-defined poses.
- `../source/travel_hanger_deployed.step.py` — deployed build entry.
- `../source/travel_hanger_folded.step.py` — folded build entry.
- `../cad/travel_hanger_deployed.step` — primary deployed STEP assembly.
- `../cad/travel_hanger_folded.step` — primary folded STEP assembly.

## Burr collision evidence

The detailed curved STEP components are valid closed BREP solids, but Burr 0.31.0
could not close their tessellated collision meshes. `../source/travel_hanger_collision.py`
therefore defines documented conservative box envelopes for the hook/hub and
four plastic links only. It excludes pins and bores and must not be presented as
the exact design.

- `../cad/travel_hanger_deployed_collision.step` — deployed envelope, Burr pass.
- `../cad/travel_hanger_folded_collision.step` — folded envelope, Burr pass.
- `../../media/` — selected CAD snapshots and Burr-native screenshots.
- `VALIDATION_REPORT.md` — validation receipts and explicit scope.
- `SHA256SUMS` — hashes for the final source and CAD artifacts.

The work makes no structural, fatigue, tolerance-stack, motion-envelope,
manufacturing, or certification claim.
