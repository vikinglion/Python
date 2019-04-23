t = 0
float(t) 
def race(v1, v2, g):
	time = []
	if v1 >= v2:
		return None	
	else:
		t = g / (v2 - v1)
		time.append(int(t))
		t = (t - int(t)) * 60
		time.append(int(t))
		t = (t - int(t)) * 60
		time.append(int(t))
		return print(time)
		
race(720, 850, 70)
race(80, 91, 37)
race(80, 100, 40)
