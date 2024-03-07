my_list = list()
try:
    user_decision = input("Press 1 to add numbers and 2 to exit ")
    while user_decision == "1":
        tuples_number = int(input("How many series do you want to add? "))
        for i in range(tuples_number):
            user_tuple = tuple(map(int, input("Enter your numbers seperated by spaces: ").split(" ")))
            my_list.append(user_tuple)
            if len(user_tuple) > 3:
                raise AssertionError("Series has to be a list of three members! ")
        user_decision = input("Press 1 to add numbers and 2 to exit")
    else:
        if user_decision == "2":
            print("your list is: ", my_list)
        else:
            raise AssertionError("Invalid input, Please insert 1 or 2")
except AssertionError as e:
    print("An error occurred: ", e)

my_tuple = tuple(my_list)


# my_tuple1 = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# my_tuple2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

num_list0 = list()
num_list1 = list()
num_list2 = list()
for i in range(len(my_tuple)):
    for j in range(len(my_tuple[i])):
        if j == 0:
            num_list0.append(my_tuple[i][j])
        elif j == 1:
            num_list1.append(my_tuple[i][j])
        else:
            num_list2.append(my_tuple[i][j])
avg = lambda item: sum(item) / len(item)
avg_list = list()
all_nums = [num_list0, num_list1, num_list2]
for i in range(len(all_nums)):
    avg_list.append(avg(all_nums[i]))
print(tuple(avg_list))


