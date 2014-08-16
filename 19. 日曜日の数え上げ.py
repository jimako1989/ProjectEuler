def sum_sunday(year) : 
	date = (1901 , 1 , 1 , 2)# 1901/1/1 , Tuesday
	LeapYear = 0
	y = date[0]
	m = date[1]
	d = date[2]
	a = date[3]

	s = 1

	while y <= year:
		a = (a + 1)%7
		m += int(d/31)
		d = 31 if d == 30 else (d + 1)%31

		if y%4 == 0 : LeapYear = 0 if y%400 != 0 and y%100 == 0 else 1
		else : LeapYear = 0

		if (m == 4 or m == 6 or m == 9 or m == 11) and d == 31:
		 	m += 1
			d = 1
		elif m == 2 and d - LeapYear == 29 : 
			m = 3
			d = 1
		elif m == 13 : 
			y += 1
			m = 1

		if d == 1 and a == 0 : 
			print (y , m)
			s += 1

	return s - 1

if __name__ == "__main__":
	print sum_sunday(2000)
