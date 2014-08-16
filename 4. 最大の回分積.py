#### DACLARE VARIABLES ####
def check(n) : 
	array = str(n)
	if (array[0] == array[-1] and array[1] == array[-2] and array[2] == array[-3]) : return True

def search_top(n) : 
	lst = []
	for i in range(999 , 99 , -1):
		for j in range(999 , 99 , -1):
			if check(i * j) : 
				lst.append(i * j)
				if len(lst) == n : return lst

if __name__ == "__main__":
	print search_top(5)
