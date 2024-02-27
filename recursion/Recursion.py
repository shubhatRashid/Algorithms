# RECURSION :
# Recursion is a method of looping using a function until the base case
# is triggered which terminated the loop by returning something...
# A recursive function solves a particular problem by calling a simpler copy
# of itself and solving smaller sub-problems of the original problems.

# examples and comparison :

# factorial :
def factorialByRecursion(number):
    if number == 1:
        return 1
    else:
        return number * factorialByRecursion (number - 1)


def factorialByIteration(number):
    res = 1
    for i in range(2,number+1):
        res *= i
    return res

# permutations
def permutations(string,pocket=""): #recursion
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            back = string[i+1:]
            front = string[:i]
            together = front + back
            print(letter,front,back,together,pocket)
            permutations(together,pocket+letter)


