#### DACLARE VARIABLES ####
M = 4000000

def Succ_fibo_odd(odd , even) : 
	return (odd + 2 * even)

def Succ_fibo_even(odd , even) : 
	return (2 * odd + 3 * even)

def sum_fibo(Upper): 
	tmp_o = 1
	s = tmp_e = 2
	while 1:
		tmp = Succ_fibo_even(tmp_o , tmp_e)
		tmp_o = Succ_fibo_odd(tmp_o , tmp_e)
		tmp_e = tmp
		if tmp_e < Upper:
			s += tmp_e
		else:
			break
	return s

if __name__ == "__main__":
	print (sum_fibo(M));

