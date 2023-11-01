def is_isogram(string):
    string=string.lower()
    char=list()

    for i in string:
        if i in char:
            return print("false")
        else:
            char.append(i)
    return print("true")

user_input=input("please enter your string: ")
is_isogram(user_input)