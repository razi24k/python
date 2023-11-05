def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

counter = 1
x = 3
while counter <= 10001:
    if is_prime(x):
        counter += 1 
    x += 2
print(x)