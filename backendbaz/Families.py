def count_first_letter(my_dict):
    first_letters = []
    family_size = []
    for i in list(my_dict.keys()):
        first_letters.append(i[0])
    for i in list(my_dict.values()):
        family_size.append(len(i))
    result = dict()
    for i in range(len(first_letters)):
        if first_letters[i] in list(result.keys()):
            result[first_letters[i]] = result[first_letters[i]] + family_size[i]
        else:
            result[first_letters[i]] = family_size[i]
    return result


print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))

