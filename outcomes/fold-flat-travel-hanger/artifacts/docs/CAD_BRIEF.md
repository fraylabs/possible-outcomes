# CAD brief: fold-flat travel hanger

- Model: a labeled mechanical assembly shown in deployed and folded poses.
- Task type: new conceptual assembly.
- Units: millimeters.
- Coordinate convention: hanger silhouette lies in XY; X is shoulder width, Y is vertical, and +Z is through-thickness. The hub center is the assembly origin.
- Deployed envelope target: about 430 mm wide, 200 mm tall, and under 20 mm thick.
- Folded envelope target: under 80 mm wide and about 230 mm tall, with the arm links layered through thickness.
- Functional features: rigid hook-and-hub body; two inner shoulder links; two outer shoulder links; four Z-axis hinge pins; clearance bores at every hinge; strap loops near both tips; lightening slots; distinct colors and labels for visual inspection.
- Positioning/mating: all hinge centers are named source parameters. Links occupy three Z layers with 0.5 mm gaps. Pins share the hinge axes and use 0.4 mm radial clearance.
- Authoritative source: `travel_hanger.py`, with pose entry generators `travel_hanger_deployed.step.py` and `travel_hanger_folded.step.py`.
- Primary outputs: `travel_hanger_deployed.step` and `travel_hanger_folded.step`.
- Validation targets: closed positive-volume solids; nine labeled components per pose; deployed and folded bounding boxes; occurrence frames; visual packet for each pose; Burr assembly-interference outcome for each STEP.
- Assumptions: conceptual glass-filled nylon links with metal hinge pins; no structural, fatigue, tolerance-stack, motion-envelope, or manufacturability claim. The small modeled gaps are for unambiguous assembly inspection, not a production fit specification.
