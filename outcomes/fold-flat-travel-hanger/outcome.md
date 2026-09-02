# Fold-Flat Travel Hanger

This is the untouched final result of a cleanroom, one-shot Burr experiment. An isolated Codex agent received only the literal prompt in `prompt.md`, the Burr skill, its routed CAD provider, and an empty workspace. No design from an earlier hanger attempt was supplied, and the parent agent did not steer or edit the geometry.

The result is a parametric nine-component travel hanger with deployed and folded STEP assemblies. It uses paired articulated arms, pivot pins, a central hub and hook, and slotted geometry that packs the links into a narrow folded form.

## What the run produced

- A 428 × 198.99 × 18.8 mm deployed assembly.
- A 76 × 223.99 × 18.8 mm folded assembly.
- Six reusable Python source files covering the detailed models and conservative collision envelopes.
- Four STEP exports with labeled components and preserved color.
- CAD snapshots, native Burr screenshots, a validation report, and SHA-256 receipts.

## What is actually verified

- Both detailed STEP assemblies contain nine labeled, valid, positive-volume BREP components.
- Independent BREP checks found no positive-volume intersection across all 36 component pairs in either detailed pose.
- Burr's current tessellation path reports the detailed deployed and folded checks as failures while also classifying all nine meshes as open. Those detailed Burr collision results are therefore preserved as incomplete evidence, not presented as proof.
- The run also generated conservative five-component collision envelopes. Burr checked all 10 pairs in each pose and passed both envelope models.

## Limits

This is a concept model, not a manufacturing release. The conservative envelopes exclude pins, bores, motion sweeps, tolerances, fastener retention, material strength, fatigue, load testing, and manufacturability. The two poses are separate exports; the cleanroom run did not add a Burr motion configuration.
