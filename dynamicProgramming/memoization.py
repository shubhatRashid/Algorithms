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