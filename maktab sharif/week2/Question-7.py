# Q7
file = open("test.txt", "r")
text = file.read()

new_text = text.title()
file.close()

file = open("test.txt", "w")
file.write(new_text)
file.close()