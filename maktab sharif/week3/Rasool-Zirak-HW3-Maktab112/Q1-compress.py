def compressor(x):
    x_unique = list(set(x))
    result = "".join(x_unique)
    for i in x_unique:
        if x.count(i) != 1:
            result += str(x.count(i))
    if "".join(sorted(result)) == x:
        return "".join(sorted(result))
    else:
        compressed_result = "".join(sorted(result))
        return compressor(compressed_result)


print(compressor("442254545"))


