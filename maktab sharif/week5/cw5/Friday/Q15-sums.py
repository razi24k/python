list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = tuple((i, j, i+j) for i in list1 for j in list2)
print(list3)
