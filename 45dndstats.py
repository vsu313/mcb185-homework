'''
In Dungeons and Dragons, each character is described by 6 statistics (strength, 
intelligence, wisdom, dexterity, constitution, charisma). 
In the old days, each stat was decided by summing up the values on 3 six-sided dice (3D6).
Each stat therefore has a range of 3-18 and an average of 10.5. 
Over the years, the official rules have changed and many players have added their own 
house rules. 
Write a program that determines the average stat value using the various rules below.

3D6: roll 3 six-sided dice
3D6r1: roll 3 six-sided dice, but re-roll any 1s
3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
4D6d1: roll 4 six-sided dice, dropping the lowest die roll

'''

import random


# 3D6
roll = 100000
turn = 0
total = 0
for i in range(roll):
	for i in range(3):
		d = random.randint(1, 6)
		turn += d
	total += turn
	turn = 0
print(f'the average stat value for 3D6 is {total / roll}')
	

# 3D6r1
roll = 100000
turn = 0
total = 0
for i in range(roll):
	for i in range(3):
		d = random.randint(1, 6)
		if d == 1:
			d = random.randint(1, 6)
		turn += d
	total += turn
	turn = 0
print(f'the average stat value for 3D6r1 is {total / roll}')


# 3D6x2
roll = 100000
turn = 0
total = 0
for i in range(roll):
	for i in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2:	dmax = d1
		else:		dmax = d2
		turn += dmax
	total += turn
	turn = 0
print(f'the average stat value for 3D6x2 is {total / roll}')


# 4D6d1
roll = 100000
total = 0
for i in range(roll):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if d1 <= d2 and d1 <= d3 and d1 <= d4:	d1 = 0
	elif d2 <= d3 and d2 <= d4:				d2 = 0
	elif d3 <= d4:							d3 = 0
	else:									d4 = 0
	total += d1 + d2 + d3 + d4
print(f'the average stat value for 4D6d1 is {total / roll}')