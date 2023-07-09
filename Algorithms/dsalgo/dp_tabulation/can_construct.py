# Write a function canConstruct(target, wordBank) that accepts a target string and an array of strings. The function should return
# a boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank array. You may reuse
# elements of wordBank as many times as needed

# Time: O(m^2 * n)
# Space: O(m)
def canConstruct(target, wordBank):
    table = [False for _ in range(len(target) + 1)]
    table[0] = True

    for i in range(len(target)):
        if table[i] != False:
            for word in wordBank:
                # If the word matches the character starting at position i
                if target[i : i + len(word)] == word:
                    if i + len(word) <= len(target):
                        table[i + len(word)] = True

    return table[len(target)]

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # true
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # false
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # true
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # false