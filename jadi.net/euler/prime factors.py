def isprime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True
num = 600851475143
divisor = 2
factors = []

while num > 1:
    if num % divisor == 0:
        factors.append(divisor)
        num //= divisor
    else:
        divisor += 1

prime_factors = [factor for factor in factors if isprime(factor)]

print(max(prime_factors))


        