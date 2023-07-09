# Acylic graphs has no cycles
# Cyclic graph has cycles = infinite loop

# Given an acyclic graph, and a source node as well as a 
# destination node, return true or false based on if
# you can travel from src node to dst node

# Approach: Can use BFS or DFS
# Time: O(e) -> # nodes , # edges (checking edges)
# Space: O(n)
# Or Time: O(n^2) -> n = # nodes, n^2 = # edges

from collections import deque
def has_path_bfs(graph, src, dst):
    queue = deque([src])

    while queue:
        current = queue.popleft()

        if current == dst:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    return False

# Recursive DFS version 
def has_path_dfs(graph, src, dst):
    # Base case to check if src is equal to dst
    if src == dst: return True

    # If not we need to recursively call this function on each
    # neighbor node 
    for neighbor in graph[src]:
        if has_path_dfs(graph, neighbor, dst) == True: return True
    
    return False

graph = {
    'f': ['g','h'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path_bfs(graph, 'j', 'f'))
print(has_path_dfs(graph, 'i', 'k'))