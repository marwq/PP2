# Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print(f'Yesterday: {yesterday.strftime("%Y-%m-%d")}')
print(f'Today: {current_date.strftime("%Y-%m-%d")}')
print(f'Tomorrow: {tomorrow.strftime("%Y-%m-%d")}')