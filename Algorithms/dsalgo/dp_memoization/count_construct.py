# Write a function countConstruct(target, wordBank) that accepts a target string and an array of strings. The function should
# return the number of ways that the target can be constructed by concatenating elements of the wordBank array. You may reuse 
# elements of wordBank as many times as needed

def countConstruct(target, wordBank, memo = None):

    if memo is None: memo = {}

    if target in memo: return memo[target]
    if target == "": return 1

    totalCount = 0

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            # numWaysForRest returns the number of ways we can generate the rest of the suffix
            numWaysForRest = countConstruct(suffix, wordBank, memo)
            totalCount += numWaysForRest

    memo[target] = totalCount
    return memo[target]

print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # 0