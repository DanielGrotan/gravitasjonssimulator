import os
from pathlib import Path

import taichi as ti

from constants import VELOCITY_RESULTS_PATH

ti.init()

n_planets = 2
delta_t = 3e-5
resolution_x = 1200
resolution_y = 800

planets = ti.Vector.field(2, dtype=ti.f32, shape=n_planets)
velocities = ti.Vector.field(2, dtype=ti.f32, shape=n_planets)
masses = ti.field(ti.f32, shape=n_planets)
radii = ti.field(ti.f32, shape=n_planets)
force_vectors = ti.Vector.field(2, dtype=ti.f32, shape=n_planets)


@ti.kernel
def step():
    calculate_force_vectors()
    move()


@ti.func
def calculate_force_vectors():
    force_vectors.fill([0, 0])
    for p1, p2 in ti.ndrange(n_planets, n_planets):
        if p1 == p2:
            continue

        distance = (planets[p2] - planets[p1]).norm(1e-3)
        change = masses[p1] * masses[p2] * (planets[p2] - planets[p1]) / (distance**3)
        force_vectors[p1] += change


@ti.func
def move():
    for planet in planets:
        velocities[planet] += force_vectors[planet] * delta_t / masses[planet]
        planets[planet] += velocities[planet] * delta_t

        if (
            planets[planet][0] - radii[planet] / resolution_x < 0
            or planets[planet][0] + radii[planet] / resolution_x > 1
        ):
            velocities[planet][0] *= -1
        if (
            planets[planet][1] - radii[planet] / resolution_y < 0
            or planets[planet][1] + radii[planet] / resolution_y > 1
        ):
            velocities[planet][1] *= -1


@ti.kernel
def init():
    # for planet in planets:
    #     planets[planet] = [ti.random() / 3 + 0.35, ti.random() / 3 + 0.35]
    #     velocities[planet] = [105 - ti.random() * 20, 10 - ti.random() * 20]
    #     masses[planet] = ti.random() * 50
    #     radii[planet] = max(1, min(40, int(masses[planet] / 5)))

    # Planet 1
    planets[0] = [0.5, 0.5]
    velocities[0] = [0, 0]
    masses[0] = 5000
    radii[0] = max(1, min(40, int(masses[0] / 5)))

    # Planet 2
    planets[1] = [0.4, 0.25]
    velocities[1] = [105, 60]
    masses[1] = 25
    radii[1] = max(1, min(40, int(masses[1] / 5)))


def write_velocity_to_file(
    velocity: tuple[float, float], time: float, path: Path
) -> None:
    with open(path, "a+") as f:
        f.write(f"{velocity[0]}, {velocity[1]}, {time}\n")


def main() -> None:
    init()
    gui = ti.GUI("Planets", res=(resolution_x, resolution_y))

    frame_count = 0

    while gui.running:
        step()

        frame_count += 1
        write_velocity_to_file(
            velocities[1], frame_count * delta_t, VELOCITY_RESULTS_PATH
        )

        planets_numpy = planets.to_numpy()
        radii_numpy = radii.to_numpy()

        for i, planet in enumerate(planets_numpy):
            gui.circle(planet, radius=radii_numpy[i])

        gui.show()


if __name__ == "__main__":
    main()
