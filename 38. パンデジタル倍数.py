import math

#### DACLARE VARIABLES ####
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

def isPandigital(num_lst) : 
	digit_lst = []
	for i in range(len(num_lst)):
		digit_lst.append(num2digit(num_lst[i]))
	if [x for x in sorted(flatten(digit_lst))] == [x for x in range(1 , 10)] : 
		return True
	else : 
		return False

def maxPandigital() : 
	for n in range(2 , 10):
		for num in range(99999 , 0 , -1):
			if isPandigital(map((lambda x : x * num) , range(1 , n))) : 
				return flatten(map((lambda x : x * num) , range(1 , n)))

if __name__ == "__main__":
	print maxPandigital()
