# Possible launch film: rules and states

## Facts (from BRIEF.md, read only)
- Copy, used word for word and nowhere else: "See what AI can make." / "Get the agents that make these." / the nine agent names / "Each one is a skill you download once and run in your own Claude Code or Codex." / "US$19 each." / last line "See what AI can make. possible.sh".
- Wordmark: text "possible.sh", Manrope ExtraBold 800, tracking -0.06em, "possible" #201f1c, ".sh" #ed6a4b. No image logo exists, so none is drawn.
- Palette: background #faf7f1, text #201f1c, accent #ed6a4b, muted #77716a, green #477a56. No other colours appear in the film, apart from the pixels of the real outputs themselves.
- Real outputs from possible.sh (ref/, supplied by the user, with the agent that made each): falling-sand-sandbox.png and ant-colony-sandbox.png (Browser Game Maker), two-angle-phone-stand.png (Prototype Engineer), bakery-deck.png (Deck Maker). The launch-kit image was withdrawn by the user (it carries old copy) and must not appear; the Launch Marketer card stays, as one of the nine names. Shown whole, unaltered, scaled only; the row of thumbnails is a centre crop of each. No other product screen exists, so none is drawn.

## Choices (mine)
- Canvas 1080x1920, 30 fps, 58.0 s = 29 bars at 120 BPM (beat 0.5 s, bar 2.0 s).
- Camera: locked-off flat 2D, no lens, no perspective. Motion is panels, type and the five real outputs sliding flat; nothing is tilted or warped.
- Type: Manrope throughout (800 for display, 700 for the agent list). Left aligned at x=80, widest line 920 px, display line height 1.04em, tracking -0.04em.
- Transitions: a full-bleed colour panel slides in over 0.4 s (ease in-out cubic) and lands exactly on a bar line. The outgoing content drifts 18% the same way. Type then rises into place from under its own line (0.35 s ease-out).
- Safe area for all copy: x 60..1020, y 120..1640 (clear of X's bottom controls).
- Real outputs: the agent's name above each at 120 px ExtraBold in #faf7f1 (cap top y=260, wrapped to 920 px), the output 920 px wide under it with a 1 px #77716a keyline. Each lands on a beat by pushing the previous one out to the left (0.3 s); the last holds for two seconds. Then all four rise into a row of 218 px squares at y=1400, and "Get the agents that make these." builds above that row, so "these" points at them.
- Sound: every panel landing and every output landing is a hit; section changes get a low boom.

## DO NOT TAKE
- The OG card's illustrations (paper plane, server box, browser window), its blue and lime panels, and its monospace wordmark. The card is for feel only: big heavy type, flat panels, hard edges.
- Apple's keynote film assets, music or typefaces. "Keynote-style" means pacing only: one idea per beat, big type.
- Claude Code or Codex logos or UI. They are named in the copy as words only.
- Any claim, number or word not in the brief (no "nine agents", no "new", no counters).

## States
| # | Time | Panel | Must be visible and readable |
|---|------|-------|------------------------------|
| S01 | 0.000 (frame 1) | #faf7f1 | Full claim "See what / AI can / make." at 214.5 px, "make." in accent, wordmark top left at 76 px. Readable at phone thumbnail size, sound off. Not black, not a fade. |
| S02 | 3.000 | #faf7f1 | Same, block drifted up at most 14 px. |
| — | 3.6 to 4.0 | | Ink panel rises from the bottom carrying the first output, lands 4.000. |
| S03 | 4.500 | #201f1c | "Browser Game / Maker" above falling-sand-sandbox.png, whole. |
| S04 | 5.500 | #201f1c | "Prototype / Engineer" above two-angle-phone-stand.png, whole (square). |
| S05 | 6.500 | #201f1c | "Deck Maker" above bakery-deck.png, whole. |
| S06 | 7.500 | #201f1c | "Browser Game / Maker" above ant-colony-sandbox.png, whole. Held to 9.0. |
| S07 | 9.800 | #201f1c | Row of four square thumbnails at y=1400, in the same order. Nothing above yet. |
| S08 | 11.500 | #201f1c | "Get the / agents" above the row. |
| S09 | 14.000 | #201f1c | "Get the / agents / that make / these." complete, "these." in accent, row of outputs underneath. Held to 15.6. |
| S10..S18 | 17, 19 ... 33 | accent, bg, green, ink (cycle) | One agent name per bar, one word per line at 171.5 px, cap top at y=300. Below, all nine names at 40 px, the current one full strength, the rest at 42% toward the panel. Name lands on its bar (16, 18 ... 32). |
| S19 | 35.600 | #faf7f1 | "Each one is / a skill you / download once" set. |
| S20 | 39.000 | #faf7f1 | Full sentence in seven lines; "Claude Code" and "Codex." in accent. Held to 41.6. |
| — | 41.6 to 42.0 | | Ink panel rises, lands on 42.000 with the drop. |
| S21 | 44.000 | #201f1c | "US$19" in accent at 313 px, "each." in #faf7f1. |
| — | 47.6 to 48.0 | | Background panel drops from the top, lands 48.000. |
| S22 | 49.200 | #faf7f1 | "See what / AI can / make." set at 200 px. |
| S23 | 53.000 | #faf7f1 | Claim plus wordmark "possible.sh" at 180 px: the exact last line. |
| S24 | 57.967 (last frame) | #faf7f1 | Same as S23, unchanged. Music has faded; nothing is cut off. |

Transition review frames: three frames 1/60 s apart at the middle of every panel wipe (landing minus 0.2 s: 4, 16, 18 ... 32, 34, 42, 48), every output push (landing minus 0.15 s: 5, 6, 7) and the last output leaving as the row rises (9.15).
