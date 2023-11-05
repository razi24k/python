def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
sums = 0
for i in range(2_000_001):
    if is_prime(i):
        sums += i
print(sums)