#Distinct Prime Factors, Problem 47
import time
t = time.time()
def isPrime(x):
	if x == 2:
		return True
	elif x%2 == 0:
		return False
	for i in range(3, int((x**0.5)) + 1):
		if x == i:
			return True
		elif (x%i == 0):
			return False 
	return True

def fasterPrime(x, l):
	if x == 2:
		return True
	elif x%2 == 0:
		return False
	for i in l:
		if x == i:
			return True
		elif (x%i == 0):
			return False 
	return True

y  = [x for x in range(2,1000) if isPrime(x)]
global primes 
primes = [x for x in range(2,1000000) if fasterPrime(x,y)]
global cheksum
cheksum = set(primes)

print time.time()-t

def primeFactors(x):
	ret = set()
	for i in primes:
		if i > int(x**0.5):
			return ret
		while (x%i == 0):
			ret.add(i)
			x = x/i
		if x in cheksum:
			ret.add(x)
			return ret
	return ret

a,b,c,d = set(),set(),set(),set()

for i in range(646, 2000000):
	if (i == 646):
		a,b,c,d = primeFactors(i), primeFactors(i+1), primeFactors(i+2), primeFactors(i+3)

	else:
		a = b
		b = c
		c = d 
		d = primeFactors(i+3)

	
	if ((len(a) ==  len(b) == len(c) == len(d)== 4)):
		print i
		exit()







