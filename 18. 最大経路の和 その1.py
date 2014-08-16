def maxsum_path() : 
	f = open('./18. nums.txt')
	lines = f.readlines()
	f.close()
	
	L = len(lines)
	array = [[0 for l in range(r + 1)] for r in range(L)]
	r = 0
	for line in lines : 
		l = len(line)
		for i in range(0 , l , 3):
			array[r][i/3] = int(line[i:i + 2])
		r += 1
	
	for r in range(1 , L):
		array[r][0] += array[r - 1][0]
		array[r][r] += array[r - 1][r - 1]
		for l in range(1 , r):
			array[r][l] += max(array[r - 1][l - 1] , array[r - 1][l])

	return max(array[L - 1])

if __name__ == "__main__":
	print maxsum_path()

