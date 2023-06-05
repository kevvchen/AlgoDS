class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(n) -> n = # of nodes
# Space complexity: O(n) 

# Using stack -- DFS

# DFS - generic
def dfs(node):

    if not node:
        return None

    # Initialize stack with root node
    stack = [node]

    while stack:
        current = stack.pop()

        # Visit the current node
        print(current.val)

        # Push right child first
        if current.right:
            stack.append(current.right)

        # Push left child 
        if current.left:
            stack.append(current.left)

# DFS - Inorder traversal - LVR
def dfs_inorder_traversal(root):
    stack, result = [], []
    current = root

    while stack or current:
        # If there is a node that has not been visisted, add it to the stack and traverse as left as possible
        if current:
            stack.append(current)
            current = current.left
        # Finish traversing the left side, so now we can go to the right
        else: 
            current = stack.pop()
            result.append(current.val)
            current = current.right
    
    return result


# DFS - Preorder traversal - VLR    
def dfs_preorder_traversal(root):
    stack, result = [], []
    current = root

    while stack or current:
        if current:
            result.append(current.val)
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            current = current.right

    return result

# DFS - Postorder traversal - LRV
def dfs_postorder_traversal(root):
    stack, result = [], []
    current = root
    prev = None

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek = stack[-1]
            if peek.right and prev != peek.right:
                current = peek.right
            else:
                result.append(peek.val)
                prev = stack.pop()
    
    return result



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

# Calling our function
dfs(root)

# Calling inorder traversal
print(dfs_inorder_traversal(root))

# Calling preorder traversal
print(dfs_preorder_traversal(root))

# Calling postorder traversal
print(dfs_postorder_traversal(root))