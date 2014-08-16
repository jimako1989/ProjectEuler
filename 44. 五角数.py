from mathlib import *

#### DACLARE VARIABLES ####
def nth_Pentagon(integer) : 
	if not isinstance(integer , int) : return "TypeError : The argument is NOT 'int'."
	return integer * (3 * integer - 1)/2

def min_diff_Pentagon(integer) : 
	if not isinstance(integer , int) : return "TypeError : The argument is NOT 'int'."
	lst = [nth_Pentagon(n) for n in range(1 , integer)]
	for P_j in lst:
		for P_k in DeleteCases(lst , P_j):
			if P_j - P_k > 0 : 
				if PentagonNumberQ(P_j - P_k) and PentagonNumberQ(P_j + P_k) : return P_j - P_k

if __name__ == "__main__":
	print min_diff_Pentagon(10000)
