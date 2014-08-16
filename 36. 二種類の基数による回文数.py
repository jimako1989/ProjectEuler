import math

#### DACLARE VARIABLES ####
def num2digit(num) : 
	return [int(x) for x in str(num)]

def digit2num(digit) : 
	num = 0
	for i in range(len(digit)):
		num += digit[i] * pow(10 , len(digit) - i - 1)
	return num

def isCycleNumber(num) : 
	digit = num2digit(num)
	l = len(str(num))
	if digit == digit[-1::-1]:
		return True
	return False

def Base2to10(num) : 
	return int(str(num) , 2)

def Base10to2(num) : 
	return format (num,'b')	

if __name__ == "__main__":
	s = 0
	for num in range(1000000):
		if isCycleNumber(num) and isCycleNumber(Base10to2(num)):
			s += num
	print s
