import functools

import taichi as ti

from solar_system import SolarSystem


class RandomPlanetsWithSun(SolarSystem):
    @ti.kernel
    def init_planets(
        self,
        sun_x: ti.f32,
        sun_y: ti.f32,
        sun_vel_x: ti.f32,
        sun_vel_y: ti.f32,
        sun_mass: ti.f32,
        pos_x_divisor: ti.f32,
        pos_x_offset: ti.f32,
        pos_y_divisor: ti.f32,
        pos_y_offset: ti.f32,
        max_vel_x: ti.f32,
        min_vel_x: ti.f32,
        max_vel_y: ti.f32,
        min_vel_y: ti.f32,
        max_mass: ti.f32,
        min_mass: ti.f32,
        min_radius: ti.i32,
        max_radius: ti.i32,
        mass_to_radius_divisor: ti.f32,
    ):
        # Create sun
        self._positions[0] = [sun_x, sun_y]
        self._velocities[0] = [sun_vel_x, sun_vel_y]
        self._masses[0] = sun_mass

        # Create random planets
        for p in range(1, self._n_planets):
            self._positions[p] = [
                ti.random() / pos_x_divisor + pos_x_offset,
                ti.random() / pos_y_divisor + pos_y_offset,
            ]
            self._velocities[p] = [
                max_vel_x - ti.random() * (max_vel_x - min_vel_x),
                max_vel_y - ti.random() * (max_vel_y - min_vel_y),
            ]
            self._masses[p] = max_mass - ti.random() * (max_mass - min_mass)

        # Find radii of planets / sun
        for p in range(self._n_planets):
            self._radii[p] = max(
                min_radius, min(max_radius, self._masses[p] / mass_to_radius_divisor)
            )


def init_rpws_planets(
    solar_system: RandomPlanetsWithSun,
    sun_x: float = 0.4,
    sun_y: float = 0.4,
    sun_vel_x: float = 0.0,
    sun_vel_y: float = 0.0,
    sun_mass: float = 5000,
    pos_x_divisor: float = 3,
    pos_x_offset: float = 0.35,
    pos_y_divisor: float = 3,
    pos_y_offset: float = 0.35,
    max_vel_x: float = 105,
    min_vel_x: float = 85,
    max_vel_y: float = 10,
    min_vel_y: float = -10,
    max_mass: float = 50,
    min_mass: float = 0,
    min_radius: int = 1,
    max_radius: int = 16,
    mass_to_radius_divisor: float = 5,
) -> None:
    solar_system.init_planets(
        sun_x=sun_x,
        sun_y=sun_y,
        sun_vel_x=sun_vel_x,
        sun_vel_y=sun_vel_y,
        sun_mass=sun_mass,
        pos_x_divisor=pos_x_divisor,
        pos_x_offset=pos_x_offset,
        pos_y_divisor=pos_y_divisor,
        pos_y_offset=pos_y_offset,
        max_vel_x=max_vel_x,
        min_vel_x=min_vel_x,
        max_vel_y=max_vel_y,
        min_vel_y=min_vel_y,
        max_mass=max_mass,
        min_mass=min_mass,
        min_radius=min_radius,
        max_radius=max_radius,
        mass_to_radius_divisor=mass_to_radius_divisor,
    )


def main() -> None:
    ti.init()


if __name__ == "__main__":
    main()
