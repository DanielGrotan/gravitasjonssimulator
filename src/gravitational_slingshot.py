import taichi as ti

from solar_system import SolarSystem


class GravitationalSlingshot(SolarSystem):
    @ti.kernel
    def init_planets(self):
        # Sun
        self._create_object(index=0, x=0.5, y=0.5, vel_x=0, vel_y=0, mass=5000)

        # Planet
        self._create_object(index=1, x=0.4, y=0.3, vel_x=200, vel_y=180, mass=10)

        # Find radii of planets / sun
        for p in range(self._n_planets):
            self._radii[p] = max(3, min(5, self._masses[p]))
