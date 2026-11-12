# Guide: "A river did this" — Grand Canyon, made from code

> **Quality note:** `film.mp4` is below the photoreal bar in `BAR.md` (target 98; critic medians after four rounds
> 35–88 per dimension, shot minimums 35–46.5). It was rendered at this quality by the user's choice; see the end of
> `ROUNDS.md`. `preview_540_round4.mp4` is an earlier 540×960 preview with the old "(1.8 km)" depth card.

Everything is generated: terrain, rock, water, trees, sky, the on-screen font and the soundtrack. No textures, meshes,
HDRIs, font files or samples are loaded. The only "texture" is a 512×512 table of random numbers made in `engine.py`.

## Run it

```bash
# once: python env (from the project root)
uv venv .venv && uv pip install --python .venv numpy scipy numba moderngl pillow pyloudnorm
cd out/src
../../.venv/bin/python terrain.py          # bake + erode the canyon (≈60 s, cached in out/cache/field.npy)
../../.venv/bin/python audio.py            # soundtrack → out/cache/soundtrack.wav (≈10 s)
../../.venv/bin/python stills.py ../rounds/rNN --w 540          # one still per shot (+ _sheet.png)
../../.venv/bin/python stills.py /tmp/t --w 540 --text           # same, with the on-screen words
../../.venv/bin/python film.py             # film: 1080×1920, 24 fps, 4 motion-blur samples → out/film.mp4
../../.venv/bin/python film.py --w 540 --mb 2 --out preview.mp4  # quick preview
```

`film.py` renders each shot to `out/cache/seg_XX_<width>.mp4` and skips segments that already exist, so a killed render
resumes where it stopped (`--force` re-renders, `--shots 3,4` renders only some). Then it joins the segments and muxes
the soundtrack (H.264 yuv420p, AAC 256k).

GPU: moderngl standalone context. On macOS this is CGL; on Linux it defaults to headless EGL (`FILM_BACKEND=egl`), and
with `LIBGL_ALWAYS_SOFTWARE=1` it runs on Mesa llvmpipe on CPU (much slower). Only OpenGL 3.3 features are used.

## Speed on this machine (Apple M1 Pro, 16 GB)

- One full-resolution sample (1080×1920): 0.14–0.41 s depending on the shot (river-level shot 5 is the slowest:
  reflections + many near-ground steps). A film frame = `--mb` samples + about 0.3 s of finishing (bloom, grade, text).
- 1080×1920 with `--mb 4` (the delivered film): measured 1.7–3.2 s per frame by shot (flat-plateau and river shots slowest), 58 min for the 57 s film (1,368 frames). Output is about 390 MB at CRF 16.
- 540×960 preview with `--mb 2`: about 0.3 s per frame.
- Preview stills (540×960, 4× AA): 0.4–0.7 s each.

## Where to change things

| What | Where |
|---|---|
| Shots: places, camera keyframes, duration, ease, drift, sun per shot, clouds, haze, grade | `src/shots.py` → `SHOTS` |
| Time-lapse (age 0 = flat plateau, 1 = today) per shot | `SHOTS[i]["age"]`; river level vs age in `camutil.zr_of_age` |
| Rock layers: order, thickness, cliff/slope behaviour, colours | `src/strata.py` → `LAYERS`, `WIDTH`, `ALBEDO`, `ledge_factor` |
| Canyon plan: river path, tributaries, noise warp, erosion strength | `src/terrain.py` (`river_z`, `bake`, `ERODE_ITERS`, `ERODE_DT`) — re-run with `--force` |
| Light: sun power, sky ambient, warm bounce in shadows | `shaders/scene.frag` → `shadeTerrain` (`skyAmb`, `bounce`); sun per shot in `shots.py` |
| Rock texture: bedding stripes, jointing, talus, soil, scrub | `shaders/scene.frag` → `rockAlbedo` |
| Vegetation density, crown shapes and colours | `shaders/scene.frag` → `vegDensity`, `treeAt`, `treeSDF`, `shadeTree` |
| Water colour (green vs silty), waves, rapids, glints | `shaders/scene.frag` → `waterShade`; per-shot `mud` in `shots.py` |
| Sky, haze, aerial perspective, clouds | `shaders/scene.frag` → `scatter`, `skyColor`, `cloudDens`; `haze`, `aerial` per shot |
| Finishing: exposure, bloom, saturation, contrast, warmth, vignette, grain | `src/post.py` → `DEFAULT` (per-shot overrides via `grade=`) |
| On-screen words, timing, sizes, the year counter, the end line | `src/overlay.py` → `CARDS`, `years_ago`; glyphs in `src/font.py` |
| Music: tempo, chords, melody, instruments, levels, nature bed, loudness | `src/audio.py` (constants at the top: `BPM`, `CHORDS`, `MELODY`, `AUTOMATION`, `STEM_GAIN_DB`, `BIRD_CALLS`, `TARGET_LUFS`) |

Cuts land on downbeats: 80 BPM, one bar = 3 s, every shot is 2 bars (end card 3 bars). If you change shot lengths,
keep them multiples of a bar, or change `CUT_TIMES` in `audio.py` to match.

## Quality loop

`rounds/CRITIC_PROMPT.md` is the rubric given to fresh critic agents; `src/scores.py rounds/rNN` takes the median;
`src/measure.py rounds/rNN` measures colour per region. History is in `ROUNDS.md` and `stills/history/`.

## Facts on screen (checked against NPS)

About a mile (1.6 km) deep (on screen; the deepest point is about 1.8 km); 277 miles (446 km) long by the river, Lees Ferry to the Grand Wash Cliffs;
carved mostly by the Colorado River in about 5–6 million years; basement rocks at the bottom about 1.84 billion years
old ("nearly 2 billion").
