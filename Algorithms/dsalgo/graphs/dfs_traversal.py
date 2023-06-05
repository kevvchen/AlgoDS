# Using stack 
def depth_first_print(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

def depth_first_recursive(graph, source):
    print(source)

    # This is essentially our base case
    for neighbor in graph[source]:
        depth_first_recursive(graph, neighbor)

from collections import deque
def breadth_first_print(graph, source):
    queue = deque([source])
    while queue:
        current = queue.popleft()
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


# This is the adjacency list
graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# depth_first_print(graph, 'a') # acebdf
# depth_first_recursive(graph, 'a')

breadth_first_print(graph, 'a') # acbedf