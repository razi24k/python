scalar = []
for i in range(7):
    new = list(map(int, input(f"Enter the {i+1}th: ").split(" ")))
    scalar.extend(new)
first_dots = []
second_dots = []
third_dots = []
for i in range(0, len(scalar), 3):
    first_dots.append(scalar[i])
for i in range(1, len(scalar), 3):
    second_dots.append(scalar[i])
for i in range(2, len(scalar), 3):
    third_dots.append(scalar[i])
result = ""
for i in first_dots:
    if first_dots.count(i) == 3:
        result += str(i) + " "
        break
for i in second_dots:
    if second_dots.count(i) == 3:
        result += str(i) + " "
        break
for i in third_dots:
    if third_dots.count(i) == 3:
        result += str(i)
        break
print(result.strip())
