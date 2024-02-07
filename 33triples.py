'''
Write a program that finds all Pythagorean triples for triangles with sides a and b 
less than 100. For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2. 
Hint: all sides, including the hypotenuse, must be an integer. 
There are 62 unique triples (half-matrix minus the major diagonal).

'''

import math

def pythagorean(a, b):
	c_squared = a**2 + b**2
	c = math.sqrt(c_squared)
	return c

for a in range(1, 100):
	for b in range(1, 100):
		res = pythagorean(a, b)
		if b > a:
			if res % 1 == 0:
				print(a, b, res)
				count = count + 1