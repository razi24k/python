def find_most_frequent_words(string):
    raw_string = string.lower().replace(".", "").replace("\n", " ")
    words = raw_string.split(" ")
    frequency = 0
    result_words = set()
    for i in words:
        if words.count(i) > frequency:
            result_words.clear()
            frequency = words.count(i)
            result_words.add(i)
        elif words.count(i) == frequency:
            result_words.add(i)
    return result_words, frequency


my_input = """This is a sample paragraph. It contains several words. some of which are repeated.
This is a good exercise to find the most frequent words."""
result_words, result_frequency = find_most_frequent_words(my_input)

print("Most frequent word(s): ", result_words)
print("Frequency: ", result_frequency)
