def gridTraveler(m, n):
    table = [[0 for _ in range(n + 1)] for _ in range (m + 1)]
    # In tabulation process, this is essentially our base case
    table[1][1] = 1

    # Use nested loops to iterate through 2D array
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            # This is to the right
            if (j + 1 <=n):
                table[i][j+1] += current
            # This is neighbor below
            if (i + 1 <= m):
                table[i+1][j] += current

    return table[m][n]

print(gridTraveler(1, 1)) #1
print(gridTraveler(2, 3)) #3
print(gridTraveler(3, 2)) #3
print(gridTraveler(3, 3)) #3
print(gridTraveler(18, 18)) #3