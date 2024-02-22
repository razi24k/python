# This code counts all unique letters of names
names_num = int(input("How many names you have?: "))
names_list = dict()
for i in range(1, names_num+1):
    names_list[input(f"Please provide name {i}: ").lower()] = 0

for i in names_list.keys():
    letter_counter = len(set(i))

    names_list[i] = letter_counter

print(names_list)
print(max(names_list.values()))

