'''
Create a program that generates DNA sequences in FASTA format. 
There should be a variable that controls how many sequences (e.g. 3). 
Each sequence should have a unique identifier (e.g. seq-1) and the length of the sequence 
should have some random range (e.g 50-60). The output should resemble the example below.

'''

import random

i = 3	# number of sequences
n = 1	# identifier
for i in range(i):
	print(f'>seq-{n}')
	for i in range(random.randint(50, 60)):
		print(random.choice('ACGT'), end='')
	n += 1
	print()