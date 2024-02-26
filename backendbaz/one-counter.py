def is_there_one(x):
    x = str(x)
    if x.count("1") >= 2:
        print(x)
for i in range(11, 912):
    is_there_one(i)