my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

bin_list = list(map(lambda x: bin(x).replace('0b', ''), my_list))
print(bin_list)