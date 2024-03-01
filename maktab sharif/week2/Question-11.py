# Q11
try:
    a = float(input("Please enter a. "))
    b = (input("Please enter operator. "))
    c = float(input("Please enter b. "))

    if b == "*":
        print(a * c)

    elif b == "-":
        print(a - c)

    elif b == "/":
        print(a / c)

    elif b == "%":
        print(a % c)

    elif b == "+":
        print(a + c)

    else:
        assert b in ["+", "-", "*", "%", "/"], "This is a typeError"

except (ZeroDivisionError, ValueError, AssertionError) as e:
    print(e)