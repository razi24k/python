Before_Dropping = {
    'Name': 'Pooja',
    'Age': 23,
    'Gender': '',
    'Mark': 488,
    'City': None
}

After_Dropping = dict(filter(lambda item: item[1], Before_Dropping.items()))
print(After_Dropping)