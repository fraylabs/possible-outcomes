import sys
from pathlib import Path

MODELS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODELS))
from hanger_common import make_arm_shoulder_pin


def gen_step():
    return make_arm_shoulder_pin()
