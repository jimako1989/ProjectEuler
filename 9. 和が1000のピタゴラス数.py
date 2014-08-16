import math

#### DACLARE VARIABLES ####

def search() : 
	m = 0
	n = 0
	for m in range(25):
		for n in range(m):
			if m * (m + n) == 500 : return m , n

if __name__ == "__main__":
	tpl= search()
	m = tpl[0]
	n = tpl[1]
	print 2 * m * n * (pow(m , 4) - pow(n , 4))


