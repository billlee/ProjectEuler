#Goldbach's Other Conjecture 
import time
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


t = time.time()
doubleSquares = [2*(x*x) for x in range(1,100)]
print doubleSquares

primes = [x for x in range(2,1000) if isPrime(x)]
secondPrimes = [x for x in range(2,1000000) if fasterPrime(x,primes)]
secondPrimes = set(secondPrimes)

print time.time()-t


for i in range(3, 100000, 2):
	if i in secondPrimes:
		pass
	else:
		for j in doubleSquares:
			print  i, " ", j
			if i < j:
				print i
				exit()
			elif (i-j) in secondPrimes:
				break



