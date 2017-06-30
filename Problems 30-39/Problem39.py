#Problem 39, Integer Right Triangles
#We observe a property of a Right Triangle when its perimeter is maximized, this happens when it is isosceles 

def solutionCount(perimeter):
	solutions = {k: [] for k in range(1001)}
	a = 1 
	b = 2
	c =3 
	while (a < perimeter/3):
		while ((b >= a) &  (b < perimeter)):
			while((c >= b) & (c < perimeter)):
				if ((a+b+c) > 1000):
					pass
				elif (((a*a) + (b*b)) == (c*c)):
					solutions[a+b+c].append((a,b,c))

				c+=1
			c= b+1
			b+=1 
		b= a+1
		a+=1

	return solutions




diction = solutionCount(1001)
maximal = 0 
largest = 0
for i in range(0, 1001):
	if len(diction[i]) > maximal:
		maximal = len(diction[i])
		largest = i 




print diction[largest], maximal