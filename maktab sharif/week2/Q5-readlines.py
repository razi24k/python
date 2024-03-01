file = open("note.txt", "r")
line_counter = 0
for line in file.readlines():
    line_counter += 1
file.close()
print(line_counter)