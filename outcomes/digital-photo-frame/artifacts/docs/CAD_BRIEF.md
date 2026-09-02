# CAD brief: Halo digital photo frame

- Model: a new desk-standing digital photo-frame assembly.
- Units: millimetres.
- Coordinate convention: the display is centred on XY; +X is right, +Y is up, and +Z points toward the viewer.
- Overall face: 274 x 186 mm with 18 mm corner radii.
- Display aperture: 224 x 140 mm with 8 mm corner radii, sized for a 10-inch-class 16:10 panel.
- Functional layers: a stepped floating bezel, display glass, display module, rear housing, cyan lower accent inlay, and angled easel stand.
- Positioning: the bezel is the fixed root. Display layers and housing use named centre-plane datums and authored offsets. The stand uses a named hinge-axis datum and a 22.5-degree authored pose.
- Source: `digital_photo_frame.step.py`.
- Primary output: `digital_photo_frame.step`.
- Validation targets: labeled assembly children; positive closed solids; 274 x 186 mm face envelope; no external-component interference in Burr; visual review from opposing isometric, front, rear, and side views.
- Assumptions: conceptual first pass; non-production display and housing envelopes; 2.0 mm display glass; 14.0 mm rear housing; 22.5-degree stand angle; no electrical internals, fasteners, tolerance stack, thermal analysis, structural analysis, or manufacturability claim.
