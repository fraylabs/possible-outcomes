# Rounds

Each round: stills of every shot at 540x960 (4x jittered AA), scored by two fresh critic subagents that see only the
stills and the rubric (`rounds/CRITIC_PROMPT.md`). Median per dimension below; colour measured with `src/measure.py`.
No reference photos were given, so the "side-by-side" is the still alone against the brief read as the real place.

## Round 1
Stills: `rounds/r01/`. Changes before this round: first full shot list; strata LUT with ledges; stream-power erosion
with layer erodibility; footprint-based LOD on detail.

| shot | composition | light | colour | water | vegetation | far_detail | min |
|---|---|---|---|---|---|---|---|
| s0_river_did_this | 70 | 60 | 57.5 | 42.5 | 42.5 | 52 | 42.5 |
| s1_flat_plateau | 57.5 | 52.5 | 60 | 35 | 27.5 | 57.5 | 27.5 |
| s2_river_cuts | 72 | 62 | 55 | 47.5 | 33.5 | 54 | 33.5 |
| s3_deepening | 55 | 60 | 53.5 | 37.5 | 25 | 52.5 | 25 |
| s4_old_rocks | 51 | 56.5 | 52.5 | 87.5 | 30 | 42.5 | 30 |
| s5_mile_deep | 65 | 50 | 47.5 | 68.5 | 27.5 | 45 | 27.5 |
| s6_long | 76 | 65 | 62 | 52.5 | 45 | 59.5 | 45 |
| s7_still_cutting | 55 | 56.5 | 49 | 45 | 42.5 | 52.5 | 42.5 |
| s8_endcard | 64.5 | 54 | 46.5 | 85 | 30 | 50 | 30 |

Weakest: s3 vegetation 25. Critics agreed on: tree "balls" and dark dots, plastic oversaturated rock, black inner gorge,
blown blocky rim, river not reading as water. Measured: ground saturation 0.54–0.81 (target 0.35–0.60), shadows R/B up to 73 (blue crushed).

## Round 2
Fixed in depth: vegetation (weakest dimension, weakest shot). Shrub crowns on slopes removed and replaced with
footprint-filtered scrub speckle; pinyon-juniper crowns rebuilt as three irregular lobes with ragged foliage, darker
grey-green albedo, clumped density shared with the far-distance canopy texture; riparian band narrowed to the bank;
crowns cast soft long shadows and occlude sky on the ground. Also from measurement: rock albedos desaturated, post
saturation 1.10 → 0.94, s7/s8 sun raised and saturation 0.8, s1/s6 aerial perspective reduced. Bug found while
checking s5: the river channel was cut as a flat slot into the V gorge, leaving 100 m vertical "carpet" walls at both
banks; the gorge walls now start at the river edge after a flat bank (shader and CPU height). Distance field now
blends smoothly into the river distance (bake seam removed).

Round 2 median (critics A, B):

| shot | composition | light | colour | water | vegetation | far_detail | min |
|---|---|---|---|---|---|---|---|
| s0_river_did_this | 70 | 62 | 63.5 | 40 | 45 | 55 | 40 |
| s1_flat_plateau | 64 | 60 | 60 | 32.5 | 43.5 | 55 | 32.5 |
| s2_river_cuts | 75 | 64 | 56.5 | 56.5 | 42.5 | 58 | 42.5 |
| s3_deepening | 61 | 62 | 60 | 32.5 | 35 | 59 | 32.5 |
| s4_old_rocks | 55 | 58 | 51 | 85 | 40 | 46.5 | 40 |
| s5_mile_deep | 75 | 61 | 53.5 | 66 | 32.5 | 57.5 | 32.5 |
| s6_long | 76 | 65 | 63 | 46.5 | 37.5 | 61 | 37.5 |
| s7_still_cutting | 62 | 61 | 57.5 | 40 | 37.5 | 55.5 | 37.5 |
| s8_endcard | 71 | 65 | 63 | 85 | 49 | 59 | 49 |

Critics: 2. Weakest: s1_flat_plateau / water = 32.5. Mean of shot minimums 38.2.

Weakest: s1 water 32.5 (river read as a cream levee / pink road; inner-gorge river invisible).

