import itertools 
import time


#ultimate brute force approach 


def checkProperty(x):
	primes = [2,3,5,7,11,13,17]
	for i in range(0,7):
		if ((int(x[i+1])*100 + int(x[i+2])*10 + int(x[i+3]))%primes[i] == 0):
			pass
		else:
			return 0
	return int(x)

a = time.time()

x = "0123456789"
permutz = list(map("".join, itertools.permutations(x)))

b = time.time()

totes = 0
for every in permutz:
	totes += checkProperty(every)


print totes, "\n", b-a, "\n", time.time()-b