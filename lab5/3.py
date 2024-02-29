# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

def match_string(string: str):
    result = re.findall(r'([a-z]+(_[a-z]+)+)', string)
    if result is not None:
        return [i[0] for i in result]

print(*(match_string(input('Enter a string: ')) or ['Not found']), sep='\n')