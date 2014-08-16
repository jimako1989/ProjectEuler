import math

Upper = 354294# 999999 -> 6 * 9^5 = 354294 -> 6 digits

if __name__ == "__main__":
	s = 0
	for n in range(2 , Upper):
		if n == sum([pow(int(x) , 5) for x in str(n)]) : 
			s += n
			print n
	print s
