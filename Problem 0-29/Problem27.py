import time
t = time.time()

def simpleSieve(a):
	for x in range(2,1415):
		if x == a:
			return True
		elif (a%x == 0):
			return False
	return True


def findPrime(memoizedList, x):
	for i in memoizedList:
		if x == i:
			return True
		elif (x%i == 0):
			return False
	return True



def chainLength(a,b,primeList):
	n = 0
	value = 0
	counter = 0
	while True:
		value = (n*n)+(a*n)+(b)
		if value in primeList:
			counter += 1 
		else:
			return counter

		n += 1


memoize = [x for x in range(2,1415) if simpleSieve(x)]
primeList = [x for x in range(2,2000) if findPrime(memoize,x)]
miniList = [x for x in range(2,1001) if findPrime(memoize,x)]

maxLen = 0 
curr = 0 
maxA = 0
maxB = 0

for b in miniList:
	x = -1*b 
	for a in range(x,b):
		curr = chainLength(a,b,primeList)
		if (curr > maxLen):
			maxLen = curr
			maxA = a
			maxB = b

print maxLen, " ", maxA, " ", maxB
print("Time Taken: %s" % (str(time.time() - t)))
