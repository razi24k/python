x = int(input("Enter a number: "))
bottom_line = x*2 * "."
for i in range(x):
    if i == 0:
        print("." * (x-1) + "D" + "." * (x-1))
    elif i < x-1:
        print("." * ((2 * (x-i) - 2) // 2) + "D" + "." * (2 * i - 1) + "D" + "." * ((2 * (x-i) - 2) // 2))
    elif i == x-1:
        new_bottom_line = ""
        for j in range(len(bottom_line)):
            if j % 2 == 0:
                new_bottom_line += "D"
            else:
                new_bottom_line += "."
        print(new_bottom_line)