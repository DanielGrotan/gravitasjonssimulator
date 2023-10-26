import taichi as ti

from random_planets import RandomPlanetsWithSun, init_rpws_planets

ti.init()


RESOLUTION_X, RESOLUTION_Y = 1200, 800
DELTA_TIME = 3e-5


def main():
    solar_system = RandomPlanetsWithSun(2, RESOLUTION_X, RESOLUTION_Y)
    init_rpws_planets(solar_system, sun_x=0.5, sun_y=0.5)

    gui = ti.GUI("Gravity Simulator", res=(RESOLUTION_X, RESOLUTION_Y))  # type: ignore

    while gui.running:
        solar_system.simulation_step(DELTA_TIME)

        positions_numpy = solar_system.get_planet_positions().to_numpy()
        radii_numpy = solar_system.get_planet_radii().to_numpy()

        for i, position in enumerate(positions_numpy):
            gui.circle(position, radius=radii_numpy[i])

        gui.show()


if __name__ == "__main__":
    main()
