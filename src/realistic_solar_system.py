import taichi as ti

from solar_system import SolarSystem


class RealisticSolarSystem(SolarSystem):
    @ti.func
    def _create_object(
        self,
        index: ti.int32,
        x: ti.f64,
        y: ti.f64,
        vel_x: ti.f64,
        vel_y: ti.f64,
        mass: ti.f64,
    ):
        print(mass)
        self._positions[index] = [x, y]
        self._velocities[index] = [vel_x, vel_y]
        self._masses[index] = mass

    @ti.kernel
    def init_planets(self):
        mass_scaling = 3.978e26
        distance_scaling = 9.93933333333334e12

        # Sun
        self._create_object(
            index=0, x=0.5, y=0.5, vel_x=0, vel_y=0, mass=1.989e30 / mass_scaling
        )

        # Mercury
        self._create_object(
            index=1,
            x=0.5 + 6.9285e10 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=100,
            mass=3.30104e23 / mass_scaling,
        )

        # Venus
        self._create_object(
            index=2,
            x=0.5 + 1.0768e11 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=100,
            mass=4.867e24 / mass_scaling,
        )

        # Earth
        self._create_object(
            index=3,
            x=0.5 + 1.4848e11 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=100,
            mass=5.972e24 / mass_scaling,
        )

        # Mars
        self._create_object(
            index=4,
            x=0.5 + 2.3451e11 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=100,
            mass=6.39e23 / mass_scaling,
        )

        # Jupiter
        self._create_object(
            index=5,
            x=0.5 + 7.78e11 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=100,
            mass=1.898e27 / mass_scaling,
        )

        # Saturn
        self._create_object(
            index=6,
            x=0.5 + 1.4578e12 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=100,
            mass=5.683e26 / mass_scaling,
        )

        # Uranus
        self._create_object(
            index=7,
            x=0.5 + 2.9344e12 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=100,
            mass=8.681e25 / mass_scaling,
        )

        # Neptune
        self._create_object(
            index=8,
            x=0.5 + 4.4727e12 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=100,
            mass=1.024e26 / mass_scaling,
        )

        print()

        # Find radii of planets / sun
        for p in range(self._n_planets):
            print(self._masses[p])
            self._radii[p] = max(3, min(5, self._masses[p]))
