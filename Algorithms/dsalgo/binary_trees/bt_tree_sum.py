# Time complexity: O(n) -> n = # of nodes 
# Space complexity: O(n) -> The implicit call stack space (solving this problem recursively with dfs)

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_tree_sum(root):
    # Base case: Sum of an empty tree is 0
    if not root:
        return 0
    
    # The tree_sum(root.left) will gather all the sum of the left subtree, while the tree_sum(root.right) gathers all sum of right subtree. We then add those together with our own root
    return root.val + dfs_tree_sum(root.left) + dfs_tree_sum(root.right)


from collections import deque
def bfs_tree_sum(root):
    
    sum = 0

    if not root:
        return 0
    
    queue = deque([root])

    while queue:
        current = queue.popleft()
        sum += current.val
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return sum

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

print(dfs_tree_sum(root))
print(bfs_tree_sum(root))