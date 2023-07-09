# # Time: n = # of nodes, e = # of edges --> O(e)
# # Space: O(n)

# # Write a function connectedComponenentsCount, that takes in the adjacency list of an undirected graph. The function should return 
# # the number of connected components within the graph

def connected_component_counts(graph):

    visited = set()
    
    count = 0

    for node in graph:
        # If this recursive call returns True, it should return a connected component, meaning we increment count
        if explore(graph, node, visited) == True:
            count += 1

    return count
    
def explore(graph, current, visited):
    # Recursive dfs base case
    if current in visited: return False

    # If current is not in visited, we visit the node
    visited.add(current)

    # Traverse the neighbor of the current node we are looking at
    for neighbor in graph[current]:
        # Recursively call the neighbors of this function
        explore(graph, neighbor, visited)

    # Returns True if there was a connected component
    return True

# Test case #1
count_components = ({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}) # --> 2

print(connected_component_counts(count_components))
