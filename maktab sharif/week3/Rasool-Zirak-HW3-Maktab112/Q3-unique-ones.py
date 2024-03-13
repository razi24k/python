from functools import reduce


def uniques(sentence):
    string_s = str(sentence).lower()
    words = string_s.split()
    unique_words = set(words)
    return unique_words


def union(*args):
    result = set()
    result = result.union(*args)
    return result


my_sentences = [
    "Hello World",
    "Python is awesome",
    "Hello Python"
]
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 2, 3, 3]

unique_words = list(map(uniques, my_sentences))
unique_numbers = list(map(uniques, my_numbers))

union_result = reduce(union, unique_words)
union_nums = reduce(union, unique_numbers)

print(union_result)
print(union_nums)
