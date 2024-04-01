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
    # Time Complexity : O(mn)
    # Space Complexity : O(m)
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
    return table[target]
    # Time Complexity : O(m^2 * n)
    # Space Complexity : O(mn)
#print(howSum(7,[2,5,3]))

def bestSum(target,nums):
    table = [None] *(target+1)
    table[0] = []
    for i in range(len(table)):
        if table[i] is not None:
            for num in nums:
                if i+num < len(table):
                    curr = table[i+num]
                    new = table[i].copy()
                    if curr is None:
                        table[i+num] = new
                        table[i + num].append (num)
                    else:
                        if len(curr) > len(new):
                            table[i+num] = new
                            table[i+num].append(num)
    return table[target]
    # Time Complexity : O(m^2 * n)
    # Space Complexity : O(mn)

# print(bestSum(8,[2,3,5]))

# House Robber II solution using tabulation
def rob(nums):
    # cannot do memoization using memo method as we have to use same nums
    # twice which leads to unexpected values from memo
        if len (nums) == 1:
            return nums[0]

        def helper(nums):
            if not nums:
                return 0
            if len (nums) == 1:
                return nums[0]

            table = [0] * len (nums)
            table[0] = nums[0]
            table[1] = nums[1] if nums[1] > nums[0] else nums[0]
            penultimate = table[0]
            prev = table[1]
            for i in range (2, len (nums)):
                table[i] = max (penultimate + nums[i], prev)
                prev = table[i]
                penultimate = table[i - 1]
            return table[-1]

        return max (helper (nums[:-1]), helper (nums[1:]))
        # Time Complexity : O(n)
        # Space Complexity : O(n)

# print(rob([1,3,1,3,100]))

# Solving house robber in const space time complexity
def houseRobber(nums):
    if len (nums) == 1:
        return nums[0]

    def helper(nums):
        if not nums:
            return 0
        if len (nums) == 1:
            return nums[0]

        loot = nums[0]
        prev = nums[1] if nums[1] > nums[0] else nums[0]
        for i in range (2, len (nums)):
            storeprev = prev
            prev = max (loot + nums[i], prev)
            loot = storeprev
        return prev

    return max (helper (nums[:-1]), helper (nums[1:]))

# print(houseRobber([1,3,1,3,100]))
def canConsruct(word,letters):
    table = [False] * (len(word)+1)
    table[0] = True
    for i in range(len(table)):
        if table[i] :
            suffix = word[i:]
            print('suffix is',suffix)
            for p in letters:
                if p in suffix and suffix.index(p) == 0 and i+len(p) < len(table):
                    print('possible prefix is',p)
                    table[i+len(p)] = True
    return table
# print(canConsruct('abcdef',['ab','abc','cd','def','abcd']))

def howConsruct(word,letters):
    table = [None] * (len(word)+1)
    table[0] = ''
    for i in range(len(table)):
        if table[i] is not None :
            suffix = word[i:]
            print('suffix is',suffix)
            for p in letters:
                if p in suffix and suffix.index(p) == 0 and i+len(p) < len(table):
                    print('possible prefix is',p)
                    table[i+len(p)] = table[i] + p
    return table
print(howConsruct('abcdef',['ab','abc','cd','def','abcd']))

