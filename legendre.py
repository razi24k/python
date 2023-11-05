p = int(input("insert p: "))
n = int(input("insert n: "))
x = 1
result = 0
while p**x <= n:
    result = result + int(n/p**x)
    x += 1
print(f"the legendre is {result}")
