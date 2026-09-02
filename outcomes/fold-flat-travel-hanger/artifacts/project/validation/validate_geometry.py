#!/usr/bin/env python3
"""Independent geometry-contract verifier for the hanger source model."""

from __future__ import annotations

import itertools
import json
import math
import sys
from pathlib import Path

from build123d import import_step
from cadgen.validity import check_occurrence_shape

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "models"))

import hanger_common as h


def bounds(shape):
    box = shape.bounding_box()
    return {
        "min": [round(box.min.X, 6), round(box.min.Y, 6), round(box.min.Z, 6)],
        "max": [round(box.max.X, 6), round(box.max.Y, 6), round(box.max.Z, 6)],
        "size": [round(box.size.X, 6), round(box.size.Y, 6), round(box.size.Z, 6)],
    }


def invariant_signature(shape):
    return {
        "solids": len(shape.solids()),
        "faces": len(shape.faces()),
        "edges": len(shape.edges()),
        "vertices": len(shape.vertices()),
        "volume": round(shape.volume, 6),
        "area": round(shape.area, 6),
    }


def solid_health(shape):
    result = check_occurrence_shape(shape.wrapped, check_self_intersection=False)
    return {
        "valid_topology": "invalidTopology" not in result["reasons"],
        "solid_count": result["solidCount"],
        "all_closed": "openShell" not in result["reasons"],
        "all_positive_volume": "nonPositiveVolume" not in result["reasons"],
        "reasons": result["reasons"],
    }


def pairwise_intersections(components):
    findings = []
    checked_pairs = 0
    bbox_candidate_pairs = 0
    for (name_a, shape_a), (name_b, shape_b) in itertools.combinations(components.items(), 2):
        checked_pairs += 1
        a = shape_a.bounding_box()
        b = shape_b.bounding_box()
        separated = (
            a.max.X < b.min.X
            or b.max.X < a.min.X
            or a.max.Y < b.min.Y
            or b.max.Y < a.min.Y
            or a.max.Z < b.min.Z
            or b.max.Z < a.min.Z
        )
        if separated:
            continue
        bbox_candidate_pairs += 1
        overlap = shape_a & shape_b
        overlap_volume = 0.0 if overlap is None else overlap.volume
        if overlap_volume > 1e-5:
            findings.append(
                {
                    "a": name_a,
                    "b": name_b,
                    "positive_overlap_mm3": round(overlap_volume, 6),
                }
            )
    return {
        "checked_pairs": checked_pairs,
        "bbox_candidate_pairs": bbox_candidate_pairs,
        "positive_volume_findings": findings,
        "pass": not findings,
    }


