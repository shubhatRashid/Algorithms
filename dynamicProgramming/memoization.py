"""
Memoization is a specific form of caching that is used in
dynamic programming. The purpose of caching is to improve
the performance of our programs and keep data accessible that
can be used later. It basically stores the previously calculated
result of the subproblem and uses the stored result for the
same subproblem

example :
"""

# calculation nth number in fib series
def fib(n):
  if n == 0 or n == 1:
    return n
  return fib(n - 1) + fib(n - 2)
  # Time: O (2 ^ n)
  # Space: O (n)


store = {}
def fibM(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n not in store:
        store[n] = fibM (n - 1) + fibM (n - 2)
    print (store)
    return store[n]
    # Time: O (n)
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