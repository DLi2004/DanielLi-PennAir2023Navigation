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


def helper(id1, id2):
    wps = get_waypoints()
    return distance_between_two_waypoints(wps[id1-1], wps[id2-1])


wps = get_waypoints()

# Create a 2D array of distances between waypoints
dists = [[0 for _ in range(len(wps))] for _ in range(len(wps))]
for i in range(len(wps)):
    for j in range(len(wps)):
        if i != j:
            dists[i][j] = distance_between_two_waypoints(
                wps[i], wps[j])
