'''
Write a program that reads a GFF file and reports the following information about 
the length of GFF features.

count
min
max
mean
standard deviation
median

'''

import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]

genelengths = []
exonlengths = []
cdslengths = []

with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] == '#':	continue
		words = line.split()
		if words[2] == 'gene':
			beg = int(words[3])
			end = int(words[4])
			genelengths.append(end - beg + 1)
			genelengths.sort()
		if words[2] == 'exon':
			beg = int(words[3])
			end = int(words[4])
			exonlengths.append(end - beg + 1)
			exonlengths.sort()
		if words[2] == 'CDS':
			beg = int(words[3])
			end = int(words[4])
			cdslengths.append(end - beg + 1)
			cdslengths.sort()

def minimum(vals):
	mini = vals[0]
	return mini
	
def maximum(vals):
	maxi = vals[len(vals) - 1]
	return maxi
	
def mean(vals):
	total = 0
	for val in vals:	total += val
	return round(total / len(vals))
	
def standev(vals):
	total = 0
	for val in vals:	total += (val - mean(vals)) ** 2
	return round(math.sqrt(total / (len(vals))))
	
def median(vals):
	if len(vals) % 2 != 0:
		med = vals[len(vals) // 2]
	else:
		top = len(vals) // 2
		bottom = top - 1
		med = (vals[bottom] + vals[top]) / 2
	return round(med)

if feature == 'gene':	listy = genelengths
elif feature == 'exon':	listy = exonlengths
else:					listy = cdslengths


print(f'{feature} count is {len(listy)}')
print(f'min of {feature} is {minimum(listy)}')
print(f'max of {feature} is {maximum(listy)}')
print(f'mean of {feature} is {mean(listy)}')
print(f'standard deviation of {feature} is {standev(listy)}')
print(f'median of {feature} is {median(listy)}')
