class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list_iterative(head):
    current = head

    while current:
        print(current.val)
        current = current.next

def print_linked_list_recursive(head):
    # Base case
    if not head:
        return
    print(head.val)
    print_linked_list_recursive(head.next)

# Creating our linked list
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

# A -> B -> C -> D -> NULL

# Calling print_linked_list_iterative with our head node
print_linked_list_iterative(a)

# Calling print_linked_list_recursive with our head node
print_linked_list_recursive(a)