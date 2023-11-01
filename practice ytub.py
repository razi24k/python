# number 1
def print_date(day, month, year):
    resault="%d/%d/%d" %(year, month, day)
    print(resault)

print_date(23,8,2023)

# number 2
def max_number(num1, num2,num3):
    if num1 > num2 and num1 > num3:
        max= num1
    elif num2 > num1 and num2 > num3:
        max=num2
    else:
        max= num3
    print("maximum number between %d, %d and %d is %d" %(num1, num2, num3, max))

# max_number(int(input("enter first number:")), int(input("enter second number:")), int(input("enter third number:")))

# number 3
def even_odd(x):
    if x % 2 ==0:
        print("it's Even huuraaa!")
    elif x % 2 != 0:
        print("it's odd hayyaaah!")
    else:
        print("you have to give me an integer!")
y=int(float(input("give me a integer: ")))

# even_odd(int(input("give me a integer: ")))