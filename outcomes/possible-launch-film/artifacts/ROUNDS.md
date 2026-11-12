# Review rounds

## Round 1 (52 s cut, type only)
- Rendered by the user with `bash render.sh round 1`. Sheets: out/sheets/round1_states.png, out/sheets/round1_transitions.png.
- Measurements (out/checks/round1.json): repeat renders identical in two fresh processes plus once in-process (4 frames); copy matches the brief word for word with 0 invented words; 0 lines outside the safe area; 0 line overlaps; panel and text colour ΔE2000 0.00 on all 19 states; all 13 panels land on their expected frame; audio hits within 1.3 ms; -14.01 LUFS, -1.68 dBTP; 0.073 s per frame.
- Reviewer A: CLEAN. Note: the 54 px wordmark in frame 1 can't be read at thumbnail size (frame 0). Fix: 76 px.
- Reviewer B: CLEAN. Same wordmark note; also the S04 caption runs into S05's on the sheet (sheet only, not the film). Fix: truncate captions to the thumbnail width.
- Both fixed for round 2.

## Round 2 (58 s cut, real outputs added)
- Change: the user supplied five real outputs. New 6 s section between the claim and "Get the agents that make these." (see STATES.md S03 to S10); everything after it moves 6 s later. Wordmark in frame 1 is 76 px.
- Rendered by the user with `bash render.sh round 2`. Sheets: out/sheets/round2_states.png, out/sheets/round2_transitions.png.
- Measurements (out/checks/round2.json): repeat renders identical (4 frames incl. one mid-push); copy matches, 28 scenes, 0 invented words; 0 outside the safe area; 0 overlaps; colour ΔE2000 0.00 on 25 states; real outputs untinted (mean channel shift 0.02 to 0.12); 13/13 panels on frame; 18 audio hits, worst 1.3 ms; -14.01 LUFS, -1.68 dBTP.
- Reviewer A: CLEAN.
- Reviewer B: NOT CLEAN. One defect, frames 274 to 275: the row thumbnails grow from zero height in place instead of rising, so the dark third thumbnail reads as a thin grey keyline rule for one frame. Cause: `draw_image(reveal=p)` grew the mask and drew a bottom keyline at any height. Fix: the thumbnails slide up from behind the row's bottom edge (`clip_bottom`), and no bottom keyline is drawn while clipped.
- My own read: the outputs sat small in a tall dark frame, with a 44 px caption that can't be read on a phone. Fix: the agent name is now 120 px ExtraBold above each output.
- User change: the launch-kit image was withdrawn because it carries old copy. Four outputs now; the last holds 2 s. The Launch Marketer card stays, as one of the nine names.

## Round 3 (four outputs, big agent names, row rises)
- Rendered together with the final in one command, to save a hand-off (see RENDER.md). If the round 3 sheets are not clean, the affected frames are fixed and the final is rendered again.
- Rendered by the user with `bash render.sh round 3 && bash render.sh final`. Sheets: out/sheets/round3_states.png, out/sheets/round3_transitions.png.
- Source measurements (out/checks/round3.json): all PASS. Repeat renders identical; copy matches, 27 scenes, 0 invented words; 0 outside the safe area; 0 overlaps; ΔE2000 0.00 on 24 states; outputs untinted (shift 0.02 to 0.12); 13/13 panels on frame; 17 hits, worst 1.3 ms; -14.01 LUFS, -1.68 dBTP.
- Reviewer A: CLEAN. Reviewer B: CLEAN. (Both checked frame 275: the thin light edge is the top of the deck thumbnail rising from under its mask, not a stray line.) The user watched the film and approved it.
- Shipped-file checks (out/checks/final.json): two FAILs.
  - Brand colour after encode ΔE2000 2.47 (ink #201f1c decoded as #1f1c1b; background #faf7f1 as #f9f5ee). Ideal 8-bit limited-range rounding would give ΔE 1.17 for ink and 0.82 for background, so most of the error is rounding bias in swscale's default RGB-to-YUV conversion. The measuring decoder used default rounding too.
  - Real outputs shift 1.9 to 2.4 levels after encode: the same bias.
  - Also found: ffprobe shows color_transfer and color_primaries as `unknown`; the `-color_*` flags did not reach the stream.
- Fix: the final step now encodes a brand-colour strip with each candidate setting (default, accurate_rnd, accurate_rnd+full_chroma_int, with and without bt709 tags via setparams), measures it, and encodes the film with the best. The measuring decoder uses accurate rounding. Source frames unchanged, so no new sheets are needed.

## Final re-encode
- Rendered by the user with `bash render.sh final`.
- Encoder probe: default rounding, accurate_rnd, accurate_rnd+full_chroma_int, and the untagged fallback all gave worst ΔE2000 1.17 on the brand strip, which is the ideal 8-bit limited-range error. So my round 3 diagnosis was wrong: the encode was never biased. The 2.47 came from default rounding in the decoder that measures, and the real defect was only the missing colour tags. Used: accurate_rnd.
- Shipped file, every check passed. Measured 1740 frames = 58.000 s; audio minus video 0.0 ms; -14.02 LUFS, -1.49 dBTP, 0 clipped samples; 17 hits, worst 1.3 ms; brand colour worst delta E (CIEDE2000) 1.17; outputs shift 0.08 to 0.89; decoded vs source PSNR min 42.18 dB; 13/13 panels on frame. ffprobe: h264 yuv420p 1080x1920 30 fps, tv range, bt709 primaries/transfer/matrix; AAC 58.000 s.
- Closed.

