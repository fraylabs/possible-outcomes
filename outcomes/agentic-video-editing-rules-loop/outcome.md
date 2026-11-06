# Agentic Video Editing: Teach Claude Your Cuts

Claude Code edits your video for you, and gets closer to your taste with every note. It transcribes the video with Whisper so it knows where every word starts and ends, removes pauses longer than 0.45 s without clipping the last sound of a word, and exports the cut as an FCPXML timeline you open in DaVinci Resolve. Every note you give it goes into rules.md, which it reads before the next edit.

## Try it

Make a folder with one talking-head video you've already edited by hand, open it in Claude Code, and ask it to install ffmpeg and Whisper. Rename your video to talking_head.mp4 (or change the name in the prompt), then paste the prompt. In Resolve, use File > Import > Timeline to open the cut, watch it, and tell Claude what you'd change as numbers ("0:09 caption covers her face"). The prompt ends with the creator's starter rules; copy them into rules.md to start from his numbers.

## Creator and prompt

By [Lad](https://x.com/ladprofit), from his free guide [Agentic Video Editing: How to Train AI to Edit Like You](https://x.com/ladprofit/status/2115450836398882941). The copyable text is the guide's "first agentic edit" prompt as posted, followed by the starter rules list from step 3 of the same guide.

## What to know

The guide's loop is: read the video as text, write the edit down, give rules as numbers, feed it edits you love, preview cheap and render once, turn every note into a rule. The creator keeps jump cuts on talking heads for himself in Resolve, because the agent's joins sounded wrong. He also posted a [42-second true-crime ad](https://x.com/ladprofit/status/2118351185241686446) that Claude Code cut from Internet Archive film clips; that workflow is only sent by DM and isn't included here. We haven't run the prompt ourselves.

**Model provenance:** Claude in Claude Code is reported by the creator, with no version given. Possible verified the source pairing, not an independent generation. There is no preview media; the original posts remain linked.
