# Write a function howSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments. The function should return
# an array containing any combination of elements that add up to exactly the targetSum. If there is no combination that adds up to 
# the targetSum, then return null. If there are multiple combinations possible, you may return any single one. 

def howSum(targetSum, numbers, memo = None):
    if memo is None: memo = {}

    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult  = howSum(remainder, numbers, memo)
        if remainderResult != None:
            memo[targetSum] = [*remainderResult, num]
            return memo[targetSum]

    memo[targetSum] = None
    return None


# m = targetsum
# n = numbers.length
# Brute force time complexity: O(n^m * m)
# Space complexity: O(m)

# Memoized
# time: O(n * m^2)
# space: O(m^2)

# Test cases:
print(howSum(7, [2, 3])) 
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [2, 3, 5]))
print(howSum(300, [7, 14]))