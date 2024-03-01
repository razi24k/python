a, b = map(float, input("Please enter two numbers: ").split())


def multiply(x, y):
    result = 0
    x_str = str(x)
    if isinstance(x, int) and x > 0:
        for i in range(int(x)):
            result += y
    elif isinstance(x, int) and x < 0:
        for i in range(abs(int(x))):
            result += y
        result = -result
    elif isinstance(x, float) and x > 0:
        integer_p, decimal_p = map(int, x_str.split("."))
        for i in range(integer_p):
            result += y
        side = 0
        for i in range(decimal_p):
            side += y
        side = side / 10
        result += side
    elif isinstance(x, float) and x < 0:
        integer_p, decimal_p = map(int, x_str.split("."))
        for i in range(abs(integer_p)):
            result += y
        result = -result
        side = 0
        for i in range(decimal_p):
            side += y
        side = -side / 10
        result += side
    elif x == 0 or y == 0:
        return 0
    return result


print(multiply(a, b))
