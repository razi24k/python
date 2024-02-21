# this function returns all numbers including int and floats from multi dimension arrays.
def listless_list(arr):
    numbers = []
    for item in arr:
        if isinstance(item, list):
            numbers.extend(listless_list(item))
        else:
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                numbers.append(item)
    return numbers

