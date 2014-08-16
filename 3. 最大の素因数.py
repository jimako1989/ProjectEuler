size = 100000
val = 600851475143

def sieve(n) : 
	search = range(2 , n)
	prime = []

	while len(search) > 0 : 
		p = search.pop(0)
		i = 1
		while 1:
			if i >= len(search) : break
			if search[i]%p == 0 : search.pop(i)
			i += 1
		prime.append(p)

	return prime

def FactorInteger(n) :
	prime = sieve(n)
	lst = []

	while len(prime) > 0 :
		p = prime.pop(0)
		i = 0
		tmp = n
		while tmp%p == 0 :
			i+= 1
			tmp /= p
		if i > 0 : lst.append((p , i))
	return lst

def max_factor_search(n , lst) : 
	
	while len(lst) > 0 : 
		p = lst.pop()
		if n%p == 0 : return p
	return None

if __name__ == "__main__":
	print max_factor_search(val , sieve(size))
