"""
Write a program that computes oligo melting temperature given the number of As, Cs, Gs, and Ts in the oligo.
Use these two methods:
1. For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
2. For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)
Demonstrate that your program works by computing the Tm of several oligos of different sizes.

"""


