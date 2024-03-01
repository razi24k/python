# f = open("note.txt", "r")
# x = input("Enter a string: ")
# text = f.read()
# counter = text.count(x)
# # print(text)
# print(counter)

my_input = list(str(input("Enter Your Text: ")))

file = open("note.txt", "r")
text = file.read()
my_list = list(text)
print(my_list)

counter = 0

for i in range(len(text)):
    if my_list[i:len(my_input)+i] == my_input:
        counter += 1

print(counter)
