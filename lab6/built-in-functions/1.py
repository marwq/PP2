# Write a Python program with builtin function to multiply all the numbers in a list

from functools import reduce

def multiply_all(numbers: list):
    return reduce(lambda x, y: x * y, numbers)

print(multiply_all([1, 2, 3, 4, 5]))