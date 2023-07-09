# Write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments. The function should
# return an array containing the SHORTEST combination of numbers that add up to exactly the targetSum. If there is a tie for the 
# shortest combination, you may return any one of the shortest

# m = targetSum
# n = numbers.length
# Time complexity: O(m^2n)
# Space: O(m^2)
def bestSum(targetSum, numbers):
    table = [None for _ in range(targetSum + 1)]
    table[0] = []

    for i in range(targetSum):
        if table[i] != None:
            for num in numbers:
                if i + num <= targetSum:
                    combination = [*table[i], num]
                    if table[i + num] is None or len(combination) < len(table[i + num]):
                        table[i + num] = combination
    
    return table[targetSum]


print(bestSum(7, [5, 3, 4, 7])) # [7]
print(bestSum(8, [2, 3, 5])) # [3, 5]
print(bestSum(8, [1, 4, 5])) # [4, 4]
print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]