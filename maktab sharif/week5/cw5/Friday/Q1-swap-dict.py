dict1 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}
dict_swap = {value: key for key, value in dict1.items()}
print(dict_swap)
