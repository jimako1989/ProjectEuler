import math

def isPrime(n) : 
	if n <= 1 : return False
	if n < 4 : return False
	if n%2 == 0 : return False
	if n < 9 : return True
	if n%3 == 0 : return False
	r = int(math.sqrt(n))
	f = 5
	while f <= r : 
		if n%f == 0 : return False
		if n%(f + 2) == 0 : return False
		f = f + 6
	return True

def find_quadratic_prime() : 
	s = 0
	for a in range( -999 , 1000):
		for b in range( -999 , 1000):
			n = 0
			while 1 : 
				if isPrime(n * n + a * n + b) : 
					n += 1
				else : 
					if n > s : 
						s = n
						t = (a , b , n)
						print t
					else : 
						break
	return t[0] * t[1]

if __name__ == "__main__":
	print find_quadratic_prime()
