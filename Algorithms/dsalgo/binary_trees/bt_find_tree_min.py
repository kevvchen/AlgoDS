# Figure out what the minimum value of the tree is --> This is a BT not a BST
# Time: O(n) -> n = # nodes
# Space: O(n) 

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This given problem tells us beforehand that the root definitely exists
def dfs_tree_min_iterative(root):
    smallest = float('inf')
    # print(type(smallest))
    # print(smallest)

    stack = [root]

    while stack:
        current = stack.pop()
        if current.val < smallest: smallest = current.val

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    return smallest

# BFS 
from collections import deque
def bfs_tree_min(root):
    smallest = float('inf')

    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.val < smallest: smallest = current.val

        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

    return smallest

# DFS - recursion
def dfs_tree_min_recursive(root):
    if not root:
        return float('inf')
    
    leftMin = dfs_tree_min_recursive(root.left)
    rightMin = dfs_tree_min_recursive(root.right)
    return min(root.val, leftMin, rightMin)
    

# Creating our Binary Tree
root = Node(3)
root.left = Node(11)
root.right = Node(4)
root.left.left = Node(4)
root.left.right = Node(-2)
root.right.right = Node(1)

#       3
#      / \
#     11   4
#    / \    \
#   4   -2   1

print(dfs_tree_min_iterative(root))
print(bfs_tree_min(root))
print(dfs_tree_min_recursive(root))