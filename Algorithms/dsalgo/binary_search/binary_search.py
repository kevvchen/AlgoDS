def search(lst, target, low, high):
    while low <= high:
        # Find the midpoint in each iteration
        mid = (low + high) // 2

        # If we found the target we are looking for, we can just return it
        if lst[mid] == target:
            return mid
        # If the element we are currently inspecting is larger than the target, we want to search the 
        # left-hand side
        elif lst[mid] > target:
            high = mid - 1
        # Last case is if the current element we are looking at is smaller than the target, search the right side
        else:
            low = mid + 1

    # If the target was never found, we can just return -1
    return -1 

def search_recursive(lst, target, low, high):
    # Base case
    if low > high: return -1

    # Calculate the midpoint
    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return search_recursive(lst, target, low, mid - 1)
    else:
        return search_recursive(lst, target, mid + 1, high)

my_list = [3, 4, 5, 6, 7, 8, 9]

print(search(my_list, 7, 0, len(my_list) - 1))

print(search_recursive(my_list, 7, 0, len(my_list) - 1))