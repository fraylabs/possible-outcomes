# Two-angle desk phone stand: digital pre-build report

Status: **digital pre-build only.** Nothing has been printed or measured. Every load, friction and strength figure below is a calculation or an assumption, not a test result.

## 1. Design targets (from the brief)

| # | Target | Source |
|---|---|---|
| T1 | Holds a phone at two viewing angles: **video call 70°** and **reading 55°** from horizontal | Brief gives "two angles"; the values are **assumptions** |
| T2 | Fits phones **65–80 mm wide**, **up to 11 mm thick** including case | Brief |
| T3 | Phones down to **7 mm thick** (no case) are also held | **Assumption** |
| T4 | Phone lengths checked: 140 mm (small) to 168 mm (large, in a case) | **Assumption** |
| T5 | Charging cable stays plugged in: a slot and clear space for a **12 × 8.5 × 30 mm** straight plug plus strain relief before the cable bends | Brief asks for a slot; plug size is an **assumption** (USB-C / Lightning overmould) |
| T6 | Stays put when the screen is tapped. Design tap: **1 N** normal to the screen, anywhere up to the top of the phone | Brief; the tap force is an **assumption** |
| T7 | Footprint **under 90 × 90 mm** | Brief |
| T8 | FDM, PLA, **220 mm bed**, no supports, no screws, no glue | Brief; bed taken as 220 × 220 × 250 mm Z (**Z is an assumption**; parts need 72 mm) |
| T9 | Phone mass 140 g (small) to 240 g (large with case); PLA density 1.24 g/cm³; PLA-on-desk friction μ = 0.3 | **Assumptions** |

## 2. What was built

Two printed parts. There are no fasteners and no glue.

- **SB-01 Base**: an 88 × 88 × 22 mm solid block. It holds two angled sockets: the front one sets 55° (reading) and the rear one sets 70° (video). It also has a central cable notch open to the front and a cable channel on the underside that runs to the rear edge. The block is deliberately solid because its weight is what keeps the stand from tipping back when the screen is tapped.
- **SB-02 Cradle**: a 72 mm wide L-shaped holder. It has a 5 mm backrest (90 mm tall above the ledge), a 6 mm ledge, a 6 mm lip, and a 15 mm cable slot through the ledge. A 14 mm tongue continues the backrest below the ledge.

**Changing angle:** lift the cradle out along its tongue and drop it into the other socket.
- **Positive stop:** the tongue tip seats flat on the socket floor (270 mm² contact, which is the whole tongue tip).
- **Sideways location:** the socket end walls locate the cradle to ±0.25 mm.
- **Holding the angle:** the tongue's faces bear on the socket walls. No part of this depends on friction.

The cable goes from the phone, through the ledge slot, down into the notch. From there it can leave forward over the desk or backward through the underside channel.

Renders: `renders/assembled_video.png`, `assembled_reading.png`, `in_use_*.png` (phone envelope and plug keep-out shown), `side_video.png` / `side_reading.png` (the two mechanism positions in true side view), `exploded.png`, `base_top.png`, `base_under.png`.

## 3. Key dimensions

All values are named parameters in `cad_source/params.py`.

| Item | Value |
|---|---|
| Stand footprint (both positions) | 88.0 × 88.0 mm |
| Height without phone | 114.4 mm (video) / 103.7 mm (reading) |
| Base | 88 × 88 × 22 mm, corner R6, 1 mm top chamfer, 0.6 mm bottom chamfer |
| Cradle width × backrest height × thickness | 72 × 90 × 5 mm |
| Phone pocket (backrest face to lip) | 12.5 mm (11 mm phone + 1.5 mm) |
| Lip height above ledge | 6 mm |
| Ledge top above desk | 30.3 mm (video) / 30.8 mm (reading) |
| Cable slot through ledge | 15 × 12.5 mm |
| Tongue | 72 × 5 × 14 mm; socket clearance 0.25 mm per side |
| Tongue engagement in socket | 11.1 mm (video) / 9.3 mm (reading) |
| Wall between sockets / in front of the reading socket / under the floors | 6.4 / 5.5 / 9.8 mm |
| Cable notch / underside channel | 18 mm wide / 8 × 5 mm |
| Mass at 100 % infill | Base 184 g, cradle 57 g, total 241 g |

