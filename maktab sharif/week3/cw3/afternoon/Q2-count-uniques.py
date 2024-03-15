my_input = input("Enter your text: ").split(" ")
uniques = 0
for char in set(my_input):
    if my_input.count(char) == 1:
        uniques += 1
print(uniques)
