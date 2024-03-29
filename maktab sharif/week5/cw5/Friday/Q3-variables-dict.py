A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Z = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
dict_1 = {}


assigned_variables = {name: value for name, value in locals().items()
                      if isinstance(value, list)}

print(assigned_variables)