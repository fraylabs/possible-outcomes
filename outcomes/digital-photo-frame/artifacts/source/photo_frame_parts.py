"""Parametric mechanical authority for the cleanroom seven-inch photo frame.

Coordinate convention: product origin is the center of the front face; X is
landscape-right, Y is up, and +Z points toward the rear of the product.
"""

from build123d import *
from cadgen import srgb

OUTER_W = 216.0
OUTER_H = 138.0
FRONT_T = 4.0
ENCLOSURE_BACK_Z = 29.0
CORNER_R = 8.0

DISPLAY_W = 180.0
DISPLAY_H = 100.0
DISPLAY_T = 12.8
DISPLAY_FRONT_Z = 4.5
ACTIVE_W = 154.08
ACTIVE_H = 85.92

PCB_W = 112.0
PCB_H = 70.0
PCB_T = 1.6
PCB_CENTER_X = 42.0
PCB_CENTER_Y = 0.0
PCB_Z = 18.5
PCB_HOLES = [(-10.0, -31.0), (94.0, -31.0), (-10.0, 31.0), (94.0, 31.0)]

HINGE_Y = 35.0
HINGE_Z = 29.0
STAND_W = 140.0
STAND_H = 105.0
STAND_T = 4.0
DEPLOY_ANGLE_DEG = -18.0


def rounded_prism(width: float, height: float, depth: float, radius: float, z: float = 0.0):
    with BuildPart() as part:
        with BuildSketch(Plane.XY.offset(z)):
            RectangleRounded(width, height, radius)
        extrude(amount=depth)
    return part.part


def colored(shape, label: str, hex_color: str, alpha: float = 1.0):
    shape.label = label
    shape.color = srgb(hex_color, alpha)
    return shape


def make_front_bezel():
    outer = rounded_prism(OUTER_W, OUTER_H, FRONT_T, CORNER_R, 0.0)
    window = rounded_prism(ACTIVE_W + 4.0, ACTIVE_H + 4.0, FRONT_T + 2.0, 3.0, -1.0)
    bezel = outer - window
    # A rear ledge locates the module by its metal frame, not the active glass.
    ledge_outer = rounded_prism(DISPLAY_W + 4.0, DISPLAY_H + 4.0, 2.5, 3.0, FRONT_T)
    ledge_inner = rounded_prism(DISPLAY_W + 0.6, DISPLAY_H + 0.6, 3.5, 2.0, FRONT_T - 0.5)
    bezel = bezel + (ledge_outer - ledge_inner)
    return colored(bezel, "front_bezel_with_display_ledge", "#26282D")


def make_rear_chassis():
    outer = rounded_prism(OUTER_W, OUTER_H, 23.0, CORNER_R, 4.0)
    cavity = rounded_prism(206.0, 128.0, 25.0, 5.0, 3.0)
    chassis = outer - cavity
    # Side connector apertures are tied to the KiCad coordinate mapping.
    usb_cut = Box(8.0, 14.0, 7.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).located(Location((106.0, -23.0, 17.0)))
    sd_cut = Box(8.0, 18.0, 6.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).located(Location((106.0, 15.0, 17.0)))
    chassis = chassis - [usb_cut, sd_cut]
    # Insert bosses for the reusable M3 service-cover fasteners.
    for x in (-98.0, 98.0):
        for y in (-59.0, 59.0):
            boss = Cylinder(5.0, 8.0).located(Location((x, y, 19.0)))
            hole = Cylinder(2.35, 10.0).located(Location((x, y, 18.0)))
            chassis = chassis + (boss - hole)
    # PCB standoffs and ribs start at the documented display rear envelope.
    for x, y in PCB_HOLES:
        post = Cylinder(4.0, PCB_Z - (DISPLAY_FRONT_Z + DISPLAY_T)).located(Location((x, y, DISPLAY_FRONT_Z + DISPLAY_T)))
        bore = Cylinder(1.7, 4.0).located(Location((x, y, DISPLAY_FRONT_Z + DISPLAY_T - 0.5)))
        direction = 1.0 if y > 0 else -1.0
        rib_h = 64.0 - abs(y)
        rib = Box(5.0, rib_h, PCB_Z - (DISPLAY_FRONT_Z + DISPLAY_T), align=(Align.CENTER, Align.CENTER, Align.MIN)).located(
            Location((x, y + direction * rib_h / 2.0, DISPLAY_FRONT_Z + DISPLAY_T))
        )
        chassis = chassis + (post - bore) + rib
    # Hinge blocks and deployed hard-stop shoulders are part of the chassis.
    for x in (-66.0, 66.0):
        block = Box(12.0, 9.0, 5.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).located(Location((x, HINGE_Y, 24.0)))
        hinge_hole = Cylinder(2.6, 14.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).rotate(Axis.Y, 90).moved(Location((x-7.0, HINGE_Y, HINGE_Z)))
        chassis = chassis + (block - hinge_hole)
        stop = Box(10.0, 7.0, 2.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).located(Location((x, HINGE_Y-6.0, 27.0)))
        chassis = chassis + stop
    return colored(chassis, "rear_chassis_with_standoffs_and_hinge_stops", "#30333A")


