import itertools
def isPrime(a): 
	for x in range(2,316):
		if(x == a):
			return True
		if (a%x == 0):
			return False

	return True


def largePrimes(num, a):
	for x in a:
		if(num%x == 0):
			return False
	return True
	

primeList = [x for x in range(2,99381) if isPrime(x)]


x = "1234567"

l = list(map("".join, itertools.permutations(x)))

l= l[::-1]




for j in l:
	num = int(j)
	if(largePrimes(num, primeList)):
		print num
		break
