# Write a function howSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments. The function should return
# an array containing any combination of elements that add up to exactly the targetSum. If there is no combination that adds up to 
# the targetSum, then return null. If there are multiple combinations possible, you may return any single one. 

# Time: O(m^2n)
# Space: O(m^2)
def howSum(targetSum, numbers):
    # Sizing the table based on the inputs and initialize with default values
    table = [None for _ in range(targetSum + 1)]
    # Seed value -- base case 
    table[0] = []

    # Iterate through the table
    for i in range(targetSum):
        # Need to check if current position is not None
        if table[i] != None:
            # Iterate through the numbers
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = [*table[i], num]

    return table[targetSum]


print(howSum(7, [2, 3])) 
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [2, 3, 5]))
print(howSum(300, [7, 14]))