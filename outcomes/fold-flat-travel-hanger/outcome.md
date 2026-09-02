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
- Burr-native snapshots of both detailed poses and two reviewed check views
- Local generation and Burr viewing instructions

## Verified digital behavior

- Both detailed assemblies contain three labelled component occurrences.
- Both detailed and check STEP files pass CAD structural validation.
- Burr checks all three component pairs in each collision-envelope pose and
  reports no solid-volume interference.
- Burr exports non-empty PNG snapshots of both detailed poses from the active
  Solid-mode viewport.
- The pin-to-bore radial clearance is 0.4 mm and the hub-to-arm axial clearance
  is 0.6 mm in the authored source.

The current Burr viewer dependency drops two curved faces from the detailed
STEP assemblies, so those models correctly report an incomplete interference
check. The closed check envelopes are explicitly limited to the hub body and
load-bearing arm spans; they are not presented as exact geometry.

This is a digitally inspected concept, not proof of physical load capacity,
fatigue life, print quality, hinge durability, garment retention, or safe use.
