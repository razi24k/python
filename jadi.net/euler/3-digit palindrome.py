the_list = []
def reverse_number(n):
    reverse = 0
    while n > 0:
        baghimande = n % 10
        reverse = (reverse * 10) + baghimande
        n = n // 10
    return reverse
for digits in range(100, 1000):
    for digit2 in range(100, 1000):
        num = digits * digit2
        if num == reverse_number(num):
            the_list.append(num)

print(max(the_list))
