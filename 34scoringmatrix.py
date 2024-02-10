'''
Write a program the displays a +1/-1 scoring matrix as shown below. 
The program must have a single variable for the alphabet (don't hard code it multiple times). 
Hint: use print(end=' ') to terminate print() statements with a space instead of the default newline.

'''

nts = 'ACGT'

for nt in nts:
	if nt == 'A':	print('  ', nt, end='  ')
	elif nt == 'T':	print(nt)
	else:			print(nt, end='  ')

for nt1 in nts:
	print(nt1, end=' ')
	for nt2 in nts:
		if nt1 == nt2:	print('+1', end=' ')
		else:			print('-1', end=' ')
	print()