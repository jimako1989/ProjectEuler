#### DACLARE VARIABLES ####
N = 20

def GCD(m , n) : 
	a = max(m , n)
	b = min(m , n)

	r = a%b
	if r == 0 : return b
	return GCD(b , r)

def LCM(a , b) : 
	return a * b / GCD(a , b)

def nLCM(lst) : 
	while len(lst) > 1 : 
		a = lst.pop(0)
		b = lst.pop(0)
		lst.append(LCM(a , b))
	if len(lst) == 1 : return lst[0]

if __name__ == "__main__":
	print nLCM(range(1 , N + 1))
