"""Parametric source for a layered, fold-flat travel hanger.

The hanger is modeled in the XY plane with thickness along Z.  Each pose is a
static realization of four revolute links about named Z-axis hinge centers.
Generated STEP files are derived artifacts; this module is authoritative.
"""

from __future__ import annotations

from math import atan2, degrees, hypot
from typing import Iterable, Literal, Sequence

from build123d import Align, Axis, Box, Compound, Cylinder, Location
from cadgen import srgb


Point2 = tuple[float, float]
Pose = Literal["deployed", "folded"]

# Overall assembly parameters (millimeters)
CORE_THICKNESS = 5.0
LINK_THICKNESS = 4.0
INNER_LINK_Z = 5.0
OUTER_LINK_Z = -5.0
PIVOT_HOLE_RADIUS = 2.6
PIN_RADIUS = 2.2
PIN_SHAFT_HEIGHT = 16.4
PIN_HEAD_RADIUS = 4.4
PIN_HEAD_THICKNESS = 1.2

CENTRAL_LEFT: Point2 = (-24.0, 0.0)
CENTRAL_RIGHT: Point2 = (24.0, 0.0)

POSE_POINTS: dict[Pose, dict[str, Point2]] = {
    "deployed": {
        "left_elbow": (-112.0, -48.0),
        "left_tip": (-205.0, -76.0),
        "right_elbow": (112.0, -48.0),
        "right_tip": (205.0, -76.0),
    },
    "folded": {
        "left_elbow": (-24.0, -100.0),
        "left_tip": (-24.0, -16.0),
        "right_elbow": (24.0, -100.0),
        "right_tip": (24.0, -16.0),
    },
}


def _at(shape, x: float, y: float, z: float = 0.0):
    return shape.moved(Location((x, y, z)))


def _capsule_between(
    start: Point2,
    end: Point2,
    width: float,
    thickness: float,
    z_center: float,
):
    """Make a straight, round-ended prism between endpoint centers."""
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = hypot(dx, dy)
    angle = degrees(atan2(dy, dx))
    midpoint = ((start[0] + end[0]) / 2.0, (start[1] + end[1]) / 2.0)

    beam = Box(
        length,
        width,
        thickness,
        align=(Align.CENTER, Align.CENTER, Align.CENTER),
    ).rotate(Axis.Z, angle)
    beam = _at(beam, midpoint[0], midpoint[1], z_center)
    end_a = _at(
        Cylinder(
            width / 2.0,
            thickness,
            align=(Align.CENTER, Align.CENTER, Align.CENTER),
        ),
        start[0],
        start[1],
        z_center,
    )
    end_b = _at(
        Cylinder(
            width / 2.0,
            thickness,
            align=(Align.CENTER, Align.CENTER, Align.CENTER),
        ),
        end[0],
        end[1],
        z_center,
    )
    return beam.fuse(end_a, end_b)


def _point_on_segment(start: Point2, end: Point2, fraction: float) -> Point2:
    return (
        start[0] + (end[0] - start[0]) * fraction,
        start[1] + (end[1] - start[1]) * fraction,
    )


def _cut_cylinders(body, centers: Iterable[Point2], radius: float, z_center: float):
    cutters = [
        _at(
            Cylinder(
                radius,
                LINK_THICKNESS + 2.0,
                align=(Align.CENTER, Align.CENTER, Align.CENTER),
            ),
            x,
            y,
            z_center,
        )
        for x, y in centers
    ]
    return body.cut(*cutters)


def _make_link(
    start: Point2,
    end: Point2,
    width: float,
    z_center: float,
    label: str,
    color_hex: str,
    pivot_centers: Sequence[Point2],
    slot_span: tuple[float, float],
    slot_width: float,
    strap_loop: bool = False,
):
    body = _capsule_between(start, end, width, LINK_THICKNESS, z_center)
    body = _cut_cylinders(body, pivot_centers, PIVOT_HOLE_RADIUS, z_center)

    slot_start = _point_on_segment(start, end, slot_span[0])
    slot_end = _point_on_segment(start, end, slot_span[1])
    slot = _capsule_between(
        slot_start,
        slot_end,
        slot_width,
        LINK_THICKNESS + 2.0,
        z_center,
    )
    body = body.cut(slot)

    if strap_loop:
        strap_center = _point_on_segment(start, end, 0.84)
        body = _cut_cylinders(body, [strap_center], 3.2, z_center)

    body.label = label
    body.color = srgb(color_hex)
    return body


