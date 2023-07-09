# Time complexity: O(rc) -> r = # rows, c = # of cols
# Space complexity: O(rc)

# Prompt: Write a function minimum_island that takes in a grid containing Ws and Ls. W represents water and L represents land. The function
# should return the size of the smallest island. An island is a vertically or horizontally connected region of land. You
# may assume the grid contains at least one island 

def minimum_island(grid):
    # Keep track of a visited set 
    visited = set()

    # Create a minimum size 
    minimum_size = float('inf')

    # Iterate through each position in the grid
    for rows in range(len(grid)):
        # The purpose of grid[0] is 
        for cols in range(len(grid[0])):
            cur_size = explore(grid, rows, cols, visited)
            if cur_size > 0 and cur_size < minimum_size:
                minimum_size = cur_size

    # print(len(grid)) # --> 6
    # print(len(grid[0])) # --> 5

    return minimum_size

def explore(grid, rows, cols, visited):
    # First we need to check the bounds
    rows_inbound = 0 <= rows < len(grid)
    cols_inbound = 0 <= cols < len(grid[0])

    # Guardian case to see if the current position is within bounds
    if not rows_inbound or not cols_inbound: return 0

    # Check to see if the current position is already visited
    if (rows, cols) in visited: return 0

    # Check to see if we are dealing with water case in grid, then we do not care
    if grid[rows][cols] == 'W': return 0

    # Add the current position to visited
    visited.add((rows, cols))

    # Keep track of the current size
    size = 1

    # Perform a DFS on the graph to see if there are current islands nearby and add them to the size
    size += explore(grid, rows-1, cols, visited)
    size += explore(grid, rows+1, cols, visited)
    size += explore(grid, rows, cols - 1, visited)
    size += explore(grid, rows, cols + 1, visited)

    return size

# Test case
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

print (minimum_island(grid)) # --> 2