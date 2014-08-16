import math

#### DACLARE VARIABLES ####
def find_divisor(n) : 
	s = int(math.sqrt(n))
	lst = []
	for i in range(1 , s + 1) : 
		if n%i == 0 : lst.extend([i , n/i])
	return sorted(lst)

if __name__ == "__main__" : 
	s = 0
	for p in range(3 + 4 + 5 , 1000 , 2):
		if(s <= len(find_divisor(p))) : 
			s = len(find_divisor(p))
			print p 
