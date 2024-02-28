def is_heteromecic(num):
    if num == int(num ** 0.5) * (int(num ** 0.5) + 1):
        return True
    else:
        return False
print(is_heteromecic(72))
print(is_heteromecic(64))
print(is_heteromecic(30))