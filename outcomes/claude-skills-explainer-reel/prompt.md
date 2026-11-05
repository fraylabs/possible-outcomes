# EXPLAINER REEL STUDIO (lecture style)

Save this file as `CLAUDE.md` in an empty folder, open Claude Code in that folder, and say **"make a reel"**.
Latest version, the rater and example videos: https://theoxmotion.pages.dev/r/explainer-reel-studio/

You (Claude) make ONE finished vertical explainer reel, 45 to 60 seconds. It works like a short lecture: a cartoon teacher stands bottom right and talks the viewer through one usable thing. Slide-like titles, cards, typing terminals, rolling numbers and red stamps land on the exact word that's spoken, and captions build word by word at the top. The last frame matches the first, so the reel loops.

Everything is free and runs on this computer: the person needs a Claude subscription and nothing else. No API keys, no accounts, no paid services. The person sees three checkpoints: **the script, then key stills, then the finished video.**

---

## <inputs>

Ask for these once, in one message. Use the defaults for anything the person skips.

| input | default |
|---|---|
| **The topic:** one usable thing the viewer can do today | none. If the person says "you pick", choose one yourself (AI tools if they name no niche) and say what you picked in one line. |
| Handle shown nowhere / anywhere | none (the format has no watermark) |
| Length | 45 to 60 s |
| Voice | Kokoro `am_liam+am_puck`, a 50/50 mix (a calm, young male narrator), speed 0.97 |

---

## <direction>

**The feel:** a calm, clear lecture. One point at a time. The teacher talks the whole time, and each point is acted out on the "slide" while it's said.

**Page:** 1080x1920, cream paper `#EBE7E1` with a fine grain. Ink `#1E1C1A`, accent red `#D7372C`, grey `#8A857E`. Nothing else is coloured, except the folder blue in the payoff card and the presenter.

**Type:**
- **Titles:** Anton, upper case, about 190 px. Usually two words: the first in ink, the second in red with a hand-drawn red swash under it. They slam in (scale 1.6 to 1, 0.26 s, power4.in), then the swash draws (0.35 s).
- **Labels:** JetBrains Mono, 30 px grey: `// 01 · the problem` top left, and a stat top right (`TOKENS 100`, with the number in red). The number counts up when it's said.
- **Captions:** Instrument Sans, 58 px, top left under the label.
  - One line of 2 to 5 words, split by meaning.
  - Unsaid words are light grey and turn ink as they're spoken.
  - One key word per line is set in red Instrument Serif italic.

**Cards:** off-white `#F8F6F2`, a 3 px ink border, radius 16, and a halftone dot shadow offset down-left. Kinds:
- chat;
- file tree;
- code;
- terminal;
- compare bars;
- checklist;
- split;
- a folder that paper cards drop into.

A black terminal bar under the card types a command with a red `$` and a red block caret.

**Marks:**
- **Stamps:** red, Anton, a 7 px border, tilted -6°, slam in (scale 1.9 to 1, 0.28 s).
- **Badges:** a red `#N` circle on the card corner for each numbered point.
- **Strike:** a red strike-through line.
- **Ring:** a hand-drawn red circle around a number.
- **Wipes between points:** halftone dots grow from the centre, cover the page, then shrink away (0.65 s).

**The presenter (the teacher):**
- An original cartoon person, bottom right, cropped at the chest, about a third of the frame.
- Flat colours with dark outlines and a halftone dot shadow.
- The kit's character has curly black hair, red headphones and a mustard sweater, with no glasses.
- Never draw a real person.
- The mouth is lip-synced from the voice's phonemes and loudness. The eyes blink and glance at what lands. The head nods on stamps and titles.
- One hand rises to point at each new point, and the other waves at the start and at the end.

**Sound:**
- one Mixkit effect per on-screen event (wipe, card, title slam, typing, tick, check, stamp, strike, ring, badge);
- a quiet instrumental bed about 18 dB under the voice;
- the mix at -14.5 LUFS, true peak about -1.5 dBFS in the delivered files (check.py fails anything above -1.0).

---

## <structure>

10 to 12 beats, 140 to 170 words, 45 to 60 s:

| beat | job | on screen |
|---|---|---|
| 1 | **The hook**: the biggest true number or a surprising claim, said in the first second, plus the problem it solves ("Under two hundred lines. That's Anthropic's target for your CLAUDE.md." / "Instagram can show your next reel to strangers first, and tell you in twenty four hours if it works."). A familiar setup with no number is not a hook: a blind rater scored one 6. | frame 0 = the thumbnail: a two-word title that carries the number ("24 HOURS", "200 LINES"; a digit in a title must be spoken within the first second), a card showing the problem, then a **strike-through** on the bad part and a red **stamp** by about 1.5 s |
| 2 | **The fix**, landing by about 3 s | label `// 02 · the fix`, title, the **folder card** (2 to 4 small paper cards drop in) with a pill that counts up, and a red **ring** around the number |
| 3 to 8 | **The points**, one per beat. Numbered points start "Step one." / "Two." | a halftone **wipe**, then a title slam + swash, a card that builds on the spoken words, a `#N` **badge**, the **terminal bar** typing the real command, a **count-up** when a number is said, and a **stamp** with the takeaway |
| 9 | **Why it works**, the mechanism in a line or two | a compare or checklist card, with numbers counting up as they're said |
| 10 | **Use it** | the command or the first thing to try, typed out |
| last | **Loop line**: 6 to 9 words, a recap that flows back into line 1, its landing word 1 to 2 s before the end (nothing else can be cued in this beat, so keep it short) | at that word, the screen snaps back to beat 1's frame 0 (rows that were cued later stay hidden, the wave comes back up), so the reel loops |

**Lines:**
- One idea per beat, 8 to 20 words, plain spoken English.
- **Numbers as words** in `say` ("one thousand and twenty four"), digits on screen ("1,024").
- **Code and paths in spoken form** ("skill dot M D", "slash weekly report"), mapped back for the captions with `"captions": {"skill dot M D": "SKILL.md"}`.
- Banned: greetings, "in this video", "let's dive in", "like and subscribe", "imagine", hype words, any claim you didn't verify today.

---

## <build>

### Setup (once per folder, about 5 minutes)

Unpack the kit at the end of this file:

```
python -c "import re,os;q=chr(96)*4;t=open('CLAUDE.md',encoding='utf-8').read().replace(chr(13),'');fs=re.findall('<!-- FILE: ([a-zA-Z0-9_./-]+) -->\n'+q+'[a-z]*\n(.*?)\n'+q,t,re.S);[(os.makedirs(os.path.dirname(p) or '.',exist_ok=True),open(p,'w',encoding='utf-8',newline='').write(b+chr(10))) for p,b in fs];print('unpacked',len(fs),'files')"
```
(On a Mac use `python3`.)

Then install, all inside this folder:

| what | Windows (PowerShell or Git Bash) | Mac / Linux |
|---|---|---|
| Python env | `python -m venv .venv` | `python3 -m venv .venv` |
| Python packages | `.venv\Scripts\python -m pip install kokoro-onnx soundfile faster-whisper numpy pillow imageio-ffmpeg` | `.venv/bin/python -m pip install kokoro-onnx soundfile faster-whisper numpy pillow imageio-ffmpeg` |
| Node packages | `npm init -y` then `npm i playwright@1.64.1 gsap@3.15.0` | same |
| Assets (~490 MB, once) | `.venv\Scripts\python kit\fetch_assets.py` | `.venv/bin/python kit/fetch_assets.py` |

- Python 3.10+ and Node 18+ are needed. If one is missing, give the person the one installer to run (python.org, nodejs.org) and wait.
- The renderer drives the Edge or Chrome already on the computer, on the CPU only. If it says "No browser found", run `npx playwright install chromium` once.
- Below, `PY` means `.venv\Scripts\python` on Windows and `.venv/bin/python` elsewhere.

**Rules:**
- Free and local only.
- Never clone or imitate a real voice.
- Mixkit sounds and music are downloaded on this computer by `fetch_assets.py`; their licence allows them inside videos but not as files handed on, so never commit, zip or upload `assets/`.
- Every number and fact comes from a primary source you opened today (WebSearch / WebFetch), and goes into `story.json` → `"sources"`.
- Never draw a real app's logo or copy its interface.

### The steps

1. **Facts, then the script (checkpoint 1).**
   - Write `story.json` by copying the shape of `kit/example_story.json`.
   - Show the person a table: beat, what's said, what's on screen, then the sources.
   - Ask for an OK. If they said "you pick" or "go", don't wait.
2. **Voice:** `PY kit/voice.py`.
   - Kokoro reads each line, faster-whisper times every word, and the mouth track is built.
   - Aim for **45 to 60 s and 165 to 185 words a minute**. Too long: cut words, never speed.
   - Run it again after ANY change to a `say` line.
3. **Stills (checkpoint 2):** `node kit/render.js stills`.
   - Look at `build/stills/sheet.jpg` yourself first: titles fit, no card cut off, nothing over the presenter, and `build/warnings.txt` is empty.
   - The default stills catch beats early. `node kit/render.js stills 12.5 30` shows chosen seconds in `build/stills/at/`.
   - Then show the person the sheet.
4. **Render:**
   - `node kit/render.js final` (1 to 4 minutes; `--workers 1` on a low-memory computer);
   - then `PY kit/sound.py`;
   - then `PY kit/finish.py`.
5. **Check:** `PY kit/check.py` writes `build/qa/report.md`.
   - Fix every FAIL. A `say` change means voice.py again; a card, cue or title change means render.js again (stale frames are cleared by themselves).
   - Then open `build/qa/sheet_*.jpg` (a frame every 0.5 s) and `build/qa/lips.jpg` and look.
6. **Deliver:**
   - `out/<slug>.mp4` (9:16);
   - `out/<slug>_x78.mp4` (7:8 for X: the whole frame with plain black side bars, never a blurred copy);
   - `out/<slug>_cover.jpg`;
   - the length, the check table and the sources.

   Tell them to listen to the first 10 seconds once: you can't hear audio.

### story.json

```
{
 "topic": "...", "slug": "file_name", "voice": "am_liam+am_puck", "speed": 0.97, "tail": 0.8,
 "captions": {"spoken words": "screen text"},
 "keys": ["words", "set", "in", "red", "italic"],
 "sources": ["url (read YYYY-MM-DD): the fact it backs"],
 "beats": [ {beat}, ... ]
}
```

**A beat:**
- `say` (required): the line.
- `label`: the text after `// 0N · ` (the number counts up by itself).
- `stat`: `{"label": "TOKENS", "value": 100, "at": "hundred"}`, top right; the number counts up on the word.
- `title`: two words, the red one in `*stars*`: `"ONE *FOLDER*"`. Use `+` for a plus sign: `"CLAUDE + *SKILLS*"`. A beat without a title keeps the last one. A digit in a title counts as a number on screen: it lands with the title, so the line must start with that number (beat 1's hook, or "Twenty four hours. ...").
- `card`: the card (types below). A beat without a card keeps the last one.
- `point`: n. A numbered point: halftone wipe, `#n` badge, the hand points up.
- `term`: `{"cmd": "mkdir ~/.claude/skills/weekly-report", "at": "make"}`, the black terminal bar under the card. Keep it under 40 characters. Only for a real command: if the topic has none (an app setting, a platform feature), leave `term` out and never invent one.
- `strike`: `[row, "cue"]`, a red line through a row of the card on screen.
- `ring`: `[row or "pill", "cue"]`, a red hand-drawn circle around it.
- `stamp`: `{"text": "AGAIN", "at": "cue"}`, over the card's lower right edge. 1 to 3 short words. `"left": true` puts it on the left (use it when the card's right side holds the key text).
- `focus`: `[row, "cue"]`, highlights a row.
- `keys`: more caption words for red italic in this beat.
- `loop`: true, on the last beat, with `loopAt`: the word where beat 1's frame comes back. A `title` here shows before that word. `stamp`, `ring` and `strike` are ignored on the loop beat (they would break the match with frame 0).
- `pause`: extra seconds of silence after this line.

**Story-level timing (optional):** `gap` (0.28 s between lines), `step_gap` (0.45 s before a numbered point), `max_pause` (0.32 s, the longest pause kept inside a line), `tail` (0.8 s after the last word). Words a minute a little high? Raise `gap` before cutting words.

**Cues.** Anything with `at` or `cues` lands ON A WORD of its own line:
- `"at": "hundred"`, or `"hundred#2"` for the 2nd time it's said;
- a fraction of the line (`0.5`);
- `null`, for "with the card".

A cue that isn't a word in the line is listed in `build/warnings.txt`. A row can wait for a later beat's word with `"beat": n`.

**Cards:**

| type | fields |
|---|---|
| `chat` | `msgs: [{"from": "you" or "ai", "text": "..."}]`, `cues` |
| `files` | `rows: [["~/.claude/", 0, "folder"], ["SKILL.md", 3, "file"]]` (text, indent, icon), `cues`, `hl` (row in red) |
| `code` | `lines: ["---", "name: weekly-report"]`, `cues` (one per line; they type in). Lines under 30 characters. |
| `terminal` | `cmd`, `out: ["ok: done", "..."]`, `cues` (command first, then each output line) |
| `folder` | `name`, `items: ["name", "description", "steps"]` (paper cards that drop in on `cues`), `pill: {"label": "AT STARTUP", "value": 100, "at": "hundred"}` |
| `compare` | `items: [{"label": "at startup", "value": 100, "unit": "tokens", "at": "hundred", "show": "startup", "note": "name + description", "note_at": "name"}]` |
| `counter` | `value`, `unit`, `label`, `at` |
| `checklist` | `items: ["text", {"text": "...", "mark": "x"}]`, `cues` |
| `split` | `left: {"title": "BEFORE", "lines": [...]}`, `right: {...}`, `cues` |

Any card can also take:
- `tab` (the small grey label at its top);
- `extra: [{"kind": "chip" or "msg", "text": "...", "ok": true, "at": "cue"}]`;
- `focus`.

---

## <gotchas> (each one cost a render or a rating)

- **Something new every 1.5 to 2 s.** `check.py` lists every stretch over 1.8 s where nothing arrives and fails anything over 2.4 s. To fill a gap, cue a row, an `extra`, a `stamp`, a `ring`, a `focus` or the `term` on a word inside it. A spoken word that's written on a visible row makes that row pulse by itself.
- **No empty cards.** The first row lands within 1.5 s of the card (`check.py`: "cards fill fast"). Use `null` cues for rows that should be there from the start.
- **Number words never join across a full stop** in the check ("Three. One hour" is 3 and 1), but keep step numbers and data numbers in separate sentences anyway.
- **Numbers land when they're said.** Every number on screen (stat, pill, compare, counter, title digits, `#N` badges) is checked against the spoken words: it must appear within 0.3 s of the word and stay at least 1.2 s after. When the next beat starts a numbered point, put the number early in its line, because the wipe covers the screen.
- **Never clip the last syllable.** voice.py keeps 60 ms after each line and the `tail` (0.8 s) after the last. Don't trim the audio by hand.
- **Audio crackle / true peak above 0 dBFS after finish.py:** ffmpeg's built-in AAC encoder can wreck one frame where a click hits a vowel. finish.py already encodes at 256k with noise substitution and intensity stereo off; leave those flags in.
- **Counter cards and big numbers** count as content for "cards fill fast"; a card that only shows a number later still needs something at the start.
- **Captions follow meaning.** Never more than one line. They break at sentence and clause ends and never leave one word alone. If a caption is too wide, `warnings.txt` says so: shorten the words or add a comma.
- **Kokoro holds full stops.** voice.py squeezes any pause inside a line to 0.32 s.
- **faster-whisper and PyAV:** never pass whisper a file path. The kit decodes audio with ffmpeg into numpy first.
- **"timing has N lines but story has M beats":** run voice.py again.
- **A card is too tall** (`warnings.txt`): the zone is about 570 px including the terminal bar. Cut a row or a line.
- **Titles:** at most two short words plus `+`. They shrink to fit, but a long word looks small.
- **If you ever edit `kit/reel.html`:** each frame must depend only on time. No `Math.random()`, no `Date`, no CSS transitions or `@keyframes`. Use the GSAP timeline (`ft(...)`, `tl.to(...)`) or compute from `t` in `seek()`.
- **The X version** is the full 9:16 frame scaled into 1008x1152 with plain black bars. Never fill the sides with a blurred copy.
- **A crashed render:** run it again. Finished frames are kept while nothing has changed.

