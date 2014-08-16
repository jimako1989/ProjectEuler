size = 13

array = [[0 for i in range(size)] for i in range(100)] 

def put_in_array() : 
	f = open('/Users/jimako/Documents/WorkSpace/2013/06/PE/13. nums.txt')
	lines = f.readlines()
	f.close()
	i = 0
	for line in lines : 
		array[i] = int(line[:size])
		i += 1
	return array

if __name__ == "__main__":
	print str(sum(put_in_array()))[:10]
