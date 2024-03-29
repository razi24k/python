words = ['apple', 'banana', 'cherry', "Apple"]
dict_a = {word: sum(list(map(lambda x: word.count(x), ['a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E']))) for word in
          words}
print(dict_a)