"""
Given values for true positives, false positives, true negatives, and false negatives,
write a function that reports the accuracy and F1 score.
Demonstrate your function works by using it several times in the program.

"""

def accuracy(TP, FP, TN, FN):
	a = ((TP + TN) / (TP + FP + TN + FN))
	p = (TP / (TP + FP))
	r = (TP / (TP + FN))
	f = (2 / ((1 / r) + (1 / p)))
	print(a, f)

accuracy(50, 10, 100, 5)
accuracy(12, 23, 23, 92)
accuracy(72, 12, 34, 26)