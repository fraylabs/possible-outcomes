# CHECKS.md: every QA result for out/short.mp4

All checks below ran on this machine without a browser. Rendering happened on the buyer's render machine through RENDER.md.

## Shipped-file QA (`scripts/qa.py out/short.mp4`, raw output in `out/qa.json`)
| Check | Result |
|---|---|
| Resolution / fps | 1080x1920, 30/1. **PASS** |
| Frames decoded | 1770 of 1770 (59.0 s). **PASS** |
| Video codec / pixel format | H.264, yuv420p. **PASS** |
| Audio | exactly 1 stream, AAC 48 kHz (the synthesized mix). **PASS** |
| Audio vs video length | 59.000 s vs 59.000 s, difference 0.000 s. **PASS** |
| Black spans ≥ 12 frames (mean luma < 8) | none. **PASS** |
| White spans ≥ 12 frames (mean luma > 247) | none. **PASS** |
| Frozen spans ≥ 12 frames (mean abs diff < 0.05) | none, including the 4 s end card, which keeps a slow push. **PASS** |
| Single-frame pops | none. **PASS** |
| Integrated loudness | -14.01 LUFS (target about -14). **PASS** |
| Sample peak of the shipped AAC | -1.02 dBFS. **PASS** |
| True peak of the mix before AAC (4x oversampled) | -1.0 dBTP. **PASS** |
| True peak of the shipped AAC (oversampled) | **NOT RUN.** Only the sample peak was measured on the AAC file. |
| Film grain | none in the pipeline (no grain pass exists). **PASS by construction** |

**Loudness defect found and fixed.** The first mux measured -11.02 LUFS. The master had measured the mono signal, but the file carries it on two identical channels, which reads 3 dB louder. `sound/make_sound.py` now measures the stereo signal it ships. It was re-mastered, re-muxed and re-checked at -14.01.

## Determinism / seekability
| Check | Result |
|---|---|
| Frame rendered twice, compared pixel by pixel (f0770 and f1300, half size, in every round 1-6) | max diff 0 in all 12 comparisons. **PASS** |
| Same test at full size | **NOT RUN.** Only the half-size stills were repeated. The code path is identical; only the output height differs. |
| No clocks, timers or unseeded randomness | by construction: the frame number is the only input. All randomness uses `hash()` in `src/util.ts`; the audio is seeded (`default_rng(1940)`). |

## Build and code
| Check | Result |
|---|---|
| `tsc --noEmit` | pass |
| Webpack bundle (`@remotion/bundler`, no browser) | pass before every render request |
| Framing check (`scripts/framing_check.ts`, pure maths) | Run before every render. It reports subject positions, horizon height and the deck's on-screen tilt per shot. Subjects that intentionally leave frame are listed in ROUNDS.md. |

## Story, words and timing
| Check | Result |
|---|---|
| Closing line on screen | Matches the brief exactly: "Email, logins and 2FA codes for each of your AI agents. actas.dev". Only the layout breaks the line before the URL. **PASS** |
| Main claim on screen in the first second | "A 40 mph breeze destroyed this bridge." from frame 0. **PASS** |
| Captions are the approved on-screen words | Yes, with one layout change: "=" moved to the end of the line before "FLUTTER". **PASS** |
| Each caption line pops 0-3 frames before its word | Every line is keyed to `W(i) - 2` (or `- 3` for one), from words.json. **PASS** |
| Caption safe area | Block starts at 0.17 H and ends by about 0.33 H. Nothing below 0.78 H. **PASS** |
| Length | 59.0 s (brief: 45-60 s). **PASS** |
| Voice / script match | Whisper transcription of voice.wav reproduces the approved script word for word, apart from the two name spellings it misheard ("girdy" for Gertie), fixed by hand. **PASS** |
| Facts | Every fact in SCRIPT.md carries a source. |

## Sound
| Check | Result |
|---|---|
| Event table taken from story.ts (`audio/events.json`) | yes |
| Timing locked before the sound | Yes. No cut or word time changed after the mix; the post-loop fixes changed pictures only. |
| Ducking | Music up to -10 dB and effects -4 dB under the voice (envelope from the voice level). |
| Listening test by ear | **NOT RUN.** This machine can't play audio to me. Balance was checked by measuring stems per shot (`scripts/mix_balance.py`). |

## Look-match loop
Six rounds, every score in ROUNDS.md. The loop stopped by rule after two rounds in a row with no gain (rounds 5 and 6). **No area reached 8**; ROUNDS.md lists the reasons per area. The post-loop readability fixes were checked by eye on frames decoded from out/short.mp4 (`sheets/final_frames.jpg`), not re-scored.

## Known remaining issues (seen on the shipped frames)
- Poster (f41): a thin cream sliver of a pier peeks in at the right edge around 0.6 H.
- S6c (f1050-1090): the caption's orange key words sit over the kid's yellow cap; the ink stroke keeps them legible.
- Wide bridge shots still show more water than the bible's 22 % share, and long-lens deck views stack hangers densely.
