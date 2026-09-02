# Publication review

This receipt records findings made after the one-shot cleanroom run. The generated archive, CAD, source, prompt, and original run report remain unchanged so the published pack is evidence of the actual run rather than a parent-edited redesign.

## Reproducibility

- Burr package: `@fraylabs/burr` version `0.31.0`, skill commit `3a1b8ebf17e178b28c6d65f67ad04fc97f009a55`, source: <https://github.com/fraylabs/burr/tree/3a1b8ebf17e178b28c6d65f67ad04fc97f009a55/skills/burr>.
- CAD skill commit: `fc4f7069fb31c131a55f1ecd334b505f031f486b`, source: <https://github.com/earthtojake/text-to-cad/tree/fc4f7069fb31c131a55f1ecd334b505f031f486b/skills/cad>.
- Archive source: `models/hanger_common.py`.
- Archive model endpoints: `models/assemblies/hanger_deployed.step` and `models/assemblies/hanger_folded.step`.
- Published source mirror: `artifacts/source/hanger_common.py`.
- Reviewed snapshots: `media/deployed.png`, `media/folded.png`, `media/lock-engaged.png`, `media/lock-released.png`, `media/burr-folded.png`, and `media/burr-checks-deployed.png`.

Paths beginning with `models/` are valid relative to the extracted archive root. Paths beginning with `artifacts/` or `media/` are valid relative to this outcome pack.

## Confirmed source defect

`make_lock_bar()` combines the transverse bar and thumb pad but does not create the two guide pegs named by `docs/ASSEMBLY.md`. The documented compression springs therefore have no modeled pegs, and the spring-loaded return/folded-retention assembly cannot be reproduced from the generated geometry.

This is a repair blocker, not a physical validation result. A future design pass must add compatible guide and spring geometry, regenerate every pose and export, rerun exact geometry checks and Burr checks, and physically verify release and retention forces. Until then, this pack remains repair-required.
