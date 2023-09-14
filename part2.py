from part1 import get_waypoints
from geopy.distance import geodesic
from math import sqrt


def distance_between_two_waypoints(waypoint1, waypoint2):
    """Returns the distance between two waypoints"""
    lt1, lg1, alt1, _ = waypoint1.values()
    lt2, lg2, alt2, _ = waypoint2.values()
    ground_dist = geodesic((lt1, lg1), (lt2, lg2)).feet
    alt_diff = alt1 - alt2
    return sqrt(ground_dist ** 2 + alt_diff ** 2)


if __name__ == "__main__":
    wps = get_waypoints()
    distance_example = distance_between_two_waypoints(wps[0], wps[1])
    print(f"Distance between Waypoint 1 and Waypoint 2: {distance_example}")
