Dictionary = {"m1": 78, "m2": 89, "m3": 64, "m4": 35, "m5": 71}
list_1 = list(Dictionary.items())


def sorter(list_one):
    new_list = sorted(list_one, key=lambda x: x[1])
    print(f"Ascending Order: {new_list}")
    new_list = sorted(list_one, key=lambda x: x[1], reverse=True)
    print(f"Descending Order: {new_list}")


sorter(list_one=list_1)
