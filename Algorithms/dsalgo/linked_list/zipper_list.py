# Iterative:
# n = length of list1
# m = length of list2
# Time: O(min(n,m))
# Space: O(1)

# Recursive:
# Time:

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def zipper_list(head1, head2):
    tail, current1, current2, count = head1, head1.next, head2, 0

    while current1 and current2:
        # If count is even, then we append from head1
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count += 1

    if not current1:
        tail.next = current1
    if not current2:
        tail.next = current2

    return head1

def zipper_list_recursive(head1, head2):
    if not head1 and not head2:
        return None
    if not head1:
        return head2
    if not head2:
        return head1
    
    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipper_list_recursive(next1, next2)
    return head1


# Some examples of the problem:
# List1: A -> B -> C -> D -> E -> F
# List2: Q -> R
# Result: A -> Q -> B -> R -> C -> D -> E -> F

# List1: A -> B -> C
# List2: D -> E -> F
# Result: A -> D -> B -> E -> C -> F
