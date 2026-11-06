# Escape: an Animated Short from Claude Code, Codex and Seedance

Escape is a 138-second animated short in a soft, hand-drawn 2D style, framed on the golden ratio. Claude Code is the director: it writes the story, shot list and every prompt, checks each picture, and edits with code. Codex paints the character sheets and each shot's first and last frames, and Seedance turns each pair into a 5-second clip. The creator says it took 20+ clips with only one reshoot, and he redid that one by choice, not because it was broken.

## Try it

The copyable text is the creator's whole workflow as a set of prompts, in his order. Send the first one, the director setup, to Claude Code before you start; it asks for length, aspect ratio, budget and music, and checks Codex, FFmpeg, Python and your Seedance key. Then send each later prompt at its step: story, a fresh review agent for the story, shot list and colours, frame check, the seven-part video prompt, the pre-submit review, the edit and the final review. The last prompt sets up his four-agent mode (maker, reviewer, supervisor and a proxy that approves spend within your budget). The prompts are in Chinese; you can ask the agent to work and reply in English. The preview is the creator's actual film, not a Possible-generated substitute.

## Creator and prompt

By [Eian](https://x.com/EianLu). [Read the full article](https://x.com/EianLu/status/2118317430665613741) (Chinese) · [See the film](https://x.com/EianLu/status/2117580488567406794). The copyable text is every prompt block from the article, joined in order with short step headings; the article's explanations and pictures aren't copied.

## What to know

Unlike the code-rendered video Outcomes, this one pays for a video model: Seedance bills per second through a Volcengine account: about ¥0.5/s for 2.0 mini or ¥1.5/s for 2.5 at 720p, per the prompt, and the creator says 2.0 mini is enough for most shots. The whole method is built to catch mistakes in text and stills before anything is sent to Seedance, and the director prompt forbids topping up or buying credit. We haven't run the workflow ourselves.

**Model provenance:** Claude, Codex image generation and Seedance are reported by the creator, without exact versions for Claude or the image model. Possible verified the source pairing and media presentation, not an independent generation. The preview is the creator's film at 720p, copied without re-encoding. Creator media is excluded from the repository's MIT license; the original posts remain linked.
