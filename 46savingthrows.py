'''
One of the core mechanics of D&D is the "saving throw". 
When certain events happen, you need to roll a d20 to figure out if you succeed or not. 
For example, you are walking across a frozen lake and it begins to crack underfoot. 
If you make a saving throw, you step aside. 
If you fail, you fall in. Some saving throws are more difficult than others. 
If the ice is very thick, the "difficulty class" (DC) may be only 5. 
This means you only need to roll a 5 or higher to succeed. 
However, if the ice is thin and has a DC of 15, you will need a roll of 15 or higher to 
succeed. Certain events may give you "advantage" or "disadvantage". 
For example, if you have a rope tied around your waist and a friend is instructed to pull 
you aside if anything bad happens, you could have "advantage". 
This allows you to roll two d20s and take the larger value. 
You may also have disadvantage, for example another "friend" pushes you from behind, 
causing you to stumble forward. 
In this case, you have "disadvantage" and must take the lower of two d20 rolls.

Write a program that simulates saving throws against DCs of 5, 10, and 15. 
What is the probability of success normally or with advantage/disadvantage? 
Make a table showing the results.

'''

# co-author by conner suen and vanessa su

import random

roll = 10000

# DC 5
d5suc = 0
d5fail = 0
for i in range(roll):
	d = random.randint(1, 20)
	if d >= 5:    d5suc += 1
	else:        d5fail += 1

# DC 5 advantage
d5asuc = 0
d5afail = 0
for i in range(roll):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2:
		if r1 >= 5: d5asuc += 1
		else: d5afail += 1
	else:
		if r2 >= 5: d5asuc += 1
		else: d5afail += 1

# DC 5 disadvantage
d5dsuc = 0
d5dfail = 0
for i in range(roll):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2:
		if r2 >= 5: d5dsuc += 1
		else: d5afail += 1
	else:
		if r1 >= 5: d5dsuc += 1
		else: d5afail += 1

# DC 10
d10suc = 0
d10fail = 0
for i in range(roll):
	d = random.randint(1, 20)
	if d >= 10:    d10suc += 1
	else:        d10fail += 1 

# DC 10 advantage
d10asuc = 0
d10afail = 0
for i in range(roll):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2:
		if r1 >= 10: d10asuc += 1
		else: d5afail += 1
	else:
		if r2 >= 10: d10asuc += 1
		else: d10afail += 1

# DC 10 disadvantage
d10dsuc = 0
d10dfail = 0
for i in range(roll):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2:
		if r2 >= 10: d10dsuc += 1
		else: d10dfail += 1
	else:
		if r1 >= 10: d10dsuc += 1
		else: d10dfail += 1

# DC 15
d15suc = 0
d15fail = 0
for i in range(roll):
	d = random.randint(1, 20)
	if d >= 15:    d15suc += 1
	else:        d15fail += 1

# DC 15 advantage
d15asuc = 0
d15afail = 0
for i in range(roll):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2:
		if r1 >= 15: d15asuc += 1
		else: d15afail += 1
	else:
		if r2 >= 15: d15asuc += 1
		else: d15afail += 1

# DC 15 disadvantage
d15dsuc = 0
d15dfail = 0
for i in range(roll):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2:
		if r2 >= 15: d15dsuc += 1
		else: d15dfail += 1
	else:
		if r1 >= 15: d15dsuc += 1
		else: d15dfail += 1


print(f'Difficulty Class\tD5\tDa5\tDd5\tD10\tDa10\tDd10\tD15\tDa15\tDd15')
print(f'Probability\t', (d5suc / roll), (d5asuc / roll), (d5dsuc / roll), (d10suc / roll), (d10asuc / roll), (d10dsuc / roll), (d15suc / roll), (d15asuc / roll), (d15dsuc / roll), sep='\t')

