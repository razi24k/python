def middle_element(arr):
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return (arr[(len(arr)-1) // 2] + arr[(len(arr)+1) // 2]) / 2


print(middle_element([1, 7, 8, 3, 6, -10, -7])) # 3
print(middle_element([4, 8, 9, 2, -11, -7, 4, 6, 9, 10])) # -11 + -7 = -9
print(middle_element([4, 8, 9, 2, -10, 7, 4, 6, 9, 10, 7])) # 7