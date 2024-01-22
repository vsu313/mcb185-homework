# 20demo.py by Vanessa Su

import math

# greeting
print('hello, again')


# math
print(1.5e-2)
print(1 + 3)
print(1 - 3)
print(1 * 3)
print(1 / 3)
print(1 ** 3)
print(4 // 3)
print(4 % 3)
print((4 * 3) + 1)

print(abs(-34)) 
print(pow(2, 3))
print(round(3.4568, ndigits = 3))

print(math.ceil(3.2))
print(math.floor(3.8))
print(math.log(2))
print(math.log2(2))
print(math.log10(2))
print(math.sqrt(9))
print(math.pow(3, 2))
print(math.factorial(3))

print(0.1 * 1)
print(0.1 * 3)


# assignment
a = 3						# side of triangle
b = 4						# side of triangle
c = math.sqrt(a**2 + b**2)	# hypotenuse
print(c)

print(type(a), type(b), type(c), sep=', ')


# functions
def greeting():
	print('hello yourself')
	
greeting()
	
def pythagoras(a, b):
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)
	
print(pythagoras(3, 4))
print(pythagoras(1, 1))


# practice
def sign_switch(a):
	if a < 0:
		return abs(a)
	if a > 0:
		return -a
print(sign_switch(3))


# strings 
s = 'hello world'
print(s, type(s))

# conditionals
a = 2
b = 3
if a == b:
	print('a equals b')
if a != b:
	print('a does not equal b')
print(a, b)

c = a == b
print(c, type(c))

if a < b: 	print('a < b')
elif a > b:	print('a > b')
else:		print('a == b')

if a < b or a > b:	print('all things being equal, a and b are not')
if a < b and a > b:	print('you are living in a strange world')
if not False:		print(True)


a = 0.3
b = 0.1 * 3
if a < b:	print('a < b')
elif a > b:	print('a > b')
else:		print('a == b')

if math.isclose(a, b): print('close enough')


s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2:	print('A < B')
if s2 < s3:	print('B < a')


# more practice
def is_odd(a):
	if a % 2 == 0:	print('a is even')
	else:			print('a is odd')
is_odd(4)

def dna_molweight(a):
	if a == 'A':	print('molecular weight of dATP is 491.2 g/mol')
	elif a == 'C':	print('molecular weight of dCTP is 467.2 g/mol')
	elif a == 'G':	print('molecular weight of dGTP is 507.2 g/mol')
	elif a == 'T':	print('molecular weight of dTTP is 482.2 g/mol')
	else:			print('that is not a valid DNA letter')
dna_molweight('C')