N = 1001

if __name__ == "__main__":
	s = 1
	x = 1
	for i in range(1 , (N - 1)/2 + 1):
		s += sum(range(x + 2 * i , x + 5 * 2 * i , 2 * i))
		x = x + 4 * 2 * i
	print s
