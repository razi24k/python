#تست ایسوگرام
def is_isogram(string):
    string=string.lower()
    seen_letters=set()
    for letter in string:
        if letter in seen_letters:
            return False
        else:
            seen_letters.add(letter)
    return True

user_input=input("please insert a string:")
resault=is_isogram(string=user_input)
print(resault)
