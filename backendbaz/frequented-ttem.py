def more_frequent_item(arr, num1, num2):
    if arr.count(num1) == arr.count(num2) or arr.count(num1) > arr.count(num2):
        return num1
    else:
        return num2


print(more_frequent_item([2, 3, 2, 3, 2, 2, 2, 2, 3, 3, 3, 3, 2, 3], 2, 3))
print(more_frequent_item([2, 3, 2, 3, 2, 2, 2, 2, 3, 3, 3, 3, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2], 2, 3))
print(more_frequent_item([1, 2, 9, 9, 3, 2, 1, 9, 1, 1], 2, 9))
