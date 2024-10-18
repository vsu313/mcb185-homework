# co-author by conner suen and vanessa su

import sys
import dogma

'''
seq = sys.argv[1]
w =	int(sys.argv[2])
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')
'''

seq = sys.argv[1]
w =	int(sys.argv[2])
g =	seq[0:w].count('G')
c =	seq[0:w].count('C')

for i in range(len(seq) - w):
	s = seq[i:i + w]
	new = seq[i + w]
	dump = seq[i]
	if i == 0:
		if g + c != 0:
			print(i, dogma.gc_comp(s), dogma.gc_skew(s))
		else:
			print(i, dogma.gc_comp(s), 0)
	
	if dump == 'C':		c -= 1
	elif dump == 'G':	g -= 1
	
	if new == 'C':		c += 1
	elif new == 'G':	g += 1
	
	if g + c != 0:
		print(i + 1, dogma.gc_comp(s), dogma.gc_skew(s))
	else:
		print(i + 1, dogma.gc_comp(s), 0)