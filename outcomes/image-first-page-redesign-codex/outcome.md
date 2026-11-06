# Image-First Page Redesign in Codex

A one-line prompt for agents that are weak at visual design. Instead of having the coding model guess the look while it writes code, Codex uses its built-in image model to draw the redesigned page first, then the coding model implements what it drew. The creator says many of the 3D game scenes, characters and animations people share are built this way.

## Try it

Open the page or project in **Codex** and send the first line of the prompt. If you only use Claude Code, the creator suggests having Opus call Codex through `codex exec` to make the images, or calling the OpenAI Images API directly. The second part of the prompt asks Claude Code to write a script that turns prompts.txt into numbered PNGs, prints the cost as it goes and stops when your credit runs out.

## Creator and prompt

By [Vox](https://x.com/Voxyz_ai). [See the original post](https://x.com/Voxyz_ai/status/2118327475294097710) and [the follow-up with the bulk script prompt](https://x.com/Voxyz_ai/status/2118327476250407164). The copyable text is both prompts as posted, with only the posts' introductions removed.

## What to know

The bulk script calls a paid API and spends real credit. The creator says ChatGPT Pro includes monthly API credits, which make image generation close to free for him; check what your own plan includes. The $30 per million output tokens figure and the model name come from his post. Use a key from the organization that has the credits; the first image-model call may ask you to verify your organization in the OpenAI developer console. We haven't run the prompts ourselves.

**Model provenance:** Images 2.6 and Sol or Astra in Codex are reported by the creator. Possible verified the source pairing, not an independent generation. The preview is the creator's diagram from the post. Creator media is excluded from the repository's MIT license; the original post remains linked.
