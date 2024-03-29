number1, number2 = map(int, input("Enter number1 and number2 seperated by a space: ").split())

list1 = [i for i in range(number1, number2 + 1) if all([False if i % v == 0 else True for v in range(2, i)])]
print(list1)

