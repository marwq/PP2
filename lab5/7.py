# Write a python program to convert snake case string to camel case string.

import re

def snake_to_camel(string: str):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), string)

print(snake_to_camel(input('Enter a snake case string: ')))