# Write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments. The function should
# return an array containing the SHORTEST combination of numbers that add up to exactly the targetSum. If there is a tie for the 
# shortest combination, you may return any one of the shortest

def bestSum(targetSum, numbers, memo = None):
    if memo is None: memo = {}

    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination != None:
           combination = [*remainderCombination, num]
           # if combination is shorter than the current shortest, then update it
           if shortestCombination == None or len(combination) < len(shortestCombination):
               shortestCombination = combination

    memo[targetSum] = shortestCombination
    return shortestCombination

# m = target sum
# n = numbers.length

# Brute force
# time: O(n^m * m)
# space: O(m^2)

# Memoized
# time: O(m^2 * n)
# space: O(m^2)

# Test cases:
print(bestSum(7, [5, 3, 4, 7])) # [7]
print(bestSum(8, [2, 3, 5])) # [3, 5]
print(bestSum(8, [1, 4, 5])) # [4, 4]
print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]
