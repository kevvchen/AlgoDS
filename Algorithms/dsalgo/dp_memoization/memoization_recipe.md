Alvin's Memoization Recipe:
1. Make it work (Brute force recursive approach (most likely be slow))
    - Visualize the problem as a tree (Each node is a problem, and each connecting edge is a subproblem)
    - Implement the tree using recursion (Think of leaves as base case)
    - Test it 
2. Make it efficient
    - Add a memo object (Use a dictionary)
    - Add a new base case to return memo values
    - Store return values into the memo