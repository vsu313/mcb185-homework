"""
Write a function that returns the Kyte-Doolittle hydrophobicity value for an amino acid letter. 
Demonstrate that the function works by calling it multiple times with different letters.

"""

def KD_value(x):
	if x == 'I': print(4.5)
	elif x == 'V': print(4.2)
	elif x == 'L': print(3.8)
	elif x == 'F': print(2.8)
	elif x == 'C': print(2.5)
	elif x == 'M': print(1.9)
	elif x == 'A': print(1.8)
	elif x == 'G': print(-0.4)
	elif x == 'T': print(-0.7)
	elif x == 'S': print(-0.8)
	elif x == 'W': print(-0.9)
	elif x == 'Y': print(-1.3)
	elif x == 'P': print(-1.6)
	elif x == 'H': print(-3.2)
	elif x == 'Q': print(-3.5)
	elif x == 'N': print(-3.5)
	elif x == 'E': print(-3.5)
	elif x == 'D': print(-3.5)
	elif x == 'K': print(-3.9)
	elif x == 'R': print(-4.5)
	else: print('That is not a valid amino acid letter')
	
KD_value('F')
KD_value('N')
KD_value('Z')