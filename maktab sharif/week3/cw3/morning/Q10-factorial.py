import math


def factorial(x):
    return math.factorial(x)


my_list = [1, 5, 7, 11]
factorial_list = list(map(factorial, my_list))
print(factorial_list)
