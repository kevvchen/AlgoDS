# Add all the sum of the linked list starting from head and return the total sum
# Time: O(n)
# Space: O(1) if iteratively, O(n) if recursive because of stack

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sum_list_iterative(head):
    sum = 0
    current = head

    while current:
        sum += current.val
        current = current.next

    return sum

def sum_list_recursive(head):
    if not head:
        return 0
    return head.val + sum_list_recursive(head.next)

# Creating our linked list
a = Node(5)
b = Node(6)
c = Node(9)
d = Node(10)

a.next = b
b.next = c
c.next = d

print(sum_list_iterative(a))
print(sum_list_recursive(a))