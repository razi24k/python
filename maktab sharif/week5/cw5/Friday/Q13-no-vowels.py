string = "Hello, how are you?"
my_list = [letter for letter in string if letter not in {'a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E'} and letter.isalpha()]
print(f"Number of Vowels: {my_list}")