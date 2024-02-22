# Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print(f'Current date: {current_date.strftime("%Y-%m-%d")}')
print(f'Five days ago: {five_days_ago.strftime("%Y-%m-%d")}')