import math

#### DACLARE VARIABLES ####
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

def RotateNumber(num) : 
	digit = num2digit(num)
	newdigit = digit[1:]
	newdigit.append(digit[0])
	newnum = digit2num(newdigit)
	return newnum

def isOnlyOdd(num) : 
	digit = num2digit(num)
	for i in digit:
		if i%2 == 0:
			return False
	return True

def isRotatePrime(num , loop) : 
	if isPrime(num):
		if loop < len(num2digit(num)) : 
			return isRotatePrime(RotateNumber(num) , loop + 1)
		else : 
			return True
	return False

if __name__ == "__main__":
	s = 1
	for num in range(3,1000000,2):
		if isOnlyOdd(num) : 
			if isRotatePrime(num , 0) : 
				s += 1
	print s
