# Write a Python program to split a string at uppercase letters.

import re

def split_string(string: str):
    return re.split(r'(?=[A-Z])', string)
    # return re.split(r'[A-Z]', string)

print(*(split_string(input('Enter a string: ')) or ['Not found']), sep='\n')