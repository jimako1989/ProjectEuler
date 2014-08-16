size = 20

def factorial(n) : 
	return 1 if n == 1 else n * factorial(n - 1)

if __name__ == "__main__":
	print factorial(2 * size)/factorial(size)/factorial(size)