def make_service_cover():
    cover = rounded_prism(208.0, 130.0, 2.0, 6.0, 27.0)
    cuts = []
    for x in (-98.0, 98.0):
        for y in (-59.0, 59.0):
            cuts.append(Cylinder(1.8, 4.0).located(Location((x, y, 26.0))))
    # Controller/power ventilation: ten narrow vertical slots.
    for x in range(-5, 76, 9):
        cuts.append(Box(3.0, 24.0, 4.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).located(Location((float(x), -8.0, 26.0))))
    # Rear-access button, ambient-light, and status-LED openings.
    for x in (52.0, 62.0, 72.0):
        cuts.append(Cylinder(2.3, 4.0).located(Location((x, 19.0, 26.0))))
    cuts.append(Cylinder(2.0, 4.0).located(Location((29.0, 25.0, 26.0))))
    cuts.append(Cylinder(1.2, 4.0).located(Location((41.0, 21.0, 26.0))))
    cover = cover - cuts
    return colored(cover, "removable_service_cover", "#3A3D44")


def make_stand():
    plate = rounded_prism(STAND_W, STAND_H, STAND_T, 7.0, 0.0).located(Location((0.0, -STAND_H / 2.0, 0.0)))
    barrel = Cylinder(4.2, STAND_W - 12.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).rotate(Axis.Y, 90).moved(Location((-(STAND_W-12.0)/2.0, 0.0, 2.0)))
    stand = plate + barrel
    # Detent bumps engage the cover dimples when folded; stop tabs engage the chassis when open.
    for x in (-58.0, 58.0):
        stand = stand + Sphere(2.0).located(Location((x, -78.0, 1.0)))
        stand = stand + Box(8.0, 5.0, 4.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).located(Location((x, -3.0, 0.0)))
    return colored(stand, "folding_easel_stand_with_detents", "#25272C")


def make_display_envelope():
    envelope = Box(DISPLAY_W, DISPLAY_H, DISPLAY_T, align=(Align.CENTER, Align.CENTER, Align.MIN)).located(Location((0,0,DISPLAY_FRONT_Z)))
    active = Box(ACTIVE_W, ACTIVE_H, 0.35, align=(Align.CENTER, Align.CENTER, Align.MIN)).located(Location((0,0,DISPLAY_FRONT_Z-0.35)))
    return Compound(children=[
        colored(envelope, "ER-TFTM070-4V3_documented_max_envelope", "#5D626B"),
        colored(active, "display_active_area_154p08x85p92", "#111722"),
    ], label="display_subsystem")


def make_pcb_envelope():
    board = Box(PCB_W, PCB_H, PCB_T, align=(Align.CENTER, Align.CENTER, Align.MIN)).located(Location((PCB_CENTER_X, PCB_CENTER_Y, PCB_Z)))
    components = Box(PCB_W, PCB_H, 4.5, align=(Align.CENTER, Align.CENTER, Align.MIN)).located(Location((PCB_CENTER_X, PCB_CENTER_Y, PCB_Z + PCB_T)))
    return Compound(children=[
        colored(board, "pcb_112x70x1p6", "#147A4A"),
        colored(components, "unverified_populated_component_envelope_4p5mm", "#2F5D49", 0.55),
    ], label="populated_pcb_conservative_envelope")


def stand_pose(angle_deg: float):
    stand = make_stand().located(Location((0.0, HINGE_Y, HINGE_Z)))
    return stand.rotate(Axis((0.0, HINGE_Y, HINGE_Z), (1.0, 0.0, 0.0)), angle_deg)


def make_product(angle_deg: float = DEPLOY_ANGLE_DEG, exploded: bool = False):
    front = make_front_bezel()
    chassis = make_rear_chassis()
    cover = make_service_cover()
    display = make_display_envelope()
    pcb = make_pcb_envelope()
    stand = stand_pose(angle_deg)
    if exploded:
        cover = cover.moved(Location((0,0,35)))
        stand = stand.moved(Location((0,0,48)))
        pcb = pcb.moved(Location((-35,0,28)))
    return Compound(children=[front, chassis, cover, display, pcb, stand], label="digital_photo_frame")
