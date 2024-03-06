import math
import random

try:
    you_or_me = int(input("Enter 1 to generate random numbers and 2 to do it yourself: "))
    while you_or_me not in [1, 2]:
        print("Invalid input")
        you_or_me = int(input("Enter 1 to generate random numbers and 2 to do it yourself: "))
    else:
        if you_or_me == 1:
            operator = input(
                "What operation is in your mind: (+, -, *, /, exponentiation, square root, logarithm, factorial)")
            if operator not in ["+", "-", "*", "/", "exponentiation", "logarithm", "factorial", "square root"]:
                raise TypeError(
                    "We are struggling here, you don't know what has happened to us, your operator not found!")
            if operator in ["+", "-", "*", "/", "exponentiation", "logarithm"]:
                first_num = random.randint(1, 1001)
                second_num = random.randint(1, 1001)
            else:
                first_num = random.randint(1, 1001)

        else:
            first_num = float(input("Enter first number: "))
            operator = input(
                "What operation is in your mind: (+, -, *, /, exponentiation, square root, logarithm, factorial)")
            if operator not in ["+", "-", "*", "/", "exponentiation", "logarithm", "factorial", "square root"]:
                raise TypeError("Invalid. your operator not found!")
            if operator in ["+", "-", "*", "/", "exponentiation", "logarithm"]:
                second_num = float(input("Enter second number: "))

    if operator == "+":
        print(f"{first_num} plus {second_num} equals {first_num + second_num}")
    elif operator == "-":
        print(f"{first_num} minus {second_num} equals {first_num - second_num}")
    elif operator == "*":
        print(f"{first_num} times {second_num} equals {first_num * second_num}")
    elif operator == "/":
        print(f"{first_num} over {second_num} equals {first_num / second_num}")
    elif operator == "exponentiation":
        print(f"{first_num} raised to the power of {second_num} equals {math.pow(first_num, second_num)}")
    elif operator == "logarithm":
        print(f"logarithm of {first_num} with base {second_num} is {math.log(first_num, second_num)}")
    elif operator == "square root":
        print(f"square root of {first_num} is {math.sqrt(first_num)}")
    elif operator == "factorial":
        print(f"{first_num} factorial is: {math.factorial(first_num)}")
except TypeError:
    print("hey bro, your operator not found!")
except ZeroDivisionError:
    print("is mathematics a joke for you?I really can't divide any number by zero!")
except ValueError:
    print(
        "you must know these rules:\n1.factorial not defined for negative values\n"
        "2.logarithm of a number can't be zero or less than zero\n"
        "3.base of a logarithm must be positive and not equal to one\n4.square root is not defined for "
        "negative values\n5.at the end you must know you have to insert numbers as input to complete task")
except Exception as e:
    print("An error occurred:", e)
else:
    print(f"The operation completed successfully")
