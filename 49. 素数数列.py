from mathlib import *

if __name__ == "__main__":
	print 'making a 4digits prime list...'
	lst = [digits for digits in range(1000 , 10000) if PrimeQ(digits)]
	print 'done! finding the arithmetic sequence...'
	for num1 in lst:
		for num2 in DeleteCases(lst , num1):
			if sorted(ToDigit(num1)) == sorted(ToDigit(num2)) : 
				num3 = 2 * num2 - num1
				if num3 in DeleteCases(lst , [num1 , num2]) and sorted(ToDigit(num1)) == sorted(ToDigit(num3)): 
					print (num1 , num2 , num3)
	print 'done!'
