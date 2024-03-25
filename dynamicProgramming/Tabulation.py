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

print(gridTravel(3,3))