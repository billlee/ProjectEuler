#Problem 44, Pentagonal numbers

pentagons = [ (x*((3*x)-1))/2 for x in range(1, 10000)]

setagons = set(pentagons)

solutionSet = []

for i in pentagons:
	for j in pentagons:
		if ((i+j) in setagons) & (abs(j-i) in setagons):
			solutionSet.append(abs(i-j))
			print abs(i-j)



print solutionSet