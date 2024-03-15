print("Enter a string: ")
raw_input = input()
raw_input += " " + input()
raw_input += " " + input()
words = raw_input.split(" ")
unique_words = set(words)
result_dict = {}
for i in unique_words:
    result_dict[i] = words.count(i)

print(result_dict)