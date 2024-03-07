def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


n = int(input("Please enter n. "))
print("The factorial of", n, "is:", factorial(n))