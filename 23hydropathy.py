"""
Write a function that returns the Kyte-Doolittle hydrophobicity value for an amino acid letter. 
Demonstrate that the function works by calling it multiple times with different letters.

"""

def KD_value(x):
	if x == 'I': return 4.5
	elif x == 'V': return 4.2
	elif x == 'L': return 3.8
	elif x == 'F': return 2.8
	elif x == 'C': return 2.5
	elif x == 'M': return 1.9
	elif x == 'A': return 1.8
	elif x == 'G': return -0.4
	elif x == 'T': return -0.7
	elif x == 'S': return -0.8
	elif x == 'W': return -0.9
	elif x == 'Y': return -1.3
	elif x == 'P': return -1.6
	elif x == 'H': return -3.2
	elif x == 'Q': return -3.5
	elif x == 'N': return -3.5
	elif x == 'E': return -3.5
	elif x == 'D': return -3.5
	elif x == 'K': return -3.9
	elif x == 'R': return -4.5
	else: return 'That is not a valid amino acid letter'
	
print(KD_value('F'))
print(KD_value('N'))
print(KD_value('Z'))