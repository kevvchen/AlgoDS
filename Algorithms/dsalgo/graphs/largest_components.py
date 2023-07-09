# Time: O(e)
# Space: O(n)

def largest_component(graph):
    # Create a set that holds the node b/c set lookup time is O(1)
    visited = set()

    longest_comp = 0

    # This is iterating through each key of the adjacency list
    for node in graph:
        cur_size = explore_size(graph, node, visited)
        # print(cur_size)
        if longest_comp < cur_size:
            longest_comp = cur_size


    return longest_comp

def explore_size(graph, current, visited):

    if current in visited: return 0

    visited.add(current)

    size = 1
    # Dfs recursive traversal
    for neighbor in graph[current]:
        size += explore_size(graph, neighbor, visited)

    return size

largestComponent = ({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}) # --> 4

print(largest_component(largestComponent))