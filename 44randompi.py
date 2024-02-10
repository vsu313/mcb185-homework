'''
Write a program that estimates pi using Monte Carlo methods as was described above. 
Generate random values for x and y from 0 to 1. Calculate the distance to the origin. 
If the distance is less than 1, the point is inside the circle. 
The ratio of points that fall inside compared to the total is pi/4. 
Output each iteration and watch as the ratio gets closer to pi. 
Use an endless while loop in your program and stop it with ^C.

'''

import math
import random

inner = 0
total = 0
while True:
	x = random.random()
	y = random.random()
	h = math.sqrt((x ** 2) + (y ** 2))
	if h < 1:
		inner += 1
	total += 1
	print(4 * (inner / total))