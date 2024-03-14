my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_odd = list(map(lambda x: "even" if x % 2 == 0 else "odd", my_list))
print(even_odd)