## Round 3
Fixed in depth: water (weakest dimension, weakest shot). Water rewritten as a single-scattering body (clear green
today, silty red-brown during the time-lapse) with depth-dependent transmittance, flow-aligned waves whose amplitude
follows a current field (glassy runs, choppy riffles, rapids with whitewater streaks), footprint-aware roughness so
glints become a sheen at distance, a thin wet line at the waterline, and the wide bank foam removed. River width now
varies along its course, with sand/gravel bars; riparian growth is patchy instead of continuous hedgerows; bank sand
darkened. s1 reframed to follow the young river from 400 m up; gentle valley slopes on the plateau take soil cover
(no cream levee).

Round 3 median:

| shot | composition | light | colour | water | vegetation | far_detail | min |
|---|---|---|---|---|---|---|---|
| s0_river_did_this | 72 | 64 | 61 | 42.5 | 50 | 56.5 | 42.5 |
| s1_flat_plateau | 66 | 63 | 60 | 46.5 | 38 | 52.5 | 38 |
| s2_river_cuts | 74 | 63 | 53.5 | 50 | 45 | 58 | 45 |
| s3_deepening | 55 | 60 | 57.5 | 57.5 | 45 | 55 | 45 |
| s4_old_rocks | 52 | 56.5 | 50 | 85 | 45 | 43.5 | 43.5 |
| s5_mile_deep | 73 | 53.5 | 50 | 64 | 37.5 | 50 | 37.5 |
| s6_long | 77 | 65 | 62 | 53.5 | 42.5 | 57 | 42.5 |
| s7_still_cutting | 60 | 64 | 57.5 | 47.5 | 35 | 55 | 35 |
| s8_endcard | 70 | 66 | 62 | 85 | 42 | 58 | 42 |

Critics: 2. Weakest: s7_still_cutting / vegetation = 35. Mean of shot minimums 41.2.

Water rose most (s1 32.5→46.5, s3 32.5→57.5). Weakest now: s7 vegetation 35. Every critic still flags "melted clay"
rock with contour swirls, curtain-like vertical streaks, blocky white rim teeth and a mint-green Tonto.

## Round 4
Fixed in depth: vegetation (s7 weakest). Woodland density lowered to 6–36 % cover with soft clump edges and gaps
(no carpets); scrub speckle lighter grey-green and sparser (no black specks); s7 reframed from 360–420 m above the rim
so no orange mound fills the foreground. Rock (flagged by every critic): stretched varnish streaks replaced by
triplanar vertical jointing and broad varnish; talus/rubble mantle on soft-layer slopes mutes the bedding; bedding
ledges weaker in slope layers than in cliffs; Tonto recoloured grey-tan; rim breakup uses fbm instead of ridged
noise (less blocky); Kaibab/Coconino albedo lowered.

Round 4 median:

| shot | composition | light | colour | water | vegetation | far_detail | min |
|---|---|---|---|---|---|---|---|
| s0_river_did_this | 72 | 64 | 63 | 47.5 | 45 | 55 | 45 |
| s1_flat_plateau | 68 | 64 | 61 | 48 | 37.5 | 54 | 37.5 |
| s2_river_cuts | 75 | 62.5 | 55 | 55 | 43.5 | 59 | 43.5 |
| s3_deepening | 55 | 60 | 58 | 87.5 | 42.5 | 53.5 | 42.5 |
| s4_old_rocks | 50 | 58 | 53.5 | 87.5 | 35 | 47.5 | 35 |
| s5_mile_deep | 75 | 59 | 55.5 | 67 | 37.5 | 59 | 37.5 |
| s6_long | 78 | 66 | 64 | 55 | 41.5 | 59 | 41.5 |
| s7_still_cutting | 62 | 62 | 62 | 45 | 40 | 55 | 40 |
| s8_endcard | 71 | 66 | 62.5 | 86.5 | 46.5 | 56.5 | 46.5 |

Critics: 2. Weakest: s4_old_rocks / vegetation = 35. Mean of shot minimums 41.0.


## Outcome: film rendered below the bar (user decision)
After four rounds the critic medians are 35–88 per dimension (shot minimums 35–46.5, mean 41.0), far below the 98 target,
and rounds 3→4 were flat (41.2 → 41.0). The remaining gap is structural (walls read as "melted clay", hidden inner-gorge
river, blocky rim bands, carpet-like trees), not tuning. The user watched the round-4 preview
(`preview_540_round4.mp4`) and chose to render the final film at this quality. **`film.mp4` is below the photoreal
bar set in BAR.md.** One change after the preview: the depth card now reads "a mile deep (1.6 km)" (was 1.8 km, which is
the deepest point, not a mile); the preview still shows the old 1.8 km card.
