# Reverse the order of the list and return the new head
# Time: O(n)
# Space: O(1) -- Iterative

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list_iterative(head):
    prev = None
    current = head

    while current:
        store_next = current.next
        current.next = prev
        prev = current
        current = store_next

    return prev.val

def reverse_list_recursive(head, prev = None):
    if not head:
        return prev
    store_next = head.next
    head.next = prev
    return reverse_list_recursive(store_next, head)


# Creating our linked list
a = Node(5)
b = Node(6)
c = Node(9)
d = Node(10)

a.next = b
b.next = c
c.next = d

# 5 -> 6 -> 9 -> 10

print(reverse_list_iterative(a))
print(reverse_list_recursive(a))