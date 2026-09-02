# Fold-flat travel hanger

This example starts with Burr as the user-facing environment, delegates the
editable geometry to a mechanical CAD source, and returns both poses to Burr
for local viewing and assembly-interference checks.

## Design brief

- Adult hanger: approximately 467 mm wide when deployed.
- Compact pose: approximately 109 mm wide when folded.
- Three manufactured components: fixed hook/hub and two folding arms.
- Hinge axes are parameterized in the shared `hanger.py` source.
- Pin-to-bore radial clearance is 0.4 mm; hub-to-arm axial clearance is 0.6 mm.
- Fixed pins touch the arm roots at the deployed angle to demonstrate a simple
  mechanical stop without intentional solid overlap.
- This is a concept fixture, not a structural or manufacturing certification.

## Model roles

- `hanger-deployed.step` and `hanger-folded.step` are the full-detail display
  models. They include the open hook, hinge pins, bores, and mechanical stops.
- `hanger-deployed-check.step` and `hanger-folded-check.step` are deliberately
  simple, closed collision envelopes for Burr's current interference check.
  They cover the hub body and the load-bearing span of both arms. They do not
  prove hook, pin, bore, stop, clearance, strength, or manufacturability.

The split is explicit because Burr's viewer dependency currently drops two
curved faces from the detailed STEP files. Those display models therefore
report `incomplete`; the check envelopes are not presented as exact geometry.

## Generate

Each pose is an independent STEP entry over the same source:

```bash
uv run hanger-deployed.step.py
uv run hanger-folded.step.py
uv run hanger-deployed-check.step.py
uv run hanger-folded-check.step.py
```

Then open this folder in Burr:

```bash
burr .
```

Select the two full-detail files to inspect the mechanism. Select each
`*-check.step` file to run Burr's supported component-pair check; it should
complete without reporting solid-volume interference in either pose.
