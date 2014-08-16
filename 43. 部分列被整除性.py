from mathlib import *

#### DACLARE VARIABLES ####
def PartialDivisibleQ(lst) : 
	if not isinstance(lst , list) : return False
	if not Pandigital0Q(lst) : return False
	prime_lst = [2 , 3 , 5 , 7 , 11 , 13 , 17]
	result = [ToInteger(lst[index : index + 3]) % prime_lst[index - 1] == 0 for index in range(1 , 8)]
	if result == [True] * 7 : return True
	return False

if __name__ == "__main__":
	s = 0
	print 'making a permutations list...(few minutes)'
	for num in Permutations(range(10) , 10):
		print num
		if PartialDivisibleQ(num) : 
			print '* found it ! *'
			s += ToInteger(num)
	print s
	
