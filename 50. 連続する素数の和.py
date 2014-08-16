from mathlib import *
import sys

upper = 1000000
prime_lst = [num for num in range(3 , upper - 1, 2) if PrimeQ(num)]

def DirectSum(lst , loop) : 
	return [sum(num) for num in Transpose([lst[1:] , prime_lst[:-loop]]) if sum(num) < upper]

def IterateDirectSum(loop) : 
	lst = DirectSum(DirectSum(IterateDirectSum(loop - 2) , loop - 2) , loop - 1) if loop > 1 else prime_lst
	Find_First(lst , loop)
	if len(lst) > 0 : Find_First(lst + [int(lst[0]) + 2] , loop)
	return lst

def Find_First(lst , loop) : 
	for prime in prime_lst : 
		if prime in lst : 
			print (loop , prime)
			break
	return None

if __name__ == "__main__":
	print 'finish making the prime table under 1000000.'
	recursion = 600
	sys.setrecursionlimit(2 * recursion)
	IterateDirectSum(recursion + 1)
	print '^^^ The last one is the answer!!'

