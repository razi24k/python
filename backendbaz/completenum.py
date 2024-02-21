# this function returns YES if provided number is complete else returns NO
def complete_number(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if num == sum(divisors):
        return "YES"
    else:
        return "NO"