from decimal import *

getcontext().prec = 5000

def frac_circ(d) : 
	frac = str(Decimal(1)/Decimal(d))
	i = 0
	l = len(frac) - 1
	for i in range(l - 2 , 2 , -1):
		b = True
		if frac[l - 1] == frac[i] : 
			c = l - i - 1
			for j in range(c):
				if frac[i + j] != frac[i + j - c] : 
					b = False
					break
			if b : return c
	return 0

if __name__ == "__main__":
	s = 0
	I = 0
	for i in range(1 , 1000):
		if frac_circ(i) > s : 
			print i , frac_circ(i)
			s = frac_circ(i)
			I = i
	print I
