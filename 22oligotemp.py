"""
Write a program that computes oligo melting temperature given the number of As, Cs, Gs, and Ts in the oligo.
Use these two methods:
1. For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
2. For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)
Demonstrate that your program works by computing the Tm of several oligos of different sizes.

"""

def oligo_temp(A, C, G, T):
	if (A + C + G + T) <= 13:
		return 2*(A + T) + 4*(G + C)
	else:
		return 64.9 + (41*(G + C - 16.4) / (A + C + G +T ))
		
print(oligo_temp(3, 4, 4, 3))
print(oligo_temp(9, 5, 5, 9))
print(oligo_temp(41, 26, 26, 41))