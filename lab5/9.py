# Write a Python program to insert spaces between words starting with capital letters.

import re

def insert_spaces(string: str):
    return re.sub(r'([A-Z][A-Za-z]+)', r' \1', string)

print(insert_spaces(input('Enter a string: ')))