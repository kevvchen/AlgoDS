# Traverse the link list and append the value to our list
# Time: O(n) -> n = # of nodes
# Space: O(n)

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_values_iterative(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    
    return result
    
def linked_values_recursive(head):
    result = []
    # Helper function
    fill_values(head, result)
    return result

# Helper function for recursive call -- This helps because our main linked_values_recursive will not have to create multiple arrays
def fill_values(head, result):
    if not head:
        return
    result.append(head.val)
    fill_values(head.next, result)


# Creating our linked list
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

print(linked_values_iterative(a))
print(linked_values_recursive(a))