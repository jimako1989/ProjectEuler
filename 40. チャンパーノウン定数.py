import math

#### DACLARE VARIABLES ####
def int2digit(integer) : 
	return [int(x) for x in str(int(integer))]

def flatten(L):
    if isinstance(L, list):
        if L == []:
            return []
        else:
            return flatten(L[0]) + flatten(L[1:])
    else:
        return [L]

def nth_ChampernowneNumber(n) : 
	res = n
	digit = 1
	while res > 0 : 
		if res - 9 * math.pow(10 , digit - 1) * digit > 0:
			res -= int(9 * math.pow(10 , digit - 1) * digit)
			digit += 1
		else : 
			num = int((res - 1)/digit)
			res -= digit * num
			break
	if digit == 1:
		return n
	else : 
		return int2digit(math.pow(10 , digit - 1) + num)[res - 1]

if __name__ == "__main__":
	prod = 1
	for i in range(7):
		prod *= nth_ChampernowneNumber(int(math.pow(10 , i)))
	print prod

