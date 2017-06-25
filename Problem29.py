#Distinct Powers, Problem 29

w, h = 99, 99
Mat = [[0 for x in range(w)] for y in range(h)] 


temp = 0

x = 0
y = 0

a = 2
b = 2
temp = 0

counter = 0

for i in range(0,99):
	for j in range(0,99):
		temp = a ** b
		if any(temp in array for array in Mat):
			Mat[i][j] = 0
			counter += 1
		else:
			Mat[i][j] = temp
		b += 1
	a += 1
	b = 2





print (99*99)-counter

