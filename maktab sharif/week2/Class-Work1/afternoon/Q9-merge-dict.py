# Q9
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'b': 200, 'd': 400, 'a': 300}
#
# d3 = {}
# print(d1.keys())
# for i in d1.keys():
#     for j in d2.keys():
#         print(i, j)
#         if i == j:
#             temp = d1.get(i) + d2.get(j)
#             d3[i] = temp
#             # print(temp)
#         else:
#             if i not in d2.keys():
#                 d3[i] = d1.get(i)
#             elif j not in d1.keys():
#                 d3[j] = d2.get(j)
#
# print(d3)

def merge_dicts(dict1, dict2):

    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    return merged_dict


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'b': 200, 'd': 400, 'a': 300}