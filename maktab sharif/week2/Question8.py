in_text = input("Enter a string: ")
file = open("text.txt", "a")
file.write(in_text)

file.close()
