import sys
from pathlib import Path
from build123d import Compound

MODELS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODELS))
from hanger_common import build_lock_detail_children


def gen_step():
    return Compound(children=build_lock_detail_children(False), label="lock_detail_engaged")
