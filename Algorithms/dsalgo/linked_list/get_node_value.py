# Given a target value, return True if node exists and False otherwise
# Time: O(n) both recursive and iterative
# Space: O(1) -- Iterative, O(n) -- Recursive

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_node_value_recursive(head, index):
    if not head:
        return None
    if index == 0:
        return head.val
    
    return get_node_value_recursive(head.next, index - 1)

def get_node_value_iterative(head, index):
    if not head:
        return None
    
    current = head
    count = 0

    while current:
        if count == index:
            return head.val
        count += 1
        current = current.next

    return None

# Creating our linked list
a = Node(5)
b = Node(6)
c = Node(9)
d = Node(10)

a.next = b
b.next = c
c.next = d

print(get_node_value_recursive(a, 3))
print(get_node_value_iterative(a, 3))