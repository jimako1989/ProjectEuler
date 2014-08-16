lim = 1000000

def find_collatz_chain(n) : 
	cnt = 1
	while n != 1 : 
		n = n/2 if n%2 == 0 else 3 * n + 1
		cnt += 1
	return cnt

if __name__ == "__main__":
	m = 0
	M = 0
	for i in range(1 , lim):
		c = find_collatz_chain(i)
		if m < c : 
			m = c
			M = i
	print M

