from mathlib import *

upper = 1000000
prime_lst = [PadLeft(ToDigitL(num) , int(log10(upper))) for num in range(upper/10 + 1 , upper - 1, 2) if PrimeQ(num)]

def prime_eight_replace() : 
	for digits in prime_lst:
		print digits
		for num in range(10):
			if digits[:-1].count(num) == 3 :
				new_digits = []
				for replace_num in range(10):
					new_num = int((str(digits)[1:-1:3]).replace(str(num) , str(replace_num)))
					new_digits.append(new_num)
				prime_count = 0
				for test_prime in new_digits:
					if ToDigit(test_prime) in prime_lst : 
						prime_count += 1
				if prime_count == 8:
					return ToInteger(digits)
				break

if __name__ == "__main__" : 
	print prime_eight_replace()
