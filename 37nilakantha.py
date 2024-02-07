'''
Estimate pi using the Nilakantha series. Hint: you must figure out how to get the +/- to 
flip-flop with each iteration.

Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...

'''

def pi():
	num = 2
	total = 3
	for i in range(100):
		add = 4 / ((num) * (num + 1) * (num + 2))
		if num % 4 == 0:	total = total - add
		else:				total = total + add
		num = num + 2
	return total
	
print(pi())