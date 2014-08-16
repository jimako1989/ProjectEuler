import math
from heapq import merge

def find_divisor(n) : 
	s = int(math.sqrt(n))
	lst = []
	for i in range(1 , s):
		if n%i == 0 : lst = list(merge(lst , [i , n/i]))
	return lst

if __name__ == "__main__":
	i = 0
	while 1 : 
		tri = i * (i + 1)/2
		if len(find_divisor(tri)) >= 500 : break
		i += 1
	print tri
