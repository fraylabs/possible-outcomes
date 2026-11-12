# Galloping Gertie: how a steady wind tore a bridge apart

A 59-second vertical cartoon lesson on why the Tacoma Narrows Bridge twisted itself apart on 7 November 1940. It opens on the claim, builds the bridge and the morning, shows the deck go from bouncing to twisting until the middle falls, then explains flutter with a blade of grass held between two thumbs. It ends on Tubby the dog, the wind tunnels that came after, and a one-line card. Characters, the 3D world, the voice timing, the sound effects and the score were all made in code.

## How it was made

The Animated Shorts Maker skill, run in Claude Code with Claude Opus 5.5, got the brief shown here and nothing else. It proposed three looks, two voices and a silent or voiced end card, wrote the script with a source for every fact, and waited for a yes. Then it built the film in Remotion and three.js, with drawn characters on cards and the Mac's built-in `say` voice timed word by word. It scored half-size stills of every shot over six rounds with fresh reviewers, and stopped when two rounds gained nothing. The person giving the brief ran each render command unchanged on another machine; the final render took 34 minutes. The agent then mixed the sound and checked every frame of the shipped file. Nobody edited the film by hand.

Recorded: made by the Animated Shorts Maker skill in a clean folder holding only the skill and a brief, 12 November 2026.

## What to know

- This is below the skill's own bar. Reviewers scored the look about 5.5 to 5.9 out of 10 from round 2 on, against a target of 8. Composition and readability are weakest: a long bridge doesn't fit a tall phone frame at a readable size, so many wide shots are mostly water. The flat drawn characters look pasted onto the 3D world.
- The opening line calls a steady 40 mph wind a "breeze" and the voice says "a gentle wind". That is the agent's wording; 40 mph is close to a gale. The brief said "not a storm".
- The agent measured the sound but couldn't listen to it.
- The skill has since been told to fit words to the numbers they describe, to check framing with projection maths before the first render, to treat wide subjects differently in 9:16, to ground drawn characters with shadows and matching ink, to take the median of three scorers, and to hand renders off with exact commands when the machine can't render.
