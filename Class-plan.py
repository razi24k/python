the_week ={
    "saturday" : {},
    "sunday" : {},
    "monday" : {},
    "tuseday" : {},
    "wednesday" : {}
    }

for day in the_week:
    for x in range(5):
        the_week[day]["class:", x + 1] = input(f"{day} class{x + 1}: ")
the_day = input("What day do you want to show?: ")
the_class = input("and what class?: ")
while True:
    try:
        the_week[the_day][the_class]
        the_day = input("What day do you want to show?: ")
        the_class = input("and what class?: ")
    except:
        print("please insert day and class in correct spelling")
        the_day = input("What day do you want to show?: ")
        the_class = input("and what class?: ")
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Day", "Class 1", "Class 2", "Class 3", "Class 4", "Class 5"]

for day, classes in the_week.items():
    row = [day]
    for class_name, class_value in classes.items():
        row.append(class_value)
    table.add_row(row)

print(table)