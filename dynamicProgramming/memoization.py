# MEMOIZATION :

"""
Memoization is a specific form of caching that is used in
dynamic programming. The purpose of caching is to improve
the performance of our programs and keep data accessible that
can be used later. It basically stores the previously calculated
result of the subproblem and uses the stored result for the
same subproblem.To understand the repetetive work and how to
eliminate it draw the solution tree of the problem before implementing
the solution.

example :
"""

# Calculation nth number in fib series
def fib(n): # before memoization
  if n == 0 or n == 1:
    return n
  return fib(n - 1) + fib(n - 2)
  # Time: O (2 ^ n)
  # Space: O (n) as at any point of time max no of spaces used is n as call stacks
    # are popped and appended continously


store = {}
def fibM(n): # after memoization
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n not in store:
        store[n] = fibM (n - 1) + fibM (n - 2)
    print (store)
    return store[n]
    # Time: O (n)
<<<<<<< HEAD
    # Space: O (n)

# Memoization in 2d array:
def count_paths(grid): # count ways to react the end of the grid
    rows = len (grid)
    cols = len (grid[0])
    if grid[rows - 1][cols - 1] == 'X':
        return 0

    def dfs(i, j, memo={}):
        if i == rows or j == cols or grid[i][j] == "X":
            return 0
        key = f"{i},{j}"
        if key in memo:
            return memo[key]
        if i == rows - 1 and j == cols - 1:
            return 1

        memo[f"{i},{j}"] = dfs (i, j + 1) + dfs (i + 1, j)
        return memo[f"{i},{j}"]

    return dfs (0, 0)
=======
    # Space: O (n)

"""
Write a function minChange that takes in an amount and an array of coins. The function should return the minimum number of coins required to create the amount. You may use each coin as many times as necessary.

If it is not possible to create the amount, then return -1.
"""
def minChange(amount,coins):
    
    memo = {}
    def dfs(amount,coins):
        
        if amount in memo:
            return memo[amount]
            
        if amount == 0:
            return 0
        
        if amount < 0 :
            return 100000
        minCount = 100000    
        for c in coins:
            nums = 1+ dfs(amount-c,coins)
            minCount = min(minCount,nums)
        memo[amount] = minCount
        return minCount
        
    res = dfs(amount,coins)
    return res if res!= 100000 else -1
print(minChange(102, [1, 5, 10, 25]))
>>>>>>> d063e397f99fc87b702d6b1b0e2db260392d9ef9
