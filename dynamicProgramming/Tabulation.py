# TABULATION STRATEGY

# solving fib using tabulation
def fibTab(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(len(table)):
        if i+1 < len(table):
            table[i+1] += table[i]
        if i+2 < len(table):
            table[i+2] += table[i]
    return table[-1]

# gridTraveller using tabulation
def gridTravel(m,n):
    table = [[0 for i in range(m+1)] for j in range(n+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if i+1 <= m:
                table[i+1][j] += current
            if j+1 <= n:
                table[i][j+1] += current

    print (table)
    return table[m][n]

# Memoization Recipe
"""
    1) visualise the problem as a table
    2) figure out the size of table on basis of inputs
    3) initialize the table with given size and default values
    4) figure out the base case values for the table / seed values
    5) iterate through the table with the logic required for the problem
"""
def canSum(target,nums):
    table = [False]*(target+1)
    table[0] = True
    for i in range(len(table)):
        if table[i]:
            for num in nums:
                if i+num < len(table):
                    table[i+num] = True
    return table[target]
# print(canSum(7,[5,3,4]))
# print(canSum(7,[2,4]))

def howSum(target,nums):
    table = [None] *(target+1)
    table[0] = []
    for i in range(len(table)):
        if table[i] is not None:
            for num in nums:
                if i+num < len(table):
                    table[i+num] = table[i].copy()
                    table[i+num].append(num)
    return table
print(howSum(7,[5,3,4]))
