string = (input("Please enter a text. "))
letter = str(input("Enter the letter you want to look for. "))

# for index in string:
#     count = string.count(index)
#     if count > 1:
#         print(f"The character '{index}' is present in the string {count} time/times.")


count = string.count(letter)
print(count)
