N = 2000000

def sum_prime(n) : 
	search = range(3 , n , 2)
	Sum = 2
	print 2
	while len(search) > 0 : 
		p = search.pop(0)
		i = 1
		while i < len(search):
			if search[i]%p == 0 : search.pop(i)
			i += 1
		print p
		Sum += p
	print "result : " + str(Sum)

if __name__ == "__main__":
	sum_prime(N)
