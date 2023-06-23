# A Star Visualisation
## Visualization of A* Algorithm on Romania Map
This code implements the A* search algorithm to find the shortest path between two cities in the Romania map. The algorithm takes into account both the actual cost of reaching a city and an estimated heuristic value from the current city to the destination city. 

One impressive aspect of this code is the A* search algorithm's ability to find the shortest path between two cities efficiently. A* search combines the advantages of both Dijkstra's algorithm and Greedy Best-First Search by considering both the actual cost of reaching a city and an estimated heuristic value from the current city to the destination city.

The algorithm intelligently explores the graph, prioritizing nodes with lower estimated costs, which allows it to converge towards the shortest path more quickly. By using a heuristic function that provides informed estimates, A* search avoids exploring unnecessary paths, resulting in significant computational savings, especially in larger maps or complex graphs.

The code also leverages the NetworkX library to represent and visualize the map graph, providing an intuitive and interactive interface to explore the search results visually.

With its efficient pathfinding capabilities and user-friendly interface, this code showcases the power of A* search and its potential applications in solving real-world problems that involve finding optimal routes or paths.

## Software and Dependencies Required
To run the code, you will need Python 3.x installed on your machine, along with the following libraries:

- tkinter
- networkx
- matplotlib

You can install these dependencies using pip: pip install tkinter, networkx, matplotlib

## Working of the Code

1. The Romania map is represented as an undirected graph using the NetworkX library. The graph consists of cities as nodes and weighted edges representing the distances between cities.

2. Heuristic values are assigned to each city in the graph. These heuristic values provide an estimate of the distance from each city to the destination city. In this implementation, Bucharest is set as the destination city.

3. The A* search algorithm is implemented in the `astar_search` function. It takes the source city and the destination city as input and returns the shortest path between them.

4. The A* search algorithm works as follows:
- Initialize an open set, a closed set, g-scores, f-scores, and a dictionary to keep track of the previous node in the shortest path.
 - While the open set is not empty:
    - Select the node with the lowest f-score as the current node.
    - If the current node is the destination, reconstruct the shortest path and return it.
    - Remove the current node from the open set and add it to the closed set.
    - For each neighbor of the current node:
      - Calculate the tentative g-score by adding the weight of the edge between the current node and the neighbor.
      - If the neighbor is in the closed set and the tentative g-score is higher, skip to the next neighbor.
      - If the neighbor is not in the open set or the tentative g-score is lower:
        - Update the came_from dictionary to track the previous node.
        - Update the g-score and f-score of the neighbor.
        - If the neighbor is not in the open set, add it.

6. The `heuristic` function returns the heuristic value of a node. In this implementation, the heuristic values are pre-defined for each city based on their estimated distances to Bucharest.

7. The `reconstruct_path` function reconstructs the shortest path by following the came_from dictionary from the destination to the source.

8. The `draw_map` function visualizes the Romania map using matplotlib. It displays the nodes, edges, and labels of the graph. If a path is provided, it highlights the path in red and displays the total cost of the path.

9. The GUI interface allows the user to input the source and destination cities, and upon clicking the "Find Path" button, the code performs the A* search and displays the resulting path on the map.

## How To Use?

1. Run the script using Python:

2. Enter the source and destination cities in the respective input fields.

3. Click the "Find Path" button to initiate the A* search.

4. The resulting path will be displayed in the GUI window, and the Romania map with the path will be shown.

## Credits

- [A* Search Algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [Tkinter Documenatation](https://docs.python.org/3/library/tk.html)
