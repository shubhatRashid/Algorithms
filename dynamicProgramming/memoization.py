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
    # Space: O (n)
    # Time : O (n)

# MEMOIZATION RECIPE
"""
 1 ) Solve the problem:
 
    - find out the brute force solution by
      considering recursion as a tree.Find its
      base case and build from there.
 2 ) Make it efficient:
 
    - add a memo object
    - add a new base case considering memo object
    - add the return values in memo object.
"""

# Write a function to check if elements in an array can sumup in
# any combination to form a target element

#BruteForce solution
def canSum (target,arr): # target = 7 , arr = [5,3,4,7]
    if target == 0:
        return True
    if target < 0:
        return False

    for a in arr:
        if canSum(target-a,arr):
            return True
    return False
    # Time complexity = O(n^m) m = target , n = len(arr)
    # Space complexity = O(m)

# Memoized solution
def canSumMemoised (target,arr,memo={}): # target = 7 , arr = [5,3,4,7]
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for a in arr:
        if canSumMemoised(target-a,arr,memo):
            memo[target] = True
            return True

    memo[target] = False
    return False
    # Time complexity = O(m*n)
    # Space complexity = O(m)

# In the above problem return one of the array of numbers which
# sum up to target
def howSum (target,arr,memo={}): # target = 7 , arr = [5,3,4,7]
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    for a in arr:
        temp = howSum(target-a,arr,memo)
        if temp != None :
            temp.append(a)
            memo[target] = temp
            return temp
    memo[target] = None
    return None
    # Time complexity = O(n*m)
    # Space complexity = O(m+m*m) ~ O(m^2) recursion stack and memo
    # in memo each key can take atmost an array of length m hence m^2

# In above problem return the array with min length
# from the all solutions
def bestSum(target,arr): #bruteforce
    if target == 0:
        return []

    if target < 0:
        return None

    array = None
    for a in arr:
        temp = bestSum(target-a,arr)
        if temp is not None :
            temp.append(a)
            if  array is None or len(temp) < len(array):
                array = temp
    return array
    # Time complexity : O(n^m)
    # Space complexity : O(m*m) as we are creating an 'array' for each call

def bestSumMemoized(target,arr,memo): # memoized
    if target in memo:
        return memo[target]
    if target == 0:
        return []

    if target < 0:
        return None

    array = None
    for a in arr:
        temp = bestSumMemoized(target-a,arr,memo)
        if temp is not None :
            temp = temp[:]
            # appending to the same temp leads to unexpected behavior
            # as it is edited across all calls
            # it didnot matter in previous questions as we were returning
            # as soon as we got the answer
            temp.append(a)
            if array is None or len(temp) < len(array):
                array = temp
    memo[target] = array
    return array
    # Time complexity : O(n*m*m) as we copy temp in each call
    # Space complexity : O(m*n) # previous and memo

"""
    Given a string and an array containing substrings return True if 
    the string can be constructed using the substrings in the array and 
    false otherwise
"""
# Solution 1 : we take an empty string and build with each call
def canConstruct(s,wordbank,target,memo={}):
    if s in memo:
        return memo[s]
    if s == target:
        return True
    if len(s) > len(target):
        return False

    for sub in wordbank:
        if canConstruct(s+sub,wordbank,target,memo):
            memo[s] = True
            return memo[s]
    memo[s] = False
    return memo[s]
    # Time : O(n*m)
    # Space : O(m)

# Alternate solution : We reduce the target in each call
def canConstruct2(wordbank,target,memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return True

    for sub in wordbank:
        if sub in target and target.index(sub) == 0 :
            sufix = target[len(sub):] # O(m) operation
            if canConstruct2(wordbank,sufix,memo):
                memo[target] = True
                return True
    memo[target] = False
    return False
    # Time : O(n^m *m) before memoization and O(n*m^2) after memoization
    # Space : O(m^2)

"""
In the above problem now return the no of ways whe string can be formed
"""
def countConstruct(wordbank,target,memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return 1

    count = 0
    for sub in wordbank:
        if sub in target and target.index(sub) == 0 :
            suffix = target[len(sub):] # O(m) operation
            count += countConstruct(wordbank,suffix,memo)
    memo[target] = count
    return count
    # Time : O(n^m *m) before memoization and O(n*m^2) after memoization
    # Space : O(m^2)
print(countConstruct(['a','p','ent','enter','ot','o','t'],'enterapotentpot')) # 4