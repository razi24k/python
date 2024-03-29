def cube(num):
    return num * num * num


def by_three(num):
    if num % 3 == 0:
        cube(num)
    else:
        return False
