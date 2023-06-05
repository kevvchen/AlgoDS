class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    # Base case 1
    if not root:
        return float('-inf')
    # Base case 2 - if we encountered leaf nodes
    if not root.left and not root.right:
        return root.val
    
    # Our recursive calls
    maxChildPathSum = max(max_path_sum(root.left), max_path_sum(root.right))
    return root.val + maxChildPathSum

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

print(max_path_sum(root))