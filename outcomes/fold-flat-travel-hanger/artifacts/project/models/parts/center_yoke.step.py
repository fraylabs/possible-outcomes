import sys
from pathlib import Path

MODELS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODELS))
from hanger_common import make_center_yoke


def gen_step():
    return make_center_yoke()
