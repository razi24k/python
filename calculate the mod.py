def mode(the_list):
    my_list = []
    max_count = 1
    i = 0
    while i < len(the_list):
        count = 1
        while i + 1 < len(the_list) and the_list[i] == the_list[i + 1]:
            count += 1
            i += 1
        if count > max_count:
            my_list = [the_list[i]]
            max_count = count
        elif count == max_count and count > 1:
            my_list.append(the_list[i])
        i += 1
    return my_list
print(mode([4, 5, 6, 6, 6, 7, 7, 9, 10]))