**Largest part:** SB-01 Base, 88.0 × 88.0 × 22.0 mm, printed flat. The cradle is the longest part: 110 × 20.5 × 72 mm, printed on its side.

## 4. Print setup

| Part | Orientation | Bed footprint × height | Overhangs |
|---|---|---|---|
| SB-01 Base | Underside down, as modelled | 88 × 88 × 22 mm | One flat bridge: the ceiling of the underside cable channel at Z 5 mm, 8 mm span, held along both long sides. Sockets overhang at 20° (video) and 35° (reading) from vertical. |
| SB-02 Cradle | On its side: the L profile on the bed, width up the Z axis | 110 × 20.5 × 72 mm | One flat bridge: the ceiling of the cable slot at Z 43.5 mm, 12.5 mm span between backrest and lip (open on its 6 mm sides). No sloped overhangs. |

- Printing the cradle on its side puts every bending load (tongue, ledge, backrest) in the plane of the layers, not across them.
- It is a tall, thin print, so use a **brim**.
- For tipping resistance, print the base at **high infill (100 % recommended)**. Section 6 shows the effect.
- `stl/*_print.stl` are already in these orientations.

## 5. Checks run and results

Source: `checks.json` and `check_log.txt`, produced by `cad_source/build.py` on the remote build machine with CadQuery 2.8 / OpenCascade and trimesh. **50 of 50 checks passed** on the final build.

| Check | Result |
|---|---|
| Each part is one valid closed solid; all 5 STEP files re-import as valid solids | Pass |
| Base/cradle interference in both positions | 0.000 mm³ in both |
| Intended contact: tongue tip on socket floor | Distance 0.000; contact area 270 mm² in both |
| Sideways: free at 0.20 mm shift, blocked by end wall at 0.6 mm | Pass, both positions |
| Backrest angle measured from the placed geometry | 70.00° / 55.00° |
| Footprint < 90 × 90 | 88.0 × 88.0 mm, both positions |
| Phone envelopes 65×7×140, 80×11×168, 65×11×150: no overlap with base or cradle, resting on ledge and backrest | Pass, all 3 phones in both positions (overlap 0, contact distance 0) |
| Plug keep-out 12 × 8.5 × 30 mm clear of all parts and above the desk | Pass; lowest point 2.3 mm (video) / 6.5 mm (reading) above desk |
| Socket wall thicknesses ≥ 3 mm | 6.4 / 5.5 / 9.8 mm |
| Each part inside 220 × 220 × 250 in print orientation | Pass |
| STLs watertight | Pass |
| No sloped overhang steeper than 45° (47° allowed for STL facetting) | 0 mm² on both parts |
| Flat bridge regions | Base 8 mm span, cradle 12.5 mm span (see section 4) |

Fixes made along the way:
- **Earlier concept dropped.** I first designed a hinged cradle with a kickstand. Hand statics showed the kickstand would lift the hinge out of its seat under a large phone at the reading angle. I replaced it with the rigid tongue-in-socket layout above.
- **Overhang check corrected.** The automated check first flagged the 45° bottom chamfer. That was a threshold error and STL facetting, not a geometry problem. I corrected the threshold and re-ran everything.

## 6. Tap stability: calculation only

Model:
- Rigid bodies on a flat desk.
- A 1 N tap normal to the screen, pushing into it.
- Tipping is about the rear edge of the base. Sliding uses μ = 0.3 (assumed).
- Figures are from `analysis.json`.

| Position | Phone | Stand mass basis | Tap force to tip back: at ½ / ¾ / 95 % of phone height | Tap force to slide (μ 0.3) | μ needed for a 1 N tap |
|---|---|---|---|---|---|
| Video 70° | Large 240 g | 100 % infill (241 g) | 2.05 / 1.41 / 1.12 N | 1.69 N | 0.19 |
| Video 70° | Large 240 g | ~50 % of solid mass | 1.50 / 1.03 / 0.82 N | 1.27 N | 0.24 |
| Reading 55° | Large 240 g | 100 % infill | 2.44 / 1.52 / 1.16 N | 2.19 N | 0.15 |
| Reading 55° | Small 140 g | 100 % infill | 2.74 / 1.67 / 1.27 N | 1.74 N | 0.19 |
| Reading 55° | Small 140 g | ~50 % of solid mass | 1.79 / 1.09 / 0.83 N | 1.19 N | 0.26 |

