# Write a function allConstruct(target, wordBank) that accepts a target string and an array of strings. The function should return 
# a 2D array containing all of the ways that the target can be constructed by concatenating elements of the wordBank array. Each element
# of the 2D array should represent one combination that constructs the target. You may reuse elements of wordBank as many times as
# needed.

# Time: ~O(n^m)
# Space: ~O(n^m)
def allConstruct(target, wordBank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target)):
        for word in wordBank:
            if target[i : i + len(word)] == word:
                if i + len(word) <= len(target):
                    # Copy over the current array but adding the current word to it
                    newCombination = [sub_array + [word] for sub_array in table[i]]
                    table[i + len(word)].extend(newCombination)

    return table[len(target)]

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
#[]
