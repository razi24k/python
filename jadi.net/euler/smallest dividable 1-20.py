def calculate_lcm(a, b):
    # Calculate the LCM of two numbers using the formula LCM(a, b) = (a * b) / GCD(a, b)
    num1, num2 = a, b
    while num2:
        num1, num2 = num2, num1 % num2
    return (a * b) // num1

num_list = [i for i in range(1,21)]

# Calculate the LCM of all even numbers in the list
lcm = num_list[0]
for i in num_list[1:]:
    lcm = calculate_lcm(lcm, i)

print(lcm)