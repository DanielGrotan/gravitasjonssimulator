import math

from matplotlib import pyplot as plt

from constants import VELOCITY_RESULTS_PATH


def main() -> None:
    velocities = []
    time_stamps = []

    with open(VELOCITY_RESULTS_PATH) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue

            vel_x, vel_y, time = map(float, line.split(", "))
            velocities.append(math.sqrt(vel_x**2 + vel_y**2))
            time_stamps.append(time)

    plt.plot(time_stamps, velocities)
    plt.xlabel("Time")
    plt.ylabel("Velocity")
    plt.title("Velocity of planet orbiting another larger planet")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
