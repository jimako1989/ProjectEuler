import math

pence_lst = [200 , 100 , 50 , 20 , 10 , 5 , 2 , 1]

def patterns(pence , coins , steps) : 
	if pence == 0 : return 1
	if pence < 0 or steps == 8 : return 0
	cnt = 0
	for i in range(pence/pence_lst[steps] + 1):
		coins[steps] = i
		cnt += patterns(pence - i * pence_lst[steps] , coins , steps + 1)
#	print cnt , pence , coins , steps
	return cnt

if __name__ == "__main__" : 
	print patterns(200 , [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , 0)
