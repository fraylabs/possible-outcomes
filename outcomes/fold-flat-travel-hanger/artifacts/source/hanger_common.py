"""Authoritative parametric geometry for the Fray fold-flat travel hanger.

Units: millimetres.
Assembly axes: X is shoulder width, Y is front/back thickness, Z is vertical.
Part geometry is authored at named joint datums and placed with rigid Locations.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from build123d import Align, Axis, Box, Compound, Cylinder, Face, Location, Plane, Wire, fillet, extrude
from cadgen import srgb
from cadgen.assembly import AssemblyHelper


# Primary envelope and interface parameters.
DEPLOYED_SHOULDER_WIDTH = 442.0
FOLDED_TARGET = (230.0, 90.0, 30.0)
ARM_PIVOT_X = 29.0
ARM_BEAM_END_X = 184.0
ARM_TIP_RADIUS = 8.0
ARM_THICKNESS_Y = 7.0
ARM_HINGE_RADIUS = 9.5
PIN_DIAMETER = 5.0
PIN_BORE_DIAMETER = 5.6
PIN_RADIAL_CLEARANCE = (PIN_BORE_DIAMETER - PIN_DIAMETER) / 2.0
ARM_AXIAL_CLEARANCE_EACH_SIDE = 1.0
HOOK_AXIAL_CLEARANCE_EACH_SIDE = 0.5
LOCK_FACE_ENGAGEMENT = 6.0
LOCK_RELEASE_TRAVEL = 7.5
LOCK_RELEASE_CLEARANCE = 1.0
HOOK_INNER_RADIUS = 21.0
HOOK_ROD_MAX_DIAMETER = 38.0
HOOK_THROAT_OPENING = 40.0
HOOK_PIVOT = (0.0, 12.5, 20.0)
LEFT_ARM_PIVOT = (-ARM_PIVOT_X, 0.0, 0.0)
RIGHT_ARM_PIVOT = (ARM_PIVOT_X, 0.0, 0.0)


@dataclass(frozen=True)
class Pose:
    name: str
    arm_angle_deg: float
    hook_angle_deg: float
    lock_release_mm: float


POSES = {
    "deployed": Pose("deployed", 0.0, 0.0, 0.0),
    "fold_25": Pose("fold_25", 20.5, 45.0, LOCK_RELEASE_TRAVEL),
    "fold_50": Pose("fold_50", 41.0, 90.0, LOCK_RELEASE_TRAVEL),
    "fold_75": Pose("fold_75", 61.5, 135.0, LOCK_RELEASE_TRAVEL),
    "folded": Pose("folded", 82.0, 180.0, LOCK_RELEASE_TRAVEL),
}


JOINT_DATUMS = {
    "left_arm_fold_joint": {"origin": LEFT_ARM_PIVOT, "axis": (0.0, 1.0, 0.0)},
    "right_arm_fold_joint": {"origin": RIGHT_ARM_PIVOT, "axis": (0.0, 1.0, 0.0)},
    "hook_fold_joint": {"origin": HOOK_PIVOT, "axis": (0.0, 1.0, 0.0)},
    "positive_lock_release_slide": {"origin": (0.0, 0.0, -15.0), "axis": (0.0, 1.0, 0.0)},
}


COLORS = {
    "center": srgb("#26364A"),
    "left": srgb("#4C8CFF"),
    "right": srgb("#58A6FF"),
    "hook": srgb("#D6E4F0"),
    "lock": srgb("#F4A261"),
    "pin": srgb("#9AA7B1"),
    "nut": srgb("#697782"),
}


def _cylinder_y(radius: float, length: float):
    return Cylinder(radius, length, align=(None, None, None)).located(
        Location((0.0, length / 2.0, 0.0), (90.0, 0.0, 0.0))
    )


def _centered_cylinder_y(radius: float, length: float):
    # The combined Location in ``_cylinder_y`` rotates its translation with the
    # cylinder, leaving the Y-axis length centered at the local origin.
    return _cylinder_y(radius, length)


def _move(shape, x: float = 0.0, y: float = 0.0, z: float = 0.0):
    return shape.moved(Location((x, y, z)))


def make_center_yoke():
    """One printed yoke with arm cheek plates, lock guide slots and hook clevis."""

    plate = Box(88.0, 4.0, 54.0, align=(None, None, None))
    back = plate.moved(Location((-44.0, -8.5, -26.0)))
    front = plate.moved(Location((-44.0, 4.5, -26.0)))

    top_bridge = Box(28.0, 9.4, 8.0, align=(None, None, None)).moved(
        Location((-14.0, -4.7, 20.0))
    )
    bottom_bridge = Box(28.0, 9.4, 6.0, align=(None, None, None)).moved(
        Location((-14.0, -4.7, -26.0))
    )

    # The hook occupies a separate front layer so it can fold between the arms
    # without hidden overlap. Two clevis plates and an outboard spine capture it.
    rear_hook_cheek = Box(24.0, 1.7, 16.0, align=(None, None, None)).moved(
        Location((-16.0, 8.3, 12.0))
    )
    front_hook_cheek = Box(24.0, 1.5, 16.0, align=(None, None, None)).moved(
        Location((-16.0, 15.0, 12.0))
    )
    hook_spine = Box(6.0, 8.2, 16.0, align=(None, None, None)).moved(
        Location((-16.0, 8.3, 12.0))
    )

    yoke = back + [
        front,
        top_bridge,
        bottom_bridge,
        rear_hook_cheek,
        front_hook_cheek,
        hook_spine,
    ]

    lock_passage = Box(80.0, 24.0, 8.0, align=(None, None, None)).moved(
        Location((-40.0, -10.0, -18.0))
    )
    arm_bores = [
        _move(_centered_cylinder_y(PIN_BORE_DIAMETER / 2.0, 24.0), x=side * ARM_PIVOT_X)
        for side in (-1.0, 1.0)
    ]
    hook_bore = _move(
        _centered_cylinder_y(PIN_BORE_DIAMETER / 2.0, 34.0),
        y=4.5,
        z=20.0,
    )
    yoke = yoke - [lock_passage, *arm_bores, hook_bore]
    yoke.label = "center_yoke"
    yoke.color = COLORS["center"]
    return yoke


def _make_right_arm_unlabelled():
    # Deep trapezoidal beam: 18 mm at the root and 16 mm at the rounded tip.
    profile = Face(
        Wire.make_polygon(
            [
                (0.0, -8.0),
                (ARM_BEAM_END_X, -38.0),
                (ARM_BEAM_END_X, -22.0),
                (0.0, 10.0),
            ],
            close=True,
        )
    )
    beam = extrude(profile, ARM_THICKNESS_Y / 2.0, both=True).rotate(Axis.X, 90.0)
    try:
        beam = fillet(beam.edges(), radius=1.6)
    except Exception:
        # The controlling trapezoid remains a thick, closed beam if an OCC build
        # rejects a cosmetic fillet; validation and snapshots expose the result.
        pass

    hinge = _centered_cylinder_y(ARM_HINGE_RADIUS, ARM_THICKNESS_Y)
    tip = _move(
        _centered_cylinder_y(ARM_TIP_RADIUS, ARM_THICKNESS_Y),
        x=ARM_BEAM_END_X,
        z=-30.0,
    )
    # The solid heel is the load stop. Its bottom face overlaps the rigid lock
    # ear by 6 mm in X and bears on the bar's horizontal top face at Z=-12.
    stop_heel = Box(8.0, ARM_THICKNESS_Y, 4.5, align=(None, None, None)).moved(
        Location((4.0, -ARM_THICKNESS_Y / 2.0, -12.0))
    )
    arm = beam + [hinge, tip, stop_heel]

    bore = _centered_cylinder_y(PIN_BORE_DIAMETER / 2.0, ARM_THICKNESS_Y + 2.0)
    top_at_notch = 10.0 + (-32.0 / ARM_BEAM_END_X) * 154.0
    strap_notch = _move(
        _centered_cylinder_y(4.5, ARM_THICKNESS_Y + 2.0),
        x=154.0,
        z=top_at_notch + 1.5,
    )
    return arm - [bore, strap_notch]


def make_right_arm():
    arm = _make_right_arm_unlabelled()
    arm.label = "right_shoulder_arm"
    arm.color = COLORS["right"]
    return arm


def make_left_arm():
    arm = _make_right_arm_unlabelled().mirror(Plane.YZ)
    arm.label = "left_shoulder_arm"
    arm.color = COLORS["left"]
    return arm


def make_hook():
    """Folding C-hook with a 42 mm rod pocket and 40 mm horizontal throat."""

    outer = _centered_cylinder_y(30.0, 4.0)
    inner = _centered_cylinder_y(HOOK_INNER_RADIUS, 6.0)
    ring = _move(outer - inner, x=10.0, z=55.0)
    throat = Box(36.0, 8.0, HOOK_THROAT_OPENING, align=(None, None, None)).moved(
        Location((10.0, -4.0, 35.0))
    )
    ring = ring - throat

    eye = _centered_cylinder_y(8.5, 4.0)
    stem = Box(7.0, 4.0, 36.0, align=(None, None, None)).moved(
        Location((-8.0, -2.0, 0.0))
    )
    hook = eye + [stem, ring]
    bore = _centered_cylinder_y(PIN_BORE_DIAMETER / 2.0, 6.0)
    hook = hook - bore
    hook.label = "folding_hook"
    hook.color = COLORS["hook"]
    return hook


def make_lock_bar():
    """Rigid, linked dual-ear hard stop; release is axial, not a flexure."""

    bar = Box(78.0, 6.0, 6.0, align=(None, None, None)).moved(
        Location((-39.0, -3.0, -18.0))
    )
    thumb_pad = Box(20.0, 5.5, 4.0, align=(None, None, None)).moved(
        Location((-10.0, -8.5, -17.0))
    )
    lock_bar = bar + thumb_pad
    lock_bar.label = "dual_positive_lock_bar"
    lock_bar.color = COLORS["lock"]
    return lock_bar


def make_arm_shoulder_pin():
    shaft = _centered_cylinder_y(PIN_DIAMETER / 2.0, 18.0)
    head = _move(_centered_cylinder_y(4.5, 2.0), y=-10.0)
    pin = shaft + head
    pin.label = "m5_arm_shoulder_screw"
    pin.color = COLORS["pin"]
    return pin


def make_hook_shoulder_pin():
    shaft = _centered_cylinder_y(PIN_DIAMETER / 2.0, 26.25)
    head = _move(_centered_cylinder_y(4.5, 1.75), y=14.0)
    pin = shaft + head
    pin.label = "m5_hook_shoulder_screw"
    pin.color = COLORS["pin"]
    return pin


def make_locknut():
    # Simplified purchased-hardware envelope. A square prism keeps the axis
    # baked into the BREP so assembly Locations remain transform-only.
    nut = Box(8.6, 1.5, 8.6, align=(Align.CENTER, Align.CENTER, Align.CENTER))
    nut.label = "m5_low_profile_locknut_envelope"
    nut.color = COLORS["nut"]
    return nut


def _place(shape, translation, rotation=(0.0, 0.0, 0.0)):
    # Every component factory returns geometry in its part-local joint frame;
    # assign one occurrence Location so STEP keeps geometry unchanged by pose.
    return shape.located(Location(translation, rotation))


def build_pose_components(pose_name: str):
    """Materialize world shapes for Boolean validation from instance datums."""

    return {
        label: prototype.moved(location)
        for prototype, location, label in build_pose_instances(pose_name)
    }


def build_pose_instances(pose_name: str):
    """Identical prototypes plus pose-only rigid Locations for STEP occurrences."""

    pose = POSES[pose_name]
    return [
        (make_center_yoke(), Location(), "center_yoke"),
        (
            make_left_arm(),
            Location(LEFT_ARM_PIVOT, (0.0, -pose.arm_angle_deg, 0.0)),
            "left_shoulder_arm",
        ),
        (
            make_right_arm(),
            Location(RIGHT_ARM_PIVOT, (0.0, pose.arm_angle_deg, 0.0)),
            "right_shoulder_arm",
        ),
        (
            make_hook(),
            Location(HOOK_PIVOT, (0.0, pose.hook_angle_deg, 0.0)),
            "folding_hook",
        ),
        (
            make_lock_bar(),
            Location((0.0, pose.lock_release_mm, 0.0)),
            "dual_positive_lock_bar",
        ),
        (make_arm_shoulder_pin(), Location(LEFT_ARM_PIVOT), "left_arm_pin"),
        (make_arm_shoulder_pin(), Location(RIGHT_ARM_PIVOT), "right_arm_pin"),
        (make_hook_shoulder_pin(), Location((0.0, 4.125, 20.0)), "hook_pin"),
        (make_locknut(), Location((-ARM_PIVOT_X, 9.75, 0.0)), "left_arm_locknut"),
        (make_locknut(), Location((ARM_PIVOT_X, 9.75, 0.0)), "right_arm_locknut"),
        (make_locknut(), Location((0.0, -9.75, 20.0)), "hook_locknut"),
    ]


def build_pose_children(pose_name: str):
    children = []
    for prototype, location, label in build_pose_instances(pose_name):
        child = prototype.located(location)
        child.label = label
        children.append(child)
    return children


def make_pose_assembly(pose_name: str):
    pose = POSES[pose_name]
    return Compound(children=build_pose_children(pose_name), label=f"travel_hanger_{pose.name}")


def make_lock_detail(released: bool):
    name = "lock_detail_released" if released else "lock_detail_engaged"
    return Compound(children=build_lock_detail_children(released), label=name)


def build_lock_detail_instances(released: bool):
    lock_y = LOCK_RELEASE_TRAVEL if released else 0.0
    return [
        (make_center_yoke(), Location(), "center_yoke"),
        (make_left_arm(), Location(LEFT_ARM_PIVOT), "left_shoulder_arm"),
        (make_right_arm(), Location(RIGHT_ARM_PIVOT), "right_shoulder_arm"),
        (make_lock_bar(), Location((0.0, lock_y, 0.0)), "dual_positive_lock_bar"),
        (make_arm_shoulder_pin(), Location(LEFT_ARM_PIVOT), "left_arm_pin"),
        (make_arm_shoulder_pin(), Location(RIGHT_ARM_PIVOT), "right_arm_pin"),
        (make_locknut(), Location((-ARM_PIVOT_X, 9.75, 0.0)), "left_arm_locknut"),
        (make_locknut(), Location((ARM_PIVOT_X, 9.75, 0.0)), "right_arm_locknut"),
    ]


def build_lock_detail_children(released: bool):
    children = []
    for prototype, location, label in build_lock_detail_instances(released):
        child = prototype.located(location)
        child.label = label
        children.append(child)
    return children


def make_exploded_assembly():
    return Compound(children=build_exploded_children(), label="travel_hanger_exploded")


def build_exploded_instances():
    components = build_pose_instances("deployed")
    # Assembly-order explosion along Y; every source component remains unchanged.
    offsets = {
        "center_yoke": 0.0,
        "left_shoulder_arm": -28.0,
        "right_shoulder_arm": 28.0,
        "folding_hook": 42.0,
        "dual_positive_lock_bar": -42.0,
        "left_arm_pin": -56.0,
        "right_arm_pin": -56.0,
        "hook_pin": 58.0,
        "left_arm_locknut": 56.0,
        "right_arm_locknut": 56.0,
        "hook_locknut": 70.0,
    }
    return [
        (prototype, location * Location((0.0, offsets[label], 0.0)), label)
        for prototype, location, label in components
    ]


def build_exploded_children():
    children = []
    for prototype, location, label in build_exploded_instances():
        child = prototype.located(location)
        child.label = label
        children.append(child)
    return children


def envelope_dimensions(shape):
    bbox = shape.bounding_box()
    return (
        bbox.max.X - bbox.min.X,
        bbox.max.Y - bbox.min.Y,
        bbox.max.Z - bbox.min.Z,
    )


def assert_source_contract():
    assert math.isclose(PIN_RADIAL_CLEARANCE, 0.3, abs_tol=1e-9)
    assert LOCK_FACE_ENGAGEMENT >= 3.0
    assert HOOK_INNER_RADIUS * 2.0 - HOOK_ROD_MAX_DIAMETER == 4.0
    assert HOOK_THROAT_OPENING - HOOK_ROD_MAX_DIAMETER == 2.0
    assert len(build_pose_components("deployed")) == len(build_pose_components("folded"))


assert_source_contract()
