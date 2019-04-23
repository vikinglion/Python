def find_short():
	s=input("please input a string:\n")
	l=list(s)
	l.append(' ')
	print(l)
	count=0
	length=0
	minnum=100
	for i in l:
		count+=1
		if i == " ":
			length=len(l[:count-1])
			if minnum>length:
				minnum = length
			count=0	
	print(minnum)	
find_short()

'''
def find_short(s):
    return min(len(x) for x in s.split())
'''
