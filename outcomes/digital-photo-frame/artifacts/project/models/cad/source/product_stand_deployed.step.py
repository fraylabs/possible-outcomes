from pathlib import Path
from runpy import run_path

_parts = run_path(str(Path(__file__).with_name("photo_frame_parts.py")))

def gen_step():
    return _parts["make_product"](_parts["DEPLOY_ANGLE_DEG"], False)
