# Positive-Locking Fold-Flat Travel Hanger

This one-shot cleanroom result is a compact, parametric travel hanger with a linked positive-lock mechanism, five modeled fold poses, printable part exports, and a named Burr animation. It is published as a repair-required digital pre-build: the exact CAD evidence is strong, while Burr's tessellated interference result and every physical-performance claim remain unresolved.

An isolated Codex agent received only the exact prompt in `prompt.md`, the Burr skill, its routed CAD provider, and an empty workspace. The parent agent did not supply an earlier hanger design or steer the run after it began.

## What the run produced

- Five printable parts: center yoke, left and right shoulder arms, folding hook, and linked dual-positive-lock bar.
- Purchased-hardware envelopes for M5 shoulder screws and low-profile locknuts.
- Deployed, 25%, 50%, 75%, folded, exploded, lock-engaged, and lock-released STEP assemblies.
- Printable STL and 3MF exports for all five polymer parts.
- A portable Burr project with a 1.6-second `Fold hanger` motion.
- CAD, Burr, and machine-readable validation evidence.

The deployed assembly is 442 mm wide. Its folded envelope is 222.885 × 88 × 30 mm. Each shoulder heel has 6 mm of modeled engagement with the linked lock bar, and releasing the bar provides 7.5 mm of travel with 1 mm of modeled blocking-face clearance.

## What is actually verified

- All 16 final CAD targets passed the provider's topology, closure, and positive-volume validation.
- An independent exported-STEP verifier checked all 55 component pairs in each of five fold poses and found no positive-volume intersections.
- The deployed and folded exports preserve the same 11 named component occurrences.
- Burr loaded both endpoints and generated a 61-frame rigid motion across all 11 instances.

Burr's own interference result is **not clean**. It reports four deployed findings and three folded findings, and it cannot prove closure for seven tessellated components. Those failed/incomplete results are included unchanged alongside the separate exact-STEP evidence; neither result is used to erase the other.

## Repair-required boundary

No hanger was fabricated or physically tested. The geometry does not prove a 3 kg rating, stiffness, fatigue life, creep resistance, spring behavior, pin retention, dimensional accuracy, pinch safety, garment safety, or production readiness. The supplied test plan requires progressive symmetric and asymmetric loading, folding cycles, release-force tests, drops, warm-creep exposure, process coupons, and edge/snag review before use.

Publication review also found that the generated assembly guide tells the builder to fit two compression springs over guide pegs, but the generated lock-bar source contains no guide pegs. The spring-loaded return and folded-retention assembly therefore cannot be built as documented. This source-level defect is preserved rather than silently repaired so the outcome remains an authentic one-shot result; see `artifacts/docs/PUBLICATION_REVIEW.md`.

Extract the project archive, change into the extracted project root, and run `burr .`. Its sources and validation receipts remain editable and inspectable. The downloadable archive's motion configuration was migrated after the cleanroom run to Burr 0.34's single-source joint format; its CAD, original report, and validation receipts remain unchanged.
