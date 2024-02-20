'''
Write a program that provides the closest official color name given 
some red, green, and blue values. Each value must be in the range of 0-255.

'''

# co-author by conner suen and vanessa su

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

given = [R, G, B]

com = 1000000
vals = []
colors = []

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return int(d)

with open(colorfile, 'rt') as fp:
	for line in fp:
		row = line.split()
		vals.append(row[2])
		colors.append(row[0])
		track = 0
		for val in vals:
			stan = val.split(',')
			stan = [int(stan[0]), int(stan[1]), int(stan[2])]
			dis = dtc(given, stan)
			if dis < com: 
				finalcol = colors[track]
				com = dis
			track += 1

print(finalcol)