def make_spoonerism(text):
    a, b = text.split(" ")
    x = a.replace(a[0], b[0])
    y = b.replace(b[0], a[0])
    return x + " " + y
print(make_spoonerism("Belly Jeans"))
print(make_spoonerism("Hello, world!"))
print(make_spoonerism("A B"))