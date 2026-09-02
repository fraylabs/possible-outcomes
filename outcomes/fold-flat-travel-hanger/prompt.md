$burr

Create a parametric fold-flat travel clothes hanger as a three-component
mechanical CAD assembly: one fixed hook-and-hinge hub and two rotating hanger
arms.

Use millimetres. The deployed pose should be approximately 467 mm wide and
recognisably shaped like an adult clothes hanger. The folded pose should be
approximately 109 mm wide, with the arms lying nearly parallel for packing.
Generate both named poses from one shared editable source rather than modeling
two unrelated objects.

Include:

- an open C-shaped hanging hook;
- two fixed hinge pins in the central hub;
- matching arm bores with 0.4 mm radial clearance;
- 0.6 mm axial clearance between the hub and arms;
- simple fixed stops at the deployed arm angles;
- clear native labels for the hub, left arm, and right arm.

Return detailed deployed and folded STEP assemblies to Burr for local viewing.
Run Burr's supported assembly-interference check in both poses. If the detailed
curved STEP geometry cannot produce closed tessellated meshes, create separate,
clearly labelled closed collision envelopes for only the dimensions relevant
to the check. Do not silently substitute envelopes or describe them as exact.

Validate the generated STEP assemblies, review saved snapshots of both poses,
repair source-level problems, and include the editable source, outputs,
verification results, and honest physical-validation limits.
