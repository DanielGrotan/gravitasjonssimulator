from abc import ABC, abstractmethod

import taichi as ti


@ti.data_oriented
class SolarSystem(ABC):
    def __init__(self, n_planets: int, resolution_x: int, resolution_y: int) -> None:
        self._n_planets = n_planets
        self._resolution_x = resolution_x
        self._resolution_y = resolution_y

        self._positions = ti.Vector.field(2, dtype=ti.f32, shape=n_planets)
        self._velocities = ti.Vector.field(2, dtype=ti.f32, shape=n_planets)
        self._masses = ti.field(ti.f32, shape=n_planets)
        self._radii = ti.field(ti.f32, shape=n_planets)
        self._force_vectors = ti.Vector.field(2, dtype=ti.f32, shape=n_planets)

    @abstractmethod
    def init_planets(self) -> None:
        ...

    @ti.kernel
    def simulation_step(self, delta_time: float):
        self._calculate_force_vectors()
        self._move_planets(delta_time)

    def get_planet_positions(self):
        return self._positions

    def get_planet_radii(self):
        return self._radii

    @ti.func
    def _calculate_force_vectors(self) -> None:
        self._force_vectors.fill([0, 0])
        for p1, p2 in ti.ndrange(self._n_planets, self._n_planets):
            if p1 == p2:
                continue

            distance = (self._positions[p2] - self._positions[p1]).norm(1e-3)
            change = (
                self._masses[p1]
                * self._masses[p2]
                * (self._positions[p2] - self._positions[p1])
                / (distance**3)
            )
            self._force_vectors[p1] += change

    @ti.func
    def _move_planets(self, delta_time: float) -> None:
        for p in range(self._n_planets):
            self._velocities[p] += self._force_vectors[p] * delta_time / self._masses[p]
            self._positions[p] += self._velocities[p] * delta_time

            if (
                self._positions[p][0] - self._radii[p] / self._resolution_x < 0
                or self._positions[p][0] + self._radii[p] / self._resolution_x > 1
            ):
                self._velocities[p][0] *= -1
            if (
                self._positions[p][1] - self._radii[p] / self._resolution_y < 0
                or self._positions[p][1] + self._radii[p] / self._resolution_y > 1
            ):
                self._velocities[p][1] *= -1