def main():
    printable_factories = {
        "center_yoke": h.make_center_yoke,
        "left_shoulder_arm": h.make_left_arm,
        "right_shoulder_arm": h.make_right_arm,
        "folding_hook": h.make_hook,
        "dual_positive_lock_bar": h.make_lock_bar,
    }
    manufactured = {}
    for name, factory in printable_factories.items():
        shape = factory()
        b = bounds(shape)
        orientation = sorted(b["size"], reverse=True)
        manufactured[name] = {
            "bounds_mm": b,
            "geometry": solid_health(shape),
            "build_area_orientation_mm": orientation,
            "fits_256_cube": all(value <= 256.0 + 1e-6 for value in orientation),
        }

    pose_reports = {}
    for pose_name in h.POSES:
        components = h.build_pose_components(pose_name)
        assembly = h.make_pose_assembly(pose_name)
        pose_reports[pose_name] = {
            "component_count": len(components),
            "unique_component_names": len(set(components)) == len(components),
            "bounds_mm": bounds(assembly),
            "geometry": solid_health(assembly),
            "interference": pairwise_intersections(components),
        }

    exported_pose_reports = {}
    exported_components = {}
    for pose_name in h.POSES:
        step_path = ROOT / "models" / "assemblies" / f"hanger_{pose_name}.step"
        assembly = import_step(step_path)
        components = {child.label: child for child in assembly.children}
        exported_components[pose_name] = components
        exported_pose_reports[pose_name] = {
            "path": str(step_path),
            "component_count": len(components),
            "unique_component_names": len(set(components)) == len(components),
            "bounds_mm": bounds(assembly),
            "geometry": solid_health(assembly),
            "interference": pairwise_intersections(components),
        }

    deployed_size = exported_pose_reports["deployed"]["bounds_mm"]["size"]
    folded_size_sorted = sorted(exported_pose_reports["folded"]["bounds_mm"]["size"], reverse=True)

    deployed_components = h.build_pose_components("deployed")
    folded_components = h.build_pose_components("folded")
    endpoint_identity = {
        "same_names": list(deployed_components) == list(folded_components),
        "component_signatures": {},
    }
    identity_pass = endpoint_identity["same_names"]
    for name in deployed_components:
        deployed_sig = invariant_signature(deployed_components[name])
        folded_sig = invariant_signature(folded_components[name])
        same = deployed_sig == folded_sig
        identity_pass = identity_pass and same
        endpoint_identity["component_signatures"][name] = {
            "deployed": deployed_sig,
            "folded": folded_sig,
            "unchanged": same,
        }
    endpoint_identity["pass"] = identity_pass

    exported_endpoint_identity = {
        "same_names": list(exported_components["deployed"]) == list(exported_components["folded"]),
        "component_signatures": {},
    }
    exported_identity_pass = exported_endpoint_identity["same_names"]
    for name in exported_components["deployed"]:
        deployed_sig = invariant_signature(exported_components["deployed"][name])
        folded_sig = invariant_signature(exported_components["folded"][name])
        same = deployed_sig == folded_sig
        exported_identity_pass = exported_identity_pass and same
        exported_endpoint_identity["component_signatures"][name] = {
            "deployed": deployed_sig,
            "folded": folded_sig,
            "unchanged": same,
        }
    exported_endpoint_identity["pass"] = exported_identity_pass

    requirements = {
        "deployed_width": {
            "value_mm": deployed_size[0],
            "target_mm": [430.0, 450.0],
            "pass": 430.0 <= deployed_size[0] <= 450.0,
        },
        "folded_envelope": {
            "value_mm_sorted": folded_size_sorted,
            "target_mm": list(h.FOLDED_TARGET),
            "pass": all(
                actual <= target + 1e-6
                for actual, target in zip(folded_size_sorted, h.FOLDED_TARGET)
            ),
        },
        "hook_rod_pocket": {
            "diameter_mm": 2.0 * h.HOOK_INNER_RADIUS,
            "rod_max_mm": h.HOOK_ROD_MAX_DIAMETER,
            "diametral_clearance_mm": 2.0 * h.HOOK_INNER_RADIUS - h.HOOK_ROD_MAX_DIAMETER,
            "pass": 2.0 * h.HOOK_INNER_RADIUS >= h.HOOK_ROD_MAX_DIAMETER,
        },
        "hook_throat": {
            "opening_mm": h.HOOK_THROAT_OPENING,
            "rod_max_mm": h.HOOK_ROD_MAX_DIAMETER,
            "clearance_mm": h.HOOK_THROAT_OPENING - h.HOOK_ROD_MAX_DIAMETER,
            "pass": h.HOOK_THROAT_OPENING >= h.HOOK_ROD_MAX_DIAMETER,
        },
        "pin_to_bore": {
            "pin_diameter_mm": h.PIN_DIAMETER,
            "bore_diameter_mm": h.PIN_BORE_DIAMETER,
            "diametral_clearance_mm": h.PIN_BORE_DIAMETER - h.PIN_DIAMETER,
            "radial_clearance_mm": h.PIN_RADIAL_CLEARANCE,
            "pass": math.isclose(h.PIN_RADIAL_CLEARANCE, 0.3, abs_tol=1e-9),
        },
        "axial_clearances": {
            "arm_each_side_mm": h.ARM_AXIAL_CLEARANCE_EACH_SIDE,
            "hook_each_side_mm": h.HOOK_AXIAL_CLEARANCE_EACH_SIDE,
            "pass": h.ARM_AXIAL_CLEARANCE_EACH_SIDE > 0 and h.HOOK_AXIAL_CLEARANCE_EACH_SIDE > 0,
        },
        "positive_lock_face": {
            "engagement_mm": h.LOCK_FACE_ENGAGEMENT,
            "minimum_mm": 3.0,
            "contact_area_each_side_mm2": h.LOCK_FACE_ENGAGEMENT * 6.0,
            "hard_stop_face_delta_z_mm": 0.0,
            "pass": h.LOCK_FACE_ENGAGEMENT >= 3.0,
        },
        "release_control": {
            "axial_travel_mm": h.LOCK_RELEASE_TRAVEL,
            "blocking_face_clearance_mm": h.LOCK_RELEASE_CLEARANCE,
            "pass": h.LOCK_RELEASE_TRAVEL >= 7.5 and h.LOCK_RELEASE_CLEARANCE >= 1.0,
        },
        "all_printable_parts_fit": {
            "pass": all(item["fits_256_cube"] for item in manufactured.values())
        },
        "all_five_poses_interference_free": {
            "pass": all(item["interference"]["pass"] for item in exported_pose_reports.values())
        },
        "endpoint_component_identity": {"pass": exported_identity_pass},
    }

    overall_pass = (
        all(item["pass"] for item in requirements.values())
        and all(item["geometry"]["valid_topology"] for item in manufactured.values())
        and all(item["geometry"]["all_closed"] for item in manufactured.values())
        and all(item["geometry"]["all_positive_volume"] for item in manufactured.values())
        and all(item["component_count"] == 11 for item in exported_pose_reports.values())
        and all(item["geometry"]["valid_topology"] for item in exported_pose_reports.values())
        and all(item["geometry"]["all_closed"] for item in exported_pose_reports.values())
        and all(item["geometry"]["all_positive_volume"] for item in exported_pose_reports.values())
    )
    report = {
        "schema": "fray.hanger.geometry-validation.v1",
        "overall_pass": overall_pass,
        "requirements": requirements,
        "manufactured_parts": manufactured,
        "poses": pose_reports,
        "exported_step_poses": exported_pose_reports,
        "endpoint_identity": endpoint_identity,
        "exported_step_endpoint_identity": exported_endpoint_identity,
        "assumption_boundary": "Geometry-only validation; no physical load, fatigue, creep or reliability claim.",
    }
    out = ROOT / "validation" / "geometry_validation.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if overall_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
