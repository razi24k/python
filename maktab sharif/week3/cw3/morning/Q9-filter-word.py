def filter_long_words(strings, n):
    new_list = list()
    if len(strings) <= n:
        new_list.append(strings)
    if new_list:
        return new_list


n = int(input("n: "))
words = ["Hellooooo", "World", "Python"]
res = map(lambda x: filter_long_words(x, n), words)
print(list(res))