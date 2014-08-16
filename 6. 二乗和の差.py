#### DACLARE VARIABLES ####
N = 100

def sq_sum(n) : 
	return n * (n + 1) * (2 * n + 1)/6

def sum_sq(n) : 
	return (n * (n + 1)/2) * (n * (n + 1)/2)

if __name__ == "__main__":
	print sum_sq(N) - sq_sum(N)
