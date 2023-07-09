# Write a function countConstruct(target, wordBank) that accepts a target string and an array of strings. The function should
# return the number of ways that the target can be constructed by concatenating elements of the wordBank array. You may reuse 
# elements of wordBank as many times as needed

# Time: O(m^2n)
# Space: O(m)
def countConstruct(target, wordBank):
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1

    for i in range(len(target)):
        if table[i] != 0:
            for word in wordBank:
                if target[i : i + len(word)] == word:
                    if i + len(word) <= len(target):
                        table[i + len(word)] += table[i]

    return table[len(target)]

print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) #2
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # 0