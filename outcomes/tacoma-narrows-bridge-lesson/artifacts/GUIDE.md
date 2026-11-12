# GUIDE.md: "Galloping Gertie" short

## What's here
- `short.mp4`: the film, 1080x1920, 30 fps, 59.0 s, H.264 plus AAC, -14 LUFS.
- `poster.png`: the hook frame (f41).
- `SCRIPT.md`: the facts with sources, then the script.
- `STYLE_BIBLE.md`: the look, as numbers.
- `ROUNDS.md`: every look round and score; the sheets are in `rounds/`.
- `CHECKS.md`: every QA result.
- `LESSONS.md`: defect classes to check from the start next time.
- `source/`: everything needed to rebuild.

There are no reference shorts, so there are no topic reports (`ref/reports/`). The look is the chosen option B, written straight into the bible.

## Rendering
Remotion renders in headless Chrome, so run the render on a machine where that's allowed, from the project root (`source/`):

```sh
npm ci --no-audit --no-fund
mkdir -p .tmp && rm -rf .tmp/remotion-*                                     # Remotion copies public/ into the temp dir on every bundle
TMPDIR="$PWD/.tmp" node scripts/render_stills.mjs r7 scripts/stills.json   # half-size look stills (about 1-2.5 min for 37)
TMPDIR="$PWD/.tmp" node scripts/render_final.mjs                           # film (silent) plus poster: about 34 min at 4 tabs on the render machine
```

Then, on any machine with ffmpeg and Python (no browser needed):

```sh
python3 -m venv .venv && .venv/bin/pip install numpy scipy pyloudnorm faster-whisper opencv-python-headless pillow
./scripts/mux.sh                                   # adds audio/mix.wav as the only audio track -> out/short.mp4
.venv/bin/python -I scripts/qa.py out/short.mp4    # black/white/frozen/pop/length/loudness checks -> out/qa.json
```

- Use `CONCURRENCY=2` if the GPU runs out of memory, and `REMOTION_GL=swangle` if ANGLE fails.
- Delete `.tmp/remotion-*` when nothing is rendering.
- For 1440x2560, add a composition in `src/Root.tsx`. Every pixel size scales with height.

## Where to change things
| Change | Where |
|---|---|
| Story beats, shot list, camera keys, cuts, crossfades, shakes, blur, light per shot | `src/story.ts` (`SHOTS`) |
| Caption text and timing | `src/story.ts` (`CAPTIONS`, `END_LINE`) |
| Voice | Replace `audio/voice.wav`. Then run `scripts/transcribe.py` and `scripts/fix_words.py`, which writes `src/words.json`. Then re-time `story.ts`, re-export the events (`scripts/export_events.ts`) and re-make the sound. |
| Colours, light presets, sky, fog, toon ramp, painted textures | `src/materials.ts` (`PAL`, `LIGHTS`) |
| Bridge (deck motion, twist, collapse), new bridge, splash | `src/world/bridge.ts` |
| Terrain, water, sky, clouds, trees, culler, car | `src/world/env.ts`, `src/world/terrain-fn.ts` |
| Wind tunnel, models, streamlines | `src/world/tunnel.ts` |
| Characters (kid, close-up, Tubby, engineer), faces, blinks | `src/characters.ts` |
| Outlines, lens blur, bloom, grade, crossfade | `src/post.ts` |
| Camera interpolation and impact shake | `src/camera.ts` |
| Music, effects, ducking, master | `sound/make_sound.py`. Re-make the sound after any timing change. |
| Framing check before rendering | `npx esbuild scripts/framing_check.ts --bundle --platform=node --format=esm --outfile=.tmp/f.mjs && node .tmp/f.mjs S5` |

## Time it took on the render machine
- Half-size look stills: 52-159 s for 34-37 stills.
- Final film at 1080x1920 with 4 tabs: 2016 s (33.6 min).
- Mux plus QA here: under 1 min.
