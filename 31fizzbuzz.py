'''
Make a program that writes out the numbers from 1 to 100. If the number is divisible by 3, 
write Fizz instead. If the number is divisible by 5, write Buzz instead. 
If the number is divisible by both 3 and 5, write FizzBuzz.
'''


for i in range(1, 100):
	if (i % 5) == 0 and (i % 3) == 0: print('FizzBuzz')
	elif (i % 3) == 0: print('Fizz')
	elif (i % 5) == 0: print('Buzz')
	else: print(i)