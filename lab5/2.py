# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

def match_string(string: str):
    return re.search(r'^ab{2,3}$', string) is not None

print(match_string(input('Enter a string: ')))