---

## <start>

1. Unpack, then run the setup (skip the parts already done).
2. Ask the `<inputs>` in one message.
3. Research the facts live, write `story.json`, show the script (checkpoint 1).
4. Voice, stills (checkpoint 2), render, sound, finish, check.
5. Deliver the files, the check table and the sources.

Optional, for a blind second opinion: the rater in this guide's repo (`rater/RATER_PROMPT.md` + `rater/rate_prep.py out/<slug>.mp4 --face 620,1530,280,240`), run by a fresh Claude session. GOOD needs every row at 7 or more and 60 or more out of 80.

---

## Files (unpacked by the command in <build>)

<!-- FILE: kit/fetch_assets.py -->
````python
"""fetch_assets.py : download everything the reel needs, once, into assets/ (about 490 MB, mostly the voice and timing models).

    python kit/fetch_assets.py            (safe to run again: it skips files it already has)

What it gets, all free:
  fonts/   Anton, Instrument Sans, Instrument Serif, JetBrains Mono   (Google Fonts on GitHub, SIL Open Font License)
  sfx/     11 sound effects from Mixkit                     (Mixkit Sound Effects Free License)
  music/   1 instrumental track from Mixkit, no vocals      (Mixkit Stock Music Free License)
  voice/   Kokoro-82M voice model + voices                  (Apache-2.0)
  whisper/ faster-whisper base.en, for word timing          (MIT)

Mixkit's licence lets you use these inside your videos, but not hand the files on by themselves.
So every user downloads them here, from Mixkit, and they never go into a repo or a zip you share."""
import os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "assets")
GF = "https://github.com/google/fonts/raw/main/ofl/"
MK = "https://assets.mixkit.co/active_storage/sfx/{0}/{0}-preview.mp3"
FILES = [
    (GF + "anton/Anton-Regular.ttf", "fonts/Anton-Regular.ttf"),
    (GF + "instrumentsans/InstrumentSans%5Bwdth,wght%5D.ttf", "fonts/InstrumentSans.ttf"),
    (GF + "instrumentserif/InstrumentSerif-Italic.ttf", "fonts/InstrumentSerif-Italic.ttf"),
    (GF + "jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf", "fonts/JetBrainsMono.ttf"),
    # sound effects, one per on-screen event (event name -> Mixkit id). Swap an id here to change a sound.
    (MK.format(1490), "sfx/wipe.mp3"),       # Fast whoosh transition (halftone dot wipe)
    (MK.format(2356), "sfx/card.mp3"),       # Dry pop up notification alert (cards, rows)
    (MK.format(2364), "sfx/title.mp3"),      # Hard pop click (title slam)
    (MK.format(1109), "sfx/tick.mp3"),       # Select click (count-ups)
    (MK.format(1396), "sfx/typing.mp3"),     # Soft typing on a digital keyboard
    (MK.format(2870), "sfx/check.mp3"),      # Correct answer tone
    (MK.format(2569), "sfx/cross.mp3"),      # Negative tone interface tap
    (MK.format(2357), "sfx/badge.mp3"),      # Bubble pop up alert notification (#N badge)
    (MK.format(2182), "sfx/stamp.mp3"),      # Wood hard hit (red stamp)
    (MK.format(3115), "sfx/strike.mp3"),     # Fast transitions swoosh (strike-through)
    (MK.format(166), "sfx/ring.mp3"),        # Fast small sweep transition (red ring)
    ("https://assets.mixkit.co/music/480/480.mp3", "music/bed.mp3"),   # "Curiosity", instrumental
    ("https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx", "voice/kokoro-v1.0.onnx"),
    ("https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin", "voice/voices-v1.0.bin"),
]


def get(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return "have"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (explainer-reel kit)"})
            with urllib.request.urlopen(req, timeout=120) as r, open(dest + ".part", "wb") as f:
                while True:
                    b = r.read(1 << 20)
                    if not b: break
                    f.write(b)
            os.replace(dest + ".part", dest)
            return "got"
        except Exception as e:
            print("  retry", attempt + 1, os.path.basename(dest), e)
            time.sleep(2 + 3 * attempt)
    return "FAILED"


def main():
    bad = []
    for url, rel in FILES:
        r = get(url, os.path.join(A, rel))
        print(f"{r:6} {rel}")
        if r == "FAILED": bad.append(rel)
    wdir = os.path.join(A, "whisper")
    if not os.path.exists(os.path.join(wdir, "model.bin")):
        try:
            from faster_whisper import download_model
            download_model("base.en", output_dir=wdir)
            print("got    whisper/ (base.en)")
        except Exception as e:
            print("FAILED whisper:", e); bad.append("whisper")
    else:
        print("have   whisper/ (base.en)")
    if bad:
        sys.exit("missing: " + ", ".join(bad) + "  (check the internet connection and run this again)")
    print("assets ready")


if __name__ == "__main__":
    main()
````

<!-- FILE: kit/voice.py -->
````python
"""voice.py : story.json -> build/voice.wav + build/timing.json

    python kit/voice.py            (reads story.json in the project folder)

- Every beat's "say" line is read by Kokoro-82M (default voice: a 50/50 mix of am_liam and am_puck), on this computer's CPU.
- Silence at the start and end of each line is cut, then lines are joined with short, even gaps.
- faster-whisper listens to each line and gives every word a start and end time; the times are
  matched back to the script's own words, so captions show exactly what you wrote.
- The mouth track: each word is turned into phonemes (Kokoro's own phonemizer), each phoneme into a
  mouth shape, laid over the word's time span, and opened as wide as the voice is loud in that frame.
needs: pip install kokoro-onnx soundfile faster-whisper numpy imageio-ffmpeg"""
import difflib, json, os, re, subprocess, sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "assets")
B = os.path.join(ROOT, "build")
FPS = 30
SR = 24000


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def kokoro():
    from kokoro_onnx import Kokoro
    m = os.path.join(A, "voice", "kokoro-v1.0.onnx")
    v = os.path.join(A, "voice", "voices-v1.0.bin")
    if not (os.path.exists(m) and os.path.exists(v)):
        sys.exit("voice model missing: run  python kit/fetch_assets.py")
    return Kokoro(m, v)


def whisper():
    from faster_whisper import WhisperModel
    d = os.path.join(A, "whisper")
    return WhisperModel(d if os.path.exists(os.path.join(d, "model.bin")) else "base.en", device="cpu", compute_type="int8")


def norm(w): return re.sub(r"[^a-z0-9]", "", w.lower())


def trim(a, thr=0.012, keep=0.03):
    """cut silence at both ends of a line, keep a few ms so consonants aren't clipped"""
    loud = np.where(np.abs(a) > thr)[0]
    if not len(loud): return a
    s = max(0, loud[0] - int(keep * SR)); e = min(len(a), loud[-1] + int(keep * SR * 2))
    return a[s:e]


