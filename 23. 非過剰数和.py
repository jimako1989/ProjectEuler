import math

N = 28123
num_lst = []

#### DACLARE VARIABLES ####
def sum_divisor(n) : 
	s = int(math.sqrt(n))
	lst = [1]
	for i in range(2 , s + 1):
		if n%i == 0 : lst.extend([i]) if i == n/i else lst.extend([i , n/i])
	return sum(lst)

def non_abundant_nums() : 
	s = []
	for i in range(1 , int(N)) : 
		if i < sum_divisor(i) : s.append(i)
	return s

def two_abundant_sum(n) : 
	i = 0
	while num_lst[i] <= int(n/2) : 
		if n - num_lst[i] in num_lst : 
			return n # n can be a sum of two abundant numbers.
		i += 1
	return 0 # n can't be a sum of two abundant numbers.

if __name__ == "__main__":
	num_lst = non_abundant_nums()

	s = 0
	for i in range(1 , N):
		s += two_abundant_sum(i)
	print(N * (N - 1)/2 - s)

