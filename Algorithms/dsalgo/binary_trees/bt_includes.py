# Checking to see if target exists within our binary tree
# Time complexity: O(n) -> n = # of nodes (Depending if the queue is implemented in O(1) fashion though)
# Space complexity: O(n) 

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Checking to see if target value exists within our tree. Return True if yes, False if not
from collections import deque

def bfs_tree_includes(root, target):

    # Guardian clause to check if tree is originally empty
    if not root:
        return False
    
    # Instantiate a queue with the root element
    queue = deque([root])

    # While the queue is not empty
    while queue:
        current = queue.popleft()
        
        if current.val == target:
            return True

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return False

def dfs_tree_includes_recursive(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    return dfs_tree_includes_recursive(root.left, target) or dfs_tree_includes_recursive(root.right, target)

# Creating a binary tree
root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.right = Node('f')

#       a
#      / \
#     b   c
#    / \    \
#   d   e    f

print(bfs_tree_includes(root, "a")) # -> True
print(dfs_tree_includes_recursive(root, "a"))