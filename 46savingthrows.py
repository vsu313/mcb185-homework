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

import random

roll = 10000

# DC 5
d5suc = 0
d5fail = 0
for i in range(roll):
	d = random.randint(1, 20)
	if d >= 5:	d5suc += 1
	else:		d5fail += 1


# DC 10
d10suc = 0
d10fail = 0
for i in range(roll):
	d = random.randint(1, 20)
	if d >= 10:	d10suc += 1
	else:		d10fail += 1


# DC 15
d15suc = 0
d15fail = 0
for i in range(roll):
	d = random.randint(1, 20)
	if d >= 15:	d15suc += 1
	else:		d15fail += 1
	
print(f'Difficulty Class\tD5\tD10\tD15')
print(f'Probability\t', (d5suc / roll), (d10suc / roll), (d15suc / roll), sep='\t')


