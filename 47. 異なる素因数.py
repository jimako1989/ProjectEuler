from mathlib import *

def Distinct_four_primes_factorsQ(integer) : 
	if not isinstance(integer , int) : return "TypeError : The arguments is NOT 'int'."
	lst = [num for num in Divisors(integer) if PrimeQ(num)]
	return True if len(lst) == 4 else False

def Find_first_four_consecutive_integers(integer) : 
	for num in range(integer):
		if Distinct_four_primes_factorsQ(num) and Distinct_four_primes_factorsQ(num + 1) and Distinct_four_primes_factorsQ(num + 2) and Distinct_four_primes_factorsQ(num + 3) : return num

if __name__ == "__main__":
	print Find_first_four_consecutive_integers(1000000)
