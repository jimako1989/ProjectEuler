import math

def Union(lst , lst0) : 
	if len(lst0) == 0 : return lst
	for i in range(len(lst0)) : 
		if not (lst0[i] in lst) : 
			lst.append(lst0[i])
	return sorted(lst)

if __name__ == "__main__":
	lst = []
	for a in range(2 , 101):
		lst1 = []
		for b in range(2 , 101):
			lst1.append(pow(a , b))
		Union(lst , lst1)
		print len(lst)

	print len(lst)

