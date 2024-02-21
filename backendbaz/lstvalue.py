# This function returns value of a list in a particular way
def list_value(arr):
    negatives = []
    for i in arr[1::2]:
        j =i * -1
        negatives.append(j)
        arr.remove(i)
    return print(sum(arr) + sum(negatives))
list_value([4, 5, 2, 1]) # 4-5+2-1 = 0