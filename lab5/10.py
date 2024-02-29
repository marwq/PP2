# Write a Python program to convert a given camel case string to snake case.

import re

def camel_to_snake(string: str):
    return re.sub(r'([A-Z])', lambda x: f'_{x.group(1).lower()}', string)

print(camel_to_snake(input('Enter a camel case string: ')))