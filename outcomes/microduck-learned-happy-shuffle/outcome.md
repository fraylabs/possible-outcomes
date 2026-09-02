# MicroDuck Learned Happy Shuffle

Train MicroDuck to perform a stable, rhythmic side-to-side shuffle using reinforcement learning, then deliver the learned policy and evidence of its simulated behavior.

## Result

A fresh Codex agent received the direct prompt in this Outcome and worked from a clean checkout of the official `pollen-robotics/microduck_rl` repository. It implemented a registered reinforcement-learning task, passed the repository test suite, completed a smoke run, trained a final policy with 4,096 simulated environments, exported ONNX, and evaluated the result under nominal and perturbed conditions.

The final 16-second evaluation remained upright throughout, had no early terminations or self-collisions, and travelled less than 6.3 cm. Total derived Hugging Face compute cost was $2.86.

The motion is a compact alternating step-and-sway rather than an exaggerated dance. It is verified in MuJoCo simulation only; physical-hardware transfer and exact phrase identity are not proven.

## Original request

> Create and train one genuinely learned MicroDuck behavior called “Happy Shuffle” using the official MicroDuck reinforcement-learning stack.
