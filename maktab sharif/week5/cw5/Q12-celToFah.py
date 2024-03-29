tem_cel = [25, 30, 15, 10, 20]
print(f"original temperatures: {tem_cel}")
print(f"Converted temperatures: {list(map(lambda x: (x * (9 / 5)) + 32, tem_cel))}")
