# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

def match_string(string: str):
    return re.findall(r'[A-Z][a-z]+', string)
    
print(*(match_string(input('Enter a string: ')) or ['Not found']), sep='\n')