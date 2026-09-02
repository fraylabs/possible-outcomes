"""Parametric concept assembly for a desk-standing digital photo frame.

Coordinate convention:
    XY is the display plane, +X right, +Y up, and +Z toward the viewer.
    The bezel rear datum is Z=0 and remains the fixed assembly reference.
"""

from math import cos, radians, sin

from build123d import Axis, Cylinder, Location, RectangleRounded, extrude
from cadgen import srgb
from cadgen.assembly import AssemblyHelper


# Face and aperture
FRAME_WIDTH = 274.0
FRAME_HEIGHT = 186.0
FRAME_RADIUS = 18.0
APERTURE_WIDTH = 224.0
APERTURE_HEIGHT = 140.0
APERTURE_RADIUS = 8.0

# Layer depths (Z points toward the viewer)
BEZEL_REAR_DEPTH = 6.0
BEZEL_FRONT_DEPTH = 3.0
GLASS_THICKNESS = 2.0
DISPLAY_THICKNESS = 3.2
REAR_HOUSING_DEPTH = 14.0

# Stand geometry
STAND_WIDTH = 82.0
STAND_LENGTH = 136.0
STAND_THICKNESS = 8.0
STAND_ANGLE_DEG = 22.5


def rounded_slab(width: float, height: float, radius: float, depth: float):
    """Extrude a centred rounded rectangle from Z=0 to Z=depth."""

    return extrude(RectangleRounded(width, height, radius).face(), amount=depth)


def rounded_ring(
    outer_width: float,
    outer_height: float,
    outer_radius: float,
    inner_width: float,
    inner_height: float,
    inner_radius: float,
    depth: float,
):
    """Extrude a closed rounded-rectangle ring from Z=0 to Z=depth."""

    outer = RectangleRounded(outer_width, outer_height, outer_radius).face()
    inner = RectangleRounded(inner_width, inner_height, inner_radius).face()
    return extrude(outer - inner, amount=depth)


def make_bezel():
    """Two-step floating bezel fused into one manufactured component."""

    rear = rounded_ring(
        FRAME_WIDTH,
        FRAME_HEIGHT,
        FRAME_RADIUS,
        APERTURE_WIDTH,
        APERTURE_HEIGHT,
        APERTURE_RADIUS,
        BEZEL_REAR_DEPTH,
    )
    front = rounded_ring(
        FRAME_WIDTH - 4.0,
        FRAME_HEIGHT - 4.0,
        FRAME_RADIUS - 2.0,
        APERTURE_WIDTH + 4.0,
        APERTURE_HEIGHT + 4.0,
        APERTURE_RADIUS + 2.0,
        BEZEL_FRONT_DEPTH,
    ).moved(Location((0, 0, BEZEL_REAR_DEPTH)))
    return rear.fuse(front)


def make_stand():
    """Rounded easel stand authored around an X-axis hinge pose."""

    stand = rounded_slab(
        STAND_WIDTH,
        STAND_LENGTH,
        8.0,
        STAND_THICKNESS,
    ).moved(Location((0, 0, -STAND_THICKNESS / 2.0)))
    stand = stand.rotate(Axis.X, STAND_ANGLE_DEG)

    # Keep the angled leaf clear of the housing, then fuse in a hinge roll whose
    # front tangent meets the housing back plane without volume interference.
    half_length = STAND_LENGTH / 2.0
    half_thickness = STAND_THICKNESS / 2.0
    theta = radians(STAND_ANGLE_DEG)
    upper_surface_z_offset = half_length * sin(theta) + half_thickness * cos(theta)
    housing_back_z = -DISPLAY_THICKNESS - 1.0 - REAR_HOUSING_DEPTH
    stand_center_z = housing_back_z - 0.6 - upper_surface_z_offset
    stand_center_y = -28.0
    stand = stand.moved(Location((0, stand_center_y, stand_center_z)))

    hinge_radius = 4.0
    upper_center_y = stand_center_y + half_length * cos(theta)
    hinge = Cylinder(hinge_radius, STAND_WIDTH).rotate(Axis.Y, 90.0).moved(
        Location((0, upper_center_y, housing_back_z - hinge_radius))
    )
    return stand.fuse(hinge)


def gen_step():
    asm = AssemblyHelper("halo_digital_photo_frame")

    bezel = asm.add(make_bezel(), "floating_bezel", color=srgb("#20242D"))
    glass = asm.add(
        rounded_slab(218.0, 134.0, 6.0, GLASS_THICKNESS).moved(Location((0, 0, 1.0))),
        "display_glass",
        color=srgb("#213B57", 0.42),
    )
    display = asm.add(
        rounded_slab(219.0, 135.0, 5.5, DISPLAY_THICKNESS).moved(
            Location((0, 0, -DISPLAY_THICKNESS - 0.4))
        ),
        "display_module",
        color=srgb("#111827"),
    )
    housing_front_z = -DISPLAY_THICKNESS - 1.0
    housing = asm.add(
        rounded_slab(246.0, 160.0, 14.0, REAR_HOUSING_DEPTH).moved(
            Location((0, 0, housing_front_z - REAR_HOUSING_DEPTH))
        ),
        "rear_housing",
        color=srgb("#353B47"),
    )
    accent = asm.add(
        rounded_slab(108.0, 4.0, 1.9, 1.4).moved(
            Location((0, -80.0, BEZEL_REAR_DEPTH + BEZEL_FRONT_DEPTH))
        ),
        "cyan_accent",
        color=srgb("#2DD4BF"),
    )
    stand = asm.add(make_stand(), "easel_stand", color=srgb("#171A21"))

    # Named source datums retain assembly intent even though STEP exports the
    # resolved static pose. The bezel is the fixed reference component.
    asm.rigid_frame(bezel, "rear_datum", Location((0, 0, 0)))
    asm.rigid_frame(glass, "centre_plane", Location((0, 0, GLASS_THICKNESS / 2.0)))
    asm.rigid_frame(display, "centre_plane", Location((0, 0, DISPLAY_THICKNESS / 2.0)))
    asm.rigid_frame(housing, "front_datum", Location((0, 0, REAR_HOUSING_DEPTH / 2.0)))
    asm.revolute_frame(stand, "hinge_axis", Axis((0, STAND_LENGTH / 2.0, 0), (1, 0, 0)))

    return asm.build()
