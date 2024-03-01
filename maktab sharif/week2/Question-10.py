# Q10
# import math
a = float(input("Please enter num a. "))
b = float(input("Please enter num b. "))
c = float(input("Please enter num c. "))

if abs(a-b) < c < abs(a+b) and abs(a-c) < b < abs(a+c) and abs(c-b) < a < abs(c+b):
    s = (a + b + c) / 2
    # A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(A)
else:
    print("Dadash in Mosalas nista!!!")
