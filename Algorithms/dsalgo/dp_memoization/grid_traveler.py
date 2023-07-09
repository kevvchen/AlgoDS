# Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner.
# You can only move down or right. In how many ways can you travel to the goal on a grid with dimensions m * n?

# Write a function gridTraveler(m, n) that calculates this


# Time complexity: O(nm)
# Space complexity: O(n + m)

# Store memoization as tuples (m, n) - (4, 23)
memo = {}

def gridTraveler(m, n, memo):
    # Store m,n as tuples to key into the dictionary
    key = (m, n)

    # Base cases
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    if key in memo: return memo[key]

    # Memoization
    # m - 1 is going down, n - 1 is going right
    memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)

    return memo[key]
    

# Test cases
print(gridTraveler(1, 1, memo))   # 1
print(gridTraveler(2, 3, memo))   # 3
print(gridTraveler(3, 2, memo))   # 3
print(gridTraveler(3, 3, memo))   # 6
print(gridTraveler(18, 18, memo)) # 2333606220


