# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

def match_string(string: str):
    return re.search(r'^a.*b$', string) is not None

print(match_string(input('Enter a string: ')))