'''
This is the same problem as above, but instead of making a list of birthdays (e.g. 23) 
make a list from the calendar (e.g. 365). 

'''

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same = 0

for i in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)
	for i in range(people):
		calendar[random.randint(0, 364)] += 1
	for i in range(days):
		if calendar[i] >= 2:
			same += 1
			break
			
print(same / trials)