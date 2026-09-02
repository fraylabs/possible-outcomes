# Burr native evidence

- Burr executable: `burr`
- Burr version: `0.31.0`
- Project: isolated empty cleanroom workspace
- Selected model: `digital_photo_frame.step`
- Discovered supported model files: 1
- Viewer model type: `STEP B-REP`
- Viewer statistics after the source repair: 8,590 triangles, 25,770 vertices, 6 geometries
- Model appearance used for final evidence: Solid

## Final Checks result

`Incomplete`

`Interference check not completed`

Exact Burr reason:

> Could not prove a clean result because these tessellated components are not closed: floating_bezel, display_glass, display_module, rear_housing, cyan_accent, easel_stand.

No interfering component pair was listed after the source-level repair.

## Repair history

The first Burr check returned `Fail` with one interfering component pair:

> floating_bezel × display_glass — Overlapping solid surfaces

The authoritative generator reduced the glass envelope from 222 x 138 mm to
218 x 134 mm, the same STEP output path was regenerated, and Burr refreshed.
The pair disappeared. The remaining open-tessellation limitation makes the
final result `Incomplete`, not `Pass`, so no clean-interference claim is made.
