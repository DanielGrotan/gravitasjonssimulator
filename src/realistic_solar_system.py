import taichi as ti

from solar_system import SolarSystem


class RealisticSolarSystem(SolarSystem):
    @ti.func
    def _create_object(
        self,
        index: ti.int32,
        x: ti.f32,
        y: ti.f32,
        vel_x: ti.f32,
        vel_y: ti.f32,
        mass: ti.f32,
    ):
        self._positions[index] = [x, y]
        self._velocities[index] = [vel_x, vel_y]
        self._masses[0] = mass

    @ti.kernel
    def init_planets(self):
        mass_scaling = 3.978e26
        distance_scaling = 4.96966666666667e16

        # Sun
        self._create_object(
            index=0, x=0.5, y=0.5, vel_x=0, vel_y=0, mass=1.989e30 / mass_scaling
        )
