def reverse_number(n):
    reverse = 0
    while n > 0:
        baghimande = n % 10
        reverse = (reverse * 10) + baghimande
        n = n // 10
    return reverse

n = int(input("provide number: "))

if n == reverse_number(n):
    print("yes")
else:
    print("no")