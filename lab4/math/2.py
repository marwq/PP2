# Write a Python program to calculate the area of a trapezoid.

def area_of_trapezoid(a, b, h):
    return (a + b) * h / 2

h = float(input('Height: '))
a = float(input('Base, first value: '))
b = float(input('Base, second value: '))

print(f'Expected Output: {area_of_trapezoid(a, b, h)}')