import math
from itertools import chain

#### DACLARE VARIABLES ####
NUMS = [1 , 2 , 3 , 5 , 7 , 9]

def isPrime(n) : 
	if n == 1 : return False
	if n < 4 : return True
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

def num2digit(num) : 
	return [int(x) for x in str(num)]

def digit2num(digit) : 
	num = 0
	for i in range(len(digit)):
		num += digit[i] * pow(10 , len(digit) - i - 1)
	return num

def flatten(L):
    if isinstance(L, list):
        if L == []:
            return []
        else:
            return flatten(L[0]) + flatten(L[1:])
    else:
        return [L]

def Tuples(lst , digits) : 
	if digits == 1:
		return lst
	else : 
		return [flatten([x] + [y]) for x in lst for y in Tuples(lst , digits - 1)]

def num_tuple(digits) : 
	return [digit2num(x) for x in Tuples(NUMS , digits)]

def Prime_check(lst) : 
	prime_lst = []
	for i in range(len(lst)):
		if isPrime(lst[i]):
			prime_lst.append(lst[i])
	return prime_lst

def isTruncatable(num) : 
	digit = num2digit(num)
	if isLeftTr(digit) and isRightTr(digit):
		return True
	else : 
		return False

def isLeftTr(digit) : 
	if len(digit) == 1 : 
		if digit2num(digit) in [2 , 3 , 5 , 7] : 
			return True
		else : 
			return False
	lnum = digit[0:-1]
	if isPrime(digit2num(lnum)) : 
		return isLeftTr(lnum)
	else : 
		return False

def isRightTr(digit) : 
	if len(digit) == 1 : 
		if digit2num(digit) in [2 , 3 , 5 , 7] : 
			return True
		else : 
			return False
	rnum = digit[1:]
	if isPrime(digit2num(rnum)) : 
		return isRightTr(rnum)
	else : 
		return False


if __name__ == "__main__":
	truncatable = []
	
	for digit in range(2,7) : 
		lst = Prime_check(num_tuple(digit))
		for num in lst : 
			if isTruncatable(num) : 
				truncatable.append(num)
	print truncatable
	print len(truncatable)
	print sum(truncatable)
