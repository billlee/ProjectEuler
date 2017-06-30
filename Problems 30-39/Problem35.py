import itertools
from collections import deque 
import time 


first = time.time()

def rotator(x):
	x = deque(x)
	y = []
	temp = ""
	for i in range(0,len(x)):
		temp = x.popleft()
		x.append(temp)
		y.append("".join(x))

	return y


def isPrime(x, listy):
	for i in listy:
		if i == x: 
			return True
		elif x%i == 0:
			return False

	return True



primeList = [x for x in range(2,1000) if isPrime(x, list(range(2,1000)))]

masterPrimeList = [x for x in range(2, 1000000) if isPrime(x, primeList)]

masterPrimeList = set(masterPrimeList)


temp = []
counter = 0 
mini = 0 
checker = True 

for i in masterPrimeList:
	temp = rotator(str(i))
	mini = 0
	for j in range(0,len(temp)):
		if int(temp[j]) not in masterPrimeList:
			checker = False 
			break
		else:
			mini += 1

	if (mini == len(temp)) & checker:
		counter += 1

	checker = True

print counter








