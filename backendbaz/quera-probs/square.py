# This code gives a number (n) and returns a square with width and height of (n)
n = int(input("provide a number: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + (" " * (n-2)) + "*")