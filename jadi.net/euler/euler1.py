def multiply5_3(x):
    multiply= True
    if x % 5==0 or x % 3==0:
        multiply
    else:
        multiply = False
    return multiply
sumcount = 0
for i in range(1,1000):
    if multiply5_3(i):
        sumcount += i

print(sumcount)