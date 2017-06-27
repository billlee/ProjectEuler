x = 1
y = 1 
index = 3
z = 0

while True: 
	z = x + y
	if len(str(z)) >= 1000 :
		print "haha ", index 
		break

	x = y
	y = z
	index += 1