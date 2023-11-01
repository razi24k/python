n1 = int(input("insert first number:"))
op = input("insert operator(+ or -):")
n2 = int(input("insert second number:"))
if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
else:
    print("wrong input!")