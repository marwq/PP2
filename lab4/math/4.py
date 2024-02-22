# Write a Python program to calculate the area of a parallelogram.

def area_of_parallelogram(b, h):
    return b * h

b = float(input('Length of base: '))
h = float(input('Height of parallelogram: '))
print(f'Expected Output: {area_of_parallelogram(b, h)}')