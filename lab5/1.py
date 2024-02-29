# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

def match_string(string: str):
    return re.search(r'^ab*$', string) is not None

print(match_string(input('Enter a string: ')))