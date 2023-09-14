![alt_text](logos/image1.png 'image_tooltip')

# Readme File

Answer the following questions after you have completed your coding challenge. Please be truthful in your responses. Remember we are looking for commitment and willingness to learn, not previous knowledge, so don’t get discouraged if you’re having trouble. You have done the hard work already, so be clear, yet brief in your answers.

# Questions

1. **How far did you get with the challenge? How much time did it take?**
   I attempted all four parts and was able to get solutions for all four. I spent the most time on part 3 because I faced a couple issues with using the correct bitmask and reconstructing the final path. In total, I spent about 10 hours on all four parts.

2. **Please provide a brief description of the way that you have organized your code.**

    I split each part into separate Python files, labeled "part1.py", "part2.py", "part3.py", "part4.py". For each part, I imported the necessary functions from previous parts.

    In Part 1, in addition to reading the coordinates of the waypoints, I added IDs to each of the waypoints. This allowed me to keep track of the waypoints while recursively traversing the graph of waypoints, especially when I needed the original waypoint list indices to calculate the distances between two waypoints.

    In Part 2, I calculated the ground distances and difference in altitude between the two waypoints, then applied the Pythagorean theorem to calculate the direct distance between the two waypoints.

    In Part 3, I used a bitmask to keep track of the waypoints that have been visited, where a set bit denoted an unvisited waypoint and an unset bit denoted a visited waypoint. I recursively traversed the graph of waypoints and used a memoization array to store the shortest path and the corresponding distance. I split the problem into 2 separate functions; one to find the shortest path between the starting node and some other node i, and the other to find the shortest path for the whole graph as well as to reconstruct the final path. The result I calculated is below.

    Total distance traveled: 13358.795568246527 feet
    Path: 0 -> 13 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 3 -> 2 -> 1 -> 0

    In Part 4, I used matplotlib to plot the specified measurements for each waypoint.

3. **Please provide instructions on how to run your code.**
   To run the final solution, run `python3 solution.py`. To test individual part, run the respective python file.

4. **Is there any other relevant information that would be helpful for us to know?**
