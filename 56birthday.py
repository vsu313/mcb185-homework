'''
Write a program that simulates the problem by filling up classrooms of students with 
randomly chosen birthdays. Make the number of days in the calendar and the 
number of people in the classroom command line arguments. 
You will have to run this thousands of times to get an accurate estimate, 
so have a parameter for that too.

'''

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
same = 0

for i in range(trials):
	person1 = 0
	person2 = 1
	bdaymon = []
	bdayday = []
	for i in range(people):
		month = random.randint(1, 12)
		if month == 2:
			if days == 365:
				day = random.randint(1, 28)
				bdaymon.append(month)
				bdayday.append(day)
			elif days == 366:
				day = random.randint(1, 29)
				bdaymon.append(month)
				bdayday.append(day)
		elif month == 4 or month == 6 or month == 9 or month == 11:
			day = random.randint(1, 30)
			bdaymon.append(month)
			bdayday.append(day)
		else:
			day = random.randint(1, 31)
			bdaymon.append(month)
			bdayday.append(day)
	while person1 < people:
		while person2 < people:
			if bdaymon[person1] == bdaymon[person2]:
				if bdayday[person1] == bdayday[person2]:
					same += 1
					person2 = person1 = people
			person2 += 1
		person1 += 1
		person2 = person1 + 1

print(same / trials)