import os
from pathlib import Path

VELOCITY_RESULTS_PATH = (
    Path(os.path.abspath(os.path.dirname(__file__))).parent
    / "results"
    / "velocity_results.txt"
)
