'''import sys
print("python version:\n", sys.version , "\nversion info:\n", sys.version_info)
import datetime
now = datetime.datetime.now()
print("current date and time:")
print(now.strftime("%y-%m-%d %H:%M:%S"))
from math import pi
r = float(input("plese provide radius of your circle(in CM): "))
print("the area of the circle with radius " + str(r) + "CM, is: ", pi * r**2, "Centimeter.")
name = input("please provide your name: ")
family = input("and your last name?: ")
print(family, name)
digits = input("print some random numbers (use comma(,) to seprate numbers): ")
print(digits.split(","))
print(tuple(digits.split(",")))
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = zip(list1, list2)
print(zipped)
exam_st_date = (11, 12, 2014)
print("the examination will start from %d/%d/%d" %(exam_st_date))
print(abs.__doc__)
class MyClass:
    x = 5
print(MyClass().x)
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x = student("Rasool", "Zirak")
print(x.firstname)
print("I want to show you the average of 3 number")
x= input("please provide 3 numbers: ")
s = list(map(int, x.split()))
avg = 0
for i in range(len(s)):
    avg += s[i]
print("average of numbers %d,%d and %d is: " %(s[0],s[1],s[2]),avg/len(s))
print("maximum of these numbers: %d" %(max(s[0],s[1],s[2])))
for i in [1, 2, 3, 4, 5]:
    for x in [1, 2]:
        print("S", i, "e", x)
print(not True)'''

