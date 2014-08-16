import math

#### DACLARE VARIABLES ####
def num2digit(num) : 
	return [int(x) for x in str(num)]

def digit2num(digit) : 
	num = 0
	for i in range(len(digit)):
		num += digit[i] * pow(10 , len(digit) - i - 1)
	return num

def digit_factorial(num) : 
	if num == 0:
		return 1
	elif num == 1:
		return 1
	elif num == 2:
		return 2
	elif num == 3:
		return 6
	elif num == 4:
		return 24
	elif num == 5:
		return 120
	elif num == 6:
		return 720
	elif num == 7:
		return 5040
	elif num == 8:
		return 40320
	elif num == 9:
		return 362880

if __name__ == "__main__":
	s = 0
	for num in range(3 , 99999):
		if num == sum(map(digit_factorial , num2digit(num))) : 
			print num
			s += num
	print "Calculation was finished. Answer is " , s
