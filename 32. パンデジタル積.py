import math
def find_divisor(n) : 
	s = int(math.sqrt(n))
	lst = []
	for i in range(1 , s):
		if n%i == 0 : lst.extend([i , n/i])
	return sorted(lst)

def check_num(n) : 
	lst1to9 = [str(x) for x in range(1 , 10)]
	for d in find_divisor(n)[1:-1]:
		num_lst = []
		num_lst.extend(list(str(d)))
		num_lst.extend(list(str(n)))
		num_lst.extend(list(str(n/d)))
		num_lst.sort()
		if num_lst == lst1to9:
			return n
	return 0

def num_devide(search_lst) :
	s = 0
	for n in search_lst:
		s += check_num(n)
	return s

if __name__ == "__main__":
	print num_devide(range(1000 , 10000))
