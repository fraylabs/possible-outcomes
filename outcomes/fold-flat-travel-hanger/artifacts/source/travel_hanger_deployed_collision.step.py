"""Burr collision-envelope entry for the deployed pose."""

from travel_hanger_collision import make_collision_envelope


def gen_step():
    return make_collision_envelope("deployed")

