from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
import time

# Define the Romania map graph
romania_map = nx.Graph()
romania_map.add_weighted_edges_from([
    ('Arad', 'Zerind', 75),
    ('Arad', 'Sibiu', 140),
    ('Arad', 'Timisoara', 118),
    ('Zerind', 'Oradea', 71),
    ('Oradea', 'Sibiu', 151),
    ('Sibiu', 'Fagaras', 99),
    ('Sibiu', 'Rimnicu Vilcea', 80),
    ('Timisoara', 'Lugoj', 111),
    ('Lugoj', 'Mehadia', 70),
    ('Mehadia', 'Drobeta', 75),
    ('Drobeta', 'Craiova', 120),
    ('Craiova', 'Rimnicu Vilcea', 146),
    ('Craiova', 'Pitesti', 138),
    ('Rimnicu Vilcea', 'Pitesti', 97),
    ('Fagaras', 'Bucharest', 211),
    ('Pitesti', 'Bucharest', 101),
    ('Bucharest', 'Giurgiu', 90),
    ('Bucharest', 'Urziceni', 85),
    ('Urziceni', 'Hirsova', 98),
    ('Urziceni', 'Vaslui', 142),
    ('Hirsova', 'Eforie', 86),
    ('Vaslui', 'Iasi', 92),
    ('Iasi', 'Neamt', 87)
])

romania_map.nodes['Arad']['heuristic'] = 366
romania_map.nodes['Zerind']['heuristic'] = 380
romania_map.nodes['Oradea']['heuristic'] = 380
romania_map.nodes['Sibiu']['heuristic'] = 253
romania_map.nodes['Timisoara']['heuristic'] = 329
romania_map.nodes['Lugoj']['heuristic'] = 244
romania_map.nodes['Mehadia']['heuristic'] = 241
romania_map.nodes['Drobeta']['heuristic'] = 242
romania_map.nodes['Craiova']['heuristic'] = 160
romania_map.nodes['Rimnicu Vilcea']['heuristic'] = 193
romania_map.nodes['Fagaras']['heuristic'] = 176
romania_map.nodes['Pitesti']['heuristic'] = 100
romania_map.nodes['Bucharest']['heuristic'] = 0
romania_map.nodes['Giurgiu']['heuristic'] = 77
romania_map.nodes['Urziceni']['heuristic'] = 80
romania_map.nodes['Hirsova']['heuristic'] = 151
romania_map.nodes['Eforie']['heuristic'] = 161
romania_map.nodes['Vaslui']['heuristic'] = 199
romania_map.nodes['Iasi']['heuristic'] = 226
romania_map.nodes['Neamt']['heuristic'] = 234

def astar_search(source, destination):
    open_set = {source}
    closed_set = set()
    g_scores = {source: 0}
    f_scores = {source: heuristic(source, destination)}
    came_from = {}

    while open_set:
        current = min(open_set, key=lambda node: f_scores[node])

        if current == destination:
            return reconstruct_path(came_from, destination)

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in romania_map.neighbors(current):
            weight = romania_map[current][neighbor]['weight']
            if neighbor in closed_set:
                continue

            tentative_g_score = g_scores[current] + weight
            if neighbor not in open_set or tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + heuristic(neighbor, destination)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return []

def heuristic(node, destination):
    return romania_map.nodes[node]['heuristic']

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

def draw_map(graph, path=None, delay=1):
    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(graph, seed=42)

    # Draw nodes
    nx.draw_networkx_nodes(graph, pos, node_size=2000, node_color='lightgreen', node_shape='s')
    nx.draw_networkx_labels(graph, pos, font_size=8)

    # Draw edges
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5)

    # Draw path
    if path:
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='red', width=3.0)

        # Draw path cost
        path_cost = sum(graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, 'weight'),
                                     font_color='blue', label_pos=0.3, font_size=6)
        plt.title("Final Path (Cost: {})".format(path_cost))
    else:
        plt.title("Initial Romania Map")

    plt.axis('off')
    plt.tight_layout()
    plt.draw()
    plt.pause(delay)

def search():
    source = source_var.get().capitalize()
    destination = destination_var.get().capitalize()
    path = astar_search(source, destination)
    if path:
        result_label.config(text="Path: " + ' -> '.join(path))
        for i in range(len(path) - 1):
            partial_path = path[:i + 2]
            draw_map(romania_map, partial_path, delay=1)  # Adjust the delay time here
        draw_map(romania_map, path)
    else:
        result_label.config(text="No path found!")

# Create the GUI window
root = Tk()
root.title("A* Search on Romania Map")

# Source and destination input fields
source_label = Label(root, text="Source:")
source_label.pack()
source_var = StringVar(root)
source_entry = Entry(root, textvariable=source_var)
source_entry.pack()

destination_label = Label(root, text="Destination:")
destination_label.pack()
destination_var = StringVar(root)
destination_entry = Entry(root, textvariable=destination_var)
destination_entry.pack()

# Find Path button
search_button = Button(root, text="Find Path", command=search)
search_button.pack()

# Result label
result_label = Label(root)
result_label.pack()

# Draw the initial Romania map
draw_map(romania_map)

# Start the GUI event loop
root.mainloop()