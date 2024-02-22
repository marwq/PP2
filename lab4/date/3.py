# Write a Python program to drop microseconds from datetime.

from datetime import datetime

current_date = datetime.now()
current_date = current_date.replace(microsecond=0)

print(f'Current date: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')