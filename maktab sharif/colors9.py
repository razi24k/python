n = int(input())
colors = []
for i in range(n):
    colors.append(int(input()))

min_color = min(colors)

for color in colors:
    if colors.count(color) < colors.count(min_color):
            min_color = color
print(min_color)
    