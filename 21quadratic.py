"""
Write a function that solves the quadratic formula (ax^2 + bx + c). 
Demonstrate that it works by using the formula multiple times within the program.

"""

import math

def quadratic(a, b, c):
	x = ((-b + math.sqrt(b**2 - 4*a*c)) / 2*a)
	y = ((-b - math.sqrt(b**2 - 4*a*c)) / 2*a)
	return x, y

print(quadratic(1, 3, 1))
print(quadratic(2, -4, 1))
print(quadratic(5, -8, -2))