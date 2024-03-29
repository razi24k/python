String = "Tutor Joes"
my_list = [letter for letter in String if letter in {'a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E'}]
print(f"Number of Vowels: {len(my_list)}")