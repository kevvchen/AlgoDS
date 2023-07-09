# Write a function allConstruct(target, wordBank) that accepts a target string and an array of strings. The function should return 
# a 2D array containing all of the ways that the target can be constructed by concatenating elements of the wordBank array. Each element
# of the 2D array should represent one combination that constructs the target. You may reuse elements of wordBank as many times as
# needed.

def allConstruct(target, wordBank, memo = None):

    if memo is None: memo = {}

    if target in memo: return memo[target]

    # Base case
    # The outer collection stores all subarrays inside it that makes a path to the base case of empty string
    if target == '': return [[]]

    # Add all the possible paths
    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            # An array of all the ways to build the suffix -- think of suffixWays as just [[]] from all the paths that lead us to an ''
            suffixWays = allConstruct(suffix, wordBank, memo)

            # All the ways to make the original target -- think of as adding all the edges to the subarrays
            targetWays = [[word] + way for way in suffixWays]

            # Necessary because targetWay currently is only exploring one single path down, we want all the paths that brings us to 
            # target
            result.extend(targetWays)

    memo[target] = result
    return result

# m = target.length
# n = wordBank.length
# time: O(n^m)
# space: O(m)

print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
# [
#   ['purp', 'le']
#   ['p', 'ur', 'p', 'le']
# ]
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
# [
#   ['ab', 'cd', 'ef']
#   ['ab', 'c' 'def']
#   ['abc', 'def']
#   ['abcd', 'ef']
# ]
print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
# []
print(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
# []
