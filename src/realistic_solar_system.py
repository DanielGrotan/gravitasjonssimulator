import taichi as ti

from solar_system import SolarSystem


class RealisticSolarSystem(SolarSystem):
    @ti.kernel
    def init_planets(self):
        mass_scaling = 3.978e26  # Sun mass = 5000
        distance_scaling = 9.93933333333334e12  # Nepute distance = 0.45
        velocity_scaling = 2.97848e2  # Earth velocity = 100

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
            vel_y=47e3 / velocity_scaling,
            mass=3.30104e23 / mass_scaling,
        )

        # Venus
        self._create_object(
            index=2,
            x=0.5 + 1.0768e11 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=35.02e3 / velocity_scaling,
            mass=4.867e24 / mass_scaling,
        )

        # Earth
        self._create_object(
            index=3,
            x=0.5 + 1.4848e11 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=29784.8 / velocity_scaling,
            mass=5.972e24 / mass_scaling,
        )

        # Mars
        self._create_object(
            index=4,
            x=0.5 + 2.3451e11 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=24.08e3 / velocity_scaling,
            mass=6.39e23 / mass_scaling,
        )

        # Jupiter
        self._create_object(
            index=5,
            x=0.5 + 7.78e11 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=13.06e3 / velocity_scaling,
            mass=1.898e27 / mass_scaling,
        )

        # Saturn
        self._create_object(
            index=6,
            x=0.5 + 1.4578e12 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=9.68e3 / velocity_scaling,
            mass=5.683e26 / mass_scaling,
        )

        # Uranus
        self._create_object(
            index=7,
            x=0.5 + 2.9344e12 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=6.79e3 / velocity_scaling,
            mass=8.681e25 / mass_scaling,
        )

        # Neptune
        self._create_object(
            index=8,
            x=0.5 + 4.4727e12 / distance_scaling,
            y=0.5,
            vel_x=0,
            vel_y=5.45e3 / velocity_scaling,
            mass=1.024e26 / mass_scaling,
        )

        # Find radii of planets / sun
        for p in range(self._n_planets):
            self._radii[p] = max(3, min(5, self._masses[p]))
