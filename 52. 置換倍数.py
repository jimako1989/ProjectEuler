from mathlib import *
all_num = []

#### DACLARE VARIABLES ####
def check() : 
	for x in all_num : 
		digit = sorted(ToDigit(x))
		if sorted(ToDigit(2 * x)) == sorted(ToDigit(3 * x)) == sorted(ToDigit(4 * x)) == sorted(ToDigit(5 * x)) == sorted(ToDigit(6 * x)) == digit : 
			return x

if __name__ == "__main__":
	num_lst = [1 , 2 , 4 , 5 , 7 , 8]
	perm = Permutations(num_lst[1:] , len(num_lst) - 1)
	for tail in perm:
		all_num.append(ToInteger([1] + tail))
	print all_num
	print check()
