# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def is_palindrome(string: str):
    return string == string[::-1]

print(is_palindrome(input('Enter a string: ')))