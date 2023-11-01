word = input("insert word:")
modes = 0
for i in word:
    if i == "N" or i == "T" or i == "X" or i == "L":
        modes += 1
print(2**modes)