def count_first_letter(text1, text2, text3):
    result_dict = dict()
    names1 = [name for names in text1.values() for name in names]
    names2 = [name for names in text2.values() for name in names]
    names3 = [name for names in text3.values() for name in names]

    first_letter_text1 = list(text1.keys())[0][0]
    first_letter_text2 = list(text2.keys())[0][0]
    first_letter_text3 = list(text3.keys())[0][0]

    if first_letter_text1 == first_letter_text2 and first_letter_text1 != first_letter_text3:
        result_dict[first_letter_text1] = len(names1) + len(names2)
        result_dict[first_letter_text3] = len(names3)
    elif first_letter_text1 == first_letter_text3 and first_letter_text1 != first_letter_text2:
        result_dict[first_letter_text1] = len(names1) + len(names3)
        result_dict[first_letter_text2] = len(names2)
    elif first_letter_text2 == first_letter_text3 and first_letter_text2 != first_letter_text1:
        result_dict[first_letter_text1] = len(names1)
        result_dict[first_letter_text2] = len(names2) + len(names3)
    elif first_letter_text1 == first_letter_text2 and first_letter_text1 == first_letter_text3:
        result_dict[first_letter_text1] = len(names1) + len(names2) + len(names3)
    else:
        result_dict[first_letter_text1] = len(names1)
        result_dict[first_letter_text2] = len(names2)
        result_dict[first_letter_text3] = len(names3)
    print(result_dict)

count_first_letter({"Stark": ["Ned", "Robb", "Sansa"]}, {"Snow" : ["Jon"]}, {"Lannister": ["Jaime", "Cersei", "Tywin"]})
count_first_letter({"Stark": ["Ned", "Robb", "Sansa"]}, {"Snow" : ["Jon"]}, {"Sannister": ["Jaime", "Cersei", "Tywin"]})
count_first_letter({"Stark": ["Ned", "Robb", "Sansa"]}, {"Lannister": ["Jaime", "Cersei", "Tywin"]},{"Tion":["joun","sara"]})