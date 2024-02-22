# This code returns factorial of a given number from user
num = int(input("please provide your number: "))
fac_num = 1
for i in range(2, num+1):
    fac_num *= i
print(f"factorial of your number is: {fac_num}")