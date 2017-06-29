#Problem 45, Triangular, Pentagonal, and Hexagonal 


triangles = [(x*(x+1))/2 for x in range(1,100001)]
pentagons = [(x*((3*x)-1))/2 for x in range(1,100001)]
hexagons = [(x*((2*x)-1)) for x in range(1,100001)]
pentagons = set(pentagons)
hexagons = set(hexagons)


for i in triangles:
	if (i in pentagons) & (i in hexagons):
		print i 