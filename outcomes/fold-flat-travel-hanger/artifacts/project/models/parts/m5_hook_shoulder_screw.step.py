import sys
from pathlib import Path

MODELS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODELS))
from hanger_common import make_hook_shoulder_pin


def gen_step():
    return make_hook_shoulder_pin()
