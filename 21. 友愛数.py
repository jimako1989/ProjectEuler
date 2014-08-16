import math

N = 10000

def sum_divisor(n) : 
	s = int(math.sqrt(n))
	lst = [1]
	for i in range(2 , s + 1):
		if n%i == 0 : lst.extend([i , n/i])
	return sum(lst)

def find_friend(n) : 
	lst = []
	for i in range(2 , n):
		if i == sum_divisor(sum_divisor(i)) and i != sum_divisor(i):
			lst.append(i)
	return lst

if __name__ == "__main__":
	print sum(find_friend(N))
