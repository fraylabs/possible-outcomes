# Validation report

## Provenance

- Burr skill: `fraylabs/burr` at `3a1b8ebf17e178b28c6d65f67ad04fc97f009a55`.
- Burr binary: repository commit `c8ab6ae2eedd0d53f3f4173fff61ef1c339d7e7f`; `burr --version` reported `0.31.0`.
- CAD provider: `text-to-cad` at `fc4f7069fb31c131a55f1ecd334b505f031f486b`.
- build123d: `0.11.1`.

## Generation

All four explicit generators built successfully and wrote STEP plus adjacent
`__cadgen__` render/topology packages:

- `travel_hanger_deployed.step.py`
- `travel_hanger_folded.step.py`
- `travel_hanger_deployed_collision.step.py`
- `travel_hanger_folded_collision.step.py`

## CAD provider validation

The primary deployed STEP contains 9 labeled leaf occurrences and has bounds
`427.999962 × 198.989913 × 18.8 mm`. The primary folded STEP contains 9 labeled
leaf occurrences and has bounds `76 × 223.989913 × 18.8 mm`.

`scripts/inspect validate` passed both primary STEP files: every occurrence is
a valid, closed, positive-volume solid. The same validation passed both
five-occurrence collision-envelope STEP files.

A direct pairwise intersection check on the exported BREP assemblies found:

- `travel_hanger_deployed.step`: 9 components, 36 pairs, 0 positive-volume intersections.
- `travel_hanger_folded.step`: 9 components, 36 pairs, 0 positive-volume intersections.

The repaired folded pose moved each returning outer-link tip 6 mm farther from
the hub pins. The cleanroom workspace retained the pre-repair model and source.

## Snapshot review

Selected reviewed snapshots are published as `../../media/deployed.png` and
`../../media/folded.png`. The native Burr screenshots are beside them in the
same media directory.

The deployed views show a recognizable full-width hanger with a hook, four
linked shoulder plates, four pins, lightening slots, and strap loops. The folded
views show both outer plates returning inside the inner-plate footprint while
remaining on their separate Z layer. No new visual concern remained after the
folded-pose repair.

## Burr-native results

Detailed design files:

- `travel_hanger_deployed.step`: **fail**, 4 reported interfering pairs. Burr
  also reported all 9 tessellated components as not closed, so it could not
  prove a clean result. Screenshot: `../../media/deployed-burr-incomplete.png`.
- `travel_hanger_folded.step`: **fail**, 7 reported interfering pairs. Burr
  also reported all 9 tessellated components as not closed, so it could not
  prove a clean result. Screenshot: `../../media/folded-burr-incomplete.png`.

Because Burr's failing detailed findings conflict with the exported BREP
intersection result and accompany an explicit mesh-closure failure, they are
not treated as a clean interference conclusion in either direction.

Documented conservative collision envelopes:

- `travel_hanger_deployed_collision.step`: **pass**, 5 components, 10 checked pairs.
- `travel_hanger_folded_collision.step`: **pass**, 5 components, 10 checked pairs.

The envelope passes support only external separation among the hook/hub plate
and four plastic link plates in the two static poses. They exclude pin shafts,
pin heads, bores, clearances, detailed curved outlines, intermediate motion,
minimum clearance, tolerance stacks, strength, and manufacturability.

During the cleanroom run, a minimal two-box closure probe passed 1 checked pair,
confirming this Burr build can produce a clean result for a closed tessellation
in the same project.

## Unsupported scope

No claim is made for structural load capacity, fatigue, retained-pin design,
production fit, tolerance stack, continuous fold motion, garment-safe edge
treatment, print orientation, moldability, or certification. CAD Viewer handoff
was unavailable because the separate `$cad-viewer` skill was not installed;
Burr and the saved CAD snapshots provide the visual handoff instead.
