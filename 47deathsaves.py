'''
Death saves are a little different than normal saving throws. 
If your health drops to 0 or below, you are unconscious and may die. 
Each time it is your turn, roll a d20 to determine if you get closer to life or fall 
deeper into death. If the number is less than 10, you record a "failure". 
If the number is 10 or greater, you record a "success". If you collect 3 failures, 
you "die". If you collect 3 successes, you are "stable" but unconscious. 
If you are unlucky and roll a 1, it counts as 2 failures. If you're lucky and roll a 20, 
you gain 1 health and have "revived". Write a program that simulates death saves. 
What is the probability one dies, stabilizes, or revives?

'''

import random

repeat = 100000
rolls = 0		# number of rolls
suc = 0			# rolls for success
fail = 0		# rolls for fail
health = 0		# rolls for health
totsuc = 0		# total stabilizes
totfail = 0		# total deaths
tothealth = 0	# total revivals

for i in range(repeat):
	while True:
		d = random.randint(1, 20)
		if d == 1:			fail += 2
		elif d < 10:		fail += 1
		elif d == 20:		health += 1
		else:				suc += 1
		if health == 1: 	tothealth += 1
		elif fail == 3:		totfail += 1
		elif suc == 3:		totsuc += 1
		if health == 1 or fail == 3 or suc == 3: break
	rolls += 1
	suc = 0
	fail = 0
	health = 0
	
print(f'the probability of death is {totfail / rolls}!')
print(f'the probability of stabilizing is {totsuc / rolls}!')
print(f'the probability of revival is {tothealth / rolls}!')