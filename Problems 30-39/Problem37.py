#Problem 37, Truncatable Primes 
from collections import deque 

def stripLeft(string):
	string = deque(string)
	y = []
	temp = ""
	for i in range(0,len(string)):
			temp = string.popleft()
			if not string:
				pass
			else:
				y.append("".join(string))

	return y 

def stripRight(string):
	string = deque(string)
	y = []
	temp = ""
	for i in range(0,len(string)):
			temp = string.pop()
			if not string:
				pass
			else:
				y.append("".join(string))

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



a = []
b = []
temporary = ""
proceed = True
solution = []


for i in masterPrimeList: 
	temporary = str(i)
	a = stripLeft(temporary)
	b = stripRight(temporary)
	for j in a:
		if int(j) not in masterPrimeList:
			proceed = False 
			break
			
	if proceed:
		for k in b:
			if int(k) not in masterPrimeList:
				proceed = False 
				break
	if proceed:
		solution.append(i)

	proceed = True


total = 0 
for i in solution:
	if i > 10:
		total += i


print total









