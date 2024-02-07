'''
Create a function that solves "n choose k": n! / k!(n - k)! and demonstrate that it works 
by calling it multiple times with several values of n and k. 
It's more fun to reuse your factorial function than math.factorial().

'''

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def nchoosek(n, k):
	res = factorial(n) / (factorial(k) * factorial(n - k))
	return res

print(nchoosek(4, 3))
print(nchoosek(7, 2))
print(nchoosek(81, 78))