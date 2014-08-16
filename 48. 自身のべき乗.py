from mathlib import *

#### DACLARE VARIABLES ####
def last_ten_digits(integer) : 
	return ToIntegerL(ToDigitL(integer)[-10:])

def self_pow(integer) : 
	num = last_ten_digits(integer)
	for loop in range(1 , integer):
		integer = last_ten_digits(integer * num)
	return integer

if __name__ == "__main__":
	s = 0
	for i in range(1 , 1001) : 
		print i
		s += last_ten_digits(self_pow(i))
	print last_ten_digits(s)
