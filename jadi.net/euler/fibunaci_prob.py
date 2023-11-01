def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
first = 1
seccond = 2
sum = 0
while first < 4000000:
    new = first + seccond
    first = seccond
    seccond = new
    if isEven(first):
        sum += first
print(sum)