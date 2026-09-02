# Happy Shuffle run report

## Outcome

`Mjlab-HappyShuffle-Flat-MicroDuck` is implemented as a registered reinforcement-learning task and trained with PPO in the official `pollen-robotics/microduck_rl` stack. The final checkpoint produces a stable, rhythmic, alternating step-and-sway motion in the supported simulator playback path. A close front-view rollout shows two consecutive eight-second phrases; it is recognizably a compact shuffle rather than random twitching or a scripted joint trajectory.

This result is **verified in simulation, not on physical hardware**. The dance reads clearly in motion, but “happy” is subjective and the step size is intentionally modest. The second phrase is stable but not action-identical to the first (`phrase_repeat_action_rmse = 0.446`), so perfect loop identity is not proven.

## What changed

- Registered `Mjlab-HappyShuffle-Flat-MicroDuck` in the live task registry and documented it in `README.md`.
- Added an eight-second four-count phase command: left-out, right-close, right-out, left-close.
- Added state-based rewards for alternating contacts, body-relative lateral foot motion, lateral body rhythm, and a curriculum-gated gentle head sway. No target joint trajectory or animation is present.
- Added fall/NaN termination plus costs for unintended travel/yaw, slip, self-collision, feet tilt, joint-limit proximity, action over-limit, torque, leg speed, neck thrash, and action changes.
- Preserved the 61-dimensional actor observation contract, BAM actuators, observation noise/delay, domain randomization, and modest training pushes inherited from the production walking task.
- Added a finite supported-path checkpoint evaluator with nominal video and a 32-environment randomized perturbation battery.
- Fixed the Hugging Face training bootstrap's pre-existing one-level checkpoint lookup so the final trained checkpoint is exported through `scripts/export.py` to normalized ONNX.

## Local verification

All local work ran on CPU/configuration paths; no meaningful Mac GPU training was attempted.

| Check | Result |
|---|---|
| `uv run list-envs` | Lists `Mjlab-HappyShuffle-Flat-MicroDuck` |
| `uv run --with pytest pytest -q tests/test_happy_shuffle_cfg.py` | 6 passed |
| `uv run --with pytest pytest -q tests/` | 172 passed, 1 skipped |
| `uvx ruff check` on the new evaluator, task config, and focused tests | Passed |
| `git diff --check` | Passed |

Focused tests cover the eight-second phase/seam, four-count alternation, 61D observation layout, anti-hacking reward signs and guards, inherited robustness configuration, and distinct PPO run configuration.

## Training and checkpoint

- Private model repository: <https://huggingface.co/cowbelleh/happy-shuffle-train-20260902>
- Final checkpoint: `happy_shuffle/2026-09-01_17-15-19_happy_shuffle/model_3499.pt`
- Supported export: `exported/policy.onnx`
- Serious run: 4,096 environments, 3,500 PPO iterations, A10G Small, completed successfully.
- Final training mean reward: `172.35`; mean episode length: `800/800` steps (16 seconds).
- Final weighted task terms: contacts `2.2791`, lateral step `1.6563`, body rhythm `2.7295`, head sway `0.9705`.
- Final safety signals: `nan_state = 0`; fall term `0.0417`; slip velocity metric `0.0146`; every logged penalty remained non-positive.

## Final evaluation

Checkpoint `model_3499.pt` was loaded by RSL-RL's inference policy in the registered environment. The nominal battery recorded one robot for 800 steps (two phrases). The perturbation battery ran 32 environments for 800 steps with training-time domain randomization and pushes. All `done` events occurred at the expected final 16-second timeout; there were no early terminations.

| Metric | Nominal | Perturbed (32 envs) |
|---|---:|---:|
| Upright within 30 degrees | 1.000 | 1.000 |
| Early terminations | 0 | 0 |
| Contact-sequence score | 0.7634 | 0.7594 |
| Lateral-step score | 0.3637 | 0.3537 |
| Body-rhythm score | 0.9076 | 0.9072 |
| Mean stance-foot slip | 0.0103 m/s | 0.00947 m/s |
| Self-collision fraction | 0.000 | 0.000 |
| Maximum episode-relative travel | 0.0622 m | 0.0572 m |
| Maximum heading drift | 0.435 rad | 0.448 rad |
| Maximum absolute joint speed | 4.665 rad/s | 4.849 rad/s |
| Mean action delta L2 | 0.0638 | 0.0613 |
| Mean reward per step | 0.2112 | 0.2103 |

