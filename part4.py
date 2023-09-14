import matplotlib.pyplot as plt
import json
from part1 import get_waypoints
from part2 import distance_between_two_waypoints


def get_flyzones():
    """Returns a dictionary of coordinates"""
    with open('data/coords.json', 'r') as f:
        coords = json.load(f)
        flyzones = coords["flyZones"]
        boundary_points = flyzones[0]["boundaryPoints"]

        # Set the minimum latitude and longitude values as the origin
        minLat = min(boundary_points[i]["latitude"]
                     for i in range(len(boundary_points)))
        minLong = min(boundary_points[j]["longitude"]
                      for j in range(len(boundary_points)))
        return minLat, minLong


def get_xy(wp, minLat, minLong):
    """Returns the distance between a waypoint and the origin"""
    new_wp_x = {"latitude": minLat,
                "longitude": wp["longitude"],
                "altitude": wp["altitude"],
                "id": -1}
    x = distance_between_two_waypoints(new_wp_x, wp)

    new_wp_y = {"latitude": wp["latitude"],
                "longitude": minLong,
                "altitude": wp["altitude"],
                "id": -1}
    y = distance_between_two_waypoints(new_wp_y, wp)

    return x, y


def plot_coordinates():
    """Plots the waypoints and flyzone"""
    wps = get_waypoints()
    minLat, minLong = get_flyzones()
    x_coords = []
    y_coords = []

    for wp in wps:
        x, y = get_xy(wp, minLat, minLong)
        x_coords.append(x)
        y_coords.append(y)

    plt.scatter(x_coords, y_coords, color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Waypoint Visualization')
    plt.show()


if __name__ == "__main__":
    plot_coordinates()
