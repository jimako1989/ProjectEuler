N = 10001

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

if __name__ == "__main__":
    print sieve(114320)[N - 1]

