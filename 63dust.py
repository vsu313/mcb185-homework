'''
Input: multi-FASTA file of DNA
Output: multi-FASTA file of DNA with low complexity regions masked
Change all low-complexity regions to 'N' in the output
Provide parameters for fasta file, window size, and entropy
'''

import sys
import mcb185
import math

def shannon_entropy(A, C, G, T):
	tot = A + C + G + T
	pa = (A / tot)
	pc = (C / tot)
	pg = (G / tot)
	pt = (T / tot)
	if A == 0:	sa = 0
	else:		sa = pa*math.log2(pa)
	if C == 0:	sc = 0
	else:		sc = pc*math.log2(pc)
	if G == 0:	sg = 0
	else:		sg = pa*math.log2(pg)
	if T == 0:	st = 0
	else:		st = pa*math.log2(pt)
	s = -(sa + sc + sg + st)
	return s


seq = sys.argv[1]
w =	int(sys.argv[2])

genome = []
mygenome = []


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for nt in seq:
		genome.append(nt)
for i in range(len(genome) - w):
	s = genome[i:i + w]
	new = genome[i + w]
	dump = genome[i]
	a = s[0:w].count('A')
	c =	s[0:w].count('C')
	g =	s[0:w].count('G')
	t = s[0:w].count('T')
	entropy = shannon_entropy(a, c, g, t)
	if entropy < 1.4:	print('N')
	else:				print(s)