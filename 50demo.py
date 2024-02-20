# indexes

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for i in range(len(seq)):
	print(i, seq[i])
	
	
# slices

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])
print(s, s[::], s[::1], s[::-1])


# tuples
tax = ('Homo', 'sapiens', 9606)
print(tax)

print(tax[0])
print(tax[::-1])

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2
	
x1, x2 = quadratic(5, 6, 1)
print(x1, x2)
intercepts = quadratic(5, 6, 1)
print(intercepts[0], intercepts[1])


# enumerate() and zip()

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
for i, nt in enumerate(nts):
	print(i, nt)
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
for nt, name in zip(nts, names):
	print(nt, name)
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	

# lists

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last, nts)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)


# split() and join()

text = 'good day	to you'
words = text.split()
print(words)

line = '1.41, 2.72, 3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)


# searching

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))


# files

import gzip
with gzip.open(path, 'rt') as fp:
	for line in fp:
		print(line, end='')
		
i = int('42')
x = float('0.61803')