# Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should
# return the number of islands on the grid. An island is vertically or horizontally connected region of land

def island_count(grid):

    # Keeping track to see if we have visited a current position in grid already
    visited = set([])

    # Keep track of how many islands
    count = 0

    # In python, range works with integers (which is our grid), and len works with iterables (list)

    # Given the grid, we need to iterate through each 'node' with row and col
    for row in range(len(grid)):
        # grid[0] checks the row length of every row. Good if our grid is not like a perfect m x n grid
        for col in range(len(grid[0])):
            # Call explore to check for island
            if explore(grid, row, col, visited) == True:
                count += 1

    return count

def explore(grid, row, col, visited):
    # Need to check if row and column are in bound
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])

    # If the above two cases are not true, just return False
    if not row_inbounds or not col_inbounds: return False

    # If the current position is visited, then just return false
    if (row, col) in visited: return False

    # We only care about Land and not water, so if we encounter a water position return False
    if grid[row][col] == 'W': return False

    # Add it to the visited set if the current position is unvisited
    visited.add((row, col))

    # Now recursively call explore to check the islands connected surroudning the current position (DFS)
    # Moving up the grid 
    explore(grid, row-1, col, visited)
    # Moving down the grid
    explore(grid, row+1, col, visited)
    # Moving to the left of the grid
    explore(grid, row, col-1, visited)
    # Moving to the right of the grid
    explore(grid, row, col+1, visited)

    # Can just return True since none of the base cases has been hit
    return True

#1:58

grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]


print(island_count(grid)) # --> 3