Artifacts in this working directory:

- `artifacts/happy_shuffle/happy-shuffle-preview.mp4` — 16 seconds, 640x640, 50 fps, two phrases.
- `artifacts/happy_shuffle/happy-shuffle-one-phrase.gif` — shareable eight-second preview.
- `artifacts/happy_shuffle/metrics.json` — final nominal and perturbed metrics.
- `artifacts/happy_shuffle/frames/final-contact-sheet.png` — 0.5-second visual samples used for inspection.

Artifact checksums:

- MP4: `c359335be695e085c3b8a454de94670130578705ebe62bfb3c9042c8bf66d8d9`
- GIF: `91e255cc0ed1fb57e5c6953d524f4b2243d9e16e9df795fb54d9d3f870fa20ea`
- metrics JSON: `e9be5221bef3352c99536bf16e3596bb1408c2d4518a6fdbffbc8c953bf8109a`

The same final evaluation is preserved privately under `evaluation-final/` in the model repository.

## Hugging Face Jobs and spend

The requested L4 smoke remained queued for about 47 minutes and was canceled and verified canceled before the explicitly authorized A10G fallback. It never started and has zero measured runtime.

| Purpose | Job | Status | Runtime | Derived cost |
|---|---|---:|---:|---:|
| L4 smoke, canceled before allocation | [6a96fadf21c5aa7c8364bdd2](https://huggingface.co/jobs/cowbelleh/6a96fadf21c5aa7c8364bdd2) | CANCELED | 0 s | $0.0000 |
| A10G 64-env/5-iteration smoke | [6a97060b0718b0f6d890d682](https://huggingface.co/jobs/cowbelleh/6a97060b0718b0f6d890d682) | COMPLETED | 191.638 s | $0.0532 |
| A10G serious 4,096-env/3,500-iteration run | [6a97077a0718b0f6d890d6cb](https://huggingface.co/jobs/cowbelleh/6a97077a0718b0f6d890d6cb) | COMPLETED | 8,922.121 s | $2.4784 |
| Initial eval, missing EGL selection | [6a972c0621c5aa7c8364c3c7](https://huggingface.co/jobs/cowbelleh/6a972c0621c5aa7c8364c3c7) | ERROR | 188.710 s | $0.0524 |
| Distant-camera eval | [6a972cf80718b0f6d890de6a](https://huggingface.co/jobs/cowbelleh/6a972cf80718b0f6d890de6a) | COMPLETED | 251.862 s | $0.0700 |
| Close-view eval, score-probe config bug | [6a972f160718b0f6d890def4](https://huggingface.co/jobs/cowbelleh/6a972f160718b0f6d890def4) | ERROR | 195.688 s | $0.0544 |
| Correct close-view eval | [6a9730880718b0f6d890df2a](https://huggingface.co/jobs/cowbelleh/6a9730880718b0f6d890df2a) | COMPLETED | 261.156 s | $0.0725 |
| Final episode-relative metric confirmation | [6a97329d0718b0f6d890df98](https://huggingface.co/jobs/cowbelleh/6a97329d0718b0f6d890df98) | COMPLETED | 269.929 s | $0.0750 |

**Total derived compute cost: USD $2.8559**, below the authorized $5.00 cap.

Hugging Face's job-inspection response did not expose an actual billed-dollar field. Costs above are therefore explicitly derived from recorded `startedAt`/`finishedAt` timestamps and the live Jobs hardware price returned by the API for A10G Small (`$0.016667/minute`). Queuing time is excluded. No other paid service was used.

## Failed attempts and remaining uncertainty

- Two evaluator attempts failed before rollout due to harness defects (headless EGL selection, then unresolved scene-site configuration). Both were diagnosed without changing the trained policy, fixed, and followed by successful final evaluations.
- The behavior is proven only in MuJoCo Warp simulation. Sim-to-real transfer, hardware thermal/current behavior, and physical floor grip are not tested here.
- The randomized battery covers the repository's domain randomization and modest velocity pushes for 16 seconds. It does not prove recovery from arbitrary large disturbances or long-horizon drift.
- The two phrases are visually coherent and remain stable, but action-space phrase-repeat RMSE is `0.446`; exact trajectory identity at the seam is not proven.
- “Joyful” is a human visual judgment. The close-view evidence shows a compact alternating foot shuffle, synchronized body sway/crouch, and gentle head motion; it is not an exaggerated dance.
