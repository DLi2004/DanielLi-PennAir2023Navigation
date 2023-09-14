import json


def get_waypoints():
    """Returns a dictionary of coordinates"""
    with open('data/coords.json', 'r') as f:
        coords = json.load(f)
        waypoints = coords["waypoints"]

        # Add an id to each waypoint
        idx = 0
        for wp in waypoints:
            wp["id"] = idx
            idx += 1
        return waypoints
