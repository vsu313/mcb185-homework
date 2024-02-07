'''
Create a function that computes the Poisson probability of k events occuring with 
an expectation of n: n^k e^-n / k! and demonstrate it works by calling it with several 
values of n and k. Use math.e.

'''

import math

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def poisson(n, k):
	res = ((n ** k) * (math.e ** (-n))) / factorial(k)
	return res
	
print(poisson(2, 1))
print(poisson(4, 7))
print(poisson(6, 2))
