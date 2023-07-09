def undirected_path(edges, node_a, node_b):
    graph = build_graph(edges)

    # print(graph)
    
    # Keeping track of visited nodes with set ds
    return has_path(graph, node_a, node_b, visited = set())

def has_path(graph, src, dst, visited):
    # Since we are told this graph has a cycle, we need to take care of that
    if src == dst: return True
    if src in visited: return False

    # If been visited add the node to the set
    visited.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited) == True: return True

    return False


# I need to convert the edges of lists given to us into an
# Adjacency list of dictionary
def build_graph(edges):
    # Creating an empty dictionary
    graph = {}

    for edge in edges:
        a = edge[0]
        b = edge[1]

        # If the edges are not already in our dictionary, initialize an empty dictionary and store the edges as keys
        if not a in graph: graph[a] = []
        if not b in graph: graph[b] = []

        # If the edge is already a key, push the corrensponding value
        graph[a].append(b)
        graph[b].append(a)

    return graph


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(undirected_path(edges, 'j', 'm'))
print(undirected_path(edges,'m', 'o'))