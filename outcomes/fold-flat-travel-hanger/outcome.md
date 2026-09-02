# Fold-Flat Travel Hanger

A parametric three-part clothes hanger that opens to a familiar 467 mm adult
hanger profile and folds to approximately 109 mm wide for travel.

The outcome includes a fixed hook-and-hinge hub, two rotating arms, printable
pin-to-bore clearance, deployed-position stops, and two named poses generated
from one editable build123d source. Detailed STEP assemblies are provided for
viewing, alongside deliberately simple collision envelopes for Burr's current
assembly-interference check.

## What is included

- Editable parametric Python source
- Detailed deployed and folded STEP assemblies
- Closed deployed and folded check envelopes
- A Burr project configuration with named fold/deploy playback
- Burr-native snapshots of both detailed poses and both check envelopes
- Local generation and Burr viewing instructions

## Verified digital behavior

- Both detailed assemblies contain three labelled component occurrences.
- Both detailed and check STEP files pass CAD structural validation.
- Burr matches the same three rigid components across both detailed poses and
  exposes a named Fold hanger player with a 1.2 second transition.
- Burr checks all three component pairs in each collision-envelope pose and
  reports no solid-volume interference.
- Burr exports non-empty PNG snapshots of both detailed poses from the active
  Solid-mode viewport.
- The pin-to-bore radial clearance is 0.4 mm and the hub-to-arm axial clearance
  is 0.6 mm in the authored source.

The detailed STEP files omit optional surface parameter curves so Burr's Look
viewer can reconstruct every face from its 3D edge geometry. Their component
meshes are still not closed enough for Burr's current interference check, so
the separate check envelopes remain explicitly limited to the hub body and
load-bearing arm spans; they are not presented as exact geometry.

This is a digitally inspected concept, not proof of physical load capacity,
fatigue life, print quality, hinge durability, garment retention, or safe use.
