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
print(fibTab(7))