class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(n) -> n = # of nodes
# Space complexity: O(n) 

# There is not really a way to implement BFS recursively. A BFS traversal uses a queue but if we do recursion, it is using stacks under the hood, which makes sense

# Using queue -- BFS

# Use a deque when implementing queues - fast appends and pops from both ends
from collections import deque

def bfs_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    # Make sure queue is not empty
    while queue:
        # First to arrive leaves now - FIFO
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result



# Creating a binary tree
root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.right = Node('f')
    
# Calling our function
print(bfs_traversal(root))