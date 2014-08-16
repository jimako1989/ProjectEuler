import math
def Intersection(lst_p , lst_q) : 	
	for i in lst_p:
		if i in lst_q:
			return i
	return None

def GCD(m , n) : 
	a = max(m , n)
	b = min(m , n)

	r = a%b
	if r == 0 : return b
	return GCD(b , r)

def num2digit(num) : 
	return [int(x) for x in str(num)]

def digit2num(digit) : 
	num = 0
	for i in range(len(digit)):
		num += digit[i] * pow(10 , len(digit) - i - 1)
	return num

def check(p , q) : 
	if (p%10 == 0 and q%10 == 0) : return 1

	gcd = GCD(p , q)
	p1 = p/gcd
	q1 = q/gcd

	digit_p = num2digit(p)
	digit_q = num2digit(q)
	i = Intersection(digit_p , digit_q)
	if i is None : return 1
#	print q ,"/", p , "=" , q1 ,"/", p1
#	print digit_q , digit_p
	digit_p.remove(i)
	digit_q.remove(i)
#	print digit_q , digit_p
	if digit2num(digit_p) == 0 or digit2num(digit_q) == 0 : return 1
	gcd2 = GCD(digit2num(digit_p) , digit2num(digit_q))
#	print gcd2
#	if gcd2 == 1 : return 1
	p2 = digit2num(digit_p)/gcd2
	q2 = digit2num(digit_q)/gcd2
#	print "\t", "->" , q2 ,"/", p2

	if p1 == p2 and q1 == q2 : 
		print q ,"/", p , "=" , q1 ,"/", p1
#		print q1 , "/" , p1 , "\t" , q2 , "/" , p2 , "\t\t(*)"

	return 1

if __name__ == "__main__":
	for p in range(10 , 100):
		for q in range(10 , p):
			check(p , q)
