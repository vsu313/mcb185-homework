"""
Write a function that calculates Shannon entropy for nucleotide counts a, c, g, t.
Demonstrate it works using multiple calls.

"""

import math

def shannon_entropy(A, C, G, T):
	pa = (A / (A + C + G + T))
	pc = (C / (A + C + G + T))
	pg = (G / (A + C + G + T))
	pt = (T / (A + C + G + T))
	s = -((pa*math.log2(pa)) + (pc*math.log2(pc)) + (pg*math.log2(pg)) + (pt*math.log2(pt)))
	print(s)

shannon_entropy(3, 3, 3, 3)
shannon_entropy(43, 21, 21, 43)
shannon_entropy(40, 98, 98, 40)