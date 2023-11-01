n = int(input("how many numbers do you have?:"))
numbers = []
for i in range(n):
    num = float(input("insert numbers:"))
    numbers.append(num)
print("max:", round(max(numbers), 3),"\nmin:", round(min(numbers), 3))
majmoo = 0
for i in numbers:
    majmoo += i
avg = majmoo/n
print("avg:", round(avg, 3))