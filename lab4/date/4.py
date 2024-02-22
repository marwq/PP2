# Write a Python program to calculate two date difference in seconds.

from datetime import datetime, timedelta

def date_difference_in_seconds(date1: datetime, date2: datetime):
    difference: timedelta = date2 - date1
    return abs(difference.total_seconds())

date1 = datetime(2020, 1, 1, 0, 0, 0)
date2 = datetime(2020, 1, 1, 0, 0, 10)

print(f'Difference in seconds: {date_difference_in_seconds(date1, date2)}')