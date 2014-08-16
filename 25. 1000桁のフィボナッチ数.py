def fibo(n) : 
	fib = 3 * [1]
	cnt = 2
	while len(str(fib[2])) < n : 
		del fib[0]
		fib.append(fib[0] + fib[1])
		cnt += 1
		fib.sort()
	return cnt

if __name__ == "__main__":
	print fibo(1000)


