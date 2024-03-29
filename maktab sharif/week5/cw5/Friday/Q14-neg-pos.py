from secretstorage import item

list_1 = [10, -5, 20, -15, 30]
positive = []
negative = []
[positive.append(item) if item >= 0 else negative.append(item) for item in list_1]
print(f"positive : {tuple(positive)}\nnegative : {tuple(negative)}")
