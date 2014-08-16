import math

#### DACLARE VARIABLES ####
def factorial(n) : 
	return n * factorial(n - 1) if n > 1 else 1

def sum_digits(n):
	dgt_lst = [x for x in str(factorial(n))]
	return sum(map((lambda x: int(x)),dgt_lst))

if __name__ == "__main__":
	print sum_digits(100)



