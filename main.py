def factorial(x):
    fac = 1
    for i in range(1, x + 1):
        fac = fac * i
    return fac
print(factorial(5))