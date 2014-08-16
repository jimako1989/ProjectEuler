from mathlib import *

def against_Goldbach(integer) : 
	lst = [num for num in range(1 , integer , 2) if len(Divisors(num))>2]
	for num in lst:
		tf = False
		for w_square in range(1 , int(sqrt(num/2)) + 1):
			if PrimeQ(num - 2 * w_square * w_square) : tf = True
		if tf == False : return num

if __name__ == "__main__":
	print against_Goldbach(10000)
