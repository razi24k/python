def values_that_are_keys(word1):
    result_list = []
    keys = list(word1.keys())
    values = list(word1.values())
    for i in keys:
        if i in values:
            result_list.append(i)
    return list(set(result_list))

print(values_that_are_keys({1 : 100, 2 : 1, 3 : 4, 4 : 10}))
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
print(values_that_are_keys({1: 2, 100: 2, 2: "v", "s": 50, "v": "s"}))
