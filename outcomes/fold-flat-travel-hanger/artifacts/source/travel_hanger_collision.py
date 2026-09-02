"""Closed, conservative box envelopes for Burr link-layer checks.

These envelopes deliberately exclude hinge pins and bores.  They conservatively
cover the hook/hub and four plastic links, so a Burr pass supports only external
separation between those five moving plates in the named static pose.
"""

from math import atan2, degrees, hypot
from typing import Literal

from build123d import Align, Axis, Box, Compound, Location

from travel_hanger import (
    CENTRAL_LEFT,
    CENTRAL_RIGHT,
    CORE_THICKNESS,
    INNER_LINK_Z,
    LINK_THICKNESS,
    OUTER_LINK_Z,
    POSE_POINTS,
)


Pose = Literal["deployed", "folded"]
Point2 = tuple[float, float]


def _link_envelope(start: Point2, end: Point2, width: float, z: float, label: str):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = hypot(dx, dy) + width
    angle = degrees(atan2(dy, dx))
    center = ((start[0] + end[0]) / 2.0, (start[1] + end[1]) / 2.0, z)
    shape = Box(
        length,
        width,
        LINK_THICKNESS,
        align=(Align.CENTER, Align.CENTER, Align.CENTER),
    ).rotate(Axis.Z, angle).moved(Location(center))
    shape.label = label
    return shape


def make_collision_envelope(pose: Pose):
    points = POSE_POINTS[pose]
    core = Box(
        76.0,
        128.0,
        CORE_THICKNESS,
        align=(Align.CENTER, Align.CENTER, Align.CENTER),
    ).moved(Location((0.0, 50.0, 0.0)))
    core.label = "hook_hub_envelope"

    parts = [
        core,
        _link_envelope(
            CENTRAL_LEFT,
            points["left_elbow"],
            20.0,
            INNER_LINK_Z,
            "left_inner_link_envelope",
        ),
        _link_envelope(
            CENTRAL_RIGHT,
            points["right_elbow"],
            20.0,
            INNER_LINK_Z,
            "right_inner_link_envelope",
        ),
        _link_envelope(
            points["left_elbow"],
            points["left_tip"],
            18.0,
            OUTER_LINK_Z,
            "left_outer_link_envelope",
        ),
        _link_envelope(
            points["right_elbow"],
            points["right_tip"],
            18.0,
            OUTER_LINK_Z,
            "right_outer_link_envelope",
        ),
    ]
    assembly = Compound(children=parts)
    assembly.label = f"travel_hanger_collision_envelope:{pose}"
    return assembly

