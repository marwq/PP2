# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

def replace_string(string: str):
    return re.sub(r'[ ,.]', ':', string)

print(replace_string(input('Enter a string: ')))