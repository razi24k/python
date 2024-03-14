vowels = ["a", "e", "i", "o", "u"]


def remove_vowels(x):
    for i in x:
        if i.lower() in vowels:
            x = x.replace(i, "")
    return x


strings = ["hello", "world", "python"]
print(list(map(remove_vowels, strings)))