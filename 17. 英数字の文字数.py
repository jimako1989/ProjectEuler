def cnt1(x) :
	cnt = 0
	if x == '0' : cnt += 0
	elif x == '1' : cnt += len('one')
	elif x == '2' : cnt += len('two')
	elif x == '3' : cnt += len('three')
	elif x == '4' : cnt += len('four')
	elif x == '5' : cnt += len('five')
	elif x == '6' : cnt += len('six')
	elif x == '7' : cnt += len('seven')
	elif x == '8' : cnt += len('eight')
	elif x == '9' : cnt += len('nine')
	return cnt

def cnt2(x) :
	l = len(str(x))
	xs = str(x)
	lst = (3 - l) * ['0']
	lst.extend(xs)

	cnt = 0
	if lst[1] == '0' : 
		cnt += cnt1(lst[2])
	elif lst[1] == '1' : 
		if lst[2] == '0' : cnt += len('ten')
		elif lst[2] == '1' : cnt += len('eleven')
		elif lst[2] == '2' : cnt += len('twelve')
		elif lst[2] == '3' : cnt += len('thirteen')
		elif lst[2] == '4' : cnt += len('fourteen')
		elif lst[2] == '5' : cnt += len('fifteen')
		elif lst[2] == '6' : cnt += len('sixteen')
		elif lst[2] == '7' : cnt += len('seventeen')
		elif lst[2] == '8' : cnt += len('eighteen')
		elif lst[2] == '9' : cnt += len('nineteen')
	elif lst[1] == '2' : 
		cnt += len('twenty')
		cnt += cnt1(lst[2])
	elif lst[1] == '3' : 
		cnt += len('thirty')
		cnt += cnt1(lst[2])
	elif lst[1] == '4' : 
		cnt += len('forty')
		cnt += cnt1(lst[2])
	elif lst[1] == '5' : 
		cnt += len('fifty')
		cnt += cnt1(lst[2])
	elif lst[1] == '6' : 
		cnt += len('sixty')
		cnt += cnt1(lst[2])
	elif lst[1] == '7' : 
		cnt += len('seventy')
		cnt += cnt1(lst[2])
	elif lst[1] == '8' : 
		cnt += len('eighty')
		cnt += cnt1(lst[2])
	elif lst[1] == '9' : 
		cnt += len('ninety')
		cnt += cnt1(lst[2])
	return cnt

def letters_count(x) : 
	l = len(str(x))
	xs = str(x)
	lst = (3 - l) * ['0']
	lst.extend(xs)

	cnt = 0
	if lst[0] == '0' : 
		cnt += cnt2(xs)
	else : # ex. x == 100
		cnt += cnt1(lst[0])# 'one'
		if lst[1] == '0' and lst[2] == '0' : cnt += len('hundred')
		else : cnt += len('hundredand')
		cnt += cnt2(xs)
	return cnt

if __name__ == "__main__":
	s = 0
	for i in range(1 , 1000):
		s += letters_count(i)
	s += len('onethousand')
	print s
