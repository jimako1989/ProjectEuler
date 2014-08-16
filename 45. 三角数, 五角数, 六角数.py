from mathlib import *

def nth_Hexagon(integer) : 
	if not isinstance(integer , int) : return "TypeError : The argument is NOT 'int'."
	return integer * (2 * integer - 1)

def Search_in_Hex(integer) : 
	Hex_lst = [nth_Hexagon(n) for n in range(143 + 1 , 143 + integer)]
	for num in Hex_lst:
		if TriangleNumberQ(num) and PentagonNumberQ(num) : return num

if __name__ == "__main__":
	print Search_in_Hex(100000)
