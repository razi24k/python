from datetime import datetime
datetime_str = input("Enter a datetime string (YYYY-MM-DD HH:MM:SS): ")
text = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
print(type(text))