What this means:
- With a solid base, the calculation says a 1 N tap does not tip or slide the stand anywhere on the screen.
- The margin is thin near the top of a large phone, about 1.1 N.
- At lower infill, a 1 N tap near the top edge could tip it back.
- The combined centre of gravity sits inside the footprint in every case: Y = 46–55 mm on an 88 mm deep base.
- **The real finger-tap force and the real desk friction are unknown.** Both must be measured (section 8).

Part loads, hand calculation, worst case: large phone at 55° with a 2 N tap at the top.
- Tongue root bending: 1.5 MPa.
- Ledge bending: 0.06 MPa.

These figures are low compared with typical PLA strength figures, but they are **not** a strength claim. Layer adhesion, print quality and long-term creep of PLA under constant load have not been tested.

## 7. Assumptions and limits

- **Angles:** 70° and 55° are my choice; the brief did not specify them. Each is a single parameter. Changing one re-solves socket positions and wall checks automatically.
- **Phones:** 7–11 mm thick and 140–168 mm long were checked. Phones under 7 mm will lean further toward the lip but are still held.
- **Lip coverage:** the lip covers up to 6 mm of the phone's bottom edge. On a phone with a very thin bottom bezel it may touch the lowest few millimetres of the screen.
- **Plug envelope:** 12 × 8.5 × 30 mm is assumed. Larger right-angle or long-strain-relief plugs may not fit. A thick cable (>5 mm) will not fit the 8 × 5 mm underside channel; it can use the front exit instead.
- **Socket fit:** 0.25 mm per side assumes a calibrated printer. A tight printer may need the tongue sanded or `SOCKET_CLR` raised. A loose one gives some rattle.
- **Cradle is not latched:** it sits in the socket under gravity. Lifting the stand by the cradle pulls the cradle out, by design (this is how the angle changes).
- **No feet:** there are no rubber feet (no glue allowed), so grip depends on the PLA bottom face and the desk.
- **Material and time:** a solid base is about 184 g of PLA, a long print.

## 8. Physical tests needed before relying on it

1. **Socket fit.** Print both parts. Check that the tongue drops fully into both sockets by hand and seats on the floor. Check that it doesn't rattle and comes out without tools. Adjust `SOCKET_CLR` if needed.
2. **Angle check.** With a phone in place, measure the backrest angle in both positions. Target 70° ± 2° and 55° ± 2°.
3. **Phone fit.** Test the thinnest and thickest real phones, with and without case, at 65 and 80 mm wide. Confirm the lip does not hide usable screen.
4. **Cable fit.** Test the intended USB-C and Lightning cables, plugged in while the phone is seated, in both positions. Check that both cable exits work and nothing kinks the cable.
5. **Tap test.** Measure real tap forces with a force gauge or kitchen scale. Then tap at the top, middle and bottom of the screen on the intended desk surfaces (wood, laminate, glass). Record any tipping or sliding, at the infill actually printed.
6. **Friction.** Measure μ of the printed base on the target desk with an incline or pull test, and compare it with the assumed 0.3.
7. **Durability.** Leave a 240 g phone in the reading position for several days, including a warm room or near a window (PLA softens at about 55–60 °C). Re-measure the angle and check for creep or cracks at the tongue root and ledge.
8. **Swap cycles.** Change angle many times and inspect tongue and socket for wear or loosening.

## 9. Files in ./out

- `REPORT.md`: this report.
- `step/PhoneStand_assembled_video.step`, `step/PhoneStand_assembled_reading.step`: named assemblies in each position.
- `step/PhoneStand_exploded.step`: exploded assembly.
- `step/SB-01_Base.step`, `step/SB-02_Cradle.step`: one STEP per part.
- `stl/SB-01_Base_print.stl`, `stl/SB-02_Cradle_print.stl`: print-oriented STLs.
- `renders/*.png`: assembled, in-use, side (mechanism positions), exploded and base views.
- `checks.json`, `check_log.txt`, `analysis.json`: check and statics results.
- `cad_source/`: editable parametric CadQuery source.
  - `params.py`: all named dimensions.
  - `stand.py`: the model.
  - `build.py`: exports and checks.
  - `analysis.py`: statics.
  - `render.py`: renders.
  - `run.sh`: runs all of it; expects the `.py` files in `src/` next to it.
- `mesh_world/`: placed meshes used for the renders, including the phone and plug check envelopes.
