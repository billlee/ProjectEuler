x = 1 
total = 1

for spiral in range(1,501):
	for spiral2 in range(0,4):
		y  = (spiral*2) + x
		total += y
		x = y 

print total


