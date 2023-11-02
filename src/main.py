import os
import subprocess
from pathlib import Path

import taichi as ti

from elliptic_orbit import EllipticOrbit
from gravitational_slingshot import GravitationalSlingshot
from hyperbolic_path import HyperbolicPath
from random_planets import RandomPlanetsWithSun, init_rpws_planets
from realistic_solar_system import RealisticSolarSystem

ti.init()


RESOLUTION_X, RESOLUTION_Y = 1920, 1080
DELTA_TIME = 3e-5
ROOT_DIR = Path(os.path.abspath(os.path.dirname(__file__))).parent
OUTPUT_DIR = ROOT_DIR / "results"
SRC_DIR = ROOT_DIR / "src"

ANIMATION_DIR = OUTPUT_DIR / "animation"
ANIMATION_FRAMES_DIR = ANIMATION_DIR / "frames"

BAT_FILE_PATH = SRC_DIR / "frames_to_video.bat"

CREATE_ANIMATION = False
VIDEO_DIRNAME = "realistic-solar-system"
VIDEO_NAME = "improved_velocities"


def main():
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    if not os.path.isdir(ANIMATION_DIR):
        os.makedirs(ANIMATION_DIR)

    if not os.path.isdir(ANIMATION_FRAMES_DIR):
        os.makedirs(ANIMATION_FRAMES_DIR)

    # solar_system = RandomPlanetsWithSun(5, RESOLUTION_X, RESOLUTION_Y)
    # init_rpws_planets(solar_system, sun_x=0.5, sun_y=0.5, min_mass=10)

    solar_system = RealisticSolarSystem(9, RESOLUTION_X, RESOLUTION_Y)
    solar_system.init_planets()

    gui = ti.GUI("Gravity Simulator", res=(RESOLUTION_X, RESOLUTION_Y))  # type: ignore

    frame = 0
    while gui.running:
        solar_system.simulation_step(DELTA_TIME)

        positions_numpy = solar_system.get_planet_positions().to_numpy()
        radii_numpy = solar_system.get_planet_radii().to_numpy()

        for i, position in enumerate(positions_numpy):
            gui.circle(position, radius=radii_numpy[i])

        if CREATE_ANIMATION:
            gui.show(str(ANIMATION_DIR / "frames" / f"{str(frame).zfill(6)}.png"))
            frame += 1
        else:
            gui.show()

    if CREATE_ANIMATION:
        subprocess.run([BAT_FILE_PATH, VIDEO_DIRNAME, VIDEO_NAME])


if __name__ == "__main__":
    main()
