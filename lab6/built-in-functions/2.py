# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

def count_upper_lower(string: str):
    return (
        len(list(filter(str.isupper, string))), 
        len(list(filter(str.islower, string)))
    )

upper, lower = count_upper_lower(input('Enter a string: '))
print(f'Upper case: {upper}\nLower case: {lower}')