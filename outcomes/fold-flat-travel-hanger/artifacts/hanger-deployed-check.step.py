# /// script
# requires-python = ">=3.11"
# dependencies = ["build123d==0.11.0"]
# ///

"""Closed interference-check envelopes for the deployed hanger pose."""

from pathlib import Path

from hanger import export_burr_step, make_hanger_check_envelope


def gen_step():
    return make_hanger_check_envelope(folded=False)


if __name__ == "__main__":
    export_burr_step(gen_step(), Path(__file__).with_suffix(""))
