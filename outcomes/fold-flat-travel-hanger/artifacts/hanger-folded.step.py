# /// script
# requires-python = ">=3.11"
# dependencies = ["build123d==0.11.0"]
# ///

"""Folded pose entry point for the Burr fold-flat hanger."""

from pathlib import Path

from hanger import export_burr_step, make_hanger


def gen_step():
    return make_hanger(folded=True)


if __name__ == "__main__":
    export_burr_step(gen_step(), Path(__file__).with_suffix(""))
