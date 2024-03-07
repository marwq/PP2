# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f'{letter}.txt', encoding='utf8', mode='w') as f:
            pass
        
generate_files()