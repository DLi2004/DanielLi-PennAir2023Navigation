import part1
import part2
import part3
import part4


def print_solution():
    print("PART 1:")
    wps = part1.get_waypoints()
    print("Waypoints:")
    for wp in wps:
        print(wp)

    print("\nPART 2:")
    distance_example = part2.distance_between_two_waypoints(wps[0], wps[1])
    print(f"Distance between Waypoint 1 and Waypoint 2: {distance_example}")

    print("\nPART 3:")
    ans, min_path = part3.find_min_cost_path()
    print(f"Minimum distance: {ans}")
    print(f"Best path: {' -> '.join(str(i) for i in min_path)}")

    print("\nPART 4:")
    part4.plot_coordinates()


if __name__ == "__main__":
    print_solution()
