# This code is a train for logical comparisation
row1 = input("please provide row 1: ").split(" ")
row2 = input("please provide row 2: ").split(" ")
logic1 = [bool(int(item)) for item in row1]
logic2 = [bool(int(item)) for item in row2]
eye_to_eyes = 0
for i in range(len(logic1)):
    if logic1[i] and logic2[i]:
        eye_to_eyes += 1

print(eye_to_eyes)