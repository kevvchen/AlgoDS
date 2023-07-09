# Fibonacci sequence with memoization
# Storing each fib inside a dictionary for O(1) search up
memo = {}

# Time complexity: O(n) --> O(2n) but drop constant
# Space complexity: O(n)

def fib(n, memo):
    # Base case 1:
    if n in memo: return memo[n]
    # Base case 2:
    if n <= 2: return 1

    # The memoization process
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]

print(fib(6, memo)) # 8
print(fib(7, memo)) # 13
print(fib(8, memo)) # 21
print(fib(50, memo)) # 12586269025

