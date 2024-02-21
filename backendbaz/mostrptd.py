# This function counts top 3 most repeated characters in a string. "difficulty: medium"
def sort_name(word):
    my_dic = dict()
    my_set = set()
    for i in word:
        my_set.add(i)
    for i in my_set:
        my_dic[i] = word.count(i)
    sorted_items = sorted(my_dic.items(), key=lambda item: (-item[1], item[0]))
    top_3 = sorted_items[:3]
    top3_list = []
    for key, value in top_3:
        top3_list.append([key, value])
    return top3_list
print(sort_name("aabbbcced")) # result: [['b',3],['a',2],['c',2]]
print(sort_name("qwertyuiopasdfghjklzxcvbnm")) # result: [['a',1],['b',1],['c',1]]