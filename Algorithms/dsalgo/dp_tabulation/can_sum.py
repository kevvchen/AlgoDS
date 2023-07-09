# Write a function canSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments. The function should return
# a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array. 
# You may use an element of the array as many times as needed. You may assume that all input numbers are nonnegative 

# m = targetSum.length
# n = numbers.length
# TIME: O(mn)
# SPACE: o(m)
def canSum(targetSum, numbers):
    # Size the table based on targetSum and initializing all to false
    table = [False for _ in range(targetSum + 1)]
    # Our seed value is the base case where targetSum = 0 is True
    table[0] = True

    for i in range(targetSum):
        if table[i] == True:
            for num in numbers:
                # Checking to see if index is within range
                if i + num <= targetSum:
                    table[i + num] = True

    return table[targetSum]

print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))