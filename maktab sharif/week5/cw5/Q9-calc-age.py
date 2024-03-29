import datetime

name = input("please enter a name : ")
year = int(input("please enter a year : "))


def calc_age(year1):
    present = datetime.datetime.now().year
    return present - year1


age = calc_age(year)
print(f"Hello, {name}! You are {age} years old.")