def squeeze(a, max_pause=0.3, thr=0.01):
    """shorten any pause inside a line to max_pause seconds (Kokoro sometimes holds a full stop for ~1 s)"""
    win = int(0.02 * SR); n = len(a) // win
    if n < 3: return a
    loud = np.array([np.abs(a[i * win:(i + 1) * win]).max() > thr for i in range(n)])
    keep, i = [], 0
    while i < n:
        if not loud[i]:
            j = i
            while j < n and not loud[j]: j += 1
            run = j - i
            if 0 < i and j < n and run * win > max_pause * SR:      # a pause in the middle of the line
                k = int(max_pause * SR / win); keep.append(a[i * win:(i + k // 2) * win]); keep.append(a[(j - (k - k // 2)) * win:j * win])
            else: keep.append(a[i * win:j * win])
            i = j
        else:
            keep.append(a[i * win:(i + 1) * win]); i += 1
    keep.append(a[n * win:])
    return np.concatenate(keep)


def to16k(a):
    n = int(len(a) * 16000 / SR)
    return np.interp(np.linspace(0, len(a) - 1, n), np.arange(len(a)), a).astype(np.float32)


def estimate(words, a):
    """fallback: word times in proportion to word length inside the voiced part"""
    loud = np.where(np.abs(a) > 0.02)[0]
    t0, t1 = (loud[0] / SR, loud[-1] / SR) if len(loud) else (0, len(a) / SR)
    k = [len(w) + 2 for w in words]; tot = sum(k); out, t = [], t0
    for n in k:
        d = (t1 - t0) * n / tot; out.append((t, t + d * 0.92)); t += d
    return out


def align(model, text, a):
    """word times from faster-whisper, matched back to the script's words (missing ones share the gaps)"""
    sw = text.split()
    x = to16k(a)

    def heard_with(prompt):
        segs, _ = model.transcribe(x, language="en", word_timestamps=True, beam_size=1, initial_prompt=prompt)
        return [(w.word, w.start, w.end) for s in segs for w in s.words]

    def score(heard):
        sm = difflib.SequenceMatcher(a=[norm(w) for w in sw], b=[norm(h[0]) for h in heard], autojunk=False)
        good, last = 0, -1.0
        for i, j, n in sm.get_matching_blocks():
            for k in range(n):
                s, e = heard[j + k][1], heard[j + k][2]
                if s > last + 0.01 and e - s > 0.02: good += 1
                last = max(last, s)
        return good
    try:
        best = None
        for prompt in (text, None):      # the prompt helps spelling, but sometimes makes whisper skip or stack words
            h = heard_with(prompt)
            if best is None or score(h) > score(best): best = h
            if score(best) >= len(sw) - 1: break
        heard = best
    except Exception as e:
        print("  word timing fell back to an estimate:", e)
        return estimate(sw, a)
    times = [None] * len(sw)
    sm = difflib.SequenceMatcher(a=[norm(w) for w in sw], b=[norm(h[0]) for h in heard], autojunk=False)
    for i, j, n in sm.get_matching_blocks():
        for k in range(n): times[i + k] = (heard[j + k][1], heard[j + k][2])
    if not any(times): return estimate(sw, a)
    end = len(a) / SR
    i = 0
    while i < len(sw):                    # unmatched words share the gap between their neighbours, by length
        if times[i] is None:
            j = i
            while j < len(sw) and times[j] is None: j += 1
            t0 = times[i - 1][1] if i > 0 else max(0.0, (times[j][0] if j < len(sw) else end) - 0.3 * (j - i))
            t1 = times[j][0] if j < len(sw) else min(end, t0 + 0.35 * (j - i))
            k = [len(w) + 2 for w in sw[i:j]]; tot = sum(k); t = t0
            for m, n in zip(range(i, j), k):
                d = (t1 - t0) * n / tot; times[m] = (t, t + d); t += d
            i = j
        else: i += 1
    for k in range(len(sw) - 1):          # a zero-length word stacked on the next: split the next word's span
        (s0, e0), (s1, e1) = times[k], times[k + 1]
        if s1 - s0 < 0.04 and e1 > s0 + 0.1:
            cut = s0 + (e1 - s0) * (len(sw[k]) + 1) / (len(sw[k]) + len(sw[k + 1]) + 2)
            times[k] = (s0, cut); times[k + 1] = (cut, e1)
    out, last = [], 0.0
    for (s, e) in times:                  # keep times rising and inside the line
        s = max(s, last); e = max(e, s + 0.05); out.append((s, min(e, end))); last = s + 0.02
    return out


# mouth shapes: 0 rest, 1 closed (m b p), 2 f/v, 3 round (o u w), 4 wide (a), 5 smile (e i), 6 mid (schwa), 7 teeth (t d s n l k ...)
SHAPE = {}
for ch in "mbp": SHAPE[ch] = 1
for ch in "fv": SHAPE[ch] = 2
for ch in "ouwʊɔɒ": SHAPE[ch] = 3
for ch in "aæɑʌɐ": SHAPE[ch] = 4
for ch in "eiɪɛj": SHAPE[ch] = 5
for ch in "əɚɜᵻ": SHAPE[ch] = 6
for ch in "tdnlszʃʒθðkɡgŋhɹrʧʤç": SHAPE[ch] = 7
VOWEL = set("ouʊɔɒaæɑʌɐeiɪɛəɚɜᵻ")


def phones(tok, word):
    try:
        p = tok.phonemize(word, "en-us")
    except Exception:
        p = word.lower()
    seq = []
    for ch in p:
        if ch in SHAPE:
            seq.append((SHAPE[ch], 1.4 if ch in VOWEL else (0.9 if SHAPE[ch] == 1 else 0.75)))
        elif ch == "ː" and seq:
            seq[-1] = (seq[-1][0], seq[-1][1] + 0.6)
    return seq or [(6, 1.0)]


def style(k, name):
    # a Kokoro voice name, or a mix like "am_liam+am_puck" (equal parts) or "am_liam:0.6+am_puck:0.4"
    if "+" not in name: return name
    parts = [(p.split(":")[0], float(p.split(":")[1]) if ":" in p else 1.0) for p in name.split("+")]
    total = sum(w for _, w in parts)
    return sum(k.get_voice_style(n) * (w / total) for n, w in parts)


def main():
    story = json.load(open(os.path.join(ROOT, "story.json"), encoding="utf-8"))
    voice, speed = story.get("voice", "am_liam+am_puck"), float(story.get("speed", 0.97))
    gap, step_gap = float(story.get("gap", 0.28)), float(story.get("step_gap", 0.45))
    os.makedirs(B, exist_ok=True)
    k = kokoro(); w = whisper(); tok = k.tokenizer
    pcm, lines, t = [np.zeros(int(0.05 * SR), np.float32)], [], 0.05
    for i, beat in enumerate(story["beats"]):
        text = beat["say"].strip()
        a, sr = k.create(text, voice=style(k, beat.get("voice", voice)), speed=float(beat.get("speed", speed)), lang="en-us")
        assert sr == SR, sr
        a = squeeze(trim(np.asarray(a, np.float32)), float(story.get("max_pause", 0.32)))
        if i > 0:
            g = step_gap if (beat.get("step") or beat.get("point")) else gap
            g += float(story["beats"][i - 1].get("pause", 0))
            pcm.append(np.zeros(int(g * SR), np.float32)); t += g
        times = align(w, text, a)
        words = [{"w": wd, "s": round(t + s, 3), "e": round(t + e, 3)} for wd, (s, e) in zip(text.split(), times)]
        lines.append({"i": i, "text": text, "start": round(t, 3), "end": round(t + len(a) / SR, 3), "words": words})
        pcm.append(a); t += len(a) / SR
        print(f"  line {i:2d}  {len(a)/SR:5.2f} s  {text[:60]}")
    tail = float(story.get("tail", 0.7))
    pcm.append(np.zeros(int(tail * SR), np.float32))
    v = np.concatenate(pcm)
    peak = float(np.abs(v).max()) or 1.0
    v = v / peak * 0.89
    import soundfile as sf
    sf.write(os.path.join(B, "voice.wav"), v, SR, subtype="PCM_16")
    dur = len(v) / SR
    # mouth track, one entry per video frame: [shape, openness 0..1]
    n = int(np.ceil(dur * FPS))
    hop = SR // FPS
    rms = np.array([np.sqrt(np.mean(v[i * hop:(i + 1) * hop] ** 2)) if i * hop < len(v) else 0 for i in range(n)])
    ref = np.percentile(rms[rms > 0.01], 92) if (rms > 0.01).any() else 1.0
    env = np.clip(rms / ref, 0, 1.15) ** 0.7
    shape = np.zeros(n, int)
    for ln in lines:
        for wd in ln["words"]:
            seq = phones(tok, wd["w"])
            tot = sum(x[1] for x in seq); s = wd["s"]
            for sh, wt in seq:
                d = (wd["e"] - wd["s"]) * wt / tot
                f0, f1 = int(round(s * FPS)), max(int(round(s * FPS)) + 1, int(round((s + d) * FPS)))
                if sh == 1: f1 = max(f1, f0 + 2)            # lips stay shut for at least 2 frames on m, b, p
                for f in range(f0, min(f1, n)):
                    shape[f] = sh
                s += d
    mouth = []
    sm = 0.0
    for f in range(n):
        o = env[f] if shape[f] != 0 else 0.0
        if shape[f] == 1: o = 0.0                      # lips meet on m, b, p
        sm = o if o > sm else sm * 0.45 + o * 0.55     # opens fast, closes a little softer
        mouth.append([int(shape[f]) if sm > 0.06 else 0, round(float(sm), 3)])
    words_all = sum(len(l["words"]) for l in lines)
    speech = lines[-1]["end"] - lines[0]["start"]
    timing = {"fps": FPS, "duration": round(dur, 3), "voice": voice, "engine": "kokoro", "speed": speed,
              "wpm": round(words_all / speech * 60), "lines": lines, "mouth": mouth}
    json.dump(timing, open(os.path.join(B, "timing.json"), "w", encoding="utf-8"))
    print(f"voice: {dur:.1f} s, {words_all} words, {timing['wpm']} words a minute -> build/voice.wav, build/timing.json")


if __name__ == "__main__":
    main()
````

<!-- FILE: kit/reel.html -->
````html
<!doctype html>
<html><head><meta charset="utf-8">
<!-- reel.html : the lecture-style explainer engine. It draws one frame for any time t: window.REEL.seek(t).
     Data: ../build/data.js (written by render.js from story.json + build/timing.json).
     Look: cream paper with grain, ink + red + grey, Anton titles with a red swash, Instrument Sans captions top left
     (grey turning ink, key words in red Instrument Serif italic), JetBrains Mono "// 01 · label" + stat, bordered cards
     with a halftone dot shadow, tilted red stamps, halftone dot wipes, and a big presenter bottom right.
     Every frame depends only on t: no Math.random, no Date, no CSS transitions. -->
<style>
@font-face{font-family:Anton;src:url(../assets/fonts/Anton-Regular.ttf)}
@font-face{font-family:ISans;src:url(../assets/fonts/InstrumentSans.ttf);font-weight:400 700}
@font-face{font-family:ISerif;src:url(../assets/fonts/InstrumentSerif-Italic.ttf);font-style:italic}
@font-face{font-family:JMono;src:url(../assets/fonts/JetBrainsMono.ttf);font-weight:100 800}
:root{ /* THEME */
  --paper:#EBE7E1; --ink:#1E1C1A; --red:#D7372C; --grey:#8A857E; --soft:#BDB7AE; --card:#F8F6F2; --line:#1E1C1A;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:var(--paper)}
#stage{position:absolute;inset:0;overflow:hidden;background:var(--paper);font-family:ISans;color:var(--ink)}
#grain{position:absolute;inset:0;opacity:.55;mix-blend-mode:multiply}
/* header */
#label{position:absolute;left:90px;top:132px;font:500 30px JMono;color:var(--grey);letter-spacing:.5px;white-space:nowrap}
#stat{position:absolute;right:90px;top:132px;font:500 30px JMono;color:var(--grey);letter-spacing:2px;text-transform:uppercase;white-space:nowrap}
#stat b{color:var(--red);font-weight:700;margin-left:12px}
/* captions */
#cap{position:absolute;left:90px;right:90px;top:252px;height:90px}
.chunk{position:absolute;left:0;top:0;width:900px;font:500 58px/1.16 ISans;letter-spacing:-.5px;visibility:hidden}
.chunk span{color:var(--soft)}
.chunk span.on{color:var(--ink)}
.chunk span.key{font:italic 64px/1.0 ISerif;letter-spacing:0}
.chunk span.key.on{color:var(--red)}
/* titles */
.title{position:absolute;left:60px;width:960px;top:470px;text-align:center;font-family:Anton;font-size:190px;line-height:1;letter-spacing:1px;text-transform:uppercase;white-space:nowrap}
.title .w{display:inline-block;position:relative;margin:0 .07em}
.title .r{color:var(--red)}
.title .plus{font-size:.72em;vertical-align:middle;margin:0 .08em;position:relative;top:-.08em}
.swash{position:absolute;left:-2%;width:104%;bottom:-34px;height:40px;overflow:visible}
/* cards */
.cardwrap{position:absolute;left:110px;width:860px}
.cshadow{position:absolute;left:-16px;top:16px;right:16px;bottom:-16px;border-radius:16px;background-image:radial-gradient(circle,var(--ink) 2.1px,transparent 2.6px);background-size:9px 9px}
.card{position:relative;width:100%;background:var(--card);border:3px solid var(--line);border-radius:16px;padding:30px 34px 34px}
.tab{font:500 26px JMono;color:var(--grey);margin-bottom:16px;letter-spacing:.5px}
.row{display:flex;align-items:center;gap:20px;font:500 46px JMono;color:var(--ink);padding:8px 14px;border-radius:10px;position:relative;white-space:nowrap;transform-origin:left center}
.row.hl{background:rgba(215,55,44,.10);color:var(--red)}
.ico{width:50px;height:44px;flex:none}
.code{font:500 42px/1.45 JMono;color:var(--ink);white-space:pre;position:relative;padding:2px 14px;border-radius:8px;transform-origin:left center}
.code .k{color:var(--red)} .code .g{color:var(--soft)} .code .h{color:var(--ink);font-weight:800} .code .n{color:var(--red)}
.msg{max-width:720px;padding:20px 28px;border-radius:22px;font:500 46px/1.25 ISans;margin:12px 0;position:relative;transform-origin:center}
.msg.you{margin-left:auto;background:var(--ink);color:#fff;border-bottom-right-radius:6px}
.msg.ai{background:#E6E2DB;color:var(--ink);border-bottom-left-radius:6px}
.strike{position:absolute;left:16px;right:16px;top:52%;height:5px;border-radius:3px;background:var(--red);transform-origin:left center;transform:scaleX(0)}
.term{font:500 44px/1.5 JMono;color:var(--ink);white-space:pre}
.term .p{color:var(--red)} .term .o{color:var(--grey)} .term .ok{color:var(--red)}
.num{font-family:Anton;color:var(--ink)}
.bignum{display:flex;align-items:flex-end;gap:22px}
.bignum .num{font-size:190px;line-height:1}
.unit{font:600 54px ISans;color:var(--ink);padding-bottom:20px}
.lbl{font:500 30px JMono;color:var(--grey);letter-spacing:1px;text-transform:uppercase;margin-bottom:14px}
.cmp{margin:14px 0 26px}
.cmp .top{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:12px}
.cmp .name{font:600 44px ISans;white-space:nowrap}
.cmp .val{display:flex;align-items:flex-end;gap:12px}
.cmp .val .num{font-size:84px;line-height:1}
.cmp .val small{font:500 36px JMono;color:var(--grey);padding-bottom:8px}
.cmp .bar{position:relative;height:40px;border:3px solid var(--line);border-radius:10px;overflow:hidden;background:#fff}
.cmp .bar i{display:block;height:100%;background:var(--ink);transform-origin:left;width:100%}
.cmp.b .bar i{background:var(--red)}
.cmp .note{position:absolute;left:12px;top:3px;height:28px;display:flex;align-items:center;font:600 22px JMono;color:#fff;background:var(--red);padding:0 10px;border-radius:6px}
.item{position:relative;display:flex;align-items:center;gap:24px;font:600 52px ISans;padding:12px 4px;color:var(--ink);transform-origin:left center}
.item .dot{width:58px;height:58px;border-radius:50%;border:3px solid var(--line);flex:none;position:relative;background:#fff}
.cols{display:flex;gap:24px}
.col2{flex:1;border:3px solid var(--line);border-radius:12px;padding:22px 22px;background:#fff;transform-origin:center}
.col2 h4{font:600 28px JMono;letter-spacing:1px;margin-bottom:12px;display:flex;align-items:center;gap:12px}
.col2 p{font:600 44px/1.25 ISans;margin:8px 0}
.xtra{margin-top:18px}
.cardwrap.nodots .cshadow{display:none}
.chipx{display:inline-flex;align-items:center;gap:12px;font:600 38px ISans;padding:12px 24px;border-radius:40px;border:3px solid var(--line);background:#fff}
.chipx.ok{background:var(--ink);color:#fff}
/* folder (payoff): small paper cards drop into a folder */
.folder{position:relative;height:380px}
.fback{position:absolute;left:70px;right:70px;top:80px;bottom:30px;background:#7FA6E0;border:3px solid var(--line);border-radius:14px}
.ftab{position:absolute;left:70px;top:52px;width:230px;height:46px;background:#7FA6E0;border:3px solid var(--line);border-bottom:none;border-radius:12px 12px 0 0}
.ffront{position:absolute;left:70px;right:70px;top:150px;bottom:30px;background:#8DB3EA;border:3px solid var(--line);border-radius:14px;display:flex;align-items:center;justify-content:center;font:700 48px ISans;color:#fff;z-index:3}
.paper{position:absolute;top:0;width:210px;height:150px;background:#fff;border:3px solid var(--line);border-radius:10px;z-index:2;padding:16px 14px;font:600 34px JMono;color:var(--ink)}
.paper i{display:block;height:10px;width:60%;background:var(--red);border-radius:5px;margin-bottom:12px}
.pill{position:absolute;left:0;right:0;margin:0 auto;width:max-content;bottom:-54px;background:var(--ink);color:#fff;font:600 28px JMono;letter-spacing:2px;padding:12px 26px;border-radius:30px;white-space:nowrap;z-index:4}
.pill b{color:#FF6A5E;margin-left:10px}
/* the black terminal bar under a card */
.tbar{position:absolute;left:110px;width:860px;height:84px;background:var(--ink);border-radius:12px;color:#F3F0EA;font:500 40px JMono;display:flex;align-items:center;padding:0 30px;white-space:pre}
.tbar .p{color:var(--red);margin-right:20px}
.tbar .caret{display:inline-block;width:22px;height:46px;background:var(--red);margin-left:6px}
/* badge, stamp, ring */
.badge{position:absolute;width:120px;height:120px;border-radius:50%;background:var(--red);color:#fff;display:flex;align-items:center;justify-content:center;font:64px Anton;border:3px solid var(--line)}
.stamp{position:absolute;max-width:640px;font:88px/1 Anton;color:var(--red);border:7px solid var(--red);border-radius:12px;padding:10px 26px 6px;text-transform:uppercase;letter-spacing:2px;white-space:nowrap;background:rgba(235,231,225,.55)}
.ring{position:absolute;overflow:visible;pointer-events:none}
/* halftone dot wipe */
#wipe{position:absolute;inset:0;pointer-events:none}
/* presenter */
#pres{position:absolute;left:440px;top:1290px;width:640px;height:660px}
#pres svg{width:100%;height:100%;overflow:visible}
</style></head>
<body><div id="stage">
<canvas id="grain" width="540" height="960"></canvas>
<div id="label"></div><div id="stat"></div>
<div id="cap"></div>
<div id="scenes"></div>
<div id="pres">
<svg viewBox="0 0 640 660">
 <defs>
  <pattern id="dots" width="11" height="11" patternUnits="userSpaceOnUse"><circle cx="5.5" cy="5.5" r="2.6" fill="#1E1C1A"/></pattern>
  <clipPath id="mclip"><path id="mclipPath" d=""/></clipPath>
 </defs>
 <g id="presAll" style="transform-origin:320px 660px">
 <!-- halftone shadow -->
 <g transform="translate(-26 12)" fill="url(#dots)">
  <path d="M60 680 C70 560 150 505 250 492 L390 492 C490 505 570 560 580 680 Z"/>
  <ellipse cx="320" cy="270" rx="168" ry="196"/>
 </g>
 <!-- body: mustard sweater, white tee collar -->
 <g id="body" stroke="#1E1C1A" stroke-width="6" stroke-linejoin="round">
  <path d="M60 680 C70 560 150 505 250 492 L390 492 C490 505 570 560 580 680 Z" fill="#D9A13B"/>
  <path d="M250 492 C270 540 370 540 390 492" fill="#F6F3EE"/>
  <path d="M236 496 C262 566 378 566 404 496" fill="none" stroke-width="10" stroke="#B8842B"/>
  <path d="M150 560 C160 600 170 640 172 680" fill="none" stroke-width="5"/><path d="M490 560 C480 600 470 640 468 680" fill="none" stroke-width="5"/>
 </g>
 <path d="M282 430 L282 500 C300 520 340 520 358 500 L358 430 Z" fill="#9C6744" stroke="#1E1C1A" stroke-width="6" stroke-linejoin="round"/>
 <g id="head" stroke="#1E1C1A" stroke-width="6" stroke-linejoin="round">
  <!-- hair back -->
  <g fill="#2A1D17">
   <circle cx="200" cy="170" r="62"/><circle cx="250" cy="118" r="66"/><circle cx="320" cy="100" r="70"/><circle cx="390" cy="118" r="66"/><circle cx="440" cy="170" r="62"/>
   <circle cx="186" cy="232" r="44"/><circle cx="454" cy="232" r="44"/>
  </g>
  <!-- face -->
  <path d="M190 250 C190 150 450 150 450 250 L450 300 C450 400 390 452 320 452 C250 452 190 400 190 300 Z" fill="#B27A55"/>
  <path d="M200 330 C214 410 270 444 320 444 C370 444 426 410 440 330 C424 398 372 428 320 428 C268 428 216 398 200 330 Z" fill="#9C6744" stroke="none"/>
  <!-- hair front (fringe curls) -->
  <g fill="#2A1D17">
   <circle cx="236" cy="176" r="36"/><circle cx="290" cy="158" r="38"/><circle cx="350" cy="158" r="38"/><circle cx="404" cy="176" r="36"/>
  </g>
  <!-- headphones: band + red cups -->
  <path d="M176 262 C150 70 490 70 464 262" fill="none" stroke="#1E1C1A" stroke-width="30" stroke-linecap="round"/>
  <path d="M176 262 C150 70 490 70 464 262" fill="none" stroke="#D7372C" stroke-width="16" stroke-linecap="round"/>
  <rect x="146" y="222" width="62" height="112" rx="26" fill="#D7372C"/><rect x="432" y="222" width="62" height="112" rx="26" fill="#D7372C"/>
  <rect x="162" y="244" width="22" height="68" rx="10" fill="#1E1C1A" stroke="none"/><rect x="456" y="244" width="22" height="68" rx="10" fill="#1E1C1A" stroke="none"/>
  <!-- brows -->
  <g id="brows" fill="#2A1D17" stroke="none"><path d="M236 232 C252 216 290 214 304 226 L300 240 C286 232 256 234 242 244 Z"/><path d="M404 232 C388 216 350 214 336 226 L340 240 C354 232 384 234 398 244 Z"/></g>
  <!-- eyes -->
  <g id="eyes">
   <ellipse cx="272" cy="284" rx="27" ry="30" fill="#fff"/><ellipse cx="368" cy="284" rx="27" ry="30" fill="#fff"/>
   <g id="pupils" stroke="none"><circle cx="274" cy="288" r="14" fill="#1E1C1A"/><circle cx="370" cy="288" r="14" fill="#1E1C1A"/><circle cx="279" cy="282" r="4.5" fill="#fff"/><circle cx="375" cy="282" r="4.5" fill="#fff"/></g>
   <rect id="lidL" x="240" y="250" width="64" height="70" fill="#B27A55" stroke="none" transform="scale(1,0)" style="transform-origin:272px 254px"/>
   <rect id="lidR" x="336" y="250" width="64" height="70" fill="#B27A55" stroke="none" transform="scale(1,0)" style="transform-origin:368px 254px"/>
   <ellipse cx="272" cy="284" rx="27" ry="30" fill="none"/><ellipse cx="368" cy="284" rx="27" ry="30" fill="none"/>
  </g>
  <path d="M318 300 C312 322 306 338 318 344 C324 346 332 344 336 340" fill="none" stroke-width="5"/>
  <ellipse cx="236" cy="352" rx="24" ry="13" fill="#E0806E" stroke="none" opacity=".55"/><ellipse cx="404" cy="352" rx="24" ry="13" fill="#E0806E" stroke="none" opacity=".55"/>
  <g id="mouth" transform="translate(320 382) scale(1.9) translate(-200 -262)" stroke-width="3.2">
   <path id="mFill" d="" fill="#4A1420"/>
   <g clip-path="url(#mclip)" stroke="none"><rect id="teeth" x="150" y="0" width="100" height="0" fill="#fff"/><ellipse id="tongue" cx="200" cy="300" rx="16" ry="9" fill="#E8697A"/></g>
   <path id="mLine" d="" fill="none" stroke="#1E1C1A" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
 </g>
 <!-- pointing hand (rises at each new point) -->
 <g id="handP" stroke="#1E1C1A" stroke-width="6" stroke-linejoin="round">
  <path d="M60 700 L60 560 C60 540 140 540 140 560 L140 700 Z" fill="#D9A13B"/>
  <rect x="56" y="520" width="88" height="40" rx="12" fill="#B8842B"/>
  <path d="M68 520 C60 470 66 440 84 432 L84 360 C84 340 112 340 112 360 L112 430 C130 426 146 440 144 462 L144 520 Z" fill="#B27A55"/>
  <path d="M112 440 L112 470 M126 444 L126 476" fill="none" stroke-width="4"/>
 </g>
 <!-- open hand (waves hello at the start and the end) -->
 <g id="handW" stroke="#1E1C1A" stroke-width="6" stroke-linejoin="round">
  <path d="M500 700 L500 560 C500 540 580 540 580 560 L580 700 Z" fill="#D9A13B"/>
  <rect x="496" y="520" width="88" height="40" rx="12" fill="#B8842B"/>
  <path d="M506 522 C498 470 500 440 512 430 L512 380 C512 362 536 362 536 380 L536 420 L538 350 C538 332 564 332 564 350 L564 420 L566 366 C566 348 590 348 590 366 L590 440 C604 420 628 430 620 452 L590 522 Z" fill="#B27A55"/>
 </g>
 </g>
</svg>
</div>
<svg id="wipe" viewBox="0 0 1080 1920"></svg>
</div>
<script src="../node_modules/gsap/dist/gsap.min.js"></script>
<script src="../build/data.js"></script>
<script>
window.REEL={ready:Promise.all(['100px Anton','500 100px ISans','italic 100px ISerif','500 100px JMono'].map(f=>document.fonts.load(f))).then(()=>document.fonts.ready).then(build)};
function build(){
const W=1080,H=1920,FPS=30;
const S=window.STORY, T=window.TIMING;
const $=s=>document.querySelector(s);
const el=(tag,cls,html)=>{const e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;return e;};
const norm=w=>String(w).toLowerCase().replace(/[^a-z0-9]/g,'');
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const EVENTS=[], NUMBERS=[], NUMNODES=[], WARN=[], VIS=[], FILL=[], COUNTS=[];
let CLONE=false;
const ev=(t,type,extra)=>{ if(!CLONE) EVENTS.push(Object.assign({t:+t.toFixed(3),type},extra||{})); };
gsap.defaults({immediateRender:false});
const tl=gsap.timeline({paused:true});
const inited=new Set();
function ft(target,from,to,pos){ if(!inited.has(target)){ inited.add(target); gsap.set(target,from); } return tl.fromTo(target,from,to,pos); }
const lines=T.lines, beats=S.beats, DUR=T.duration;
if(lines.length!==beats.length) WARN.push('timing has '+lines.length+' lines but story has '+beats.length+' beats: run voice.py again');
const bStart=i=>i===0?0:lines[i].start-0.06;
const bEnd=i=>i+1<beats.length?bStart(i+1):DUR;

/* grain: a fixed noise texture (seeded, so every frame is identical) */
{ const c=$('#grain'), g=c.getContext('2d'), im=g.createImageData(c.width,c.height); let r=12345;
  for(let k=0;k<im.data.length;k+=4){ r=(r*1103515245+12345)&0x7fffffff; const v=200+(r%56); im.data[k]=v; im.data[k+1]=v-3; im.data[k+2]=v-8; im.data[k+3]=255; }
  g.putImageData(im,0,0); c.style.width='1080px'; c.style.height='1920px'; }

/* a cue is a word of the beat's line ("hundred"), the n-th match ("hundred#2"), a fraction of the line (0.5) or nothing */
function cue(i,c,fallback){
  const L=lines[i]; if(!L) return 0;
  if(c===undefined||c===null) return fallback!==undefined?fallback:Math.max(0,L.start-0.05);
  if(typeof c==='number') return L.start+(L.end-L.start)*c;
  let [word,nth]=String(c).split('#'); nth=+(nth||1); const n=norm(word); let k=0;
  for(const w of L.words){ if(norm(w.w)===n||(n.length>2&&norm(w.w).startsWith(n))){ if(++k===nth) return Math.max(0,w.s-0.08);} }
  WARN.push('beat '+i+': cue "'+c+'" is not a word in: '+L.text); return L.start;
}
function appear(node,t,from,dur){ node._appear=t; ft(node,Object.assign({autoAlpha:0},from),{autoAlpha:1,x:0,y:0,scale:1,rotation:0,duration:dur||0.42,ease:'back.out(1.7)'},t); }
function regNum(value,t,beat,where,node){ NUMBERS.push({value:Number(value),t:+t.toFixed(3),beat,where}); NUMNODES.push(node||null); }
/* count-up: drawn per frame from t (deterministic) */
function countUp(node,value,t,dur,beat,where,regNode){ const fmt=v=>Math.round(v).toLocaleString('en-US'); if(CLONE){ node.textContent=fmt(value); return; } node.textContent=fmt(0);
  COUNTS.push({node,value:Number(value),t,dur:dur||0.9,fmt}); for(let k=0;k<6;k++) ev(t+k*(dur||0.9)*0.13,'tick',{vol:.45}); regNum(value,t,beat,where,regNode||node); }

/* ---------- titles: "CLAUDE + *VIDEO*" : starred word in red with a hand-drawn swash under it ---------- */
function titleNode(s){
  const d=el('div','title'); const words=String(s).trim().split(/\s+/);
  words.forEach(w=>{ if(w==='+'){ d.appendChild(el('span','w plus','+')); return; }
    const red=/^\*.*\*$/.test(w); const sp=el('span','w'+(red?' r':''),esc(w.replace(/\*/g,''))); d.appendChild(sp);
    if(red){ const sv=document.createElementNS('http://www.w3.org/2000/svg','svg'); sv.setAttribute('class','swash'); sv.setAttribute('viewBox','0 0 100 20'); sv.setAttribute('preserveAspectRatio','none');
      sv.innerHTML='<path d="M2 12 C 25 6, 60 5, 98 9" fill="none" stroke="#D7372C" stroke-width="3.2" stroke-linecap="round" vector-effect="non-scaling-stroke" style="stroke-width:9px"/>'; sp.appendChild(sv); sp._swash=sv.querySelector('path'); } });
  return d;
}
function fitTitle(node){ let fs=190; node.style.fontSize=fs+'px'; while(node.scrollWidth>node.clientWidth+2&&fs>90){fs-=6;node.style.fontSize=fs+'px';} if(node.scrollWidth>node.clientWidth+2) WARN.push('title too long: '+node.textContent); return fs; }

const IC={
 folder:'<svg class="ico" viewBox="0 0 50 44"><path d="M3 9a4 4 0 0 1 4-4h12l5 5h19a4 4 0 0 1 4 4v22a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4z" fill="#7FA6E0" stroke="#1E1C1A" stroke-width="3"/></svg>',
 file:'<svg class="ico" viewBox="0 0 50 44"><path d="M12 3h18l10 10v26a2 2 0 0 1-2 2H12a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z" fill="#fff" stroke="#1E1C1A" stroke-width="3"/><path d="M15 20h18M15 27h14" stroke="#D7372C" stroke-width="3"/></svg>',
 check:'<svg viewBox="0 0 34 34" style="width:34px;height:34px"><path d="M6 18l7 7L28 9" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 cross:'<svg viewBox="0 0 34 34" style="width:34px;height:34px"><path d="M9 9l16 16M25 9L9 25" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/></svg>'
};
function codeHTML(line){ const s=esc(line);
  if(/^---\s*$/.test(line)) return '<span class="g">'+s+'</span>';
  if(/^#/.test(line)) return '<span class="h">'+s+'</span>';
  const m=s.match(/^(\s*[\w-]+:)(.*)$/); if(m) return '<span class="k">'+m[1]+'</span>'+m[2];
  const n=s.match(/^(\s*[-*]|\s*\d+\.)(.*)$/); if(n) return '<span class="n">'+n[1]+'</span>'+n[2];
  return s; }

/* ---------- cards ---------- */
function buildCard(i,c,t0){
  const wrap=el('div','cardwrap'); wrap.appendChild(el('div','cshadow')); const card=el('div','card'); wrap.appendChild(card); if(c.tab) card.appendChild(el('div','tab',esc(c.tab)));
  const cues=c.cues||[]; const at=k=>cues[k]===undefined?t0+0.2+k*0.12:(cues[k]===null?t0:cue(i,cues[k]));
  const quiet=(node,t)=>{ node._appear=t; };
  if(c.type==='files'){
    (c.rows||[]).forEach((r,k)=>{ const [txt,lvl,kind]=r; const row=el('div','row'+(c.hl===k?' hl':''),IC[kind||(/\/$/.test(txt)?'folder':'file')]+'<span>'+esc(txt)+'</span>');
      row.style.marginLeft=(lvl||0)*52+'px'; card.appendChild(row); const t=at(k); if(t>t0+0.05){appear(row,t,{x:-40});ev(t,'card',{vol:.45});} else quiet(row,t0); });
  } else if(c.type==='code'){
    (c.lines||[]).forEach((ln,k)=>{ const row=el('div','code',codeHTML(ln)||'&nbsp;'); card.appendChild(row); const t=at(k); row._appear=t;
      if(t>t0+0.05){ const n=Math.max(1,ln.length); ft(row,{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:Math.min(0.9,0.035*n),ease:'steps('+n+')'},t); ev(t,'typing',{dur:Math.min(0.9,0.035*n)}); } });
  } else if(c.type==='chat'){
    (c.msgs||[]).forEach((m,k)=>{ const msg=el('div','msg '+(m.from==='ai'?'ai':'you'),esc(m.text)); msg.appendChild(el('i','strike')); card.appendChild(msg);
      const t=at(k); if(t>t0+0.05){appear(msg,t,{y:30,scale:.9});ev(t,'card',{vol:.55});} else quiet(msg,t0); });
  } else if(c.type==='terminal'){
    card.style.background='#1E1C1A'; card.querySelectorAll('.tab').forEach(x=>x.style.color='#8A857E');
    const cmd=el('div','term','<span class="p">$ </span><span class="c" style="color:#F3F0EA">'+esc(c.cmd||'')+'</span>'); card.appendChild(cmd);
    const t=at(0); cmd._appear=t; const cs=cmd.querySelector('.c'); const n=Math.max(1,(c.cmd||'').length);
    ft(cs,{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:0.045*n,ease:'steps('+n+')'},t); ev(t,'typing',{dur:0.045*n});
    (c.out||[]).forEach((o,k)=>{ const ok=/^✓|^ok:/i.test(o); const line=el('div','term','<span class="'+(ok?'ok':'o')+'" style="color:'+(ok?'#FF6A5E':'#B9B3AA')+'">'+esc(o.replace(/^ok:\s*/i,'✓ '))+'</span>'); card.appendChild(line);
      const tt=cues[k+1]!==undefined?cue(i,cues[k+1]):t+0.045*n+0.25+k*0.3; appear(line,tt,{y:14}); ev(tt,ok?'check':'card',{vol:ok?.55:.35}); });
  } else if(c.type==='counter'){
    if(c.label) card.appendChild(el('div','lbl',esc(c.label)));
    const big=el('div','bignum'); const n=el('span','num'); big.appendChild(n); if(c.unit) big.appendChild(el('div','unit',esc(c.unit))); card.appendChild(big);
    const t=c.at!==undefined?cue(i,c.at):t0+0.3; quiet(big,t0); countUp(n,c.value,t,0.9,i,'counter'); if(!CLONE) ft(n,{autoAlpha:0},{autoAlpha:1,duration:0.1},Math.max(0,t-0.02));   /* no stray 0 before the number is said */
  } else if(c.type==='compare'){
    const items=c.items||[]; const max=Math.max(...items.map(x=>x.value));
    items.forEach((it,k)=>{ const ib=it.beat!==undefined?it.beat:i; const row=el('div','cmp'+(k%2?' b':'')); const top=el('div','top'); top.appendChild(el('div','name',esc(it.label)));
      const val=el('div','val'); const n=el('span','num'); val.appendChild(n); if(it.unit) val.appendChild(el('small',null,esc(it.unit))); top.appendChild(val); row.appendChild(top);
      const bar=el('div','bar'); const fill=el('i'); bar.appendChild(fill); row.appendChild(bar); card.appendChild(row);
      row._appear=t0; if(it.show!==undefined){ const ts=cue(ib,it.show); row._appear=ts; if(ts>t0+0.05){ appear(row,ts,{x:-40}); ev(ts,'card',{vol:.45}); } }
      if(it.note){ const nt=el('span','note',esc(it.note)); bar.appendChild(nt); const tn=cue(ib,it.note_at); ft(nt,{autoAlpha:0,scale:.6},{autoAlpha:1,scale:1,duration:0.3,ease:'back.out(2.5)'},tn); ev(tn,'card',{vol:.45}); }
      const t=it.at!==undefined?cue(ib,it.at):at(k);
      ft(val,{autoAlpha:0},{autoAlpha:1,duration:0.15},t); countUp(n,it.value,t,0.9,ib,'compare',val);
      ft(fill,{scaleX:0},{scaleX:Math.max(0.012,it.value/max),duration:0.9,ease:'expo.out'},t); });
  } else if(c.type==='checklist'){
    (c.items||[]).forEach((it,k)=>{ const txt=typeof it==='string'?it:it.text; const bad=typeof it==='object'&&it.mark==='x';
      const row=el('div','item'); const dot=el('div','dot'); row.appendChild(dot); row.appendChild(el('span',null,esc(txt))); card.appendChild(row);
      const t=at(k); const late=t>t0+0.05; if(late) appear(row,Math.max(t0+0.05,t-0.25),{x:-30}); else quiet(row,t0); const mark=el('div',null,bad?IC.cross:IC.check);
      mark.style.cssText='position:absolute;inset:-3px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:3px solid #1E1C1A;background:'+(bad?'var(--ink)':'var(--red)');
      dot.appendChild(mark); if(late){ ft(mark,{autoAlpha:0,scale:0},{autoAlpha:1,scale:1,duration:0.35,ease:'back.out(3)'},t); ev(t,bad?'cross':'check',{vol:.6}); } });   /* null-cued rows are there from the first frame */
  } else if(c.type==='split'){
    const cols=el('div','cols');
    [['left','var(--ink)',IC.cross],['right','var(--red)',IC.check]].forEach(([side,col,ic],k)=>{ const d=c[side]||{}; const box=el('div','col2');
      box.appendChild(el('h4',null,'<span style="width:40px;height:40px;border-radius:50%;background:'+col+';display:inline-flex;align-items:center;justify-content:center">'+ic.replace('width:34px;height:34px','width:24px;height:24px')+'</span>'+esc(d.title||(k?'AFTER':'BEFORE'))));
      (d.lines||[]).forEach(l=>box.appendChild(el('p',null,esc(l)))); cols.appendChild(box); const t=at(k); box._appear=t; if(t>t0+0.05){appear(box,t,{y:40});ev(t,k?'check':'cross',{vol:.55});} });
    card.appendChild(cols);
  } else if(c.type==='folder'){
    card.style.background='transparent'; card.style.border='none'; card.style.padding='0'; wrap.classList.add('nodots');
    const f=el('div','folder'); f.appendChild(el('div','fback')); f.appendChild(el('div','ftab')); const front=el('div','ffront',esc(c.name||'folder')); f.appendChild(front);
    (c.items||[]).forEach((it,k)=>{ const p=el('div','paper','<i></i>'+esc(it)); const n=(c.items||[]).length; p.style.left=(430-95+(k-(n-1)/2)*170)+'px'; p.style.transform='rotate('+((k-(n-1)/2)*7)+'deg)'; f.appendChild(p);
      const t=at(k); p._appear=t; ft(p,{y:-420,autoAlpha:0,rotation:(k-1)*25},{y:40,autoAlpha:1,rotation:(k-(n-1)/2)*7,duration:0.55,ease:'back.out(1.4)'},t); ev(t,'card',{vol:.55}); });
    if(c.pill){ const pl=el('div','pill',esc(c.pill.label)+'<b></b>'); f.appendChild(pl); const tp=cue(i,c.pill.at); ft(pl,{autoAlpha:0,y:20},{autoAlpha:1,y:0,duration:0.3,ease:'back.out(2)'},tp-0.05); countUp(pl.querySelector('b'),c.pill.value,tp,0.8,i,'pill',pl); }
    card.appendChild(f);
  } else WARN.push('beat '+i+': unknown card type '+c.type);
  (c.extra||[]).forEach(x=>{ const xb=x.beat!==undefined?x.beat:i; const wrap=el('div','xtra'); let node;
    if(x.kind==='msg'){ node=el('div','msg '+(x.from==='ai'?'ai':'you'),esc(x.text)); }
    else node=el('div','chipx'+(x.ok?' ok':''),(x.ok?'✓ ':'')+esc(x.text));
    wrap.appendChild(node); card.appendChild(wrap); const tx=cue(xb,x.at); node._appear=tx; wrap._appear=tx; appear(wrap,tx,{y:30,scale:.9}); ev(tx,x.ok?'check':'card',{vol:.55}); });
  const mono=[...card.querySelectorAll('.code,.term,.row span')];
  if(mono.length){ const longest=Math.max(...mono.map(m=>m.textContent.length));
    const base=c.type==='files'?46:(c.type==='terminal'?44:42); const indent=c.type==='files'?Math.max(...(c.rows||[[0,0]]).map(r=>(r[1]||0)))*52+90:30;
    const fs=Math.max(30,Math.min(base,Math.floor((786-indent)/(0.6*longest))));
    card.querySelectorAll('.code,.term,.row').forEach(m=>m.style.fontSize=fs+'px');
    if(fs===30) WARN.push('beat '+i+': a line in the '+c.type+' card is too long ('+longest+' characters): shorten it'); }
  return wrap;
}

/* ---------- scenes ---------- */
const scenes=$('#scenes');
const CARDS={}, gaze=[], brows=[], nods=[], points=[], waves=[-0.6], LABELS=[], STATS=[]; let loopLand=null;
let lastTitle=null,lastCard=null,lastBar=null,lastStamp=null,pointNo=0,labelNo=0;
function hide(node,t,dy){ if(!node)return; tl.to(node,{autoAlpha:0,y:dy===undefined?-30:dy,duration:0.2,ease:'power2.in'},Math.max(0,t-0.2)); }
function hideNow(node,t){ if(!node)return; tl.set(node,{autoAlpha:0},t); }
function placeCard(card,top){ card.style.top=top+'px'; }
const ZONE=[690,1262];

/* the halftone dot wipe: dots grow from the centre out, cover, then shrink away */
const WIPES=[]; const wipeSvg=$('#wipe'); const DOTS=[]; { const step=60; for(let y=step/2;y<H;y+=step) for(let x=step/2;x<W;x+=step){ const c=document.createElementNS('http://www.w3.org/2000/svg','circle'); c.setAttribute('cx',x); c.setAttribute('cy',y); c.setAttribute('r',0); c.setAttribute('fill','#1E1C1A'); wipeSvg.appendChild(c); DOTS.push([c,Math.hypot(x-W/2,y-H*0.45)/1100]); } }
function drawWipe(t){ let r=null; for(const w0 of WIPES){ const d=t-w0; if(d>=-0.05&&d<0.65){ r=d; break; } }
  for(const [c,dist] of DOTS){ let v=0; if(r!==null){ const grow=Math.min(1,Math.max(0,(r+0.05-dist*0.18)/0.24)); const shrink=Math.min(1,Math.max(0,(r-0.32-dist*0.12)/0.22)); v=Math.max(0,grow-shrink); }
    c.setAttribute('r',(v*44).toFixed(1)); } }

beats.forEach((b,i)=>{
  const t0=bStart(i), isPoint=!!b.point&&i>0;
  const tc=isPoint?t0+0.18:t0;      /* scene swap happens under the dots */
  if(isPoint){ WIPES.push(t0-0.12); ev(t0-0.12,'wipe',{vol:.75}); points.push(tc+0.3); }
  if(b.label!==undefined){ labelNo++; const txt='// '+String(b.no||labelNo).padStart(2,'0')+' · '+b.label; LABELS.push([i===0?0:tc,txt]); if(!b.stat&&i>0&&!b.loop) STATS.push([tc,'',null,0]); }   /* a new section without a stat clears the old one */
  if(b.stat){ const st=b.stat; const ts=st.at!==undefined?cue(i,st.at):tc; const v=st.value!==undefined?Number(st.value):null;
    const start=i===0?0:tc; const instant=i===0&&ts<0.8;
    STATS.push([start,st.label||'',v,instant?0:ts]);
    if(v!==null){ regNum(v,instant?0:ts,i,'stat',$('#stat')); if(!instant) for(let k=0;k<4;k++) ev(ts+k*0.08,'tick',{vol:.35}); } }
  /* loop: the last beat brings back beat 0's scene at its landing word */
  if(b.loop){ const land=b.loopAt!==undefined?cue(i,b.loopAt):Math.max(t0,DUR-1.2);
    if(b.card){ /* the loop line can have its own short scene first */ if(lastCard) hide(lastCard,tc); if(lastBar) hide(lastBar,tc); if(lastStamp) hide(lastStamp,tc); lastBar=null; lastStamp=null;
      const lc=buildCard(i,b.card,tc+0.12); scenes.appendChild(lc); const lh=lc.offsetHeight; placeCard(lc,Math.round(ZONE[0]+Math.max(0,(ZONE[1]-ZONE[0]-lh)/2)));
      ft(lc,{autoAlpha:0,y:70,scale:.96},{autoAlpha:1,y:0,scale:1,duration:0.5,ease:'back.out(1.4)'},tc+0.12); ev(tc+0.12,'card',{vol:.6}); lastCard=lc; CARDS[i]=lc; }
    const b0=beats[0];
    const tt=b.title?titleNode(b.title):null; if(tt){ scenes.appendChild(tt); fitTitle(tt); hide(lastTitle,tc); if(!b.card){ hide(lastCard,tc); hide(lastBar,tc); if(lastStamp) hide(lastStamp,tc); }
      lastTitle=tt; slamTitle(tt,tc+0.02,i); }
    const t2=titleNode(b0.title||''); scenes.appendChild(t2); fitTitle(t2); hide(lastTitle,land); if(lastCard) hide(lastCard,land); if(lastBar) hide(lastBar,land); if(lastStamp) hide(lastStamp,land);
    ft(t2,{autoAlpha:0,y:40},{autoAlpha:1,y:0,duration:0.35,ease:'back.out(1.6)'},land); t2.querySelectorAll('.swash path').forEach(p=>{ p.style.strokeDasharray='1'; p.setAttribute('pathLength','1'); });
    if(b0.card){ const c0=JSON.parse(JSON.stringify(b0.card)); const cued=(c0.cues||[]).map(x=>x!==null&&x!==undefined); c0.cues=(c0.cues||[]).map(()=>null); const xcued=(c0.extra||[]).length; delete c0.extra; CLONE=true; const card=buildCard(0,c0,0); CLONE=false; scenes.appendChild(card);
      { const sel={files:'.row',chat:'.msg',code:'.code',checklist:'.item',split:'.col2',folder:'.paper',terminal:'.term'}[c0.type]; const items=sel?[...card.querySelectorAll(sel)]:[]; items.forEach((n,k)=>{ if(cued[k]) n.style.visibility='hidden'; });
        for(let k=0;k<xcued;k++){ const ph=el('div','xtra','<div class="chipx">&nbsp;</div>'); ph.style.visibility='hidden'; card.querySelector('.card').appendChild(ph); } } const h=card.offsetHeight; placeCard(card,Math.round(ZONE[0]+Math.max(0,(ZONE[1]-ZONE[0]-h)/2)));
      card.querySelectorAll('*').forEach(n=>{ inited.delete(n); }); gsap.set(card.querySelectorAll('.row,.msg,.code,.item,.cmp,.col2,.paper,.term'),{autoAlpha:1,x:0,y:0,clipPath:'none'});
      ft(card,{autoAlpha:0,y:50},{autoAlpha:1,y:0,duration:0.4,ease:'back.out(1.5)'},land+0.05); }
    if(b0.label!==undefined) LABELS.push([land,'// '+String(b0.no||1).padStart(2,'0')+' · '+b0.label]);
    STATS.push(b0.stat?[land,b0.stat.label||'',b0.stat.value!==undefined&&cue(0,b0.stat.at)<0.8?Number(b0.stat.value):null,0]:[land,'',null,0]);
    ev(land,'wipe',{vol:.5}); loopLand=land; return; }
  /* title */
  if(b.title){ hide(lastTitle,tc,isPoint?0:-30); const tt=titleNode(b.title); scenes.appendChild(tt); fitTitle(tt); lastTitle=tt; const ta=i===0?0:tc+0.02; slamTitle(tt,ta,i);
    const dig=String(b.title).replace(/,/g,'').match(/\d+/g); if(dig) dig.forEach(d=>regNum(+d,ta,i,'title',tt)); }
  /* card */
  if(b.card){ if(lastCard) (isPoint?hideNow(lastCard,tc):hide(lastCard,t0+0.05)); if(lastBar) (isPoint?hideNow(lastBar,tc):hide(lastBar,t0+0.05)); if(lastStamp){ (isPoint?hideNow(lastStamp,tc):hide(lastStamp,t0+0.05)); lastStamp=null; } lastBar=null;
    const ca=i===0?0:tc+0.12; const card=buildCard(i,b.card,ca); scenes.appendChild(card); CARDS[i]=card;
    const barH=b.term?114:0; const h=card.offsetHeight; if(h+barH>ZONE[1]-ZONE[0]) WARN.push('beat '+i+': card is '+(h+barH)+' px tall, only '+(ZONE[1]-ZONE[0])+' fit: cut rows or text');
    const top=Math.round(ZONE[0]+Math.max(0,(ZONE[1]-ZONE[0]-h-barH)/2)); placeCard(card,top);
    if(i>0){ ft(card,{autoAlpha:0,y:70,scale:.96},{autoAlpha:1,y:0,scale:1,duration:0.5,ease:'back.out(1.4)'},ca); ev(ca,'card',{vol:.65}); }
    lastCard=card; gaze.push([ca,-9,-6,1.0]);
    const ts=[...card.querySelectorAll('.row,.code,.msg,.item,.cmp,.term,.col2,.xtra,.paper,.bignum')].map(n=>n._appear===undefined?ca:n._appear); FILL.push([i,+Math.max(0,(ts.length?Math.min(...ts):ca)-ca).toFixed(2)]);
    if(isPoint){ pointNo=b.point; const bd=el('div','badge','#'+b.point); bd.style.left=(110+860-150)+'px'; bd.style.top=(top-56)+'px'; scenes.appendChild(bd);
      ft(bd,{autoAlpha:0,scale:0,rotation:-30},{autoAlpha:1,scale:1,rotation:8,duration:0.45,ease:'back.out(2.5)'},ca); ev(ca+0.1,'badge',{vol:.5}); hide(bd,bEndScene(i)); regNum(b.point,ca,i,'badge',bd); }
    if(b.term){ const bar=el('div','tbar','<span class="p">$</span><span class="c"></span><span class="caret"></span>'); bar.style.top=(top+h+30)+'px'; scenes.appendChild(bar); lastBar=bar;
      const cmd=b.term.cmd||''; const tb=b.term.at!==undefined?cue(i,b.term.at):ca+0.4; bar.querySelector('.c').textContent=cmd; bar._appear=tb; const n=Math.max(1,cmd.length);
      bar.style.fontSize=Math.max(26,Math.min(40,Math.floor(740/(0.6*(cmd.length+2)))))+'px'; if(cmd.length>40) WARN.push('beat '+i+': terminal command is long ('+cmd.length+' characters): shorten it');
      ft(bar,{autoAlpha:0,y:20},{autoAlpha:1,y:0,duration:0.25},ca+0.15); ft(bar.querySelector('.c'),{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:Math.min(1.4,0.05*n),ease:'steps('+n+')'},tb); ev(tb,'typing',{dur:Math.min(1.4,0.05*n)}); VIS.push(tb); }
  } else if(b.focus && lastCard){ const rows=lastCard.querySelectorAll('.row,.code,.msg,.item,.cmp'); const r=rows[b.focus[0]];
    if(r){ const t=cue(i,b.focus[1]); ft(r,{backgroundColor:'rgba(215,55,44,0)'},{backgroundColor:'rgba(215,55,44,0.14)',duration:0.25},t); ev(t,'card',{vol:.45}); gaze.push([t,-9,-6,0.8]); } }
  /* strike-through on a row of the card on screen */
  if(b.strike && lastCard){ const rows=lastCard.querySelectorAll('.msg,.row,.code,.item'); const r=rows[b.strike[0]];
    if(r){ let s=r.querySelector('.strike'); if(!s){ s=el('i','strike'); r.appendChild(s); } const t=cue(i,b.strike[1]); ft(s,{scaleX:0},{scaleX:1,duration:0.3,ease:'power2.out'},t); ev(t,'strike',{vol:.6}); VIS.push(t); } }
  /* red ring around a row (or the pill) */
  if(b.ring && lastCard){ const t=cue(i,b.ring[1]); const target=b.ring[0]==='pill'?lastCard.querySelector('.pill'):lastCard.querySelectorAll('.msg,.row,.code,.item,.cmp,.paper')[b.ring[0]];
    if(target){ const r=layoutRect(target); const sv=document.createElementNS('http://www.w3.org/2000/svg','svg'); sv.setAttribute('class','ring');
      const pad=26; sv.style.left=(r.left-pad)+'px'; sv.style.top=(r.top-pad)+'px'; sv.setAttribute('width',r.width+2*pad); sv.setAttribute('height',r.height+2*pad);
      const w=r.width+2*pad, hh=r.height+2*pad; sv.innerHTML='<path pathLength="1" d="M'+(w*0.08)+' '+(hh*0.62)+' C '+(w*0.02)+' '+(hh*0.1)+', '+(w*0.98)+' '+(hh*-0.05)+', '+(w*0.97)+' '+(hh*0.5)+' S '+(w*0.1)+' '+(hh*1.05)+', '+(w*0.16)+' '+(hh*0.3)+'" fill="none" stroke="#D7372C" stroke-width="7" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1"/>';
      scenes.appendChild(sv); const pth=sv.querySelector('path'); ft(pth,{strokeDashoffset:1},{strokeDashoffset:0,duration:0.45,ease:'power2.inOut'},t); ft(sv,{autoAlpha:0},{autoAlpha:1,duration:0.05},t); hide(sv,bEndScene(i),0); ev(t,'ring',{vol:.5}); VIS.push(t); } }
  /* stamp */
  if(b.stamp && lastCard){ const t=cue(i,b.stamp.at); const s=el('div','stamp',esc(b.stamp.text)); scenes.appendChild(s);
    const cardBottom=parseInt(lastCard.style.top)+lastCard.offsetHeight; const top=Math.min(1170,cardBottom-(lastBar?70:22)); s.style.top=top+'px';   /* over the card's lower edge, clear of the terminal bar and the presenter */ s.style.right=(b.stamp.left?'auto':'150px'); if(b.stamp.left) s.style.left='70px';
    ft(s,{autoAlpha:0,scale:1.9,rotation:-14},{autoAlpha:1,scale:1,rotation:-6,duration:0.28,ease:'power4.in'},t); ev(t+0.26,'stamp',{vol:.8}); nods.push(t+0.26); lastStamp=s; hide(s,bEndScene(i),0); }
  /* the presenter points at each new point, and looks at what lands */
  if(b.card&&!isPoint&&i>0) points.push(tc+0.25);
  lines[i].words.forEach(w=>{ if(/\d/.test(w.w)||/^(one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|million|percent)$/i.test(norm(w.w))) brows.push(w.s); });
});
function layoutRect(node){ let x=0,y=0,n=node; while(n&&n.id!=='stage'){ x+=n.offsetLeft; y+=n.offsetTop; n=n.offsetParent; } return {left:x,top:y,width:node.offsetWidth,height:node.offsetHeight}; }
function bEndScene(i){ for(let j=i+1;j<beats.length;j++){ const b=beats[j]; if(b.card||b.title||b.loop) return bStart(j)+(b.point?0.18:0.05); } return DUR+1; }

/* auto-pulse: a spoken word that is written on a visible row makes that row pulse */
const STOP=new Set('this that with your from into what when then them they have just only about will make made like each every'.split(' '));
{ let cur=null; lines.forEach((L,i)=>{ const b=beats[i]; if(b.card) cur=i; if(b.loop) cur=null; const card=cur!==null?CARDS[cur]:null; if(!card||S.pulse===false) return;
  const rows=[...card.querySelectorAll('.row,.code,.item,.cmp,.msg,.chipx,.col2')]; const last={};
  L.words.forEach(w=>{ const n=norm(w.w); if(n.length<4||STOP.has(n)) return;
    rows.forEach((r,k)=>{ if(!norm(r.textContent).includes(n)) return; if((last[k]||-9)>w.s-1.0) return; if(r._appear!==undefined&&(Math.abs(r._appear-w.s)<0.7||r._appear>w.s)) return; last[k]=w.s;
      tl.fromTo(r,{scale:1},{scale:1.035,duration:0.14,yoyo:true,repeat:1,ease:'power2.out',immediateRender:false},w.s-0.05); VIS.push(+(w.s-0.05).toFixed(3)); }); }); }); }
tl.set({},{},DUR);

function slamTitle(tt,ta,i){ const ws=[...tt.querySelectorAll('.w')];
  if(i===0&&ta===0){ ws.forEach(w=>{ if(w._swash){ w._swash.setAttribute('pathLength','1'); w._swash.style.strokeDasharray='1'; w._swash.style.strokeDashoffset='0'; } }); return; }
  ws.forEach((w,k)=>{ ft(w,{autoAlpha:0,scale:1.6,y:-20},{autoAlpha:1,scale:1,y:0,duration:0.26,ease:'power4.in'},ta+k*0.09);
    if(w._swash){ w._swash.setAttribute('pathLength','1'); w._swash.style.strokeDasharray='1'; ft(w._swash,{strokeDashoffset:1},{strokeDashoffset:0,duration:0.35,ease:'power2.out'},ta+0.3+k*0.09); } });
  ev(ta+0.2,'title',{vol:.7}); nods.push(ta+0.25); gaze.push([ta,-9,-8,0.8]); }

/* ---------- captions: phrases by meaning, words go from grey to ink as they're said, key words in red serif italic ---------- */
const NUMW={zero:0,one:1,two:2,three:3,four:4,five:5,six:6,seven:7,eight:8,nine:9,ten:10,eleven:11,twelve:12,thirteen:13,fourteen:14,fifteen:15,sixteen:16,seventeen:17,eighteen:18,nineteen:19,twenty:20,thirty:30,forty:40,fifty:50,sixty:60,seventy:70,eighty:80,ninety:90};
const SCL={hundred:100,thousand:1000,million:1e6,billion:1e9};
function capTokens(ws){
  const map=Object.entries(S.captions||{}).map(([k,v])=>[k.split(/\s+/).map(norm),v]).sort((a,b)=>b[0].length-a[0].length);
  let out=[];
  for(let k=0;k<ws.length;){ let hit=null;
    for(const [key,val] of map){ if(k+key.length<=ws.length&&key.every((x,j)=>norm(ws[k+j].w)===x&&ws[k+j].line===ws[k].line)){ hit=[key.length,val]; break; } }
    if(hit){ const last=ws[k+hit[0]-1]; out.push(Object.assign({},ws[k],{w:hit[1]+(last.w.match(/[.,!?:;]+$/)||[''])[0],e:last.e,mapped:1})); k+=hit[0]; } else { out.push(ws[k]); k++; } }
  const res=[];
  for(let k=0;k<out.length;){ const c=norm(out[k].w);
    if(NUMW[c]!==undefined){ let total=0,curv=0,j=k,used=k;
      while(j<out.length&&out[j].line===out[k].line){ const n=norm(out[j].w);
        if(NUMW[n]!==undefined){ curv+=NUMW[n]; } else if(n==='hundred'){ curv=Math.max(curv,1)*100; } else if(SCL[n]){ total+=Math.max(curv,1)*SCL[n]; curv=0; }
        else if(n==='and'&&j>k&&j+1<out.length&&NUMW[norm(out[j+1].w)]!==undefined){ } else break;
        used=j; j++; if(/[.,!?:;]$/.test(out[used].w)) break; }
      const v=total+curv; if(v>=10){ const last=out[used]; res.push(Object.assign({},out[k],{w:v.toLocaleString('en-US')+(last.w.match(/[.,!?:;]+$/)||[''])[0],e:last.e,num:1})); k=used+1; continue; } }
    res.push(out[k]); k++; }
  return res;
}
const KEYS=new Set((S.keys||[]).map(norm)); beats.forEach(b=>(b.keys||[]).forEach(k=>KEYS.add(norm(k))));
const words=capTokens((()=>{const a=[];lines.forEach(L=>L.words.forEach(w=>a.push(Object.assign({line:L.i},w))));return a;})());
/* chunks by meaning: break at sentence and clause ends, keep 2 to 7 words, never leave one word alone */
const chunks=[]; { let cur=[]; words.forEach((w,k)=>{ cur.push(w); const next=words[k+1]; const lineEnd=!next||next.line!==w.line; const txt=cur.map(x=>x.w).join(' ');
  const left=lineEnd?0:words.slice(k+1).filter(x=>x.line===w.line).length;
  const nextLen=next?next.w.length+1:0;
  let brk=lineEnd||/[.!?:]$/.test(w.w)||(/[,;]$/.test(w.w)&&cur.length>=2)||cur.length>=5||txt.length+nextLen>27;
  if(brk&&!lineEnd&&(left===1||cur.length===1)) brk=false;
  if(brk){ chunks.push(cur); cur=[]; } }); }
const cap=$('#cap');
const chunkEls=chunks.map((ch,j)=>{ const d=el('div','chunk'); const hasKey=ch.some(w=>KEYS.has(norm(w.w)));
  let keyIdx=-1; if(hasKey) keyIdx=ch.findIndex(w=>KEYS.has(norm(w.w))); else { const cand=ch.map((w,ii)=>[w.mapped||w.num?100:norm(w.w).length,ii]).filter(x=>x[0]>=6).sort((a,b)=>b[0]-a[0]); keyIdx=cand.length?cand[0][1]:-1; }
  ch.forEach((w,ii)=>{ const s=el('span',ii===keyIdx?'key':null,esc(w.w)); d.appendChild(s); d.appendChild(document.createTextNode(' ')); }); cap.appendChild(d); return d; });
chunkEls.forEach(d=>{ d.style.visibility='hidden'; d.style.whiteSpace='nowrap'; if(d.scrollWidth>900) WARN.push('caption wider than one line: '+d.textContent); });
function drawCaptions(t){
  let k=-1; for(let j=0;j<chunks.length;j++){ const c=chunks[j]; const end=j+1<chunks.length?chunks[j+1][0].s-0.04:DUR+1; if((t>=c[0].s-0.12||j===0)&&t<end){k=j;break;} }
  chunkEls.forEach((d,j)=>d.style.visibility=j===k?'visible':'hidden');
  if(k<0) return; const c=chunks[k]; const sp=chunkEls[k].querySelectorAll('span');
  c.forEach((w,j)=>{ sp[j].classList.toggle('on',t>=w.s+0.03); });
}

/* ---------- presenter (drawn per frame) ---------- */
const SH=[[40,0,5,0,0],[38,0,2,0,0],[42,9,0,1,0],[24,22,0,0,1],[46,30,0,0,0],[52,14,0,1,0],[40,18,0,0,0],[44,11,0,1,0]];
function mouthPath(f){
  const m=T.mouth[Math.min(T.mouth.length-1,Math.max(0,f))]||[0,0]; const p=T.mouth[Math.max(0,f-1)]||m;
  const a=SH[m[0]], b=SH[p[0]]; const mix=(u,v)=>u*0.7+v*0.3;
  const open=m[1]; const w=mix(a[0],b[0]); const h=(m[0]===0||m[0]===1)?0:mix(a[1],b[1])*(0.35+0.65*Math.min(1,open)); const sm=mix(a[2],b[2]);
  const cx=200, cy=262, L=cx-w/2, R=cx+w/2, rnd=a[4];
  if(h<2.5){ const d='M'+L+' '+(cy-sm)+' Q'+cx+' '+(cy+sm*1.2+(m[0]===1?1:0))+' '+R+' '+(cy-sm); return {fill:'',line:d,clip:'M0 0',teeth:0,tongue:0,h:0}; }
  const top=cy-h*0.28, bot=cy+h*0.9, k=rnd?0.55:0.35;
  const d='M'+L+' '+(cy-sm)+' C'+(L+w*k*0.5)+' '+top+' '+(R-w*k*0.5)+' '+top+' '+R+' '+(cy-sm)+' C'+(R-w*0.1)+' '+bot+' '+(L+w*0.1)+' '+bot+' '+L+' '+(cy-sm)+'Z';
  return {fill:d,line:d,clip:d,teeth:a[3]?Math.min(9,h*0.42):Math.min(5,h*0.2),tongue:h>15?1:0,h,top,bot};
}
let rng=7; const rand=()=>{rng=(rng*16807)%2147483647;return rng/2147483647;};
const blinks=[]; for(let t=1.6;t<DUR+5;){ blinks.push(t); t+=2.4+rand()*2.2; }
const ease=x=>x<0?0:x>1?1:x*x*(3-2*x);
function handLift(list,t,hold){ let v=0; for(const p of list){ const d=t-p; if(d>=0&&d<hold+0.5){ v=Math.max(v,Math.min(ease(d/0.22),ease((hold+0.5-d)/0.3))); } } return v; }
function drawPresenter(t){
  const f=Math.round(t*FPS); const mp=mouthPath(f); const o=(T.mouth[f]||[0,0])[1];
  $('#mFill').setAttribute('d',mp.fill); $('#mLine').setAttribute('d',mp.line); $('#mclipPath').setAttribute('d',mp.clip||'M0 0');
  const th=$('#teeth'); th.setAttribute('y',mp.top||0); th.setAttribute('height',mp.teeth||0);
  const tg=$('#tongue'); tg.setAttribute('cy',(mp.bot||262)-4); tg.setAttribute('opacity',mp.tongue);
  const o2=(T.mouth[Math.max(0,f-3)]||[0,0])[1];
  let nod=0; for(const n of nods){ const d=t-n; if(d>=0&&d<0.45) nod=Math.max(nod,Math.sin(d/0.45*Math.PI)); }
  const rot=1.4*Math.sin(t*1.2)+0.7*Math.sin(t*2.7+1)+(o-o2)*3;
  $('#head').setAttribute('transform','rotate('+rot.toFixed(2)+' 320 470) translate(0 '+(-4*o+8*nod).toFixed(2)+')');
  $('#presAll').style.transform='translateY('+(2*Math.sin(t*1.9)).toFixed(2)+'px)';
  let lid=0; for(const b of blinks){ const d=t-b; if(d>=0&&d<0.16){ lid=d<0.07?d/0.07:1-(d-0.07)/0.09; break; } }
  $('#lidL').setAttribute('transform','scale(1,'+lid.toFixed(2)+')'); $('#lidR').setAttribute('transform','scale(1,'+lid.toFixed(2)+')');
  let gx=0,gy=0; for(const [g0,dx,dy,dur] of gaze){ const d=t-g0; if(d>=0&&d<dur){ const e=Math.min(1,d/0.12)*Math.min(1,(dur-d)/0.2); gx=dx*e; gy=dy*e; } }
  $('#pupils').setAttribute('transform','translate('+gx.toFixed(2)+' '+gy.toFixed(2)+')');
  let br=nod; for(const b of brows){ const d=t-b; if(d>=-0.05&&d<0.45) br=Math.max(br,Math.sin(Math.min(1,(d+0.05)/0.5)*Math.PI)); }
  $('#brows').setAttribute('transform','translate(0 '+(-9*br).toFixed(2)+')');
  const pu=handLift(points,t,1.1); $('#handP').setAttribute('transform','translate(0 '+((1-pu)*300).toFixed(1)+') rotate('+(-6*pu).toFixed(2)+' 100 600)');
  const wv=Math.max(handLift(waves,t,2.0), loopLand!==null&&t>=loopLand?ease((t-loopLand)/0.22):0);   /* the loop's wave stays up so the last frame matches frame 0 */ const wig=Math.sin(t*9)*6*wv; $('#handW').setAttribute('transform','translate(0 '+((1-wv)*300).toFixed(1)+') rotate('+wig.toFixed(2)+' 540 600)');
}
function drawCounts(t){ for(const c of COUNTS){ const node=c.node||document.querySelector(c.sel); if(!node) continue; if(c.from!==undefined&&t<c.from) continue; if(c.until!==undefined&&t>=c.until) continue;
  const p=Math.min(1,Math.max(0,(t-c.t)/c.dur)); const e=1-Math.pow(1-p,3); node.textContent=c.fmt(c.value*e); } }
function drawHeader(t){ let lab=''; for(const [a,txt] of LABELS) if(t>=a) lab=txt; const L=$('#label'); if(L.textContent!==lab) L.textContent=lab;
  let cur=null; for(const s of STATS) if(t>=s[0]) cur=s; const S2=$('#stat');
  if(!cur){ S2.innerHTML=''; return; } const [a,label,v,ts]=cur; let val='';
  if(v!==null&&t>=ts){ const p=ts===0?1:Math.min(1,Math.max(0,(t-ts)/0.6)); val=Math.round(v*(1-Math.pow(1-p,3))).toLocaleString('en-US'); }
  const html=esc(label)+'<b>'+val+'</b>'; if(S2.innerHTML!==html) S2.innerHTML=html; }
function seek(t){ t=Math.max(0,Math.min(DUR,t)); tl.seek(t,false); drawCounts(t); drawHeader(t); drawWipe(t); drawPresenter(t); drawCaptions(t); }

seek(0);
function shown(node){ for(let n=node;n&&n!==document.body;n=n.parentElement){ const cs=getComputedStyle(n); if(cs.visibility==='hidden'||+cs.opacity<0.6||cs.display==='none') return false; } return true; }
function holds(){ return NUMBERS.map((x,k)=>{ const node=NUMNODES[k]; if(!node) return null; let last=null; for(let t=Math.max(0,x.t);t<=Math.min(DUR,x.t+8);t+=0.1){ seek(t); if(shown(node)) last=t; else if(last!==null) break; } return last===null?null:+last.toFixed(2); }); }
Object.assign(window.REEL,{seek,duration:DUR,holds});
if(location.hash==='#play'){ const s0=performance.now(); const loop=()=>{ seek(((performance.now()-s0)/1000)%DUR); requestAnimationFrame(loop); }; loop(); }
/* the presenter's gestures are motion too: a wave keeps moving, a point lands */
waves.forEach(w=>{ for(let k=0;k<=2.0;k+=0.9) if(w+k>=0) VIS.push(+(w+k).toFixed(3)); }); if(loopLand!==null) for(let k=loopLand;k<DUR;k+=0.9) VIS.push(+k.toFixed(3)); points.forEach(p=>VIS.push(+p.toFixed(3)));
const visuals=[...EVENTS.map(e=>e.t),...VIS].sort((a,b)=>a-b);
return {duration:DUR,events:EVENTS.sort((a,b)=>a.t-b.t),numbers:NUMBERS,warnings:WARN,visuals,fill:FILL,layouts:[]};
}
</script>
</body></html>
````

<!-- FILE: kit/render.js -->
````js
// render.js : draws the reel frame by frame in a headless browser (CPU only, the GPU is left alone).
//   node kit/render.js stills            key stills -> build/stills/*.png + build/stills/sheet.jpg (check these first)
//   node kit/render.js stills 0 3.5 12   stills at the times you give, in seconds
//   node kit/render.js final             every frame at 30 fps -> build/frames/ -> build/video.mp4 (silent)
//   node kit/render.js final --workers 3 (default 2; each worker is one browser tab, ~250 MB of memory)
// It also writes build/events.json (sound cues), build/numbers.json (when each number appears) and
// build/warnings.txt. Frames already on disk are kept, so a crashed render resumes where it stopped.
const fs = require('fs'), path = require('path'), url = require('url'), { spawnSync, spawn } = require('child_process');
const { chromium } = require('playwright');
const ROOT = path.dirname(__dirname), B = path.join(ROOT, 'build'), FPS = 30;

function ffmpegPath() {
  const r = spawnSync(pyExe(), ['-c', 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())'], { encoding: 'utf8' });
  if (r.status !== 0) { console.error('ffmpeg not found: install the python packages first (pip install imageio-ffmpeg)'); process.exit(1); }
  return r.stdout.trim();
}
function pyExe() {
  for (const p of [path.join(ROOT, '.venv', 'Scripts', 'python.exe'), path.join(ROOT, '.venv', 'bin', 'python')]) if (fs.existsSync(p)) return p;
  return process.platform === 'win32' ? 'python' : 'python3';
}
async function launch() {
  const args = ['--disable-gpu', '--force-color-profile=srgb', '--hide-scrollbars', '--font-render-hinting=none', '--allow-file-access-from-files'];
  const tries = [{}, { channel: 'msedge' }, { channel: 'chrome' }];
  for (const t of tries) {
    try { return await chromium.launch(Object.assign({ args }, t)); } catch (e) { /* try the next browser */ }
  }
  console.error('No browser found. Run:  npx playwright install chromium'); process.exit(1);
}
function writeData() {
  const story = JSON.parse(fs.readFileSync(path.join(ROOT, 'story.json'), 'utf8'));
  const timing = JSON.parse(fs.readFileSync(path.join(B, 'timing.json'), 'utf8'));
  const data = 'window.STORY=' + JSON.stringify(story) + ';\nwindow.TIMING=' + JSON.stringify(timing) + ';\n';
  fs.writeFileSync(path.join(B, 'data.js'), data);
  // a fingerprint of everything that changes a frame: the story, the timing and the engine itself
  const stamp = require('crypto').createHash('sha1').update(data + fs.readFileSync(path.join(__dirname, 'reel.html'), 'utf8')).digest('hex');
  return { story, timing, stamp };
}
async function openPage(browser, scale) {
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale || 1 });
  const errs = [];
  page.on('pageerror', e => errs.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await page.goto(url.pathToFileURL(path.join(__dirname, 'reel.html')).href);
  const info = await page.evaluate(() => window.REEL ? window.REEL.ready : null).catch(e => { errs.push(String(e)); return null; });
  if (!info) { console.error('The page did not load:\n' + errs.join('\n')); process.exit(1); }
  return { page, info, errs };
}
async function addHolds(page, info) {
  const h = await page.evaluate(() => window.REEL.holds());
  info.numbers.forEach((x, k) => { x.shown_until = h[k]; });
  await page.evaluate(() => window.REEL.seek(0));
}
function saveInfo(info) {
  fs.writeFileSync(path.join(B, 'events.json'), JSON.stringify(info.events, null, 0));
  fs.writeFileSync(path.join(B, 'numbers.json'), JSON.stringify(info.numbers, null, 1));
  fs.writeFileSync(path.join(B, 'warnings.txt'), info.warnings.join('\n'));
  fs.writeFileSync(path.join(B, 'visuals.json'), JSON.stringify({ visuals: info.visuals || [], layouts: info.layouts || [], fill: info.fill || [] }));
  if (info.warnings.length) console.log('WARNINGS (fix these in story.json):\n  ' + info.warnings.join('\n  '));
}

async function stills(times) {
  const custom = times.length > 0;   // stills at chosen times go to build/stills/at/, so the checkpoint sheet stays
  const { story, timing } = writeData();
  const browser = await launch();
  const { page, info } = await openPage(browser, 0.5);
  await addHolds(page, info); saveInfo(info);
  if (!custom) {   // one still at the start, then each beat once its card has landed, then the end
    times = [0];
    timing.lines.forEach((L, i) => { if (i > 0) times.push(+Math.min(L.end - 0.1, L.start + Math.min(2.2, (L.end - L.start) * 0.75)).toFixed(2)); });
    times.push(+(info.duration - 0.05).toFixed(2));
  }
  const dir = custom ? path.join(B, 'stills', 'at') : path.join(B, 'stills'); fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true });
  for (let k = 0; k < times.length; k++) {
    await page.evaluate(t => window.REEL.seek(t), times[k]);
    await page.screenshot({ path: path.join(dir, `s${String(k).padStart(2, '0')}_${times[k].toFixed(2)}s.png`) });
  }
  await browser.close();
  const ff = ffmpegPath(); const cols = Math.min(6, times.length), rows = Math.ceil(times.length / cols);
  // contact sheet: copy the stills into a numbered sequence, then let ffmpeg tile them
  const seq = path.join(dir, 'seq'); fs.mkdirSync(seq, { recursive: true });
  fs.readdirSync(dir).filter(f => f.endsWith('.png') && f.startsWith('s')).sort().forEach((f, k) => fs.copyFileSync(path.join(dir, f), path.join(seq, `${String(k).padStart(3, '0')}.png`)));
  spawnSync(ff, ['-y', '-loglevel', 'error', '-i', path.join(seq, '%03d.png'), '-vf', `scale=270:-2,tile=${cols}x${rows}:padding=6:color=white`, '-frames:v', '1', path.join(dir, 'sheet.jpg')]);
  fs.rmSync(seq, { recursive: true, force: true });
  const where = custom ? 'build/stills/at/' : 'build/stills/';
  console.log(`stills: ${times.length} -> ${where} (sheet.jpg there shows them all). Times: ${times.join(', ')}`);
}

async function final(workers) {
  const { stamp } = writeData();
  const browser = await launch();
  const first = await openPage(browser, 1);
  await addHolds(first.page, first.info); saveInfo(first.info);
  const n = Math.ceil(first.info.duration * FPS);
  const dir = path.join(B, 'frames');
  const sf = path.join(dir, 'stamp.txt');
  if (fs.existsSync(dir) && (!fs.existsSync(sf) || fs.readFileSync(sf, 'utf8') !== stamp)) {   // story, voice or engine changed: old frames are stale
    console.log('story, voice or engine changed since the last render: clearing old frames');
    fs.rmSync(dir, { recursive: true, force: true });
  }
  fs.mkdirSync(dir, { recursive: true }); fs.writeFileSync(sf, stamp);
  const name = k => path.join(dir, `f${String(k).padStart(5, '0')}.jpg`);
  const todo = []; for (let k = 0; k < n; k++) if (!fs.existsSync(name(k)) || fs.statSync(name(k)).size < 2000) todo.push(k);
  console.log(`frames: ${n} (${first.info.duration.toFixed(2)} s), ${n - todo.length} already on disk, ${todo.length} to draw with ${workers} worker(s)`);
  const pages = [first.page]; for (let w = 1; w < workers; w++) pages.push((await openPage(browser, 1)).page);
  const per = Math.ceil(todo.length / workers); let done = 0; const t0 = Date.now();
  await Promise.all(pages.map(async (p, w) => {
    for (const k of todo.slice(w * per, (w + 1) * per)) {        // each worker draws a block of frames in order
      await p.evaluate(t => window.REEL.seek(t), k / FPS);
      const tmp = name(k) + '.tmp';
      await p.screenshot({ path: tmp, type: 'jpeg', quality: 93 });
      fs.renameSync(tmp, name(k));
      if (++done % 150 === 0) console.log(`  ${done}/${todo.length}  ${((Date.now() - t0) / done).toFixed(0)} ms a frame`);
    }
  }));
  await browser.close();
  const ff = ffmpegPath();
  const r = spawnSync(ff, ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(dir, 'f%05d.jpg'), '-vf', 'scale=in_range=pc:out_range=tv,format=yuv420p', '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-movflags', '+faststart', path.join(B, 'video.mp4')], { stdio: 'inherit' });
  if (r.status !== 0) { console.error('ffmpeg failed to join the frames'); process.exit(1); }
  console.log(`video: build/video.mp4 (${n} frames, ${((Date.now() - t0) / 1000).toFixed(0)} s). Next: python kit/sound.py`);
}

(async () => {
  const [mode, ...rest] = process.argv.slice(2);
  fs.mkdirSync(B, { recursive: true });
  if (!fs.existsSync(path.join(B, 'timing.json'))) { console.error('build/timing.json is missing: run python kit/voice.py first'); process.exit(1); }
  if (mode === 'stills') await stills(rest.filter(x => !x.startsWith('--')).map(Number).filter(x => !isNaN(x)));
  else if (mode === 'final') { const i = rest.indexOf('--workers'); await final(i >= 0 ? +rest[i + 1] : 2); }
  else console.log('usage: node kit/render.js stills [times...] | final [--workers N]');
})();
````

<!-- FILE: kit/sound.py -->
````python
"""sound.py : voice + one sound effect per on-screen event + a quiet music bed -> build/mix.wav at about -14.5 LUFS

    python kit/sound.py                (after render.js, which writes build/events.json)
    python kit/sound.py --no-music     (voice and effects only)

Levels: the voice sits on top; the music runs about 18 dB under it (no vocals in the track); effects are short
and quiet. The whole mix is then set to -14.5 LUFS with the true peak under -1.5 dBFS (two-pass loudnorm).
Story settings it reads (optional): "music_gain_db" (default -18, relative to the voice), "sfx_gain_db" (default 0)."""
import json, os, re, subprocess, sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A, B = os.path.join(ROOT, "assets"), os.path.join(ROOT, "build")
SR = 48000
GAIN = {"wipe": 0.50, "card": 0.30, "title": 0.34, "tick": 0.14, "typing": 0.28, "check": 0.36,
        "cross": 0.32, "badge": 0.36, "stamp": 0.55, "strike": 0.34, "ring": 0.30}


def ff():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


FF = ff()


def load(path, start=0.0, dur=None):
    """any audio file -> float32 stereo at 48 kHz"""
    cmd = [FF, "-loglevel", "error", "-ss", f"{start:.3f}", "-i", path]
    if dur: cmd += ["-t", f"{dur:.3f}"]
    raw = subprocess.run(cmd + ["-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def lufs(x):
    p = os.path.join(B, "_m.wav"); write(p, x)
    e = subprocess.run([FF, "-hide_banner", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    os.remove(p)
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", e); tp = re.findall(r"Peak:\s+(-?[\d.inf]+) dBFS", e)
    return (float(i[-1]) if i else -70.0), (float(tp[-1]) if tp and "inf" not in tp[-1] else -99.0)


def write(path, x):
    import soundfile as sf
    sf.write(path, np.clip(x, -1, 1), SR, subtype="PCM_16")


def main():
    story = json.load(open(os.path.join(ROOT, "story.json"), encoding="utf-8"))
    timing = json.load(open(os.path.join(B, "timing.json"), encoding="utf-8"))
    events = json.load(open(os.path.join(B, "events.json"), encoding="utf-8"))
    dur = timing["duration"]; n = int(dur * SR)
    voice = load(os.path.join(B, "voice.wav"))[:n]
    voice = np.pad(voice, ((0, n - len(voice)), (0, 0)))
    vl, _ = lufs(voice)
    voice *= 10 ** ((-16.0 - vl) / 20)                           # voice at -16 LUFS before the final level
    mix = voice.copy()
    # sound effects
    sfx_db = float(story.get("sfx_gain_db", 0)); cache, last = {}, {}
    for e in events:
        typ, t = e["type"], float(e["t"])
        f = os.path.join(A, "sfx", typ + ".mp3")
        if typ not in GAIN or not os.path.exists(f) or t >= dur: continue
        if t - last.get(typ, -9) < (0.06 if typ == "tick" else 0.12): continue
        last[typ] = t
        if typ == "typing":
            s = load(f, 1.0, min(1.2, float(e.get("dur", 0.5))) + 0.05)
        else:
            if typ not in cache:
                c = load(f); pk = np.abs(c).max() or 1; cache[typ] = c / pk * 0.5    # every effect peak-matched first
            s = cache[typ]
        fade = min(len(s) // 4, int(0.02 * SR))
        if fade: s = s.copy(); s[-fade:] *= np.linspace(1, 0, fade)[:, None]
        if typ == "typing": pk = np.abs(s).max() or 1; s = s / pk * 0.5
        g = GAIN[typ] * float(e.get("vol", 1)) * 10 ** (sfx_db / 20)
        i0 = int(max(0, t) * SR); i1 = min(n, i0 + len(s))
        mix[i0:i1] += s[:i1 - i0] * g
    # music bed
    bed = os.path.join(A, "music", "bed.mp3")
    if "--no-music" not in sys.argv and os.path.exists(bed):
        m = load(bed, float(story.get("music_start", 0.0)), dur + 0.1)[:n]
        if len(m) < n:                                            # short track: loop it
            m = np.concatenate([m] * (n // max(1, len(m)) + 1))[:n]
        ml, _ = lufs(m)
        m *= 10 ** ((-16.0 + float(story.get("music_gain_db", -18)) - ml) / 20)
        fi, fo = int(0.25 * SR), int(1.0 * SR)
        m[:fi] *= np.linspace(0, 1, fi)[:, None]; m[-fo:] *= np.linspace(1, 0.35, fo)[:, None]
        mix += m
    raw = os.path.join(B, "mix_raw.wav"); write(raw, mix * 0.5)
    # final level: two-pass loudnorm to -14.5 LUFS, true peak -1.5 dBFS
    target = "I=-14.5:TP=-2.0:LRA=11"   # -2.0 here leaves room for the AAC encoder; the delivered files land near -1.5
    e = subprocess.run([FF, "-hide_banner", "-i", raw, "-af", f"loudnorm={target}:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    js = json.loads(e[e.rindex("{"):e.rindex("}") + 1])
    flt = (f"loudnorm={target}:measured_I={js['input_i']}:measured_TP={js['input_tp']}:measured_LRA={js['input_lra']}"
           f":measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
    out = os.path.join(B, "mix.wav")
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", raw, "-af", flt + ",aresample=48000", "-ar", str(SR), out], check=True)
    os.remove(raw)
    i, tp = lufs(load(out))
    print(f"mix: build/mix.wav  {i:.1f} LUFS, true peak {tp:.1f} dBFS, {len([e for e in events if e['type'] in GAIN])} sound cues")
    if not (-15.2 <= i <= -13.8): print("  WARNING: loudness is off target; run sound.py again or check the voice level")


if __name__ == "__main__":
    main()
````

<!-- FILE: kit/finish.py -->
````python
"""finish.py : build/video.mp4 + build/mix.wav -> the files you post

    python kit/finish.py

out/<slug>.mp4        1080x1920, 9:16, for Reels / Shorts / TikTok
out/<slug>_x78.mp4    1008x1152, 7:8, for X: the whole 9:16 frame, scaled down, with plain black bars left and right
out/<slug>_cover.jpg  the first frame (it is also the last frame: the reel loops)"""
import json, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B, O = os.path.join(ROOT, "build"), os.path.join(ROOT, "out")


def main():
    import imageio_ffmpeg
    FF = imageio_ffmpeg.get_ffmpeg_exe()
    story = json.load(open(os.path.join(ROOT, "story.json"), encoding="utf-8"))
    slug = story.get("slug") or "reel"
    os.makedirs(O, exist_ok=True)
    v, a = os.path.join(B, "video.mp4"), os.path.join(B, "mix.wav")
    full, x78, cover = (os.path.join(O, f"{slug}{s}") for s in (".mp4", "_x78.mp4", "_cover.jpg"))
    run = lambda args: subprocess.run([FF, "-y", "-loglevel", "error"] + args, check=True)
    # ffmpeg's built-in AAC can wreck a single frame on a sharp click over speech (a crackle, true peak above 0 dBFS)
    # at 160-192k with noise substitution / intensity stereo on. 256k with both off measured clean.
    AAC = ["-c:a", "aac", "-b:a", "256k", "-aac_pns", "0", "-aac_is", "0"]
    run(["-i", v, "-i", a, "-map", "0:v", "-map", "1:a", "-c:v", "copy"] + AAC + ["-shortest", "-movflags", "+faststart", full])
    for crf in (20, 23, 26):                                   # keep the X file under 15 MB
        run(["-i", v, "-i", a, "-map", "0:v", "-map", "1:a", "-vf", "scale=648:1152:flags=lanczos,pad=1008:1152:180:0:black,setsar=1,format=yuv420p", "-color_range", "tv",
             "-c:v", "libx264", "-preset", "medium", "-crf", str(crf), "-pix_fmt", "yuv420p"] + AAC + ["-shortest", "-movflags", "+faststart", x78])
        if os.path.getsize(x78) < 15e6: break
    run(["-i", full, "-frames:v", "1", "-q:v", "2", cover])
    for p in (full, x78, cover): print(f"{os.path.relpath(p, ROOT)}  {os.path.getsize(p) / 1e6:.1f} MB")
    print("next: python kit/check.py")


if __name__ == "__main__":
    main()
````

<!-- FILE: kit/check.py -->
````python
"""check.py : quality checks on the finished reel -> build/qa/report.md (+ contact sheets to look at)

    python kit/check.py

Checks (FAIL means fix it before you post):
  length 30-75 s . loudness -15.2 to -13.8 LUFS, true peak <= -1.0 dBFS . Kokoro voice, 150-200 words a minute
  every number on screen appears within 0.3 s of being spoken (up to 0.8 s early) and stays >= 1.2 s after it
  nothing frozen for more than 1.6 s . no black frames . the first frame already shows the hook . no build warnings
Files to look at: build/qa/sheet_1.jpg ... (a frame every 0.5 s), build/qa/lips.jpg (the mouth, 10 frames a second)."""
import json, os, re, subprocess, sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B, O = os.path.join(ROOT, "build"), os.path.join(ROOT, "out")
Q = os.path.join(B, "qa")
UNITS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: 10 * i for i, w in enumerate("_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()) if w != "_"}
SCALE = {"hundred": 100, "thousand": 1000, "million": 10 ** 6, "billion": 10 ** 9}


def ff():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


FF = ff()


def spoken_numbers(words):
    """[(value, start, end)] from the timed words: 'one thousand and twenty four' -> 1024, '1,024' -> 1024"""
    out, i = [], 0
    clean = [re.sub(r"[^a-z0-9.\-]", "", w["w"].lower().replace(",", "")).strip(".-") for w in words]
    while i < len(words):
        c = clean[i]
        if re.fullmatch(r"\d+(\.\d+)?", c):
            out.append((float(c), words[i]["s"], words[i]["e"])); i += 1; continue
        parts = c.split("-")
        if parts[0] in UNITS or parts[0] in TENS or (parts[0] == "a" and i + 1 < len(clean) and clean[i + 1] in SCALE):
            total, cur, j, s = 0, 0, i, words[i]["s"]
            while j < len(words):
                c = clean[j]; ps = c.split("-")
                if c == "a" and j == i: cur = 1
                elif all(p in UNITS or p in TENS for p in ps): cur += sum(UNITS.get(p, TENS.get(p, 0)) for p in ps)
                elif c == "hundred": cur = max(cur, 1) * 100
                elif c in SCALE: total += max(cur, 1) * SCALE[c]; cur = 0
                elif c == "and" and j + 1 < len(words) and (clean[j + 1] in UNITS or clean[j + 1].split("-")[0] in TENS): pass
                else: break
                j += 1
                if re.search(r"[.!?:;]$", words[j - 1]["w"]): break
            out.append((float(total + cur), s, words[j - 1]["e"])); i = j; continue
        i += 1
    return out


def frames_gray(path, fps=10, w=54, h=96):
    raw = subprocess.run([FF, "-loglevel", "error", "-i", path, "-vf", f"fps={fps},scale={w}:{h},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)


def main():
    story = json.load(open(os.path.join(ROOT, "story.json"), encoding="utf-8"))
    timing = json.load(open(os.path.join(B, "timing.json"), encoding="utf-8"))
    slug = story.get("slug") or "reel"
    vid = os.path.join(O, f"{slug}.mp4")
    if not os.path.exists(vid): sys.exit("out/%s.mp4 is missing: run python kit/finish.py first" % slug)
    os.makedirs(Q, exist_ok=True)
    rows, fails = [], 0

    def row(name, ok, detail):
        nonlocal fails
        rows.append(f"| {'PASS' if ok else 'FAIL'} | {name} | {detail} |"); fails += (not ok)

    e = subprocess.run([FF, "-hide_banner", "-i", vid, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    dur = float(sum(float(x) * m for x, m in zip(re.search(r"Duration: (\d+):(\d+):([\d.]+)", e).groups(), (3600, 60, 1))))
    row("length", 30 <= dur <= 75, f"{dur:.1f} s (30-75)")
    i = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]); tp = re.findall(r"Peak:\s+(-?[\d.inf]+) dBFS", e)[-1]
    tpv = float(tp) if "inf" not in tp else -99
    row("loudness", -15.2 <= i <= -13.8 and tpv <= -1.0, f"{i:.1f} LUFS, true peak {tpv:.1f} dBFS (-15.2 to -13.8, peak <= -1.0)")
    row("voice", timing.get("engine") == "kokoro" and 150 <= timing["wpm"] <= 200, f"{timing.get('engine')} {timing.get('voice')}, {timing['wpm']} words a minute (150-200)")
    warns = open(os.path.join(B, "warnings.txt"), encoding="utf-8").read().strip() if os.path.exists(os.path.join(B, "warnings.txt")) else ""
    row("build warnings", not warns, warns.replace("\n", " / ") or "none")
    # numbers: appear when spoken, hold after
    words = [w for L in timing["lines"] for w in L["words"]]
    spoken = spoken_numbers(words)
    nums = json.load(open(os.path.join(B, "numbers.json"), encoding="utf-8"))
    loop = any(b.get("loop") for b in story["beats"])
    for n in nums:
        cands = [s for s in spoken if abs(s[0] - n["value"]) < 1e-6]
        if not cands:
            row(f"number {n['value']:g}", False, f"on screen at {n['t']:.2f} s ({n['where']}) but never spoken"); continue
        s = min(cands, key=lambda c: abs(c[1] - n["t"]))
        early, late = s[1] - n["t"], n["t"] - s[1]
        hold = (n["shown_until"] - s[2]) if n.get("shown_until") is not None else None
        ok_t = late <= 0.3 and (early <= 0.8 or (n["t"] < 0.05 and s[1] < 1.2))
        ok_h = n["where"] == "wipe" or (hold is not None and hold >= 1.2) or (loop and n["beat"] == len(story["beats"]) - 1)
        row(f"number {n['value']:g}", ok_t and ok_h,
            f"{n['where']}: on screen {n['t']:.2f} s, spoken {s[1]:.2f}-{s[2]:.2f} s" + (f", stays {hold:.1f} s after" if hold is not None else ""))
    # holds: the longest time with nothing new arriving on screen (cards, rows, numbers, pulses, wipes; captions don't count)
    vj = os.path.join(B, "visuals.json")
    if os.path.exists(vj):
        vis = sorted(set([0.0] + json.load(open(vj, encoding="utf-8"))["visuals"] + [timing["duration"]]))
        gaps = [(round(a, 2), round(b - a, 2)) for a, b in zip(vis, vis[1:]) if b - a > 1.8]
        longest = max([b - a for a, b in zip(vis, vis[1:])], default=0)
        row("no long holds", longest <= 2.4, f"longest {longest:.1f} s with nothing new on screen (max 2.4); over 1.8 s at: " + (", ".join(f"{a:.1f} s ({g:.1f} s)" for a, g in gaps) or "none"))
        slow = [(b, d) for b, d in json.load(open(vj, encoding="utf-8")).get("fill", []) if d > 1.5]
        row("cards fill fast", not slow, "first content within 1.5 s of every card" if not slow else "empty for: " + ", ".join(f"beat {b} ({d:.1f} s)" for b, d in slow) + ": cue the first row earlier or use null")
    # motion: frozen stretches, black frames, first frame
    g = frames_gray(vid)
    d = np.abs(np.diff(g, axis=0)).mean(axis=(1, 2))
    still, run, longest = d < 0.25, 0, 0
    for s_ in still:
        run = run + 1 if s_ else 0; longest = max(longest, run)
    row("no frozen stretch", longest / 10 <= 1.6, f"longest still {longest / 10:.1f} s (max 1.6)")
    dark = (g.mean(axis=(1, 2)) < 8).sum()
    row("no black frames", dark == 0, f"{dark} dark frames at 10 fps")
    row("first frame shows the hook", g[0].std() > 12, f"contrast {g[0].std():.0f} (a blank or fading first frame fails)")
    # sheets: one frame every 0.5 s, 48 per sheet
    for f in os.listdir(Q):
        if f.startswith("sheet_"): os.remove(os.path.join(Q, f))
    per, k, start = 48, 1, 0.0
    while start < dur - 0.6:   # skip a last sheet that would hold under a second (ffmpeg writes nothing and fails)
        subprocess.run([FF, "-y", "-loglevel", "error", "-ss", f"{start:.2f}", "-t", f"{per * 0.5:.2f}", "-i", vid, "-vf", "fps=2,scale=160:-2,tile=8x6:padding=4:color=white",
                        "-frames:v", "1", os.path.join(Q, f"sheet_{k}.jpg")], check=True)
        start += per * 0.5; k += 1
    # lips: the presenter's face, 10 frames a second, during the first card beat after the hook
    beats = story["beats"]; li = next((j for j, b in enumerate(beats) if j > 0 and b.get("layout", "card") != "hero"), 1)
    t0 = timing["lines"][li]["start"] + 0.3
    subprocess.run([FF, "-y", "-loglevel", "error", "-ss", f"{t0:.2f}", "-t", "2.4", "-i", vid, "-vf", "fps=10,crop=280:240:620:1530,tile=8x3:padding=3:color=white",
                    "-frames:v", "1", os.path.join(Q, "lips.jpg")], check=True)
    said = [w for w in words if t0 <= w["s"] < t0 + 2.4]
    lips = [f"lips.jpg: {t0:.1f}-{t0 + 2.4:.1f} s, tile n = {t0:.1f} s + n x 0.1 s. Words: " + ", ".join(f"{w['w']} {w['s']:.2f}" for w in said)]
    rep = ["# QA report: " + slug, "", f"file: out/{slug}.mp4", "", "| result | check | detail |", "|---|---|---|"] + rows
    rep += ["", "Look at: " + ", ".join(sorted(f for f in os.listdir(Q) if f.endswith(".jpg"))), "", lips[0], "",
            f"**{fails} FAIL**" if fails else "**all checks PASS**"]
    open(os.path.join(Q, "report.md"), "w", encoding="utf-8").write("\n".join(rep) + "\n")
    print("\n".join(rep))


if __name__ == "__main__":
    main()
````

<!-- FILE: kit/example_story.json -->
````json
{
 "topic": "How a Claude skill works, and how to make one",
 "slug": "claude_skills",
 "voice": "am_liam+am_puck",
 "speed": 1.1,
 "tail": 0.8,
 "captions": {
  "dot claude slash skills": ".claude/skills",
  "skill dot M D": "SKILL.md",
  "slash weekly report": "/weekly-report"
 },
 "keys": [
  "Claude",
  "skill",
  "trigger",
  "once",
  "description",
  "folder",
  "file",
  "steps",
  "prompt"
 ],
 "sources": [
  "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (read 2026-10-30): metadata ~100 tokens per Skill, loaded at startup; SKILL.md body under 5k tokens, loaded when triggered; description max 1,024 characters, must say what it does and when to use it",
  "https://code.claude.com/docs/en/skills (read 2026-10-30): ~/.claude/skills/<skill-name>/SKILL.md; descriptions in context, full content only when invoked; invoke directly with /skill-name; keep SKILL.md under 500 lines"
 ],
 "beats": [
  {
   "label": "the problem",
   "say": "You paste the same long prompt into every new Claude chat.",
   "title": "SAME *PROMPT*",
   "card": {
    "type": "chat",
    "tab": "chat · new",
    "cues": [
     null,
     null
    ],
    "msgs": [
     {
      "from": "you",
      "text": "Write it in my voice, short lines…"
     },
     {
      "from": "you",
      "text": "Write it in my voice, short lines…"
     }
    ]
   },
   "strike": [
    1,
    "every"
   ],
   "stamp": {
    "text": "AGAIN",
    "at": "chat"
   }
  },
  {
   "label": "the fix",
   "stat": {
    "label": "TOKENS",
    "value": 100,
    "at": "hundred"
   },
   "say": "About one hundred tokens. That's what a Claude skill costs, until you need it.",
   "title": "ONE *SKILL*",
   "card": {
    "type": "folder",
    "name": "weekly-report",
    "items": [
     "name",
     "description",
     "steps"
    ],
    "cues": [
     null,
     "skill",
     "costs"
    ],
    "pill": {
     "label": "AT STARTUP",
     "value": 100,
     "at": "hundred"
    }
   },
   "ring": [
    "pill",
    "need"
   ]
  },
  {
   "point": 1,
   "label": "the folder",
   "stat": {
    "label": "STEP",
    "value": 1,
    "at": "one"
   },
   "say": "Step one. In Claude Code, make a folder in dot claude slash skills, named after the job.",
   "title": "ONE *FOLDER*",
   "card": {
    "type": "files",
    "tab": "your computer",
    "cues": [
     "claude",
     "skills",
     "job"
    ],
    "hl": 2,
    "rows": [
     [
      "~/.claude/",
      0,
      "folder"
     ],
     [
      "skills/",
      1,
      "folder"
     ],
     [
      "weekly-report/",
      2,
      "folder"
     ]
    ]
   },
   "term": {
    "cmd": "mkdir ~/.claude/skills/weekly-report",
    "at": "make"
   },
   "stamp": {
    "text": "ONE PER JOB",
    "at": "job"
   }
  },
  {
   "point": 2,
   "label": "the file",
   "stat": {
    "label": "STEP",
    "value": 2,
    "at": "two"
   },
   "say": "Step two. Inside it, add one file called skill dot M D, with a name and a description on top.",
   "title": "ONE *FILE*",
   "card": {
    "type": "code",
    "tab": "SKILL.md",
    "cues": [
     null,
     "name",
     "description",
     "skill"
    ],
    "lines": [
     "---",
     "name: weekly-report",
     "description: My Monday report",
     "---"
    ]
   },
   "term": {
    "cmd": "touch SKILL.md",
    "at": "add"
   }
  },
  {
   "label": "the trigger",
   "stat": {
    "label": "MAX CHARS",
    "value": 1024,
    "at": "thousand"
   },
   "say": "Keep that description under one thousand and twenty four characters. It's the trigger.",
   "focus": [
    2,
    "description"
   ],
   "stamp": {
    "text": "THE TRIGGER",
    "at": "trigger"
   },
   "ring": [
    2,
    "characters"
   ]
  },
  {
   "point": 3,
   "label": "the steps",
   "stat": {
    "label": "MAX LINES",
    "value": 500,
    "at": "five"
   },
   "say": "Step three. Keep it under five hundred lines, and write the steps like you're briefing a new hire.",
   "title": "THE *STEPS*",
   "card": {
    "type": "code",
    "tab": "SKILL.md",
    "cues": [
     null,
     "write",
     "briefing",
     "hire"
    ],
    "lines": [
     "# Weekly report",
     "- Read my notes",
     "- Pull the numbers that moved",
     "- Write it in short lines"
    ]
   },
   "stamp": {
    "text": "UNDER 500",
    "at": "lines"
   }
  },
  {
   "label": "why it's cheap",
   "stat": {
    "label": "TOKENS",
    "value": 100,
    "at": "hundred"
   },
   "say": "Why it's cheap: at startup, Claude only reads the name and description. About one hundred tokens.",
   "title": "LOADS *LATER*",
   "card": {
    "type": "compare",
    "tab": "what Claude loads",
    "items": [
     {
      "label": "at startup",
      "show": "startup",
      "note": "name + description",
      "note_at": "name",
      "value": 100,
      "unit": "tokens",
      "at": "hundred"
     },
     {
      "label": "when it runs",
      "beat": 7,
      "show": "full",
      "value": 5000,
      "unit": "tokens",
      "at": "five"
     }
    ],
    "extra": [
     {
      "kind": "chip",
      "text": "your request matches",
      "ok": true,
      "beat": 7,
      "at": "matches"
     }
    ]
   }
  },
  {
   "say": "The full file, under five thousand tokens, loads only when your request matches that description.",
   "stamp": {
    "text": "ON DEMAND",
    "at": "only"
   }
  },
  {
   "label": "run it",
   "say": "Or type slash weekly report to run it yourself.",
   "title": "RUN *IT*",
   "card": {
    "type": "terminal",
    "tab": "Claude Code",
    "cmd": "/weekly-report",
    "cues": [
     "slash",
     "run"
    ],
    "out": [
     "ok: weekly-report loaded",
     "writing this week's report…"
    ]
   }
  },
  {
   "loop": true,
   "say": "Write it once, and stop pasting the same long prompt into every new chat.",
   "title": "WRITE IT *ONCE*",
   "loopAt": "same"
  }
 ]
}
````

