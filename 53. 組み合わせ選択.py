from mathlib import *

#### DACLARE VARIABLES ####


if __name__ == "__main__" : 
	print len([(n , r) for n in range(1 , 101) for r in range(1 , n) if StirlingApproximation(n)/(StirlingApproximation(r) * StirlingApproximation(n - r)) > 1000000])
