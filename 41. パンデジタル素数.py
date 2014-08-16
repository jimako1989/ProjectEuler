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

def isPandigital(num_lst) : 
	digit_lst = []
	for i in range(len(num_lst)):
		digit_lst.append(IntToDigit(num_lst[i]))
	if [x for x in sorted(flatten(digit_lst))] == [x for x in range(1 , len(num_lst) + 1)] : 
		return True
	else : 
		return False

def IntToDigit(integer) : 
	return [int(x) for x in str(int(integer))]

def flatten(L):
    if isinstance(L, list):
        if L == []:
            return []
        else:
            return flatten(L[0]) + flatten(L[1:])
    else:
        return [L]

if __name__ == "__main__":
	for num in range(9999999 , 0 , -1):
		if isPandigital(IntToDigit(num)) and isPrime(num):
			print num
			break
