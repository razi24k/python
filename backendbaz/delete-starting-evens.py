def delete_starting_evens(arr):
    new_arr = []
    found_odd = False
    for i in arr:
        if not found_odd and i % 2 == 0:
            continue
        else:
            found_odd = True
            new_arr.append(i)
    return new_arr
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
print(delete_starting_evens([4, 8, 10, 12, 18, 14, 16, 15, 12, 14, 16, 17]))