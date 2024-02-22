# Write a Python program to calculate the area of regular polygon.

from math import tan, pi

def area_of_regular_polygon(n: int, s: float) -> float:
    return (n * s ** 2) / (4 * tan(pi / n))

n = int(input('Input number of sides: '))
s = float(input('Input the length of a side: '))
print(f'The area of the polygon is: {area_of_regular_polygon(n, s)}')
