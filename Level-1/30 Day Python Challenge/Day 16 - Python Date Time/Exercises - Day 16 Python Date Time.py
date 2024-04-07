# Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp

print(day, month, year, hour, minute)
print("timestamp", timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}")

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

from datetime import datetime

current_date = datetime.now()
formatted_current_date = current_date.strftime("%m/%d/%Y, %H:%M:%S")

print("Formatted date:", formatted_current_date)

# Today is 5 December, 2019. Change this time string to time.

from datetime import datetime

time_string = "5 December, 2019"
time_object = datetime.strptime(time_string, "%d %B, %Y")

print("Time object:", time_object)

# Calculate the time difference between now and new year.

from datetime import datetime

current_time = datetime.now()
new_year = datetime(current_time.year + 1, 1, 1)
time_difference = new_year - current_time

print("Time difference until New Year's Day:", time_difference)

# Calculate the time difference between 1 January 1970 and now.

from datetime import datetime

start_date = datetime(1970, 1, 1)
current_date = datetime.now()
time_difference = current_date - start_date

print("Time difference between January 1, 1970, and now:", time_difference)

