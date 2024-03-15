user_input = input("Enter the sequence separated by a comma: ").split(",")
my_dict = {
    "Number of integers": len(list(filter(lambda x: x.isnumeric(), user_input))),
    "Number of strings": len(list(filter(lambda x: not x.replace(".", "").isnumeric(), user_input))),
    "Number of floats": len(list(filter(lambda x: "." in x and x.replace(".", "").isnumeric(), user_input)))

}
print(my_dict)

