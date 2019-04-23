def minimum_number():
	print("Please input 3 numbers to have a comparison:\n")
	a = input("\n")
	b = input("\n")
	c = input("\n")
	min_num = 0
	
	if a > b :
		min_num = b
		if b > c :
			min_num = c
			return min_num
		else :
			 return min_num
	elif a > c :
		min_num = c
		return min_num
	else :
		min_num = a
		return min_num
		
print(minimum_number())		 
