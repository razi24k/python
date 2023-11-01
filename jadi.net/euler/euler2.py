def sum_even_fibonacci(x=4000000):
    # Initialize variables for the first two Fibonacci numbers
    fib1, fib2 = 1, 2
    sum_count = 0
    while fib2 <= x:
        if fib2 % 2 == 0:
            sum_count += fib2
        fib1 , fib2 = fib2 , fib1 + fib2
    return sum_count
limit=4000000
resault=sum_even_fibonacci()
print(resault)