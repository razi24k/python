Dict = {'M1': [67, 79, 90, 73, 36], 'M2': [89, 67, 84], 'M3': [82, 57]}

summ = 0
items = [len(i) for i in Dict.values()]
print(sum(items))
