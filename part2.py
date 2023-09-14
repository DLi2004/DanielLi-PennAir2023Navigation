from part1 import get_waypoints
from geopy.distance import geodesic
from math import sqrt


def distance_between_two_waypoints(waypoint1, waypoint2):
    """Returns the distance between two waypoints"""
    _, lt1, lg1, alt1 = waypoint1.values()
    _, lt2, lg2, alt2 = waypoint2.values()
    ground_distance = geodesic((lt1, lg1), (lt2, lg2)).feet
    altitude = alt1 - alt2
    return sqrt(ground_distance ** 2 + altitude ** 2)


if __name__ == "main":
    wps = get_waypoints()
    distance_example = distance_between_two_waypoints(0, 1)
    print(f"Distance between Waypoint 1 and Waypoint 2: {distance_example}")
