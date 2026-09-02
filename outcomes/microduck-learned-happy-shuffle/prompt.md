Create and train one genuinely learned MicroDuck behavior called “Happy Shuffle” using the official `pollen-robotics/microduck_rl` stack. The finished robot should perform a joyful, stable, rhythmic dance in place that reads clearly as a happy side-to-side shuffle: alternating lateral steps, coherent body motion, and an approximately eight-second phrase that can repeat cleanly. It must remain recognizably balanced and physically plausible rather than looking like random twitching or a scripted animation.

The learned policy should strongly discourage falling, large unintended travel, uncontrolled spinning, foot skating, violent joint motion, self-collision, joint-limit abuse, and other reward-hacking shortcuts. Preserve enough robustness that modest simulation perturbations do not immediately destroy the behavior. Use reinforcement learning in the official repository; do not replace learning with a hard-coded trajectory or animation.

Implement everything needed as a first-class registered task in the repository: task/environment configuration, commands or phase representation, reward terms, termination behavior, agent configuration, and focused tests. Keep changes narrow and consistent with upstream conventions. The task must appear in the official environment listing.

Verification and training:

1. First run the narrow local CPU/configuration tests and the repository’s required smoke configuration. Do not attempt meaningful training on an Apple Silicon GPU.
2. Use Hugging Face Jobs for CUDA training. Load credentials without printing or copying secrets.
3. Use an NVIDIA GPU with at least 24 GB VRAM. Gate the full run on a successful 64-environment, 5-iteration smoke job. Set explicit timeouts and stop failures promptly.
4. Set and obey an explicit compute-spend cap before launching paid work. Do not use other paid services without approval.
5. After the smoke test succeeds, run a serious training attempt within the remaining budget. Preserve checkpoints in a private Hugging Face repository under the authenticated user namespace.
6. Evaluate the resulting checkpoint through the repository’s supported inference/evaluation path. Produce the strongest visual evidence available within the repository and budget, preferably a short rendered MP4 or GIF of the behavior plus concise metrics. Never claim the behavior succeeded merely because training completed.

Deliver:

- the complete source changes;
- focused tests and their results;
- exact job IDs or URLs and actual recorded compute cost if available;
- the checkpoint or repository reference;
- evaluation metrics;
- a shareable preview video or GIF if successful;
- a concise run report that distinguishes what is proven, what failed, and what remains uncertain.

Operate autonomously within these boundaries. If the smoke job fails, diagnose and repair before any full run. If genuine learning cannot be demonstrated within the approved spend cap, stop honestly with the best evidence and do not fabricate success.
