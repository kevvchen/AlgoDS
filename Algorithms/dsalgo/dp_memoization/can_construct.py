# Write a function canConstruct(target, wordBank) that accepts a target string and an array of strings. The function should return
# a boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank array. You may reuse
# elements of wordBank as many times as needed

def canConstruct(target, wordBank, memo = None):
    if memo is None: memo = {}

    if target in memo: return memo[target]
    if target == "": return True

    for word in wordBank:
        # This means that we found a prefix
        if target.startswith(word):
            # suffix = target.removeprefix(word)
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return True
    
    memo[target] = False
    return False

# m = target.length (height of tree)
# n = wordBank.length (branching factor - from one level of tree to next how does the node in each level changes)
# Brute force
# time: O(n^m * m)
# space: O(m^2)

# Memoized
# time: O(n * m^2)
# space: O(m^2)
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # true
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # false
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # true
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # false