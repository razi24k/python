empty_dict = {}


def add(key=input("Please enter the key. "), value=input("Please enter the value. ")):
    if key in empty_dict.keys():
        print("You can't add the same key")
    else:
        empty_dict.update({key: value})


def remove(key=input("Please enter the key. "), value=input("Please enter the value. ")):
    if key in empty_dict:

        if empty_dict[key] == value:
            empty_dict.pop(key)
        else:
            print("Wrong value!")

    else:
        print("wrong key!")


try:
    flag = True
    while flag:
        user_input = input("Please enter the operation you want. (1 for add, 2 for remove, 3 for display, 4 for exit): ")
        if user_input == '1':
            while len(empty_dict) < 5:
                add()
        elif user_input == '2':
            remove()
        elif user_input == "3":
            print(empty_dict)
        elif user_input == "4":
            flag = False
        else:
            raise TypeError
except TypeError:
    print("wrong input!. Just enter 1 or 2...")
