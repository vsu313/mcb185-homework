'''
A classic programming interview question is to write a program that reports 
the first 10 numbers from the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. 
This is a tricky problem. You need to initialize and keep track of 2 previous values.

'''

def fibonacci():
	num1 = 0
	num2 = 1
	print(num1)
	print(num2)
	for i in range(0, 8):
		final = num1 + num2
		num1 = num2
		num2 = final
		print(final)
			
fibonacci()