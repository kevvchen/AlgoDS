# Given a target value, return True if node exists and False otherwise
# Time: O(n) both recursive and iterative
# Space: O(1) -- Iterative, O(n) -- Recursive

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_target_iterative(head, target):
    if not head:
        return False
    
    current = head

    while current:
        if current.val == target:
            return True
        current = current.next
    
    return False

def find_target_recursive(head, target):
    if not head:
        return False
    if head.val == target:
        return True
    return find_target_recursive(head.next, target)

# Creating our linked list
a = Node(5)
b = Node(6)
c = Node(9)
d = Node(10)

a.next = b
b.next = c
c.next = d

print(find_target_iterative(a, 10))
print(find_target_recursive(a, 12))