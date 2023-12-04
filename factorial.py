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

print(factorialByIteration(5))
print(factorialByRecursion(5))
