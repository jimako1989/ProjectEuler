import math

#### DACLARE VARIABLES ####
def isInteger(n) : 
	if n - int(n) == 0:
		return True
	else : 
		return False

def isTriangleNumber(n) : 
	if isInteger(( - 1 + math.sqrt(1 + 8 * n))/2) : 
		return True
	else : 
		return False

def isTriangleWord(string) : 
	if isTriangleNumber(sum(ord_alpha(string))):
		return True
	else : 
		return False

def ord_alpha(string) : 
	lst = [c for c in string]
	num_lst = []
	for c in lst : 
		num_lst.append(ord(c) - 64)
	return num_lst

def FileToList(filepath) : 
	f = open(filepath , 'r')
	for line in f:
		itemList = line[:-1].split(',')
	return itemList

if __name__ == "__main__":
	lst = FileToList('./42. words.txt')
	s = 0
	for word in lst:
		if isTriangleWord(word[1:-1]) : 
			s += 1
	print s
