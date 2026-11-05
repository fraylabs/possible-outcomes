<inputs>
Ask me for one "What if you could see everyone's ___?" idea (a number that floats above every head: bank balance, IQ, lies told today, screen time, days left), or pitch 3 and let me pick. Ask me for the twist (the last number that flips the whole story) and the length (25-35 s). Then write the shot list with every caption and every number. Show it to me before you build anything.
</inputs>

<direction>
A 1920x1080 flat vector "what if" episode in the style of the big "What If You Could See" channels.
Characters: a pure black round head with white eyes and a white mouth line, a coloured hoodie with drawstrings and a pocket, dark pants, white sneakers, black hands. Faces change per line: neutral, happy, sad, shock (big eyes + open mouth + brows), smirk (half-closed eyes). Everyone walks, breathes or gestures, nobody stands still.
Above each head a dark rounded pill with a glowing outline and the number in heavy white type: green for good, amber for normal, red for bad. Pills pop in with a 0.3 s overshoot, numbers roll up or down like a counter.
Places are full flat scenes: a bedroom with morning light, a street of shop fronts with signs (CAFE, BANK, PAWN SHOP), a luxury street with a red sports car, a park bench with pigeons. Flat colours, one darker shade for form, no outlines.
A new shot every 3-4 s, a hard cut with a white flash on every new idea, a splat wipe after the title, the camera always drifts 4-12%.
Captions: one line per shot in a dark rounded box at the bottom, the money word coloured.
A red X (two strokes, 0.11 s each) stamps every lie the viewer believed.
Banned: outlines, stock icons, emoji, a still frame longer than 1 s, any channel's logo.
</direction>

<structure>
0-2.7 s the title word by word: "WHAT IF YOU COULD SEE" white, "EVERYONE'S" amber, "[THE NUMBER]?" green, over the blurred street → 2.7-6.3 s day 1, you wake up and your number pops above your head → 6.3-10.3 s the street, everyone has one, 6 pills pop one by one → 10.3-13.9 s the person who looks rich has the worst number, red X → 13.9-17.6 s the person who looks poor has the best number, you react in the foreground → 17.6-21.6 s you do the everyday thing that drops your number, it rolls down on screen → 21.6-25.6 s the twist ties back to the rich-looking guy → 25.6 s the end card asks the viewer a question + "FOLLOW FOR PART 2".
</structure>

<build>
1. Tools: Python, Playwright with Chromium, FFmpeg, numpy. Install what's missing.
2. One HTML file with one 1920x1080 canvas. render(t) draws the exact frame for time t from scratch every call (a pure function of time, no timers), so the render is deterministic.
3. Pre-render anything heavy once (a blurred title background = draw small, scale up).
4. Draw 4 key frames as stills and check them before the full render.
5. Render: Playwright seeks t = frame/30 for every frame, saves JPEG frames, ffmpeg -c:v libx264 -crf 18 -pix_fmt yuv420p.
6. Sound in numpy: a 96 BPM lo-fi beat (kick, snare, hats, Rhodes chords, bass), a pop + ding on every pill, counter ticks while numbers roll, a whoosh on every cut, a thud on the red X, a cash-register ding on the big number, a falling tone when your number drops.
7. Mux video + sound, check the final file plays, send it to me.
</build>