def _make_core():
    """Monolithic hook and hub with two central pivot bores."""
    hub = Box(
        48.0,
        28.0,
        CORE_THICKNESS,
        align=(Align.CENTER, Align.CENTER, Align.CENTER),
    )
    hub = hub.fuse(
        _at(
            Cylinder(14.0, CORE_THICKNESS, align=(Align.CENTER,) * 3),
            CENTRAL_LEFT[0],
            CENTRAL_LEFT[1],
        ),
        _at(
            Cylinder(14.0, CORE_THICKNESS, align=(Align.CENTER,) * 3),
            CENTRAL_RIGHT[0],
            CENTRAL_RIGHT[1],
        ),
    )

    neck = _at(
        Box(16.0, 62.0, CORE_THICKNESS, align=(Align.CENTER,) * 3),
        -8.0,
        29.0,
    )
    hook_outer = _at(
        Cylinder(34.0, CORE_THICKNESS, align=(Align.CENTER,) * 3),
        0.0,
        80.0,
    )
    hook_inner = _at(
        Cylinder(21.0, CORE_THICKNESS + 2.0, align=(Align.CENTER,) * 3),
        0.0,
        80.0,
    )
    hook_ring = hook_outer.cut(hook_inner)
    hook_opening = _at(
        Box(48.0, 32.0, CORE_THICKNESS + 2.0, align=(Align.CENTER,) * 3),
        24.0,
        56.0,
    )
    hook_ring = hook_ring.cut(hook_opening)

    core = hub.fuse(neck, hook_ring)
    core = _cut_cylinders(
        core,
        [CENTRAL_LEFT, CENTRAL_RIGHT],
        PIVOT_HOLE_RADIUS,
        0.0,
    )
    core.label = "hook_hub"
    core.color = srgb("#1F2937")
    return core


def _make_pin(center: Point2, label: str):
    shaft = _at(
        Cylinder(
            PIN_RADIUS,
            PIN_SHAFT_HEIGHT,
            align=(Align.CENTER, Align.CENTER, Align.CENTER),
        ),
        center[0],
        center[1],
    )
    head_z = PIN_SHAFT_HEIGHT / 2.0 + PIN_HEAD_THICKNESS / 2.0
    top_head = _at(
        Cylinder(
            PIN_HEAD_RADIUS,
            PIN_HEAD_THICKNESS,
            align=(Align.CENTER, Align.CENTER, Align.CENTER),
        ),
        center[0],
        center[1],
        head_z,
    )
    bottom_head = _at(
        Cylinder(
            PIN_HEAD_RADIUS,
            PIN_HEAD_THICKNESS,
            align=(Align.CENTER, Align.CENTER, Align.CENTER),
        ),
        center[0],
        center[1],
        -head_z,
    )
    pin = shaft.fuse(top_head, bottom_head)
    pin.label = label
    pin.color = srgb("#F59E0B")
    return pin


def make_hanger(pose: Pose = "deployed"):
    """Return the labeled assembly in one of its two source-defined poses."""
    points = POSE_POINTS[pose]
    left_elbow = points["left_elbow"]
    right_elbow = points["right_elbow"]
    left_tip = points["left_tip"]
    right_tip = points["right_tip"]

    components = [
        _make_core(),
        _make_link(
            CENTRAL_LEFT,
            left_elbow,
            20.0,
            INNER_LINK_Z,
            "left_inner_link",
            "#14B8A6",
            [CENTRAL_LEFT, left_elbow],
            (0.28, 0.70),
            7.5,
        ),
        _make_link(
            CENTRAL_RIGHT,
            right_elbow,
            20.0,
            INNER_LINK_Z,
            "right_inner_link",
            "#14B8A6",
            [CENTRAL_RIGHT, right_elbow],
            (0.28, 0.70),
            7.5,
        ),
        _make_link(
            left_elbow,
            left_tip,
            18.0,
            OUTER_LINK_Z,
            "left_outer_link",
            "#FB7185",
            [left_elbow],
            (0.22, 0.60),
            6.5,
            strap_loop=True,
        ),
        _make_link(
            right_elbow,
            right_tip,
            18.0,
            OUTER_LINK_Z,
            "right_outer_link",
            "#FB7185",
            [right_elbow],
            (0.22, 0.60),
            6.5,
            strap_loop=True,
        ),
        _make_pin(CENTRAL_LEFT, "left_hub_pin"),
        _make_pin(CENTRAL_RIGHT, "right_hub_pin"),
        _make_pin(left_elbow, "left_elbow_pin"),
        _make_pin(right_elbow, "right_elbow_pin"),
    ]

    assembly = Compound(children=components)
    assembly.label = f"fold_flat_travel_hanger:{pose}"
    return assembly
