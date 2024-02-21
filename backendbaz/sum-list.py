# This function returns sum of all numbers given in a list.
def sum_list(arr):
    result_sum = 0
    for i in arr:
        if isinstance(i, list):
            result_sum += sum_list(i)
        else:
            result_sum += i
    return result_sum
print(sum_list([1, [2, [1]], 3])) # 1 + 2 + 1 + 3 = 7