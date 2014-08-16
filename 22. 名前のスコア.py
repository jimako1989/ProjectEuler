def ord_alpha(string) : 
	lst = [c for c in string]
	num_lst = []
	for c in lst : 
		num_lst.append(ord(c) - 64)
	return num_lst

if __name__ == "__main__":
	lst = []
	f = open('./22. names.txt' , 'r')
	for line in f:
		itemList = line[:-1].split(',')
	for i in range(len(itemList)):
		lst.append(ord_alpha(str(itemList[i])))
	lst = sorted(lst)
	s = 0
	for i in range(len(lst)):
		s += (i + 1) * sum(lst[i])
	print s
