# Brief for the Motion Designer

## What is the film for, and the facts: exact copy, logos, brand colours as hex

A launch film for Possible (possible.sh): a site where you see real things AI agents made, with the exact prompt behind each one, and can buy the agents that make them. Exact copy you may use (use these words only, don't invent other claims):

- "See what AI can make."
- "Get the agents that make these."
- "Each one is a skill you download once and run in your own Claude Code or Codex."
- "US$19 each."
- The nine agents: Animated Shorts Maker, Browser Game Maker, Competitor Analyst, Customer Profiler, Deck Maker, Launch Marketer, Motion Designer, Procedural Film Maker, Prototype Engineer.
- Last line on screen, exactly: "See what AI can make. possible.sh"

Logo: there is no image logo. The wordmark is the text "possible.sh" in Manrope ExtraBold (800) with tight letter spacing (-0.06em), "possible" in #201f1c and ".sh" in #ed6a4b. ref/possible-og.png is our social card, for the look.

Brand colours: background #faf7f1, text #201f1c, accent #ed6a4b, muted text #77716a, green #477a56.

## References: films or styles to learn from

Keynote-style launch films: big type, one idea per beat, confident pace.

## Length, aspect and music

45 to 60 seconds, 9:16 for X. The claim in big words on screen in the very first second, and every point on screen as words, because most people watch with the sound off. Music and sound made in code, nothing bought. Nothing paid.

Use the motion-designer skill on BRIEF.md. One rule about my machine: nothing may launch a browser here (no Chrome, Chromium, Remotion render or Puppeteer run on this computer; installing packages is fine). Whenever you need anything rendered (stills, sheets or the final film), write the exact shell command to run from this folder into RENDER.md, say which output files you need back, and stop. I will run it unchanged on another machine and put the outputs back in the same paths.

The round 1 outputs are back in place (out/sheets/round1_states.png, out/sheets/round1_transitions.png, out/round1_frame1.png, out/checks/round1.json, out/logs/round_1.log; out/audio/score.wav too). I've also put five real outputs from possible.sh in ./ref: falling-sand-sandbox.png and ant-colony-sandbox.png (Browser Game Maker), possible-agents-launch-kit.png (Launch Marketer), two-angle-phone-stand.png (Prototype Engineer) and bakery-deck.png (Deck Maker). Use them where "make these" needs something to point at. Keep the brand accent as it is. Carry on, and the same rule applies: whenever anything needs rendering, write the exact command into RENDER.md, list the files you need back, and stop.

Round 2 outputs are back in place (out/sheets/round2_states.png, out/sheets/round2_transitions.png, out/round2_frame1.png, out/checks/round2.json, out/logs/round_2.log). One change from me: every launch-kit image carries old copy ("hire", "Join the waitlist") that we no longer use, so I've removed ref/possible-agents-launch-kit.png. Use the other four outputs only. The nine names in the brief, Launch Marketer included, stay as they are. Carry on to the end; same rule: write the exact render command into RENDER.md, list the files you need back, and stop.

Round 3 and the final render are back in place: out/sheets/round3_*.png, out/round3_frame1.png, out/checks/round3.json, out/checks/final.json, out/CHECKS.md, out/film.mp4, out/poster.png, out/logs/round_3.log, out/logs/final.log, plus out/source/ and out/audio/score.wav. I watched it and it looks good to me. CHECKS.md shows two FAILs after encode (brand colour ΔE 2.47, and output shift around 2 for each of the four images). Do your round 3 review and deal with those however you judge right. Then give me the final render command the same way and stop. If nothing needs re-rendering, just say the film is done.

The final re-encode is back in place: out/film.mp4, out/poster.png, out/checks/final.json, out/CHECKS.md, out/logs/final.log and out/source/. Read it and close out.
