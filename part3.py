from part1 import get_waypoints
from part2 import distance_between_two_waypoints


def create_dists_array():
    """Returns a 2D array (14x14) of distances between waypoints"""
    wps = get_waypoints()

    # Create a 2D array of distances between waypoints
    dists = [[0 for _ in range(len(wps)+1)] for _ in range(len(wps)+1)]
    for i in range(len(wps)+1):
        for j in range(len(wps)+1):
            if i != j and i != 0:
                dists[i][j] = distance_between_two_waypoints(
                    wps[i-1], wps[j-1])
    return dists


# Load the distances array
dists = create_dists_array()
#dists = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]
wps = get_waypoints()
n = len(wps)
#n = 4

# Memoization array
memo = [[-1] * (1 << (n + 1)) for _ in range(n + 1)]

# Add a new 2D array to keep track of the path
path = [[-1] * (1 << (n + 1)) for _ in range(n + 1)]


def min_cost_path(i, mask):
    # Base case: if every node except the 1st and ith bit are set,
    # then we have visited all other nodes and we return
    # the distance from the ith node to the 1st node
    if mask == ((1 << i) | (n - 1)):
        return dists[1][i]

    # If the value is already calculated, return it
    if memo[i][mask] != -1:
        return memo[i][mask]

    res = float('inf')
    # To keep track of the node with the minimum cost path
    min_j = -1

    # Travel all nodes in mask to end up at ith node
    for j in range(1, n+1):
        # If the jth bit is set (not visited yet) and j is not the 1st or ith node
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            # Find the minimum cost to go from j to i
            temp_res = min(res, min_cost_path(
                j, mask & (~(1 << i))) + dists[j][i])
            if temp_res < res:
                res = temp_res
                min_j = j

    # Save result in memo array and path
    memo[i][mask] = res
    path[i][mask] = min_j
    return res


ans = float('inf')
min_i = -1  # To keep track of the node with the minimum cost path
for i in range(1, n+1):
    # Find the minimum cost with the path starting at node 1 and ending at node i
    temp_ans = min(ans, min_cost_path(i, (1 << (n+1))-1) + dists[1][i])
    if temp_ans < ans:
        ans = temp_ans
        min_i = i


# Reconstruct the minimum cost path
mask = (1 << (n + 1)) - 1
min_path = [1]
curr = min_i

while curr != -1:
    # Get the next node in the path
    nxt = path[curr][mask]
    min_path.append(nxt)
    mask &= ~(1 << curr)
    curr = nxt


print(ans)
print(min_path)
