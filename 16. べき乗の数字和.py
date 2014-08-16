import math

def sum_digits(n):
	dgt_lst = [x for x in str(pow(2 , n))]
	return sum(map((lambda x: int(x)),dgt_lst))

if __name__ == "__main__":
	print sum_digits(1000)
