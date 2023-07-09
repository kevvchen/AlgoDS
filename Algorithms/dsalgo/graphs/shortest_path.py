# Prompt: Write a function shortest_path, that takes in an array of edges for an undirected graph
# and two nodes (node_a, node_b). The function should return the length of the shortest path between
# A and B. Consider the length as numbers of edges and not nodes. If there is no path between A and B 
# return -1

from collections import deque

# Graph problems that require you to calcuate shortest path --> BFS > DFS

def shortest_path(edges, node_a, node_b):
    # Turn the edges into an adjacency list view
    graph = build_graph(edges)
    print(graph)

    # Store as a tuple
    queue = deque([(node_a, 0)])
    visited = set([node_a])

    while queue:
        node, distance = queue.popleft()

        if node == node_b: return distance

        for neighbor in graph[node]:
            if not neighbor in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1

# Function to convert items into adjacency list
def build_graph(edges):
    # Creating an empty dictionary
    graph = {}

    for edge in edges:
        a = edge[0]
        b = edge[1]

        # If the current node is not a key in the graph
        if not a in graph: graph[a] = []
        if not b in graph: graph[b] = []

        # If the key already exists, we can just append the value onto the node list
        graph[a].append(b)
        graph[b].append(a)

    return graph
        



# Test case
edges = [
    ['w', 'y'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]


print(shortest_path(edges, 'w', 'z')) # --> 2

