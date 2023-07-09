class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive - Inorder traversal - LVR
def dfs_inorder_recursive(root):
    if not root: 
        return []
    else:
        return dfs_inorder_recursive(root.left) + [root.val] + dfs_inorder_recursive(root.right)

    # 2ND WAY
    # if not root:
    #     return [] 
    # Generating a new empty list everytime the recursive calls -- thus needing concatenation
    # result = []
    # # This contains all the left subtree 
    # result += dfs_inorder_recursive(root.left)
    # result.append(root.val)
    # # This contains all the left subtree + right subtree 
    # result += dfs_inorder_recursive(root.right)

    # return result

# Recursive - Preorder traversal - VLR
def dfs_preorder_recursive(root):
    # if not root:
    #     return []
    # else:
    #     return [root.val] + dfs_preorder_recursive(root.left) + dfs_preorder_recursive(root.right)

    if not root:
        return []
    # Generating a new empty list everytime the recursive calls -- thus needing concatenation
    result = []
    result.append(root.val)
    result += dfs_preorder_recursive(root.left)
    result += dfs_preorder_recursive(root.right)

    return result

# Recursive - Postorder traversal - LRV
def dfs_postorder_recursive(root):
    if not root:
        return []
    else:
        return dfs_postorder_recursive(root.left) + dfs_postorder_recursive(root.right) + [root.val]


# DFS - Recursive with no particular order
def dfs_traversal(root):
    if not root:
        return []
    return dfs_traversal(root.left) + dfs_traversal(root.right)

# Creating a binary tree
root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.right = Node('f')

# Calling our dfs_inorder_recursive function
print(dfs_inorder_recursive(root))

# Calling our dfs_preorder_recursive function
print(dfs_preorder_recursive(root))

# Calling our dfs_post_order_recursive function
print(dfs_postorder_recursive(root))