# This code prints a multiplication table based on the number given by the user
number = int(input("please provide your number: "))
for i in range(1, number + 1):
    for x in range(1, number+1):
        print(x*i, end=" ")
        if x == number:
            print("")