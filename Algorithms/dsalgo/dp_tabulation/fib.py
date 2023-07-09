# Write a function fib(n) that takes in a number as an argument. The function should return the n-th number of the Fibonacci sequence.
# The 0th number of the sequence is 0.
# The 1st number of the sequence is 1.
# To generate the next number of the sequence, we sum the previous two.

def fib(n):
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

print(fib(6)) #8
print(fib(7)) #13
print(fib(8)) #21
print(fib(50)) #12586269025
