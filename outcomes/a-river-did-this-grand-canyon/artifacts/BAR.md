# The bar

Brief: the Grand Canyon, carved by the Colorado River; warm low sunlight, deep shadows, not grey.
No reference photos were given, so each still is scored on its own against the brief, read as the real place (the
real Grand Canyon at golden hour: layered red and tan walls, a cream Kaibab/Coconino rim band, red Supai and Redwall,
a grey-green Tonto platform, a dark schist inner gorge with the green Colorado River, pinyon-juniper on the rim,
blue-violet haze on far rims).

Each shot is scored 0-100 on six dimensions by at least two fresh critics who see only the still and the rubric below.
**Target: 98 on every dimension of every shot, by critic median.**

| Dimension | What 98 means |
|---|---|
| Composition | Framing a cinematographer would choose for a vertical 9:16 phone film; clear subject, depth layers, leading lines, room for on-screen words in the upper third. |
| Light | Warm low sun with believable long shadows; shadows deep but filled with warm bounce and cool skylight; no blown or flat areas. |
| Colour | Reads as real Grand Canyon colour: rich but natural reds/oranges/creams, not grey, not plastic, not oversaturated; correct strata order. |
| Water | The river reads as a real river (depth colour, reflections, glints, banks); when it's small in frame, it sits correctly in the gorge. |
| Vegetation | Pinyon-juniper on the rim, sparse desert scrub on slopes, riparian green at the river: right density, size, colour and clumping, no "balls". |
| Far detail | Distant rims, temples and buttes with crisp structure and natural aerial perspective; no smears, tiling, aliasing or blocky artifacts. |

Anchors for critics: 98 = indistinguishable from a professional photo of the real place; 90 = top-tier film VFX;
80 = high-end game cinematic, clearly CG; 70 = good CG with visible flaws; 55 = obviously synthetic with artifacts;
40 = broken.

Colour is also measured every round (`src/measure.py`) per region (sky, far, mid, near; sunlit vs shadow):
targets are shadow warmth R/B ≥ 1.15, mean rock saturation (HSV) 0.35–0.60, sunlit rock luminance 0.45–0.80,
fraction of near-grey pixels (sat < 0.12) below 15 % outside the sky.
