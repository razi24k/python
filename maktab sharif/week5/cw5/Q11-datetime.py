import datetime
# text = datetime.datetime.now()
text = input("Enter a date with this format: YYYY-MM-DD hh:mm:ss: ")

list1 = {
    'year': (lambda item: item.year)(text),
    'month': (lambda item: item.month)(text),
    'day': (lambda item: item.day)(text),
    'time': (lambda item: f"{item.hour}:{item.minute}:{item.second}")(text)
}
print(list1)

