# Write a Python program to convert degree to radian.

from math import pi

degree = float(input('Input degree:'))
radian = degree * (pi / 180)
print(f'Output radian: {radian}')