N = 1000000 - 1

def factorial(n) : 
	return 1 if n == 0 else n * factorial(n - 1)

def diff_fac(n) : 
	i = 0
	m = 0
	while n >= factorial(i) : 
		if factorial(i + 1) > n : 
			m = int(n/factorial(i))
			n = n%factorial(i)
			return (n , m , i)
		i += 1

def harmonic_expand(n) : 
	lst = []

	while 1 : 
		tmp = diff_fac(n)
		n = tmp[0]
		m = tmp[1]
		i = tmp[2]
		lst.append((i , m))
		if n == 0 : return sorted(lst)

def count_perm(lst) : 
	lst = map((lambda x : x[1]) , lst)
	lst.reverse()

	num = []

	i = 0
	nums = [i for i in range(10)]

	for i in lst:
		num.append(nums[i])
		del nums[i]
	num.extend(nums)
	
	return num

if __name__ == "__main__":
	print count_perm(harmonic_expand(N))

