from datetime import datetime, timedelta

# Using current time
ini_time_for_now = datetime.now()

# printing initial_date
print('initial_date:', str(ini_time_for_now))

# for five seconds
future_date_after_five_seconds = ini_time_for_now + timedelta(seconds=5)

print('new_date    :', str(future_date_after_five_seconds))