import time
t= time.time()
def abundancy(x): 
	sum = 1
	cap = int(x**0.5)
	for i in range(2,cap+1):
		if(x%i == 0):
			sum  += (i+(x/i))
			if(x/i == i):
				sum -= i
	return sum 



startingVal = 0 


abundantNumbers = [x for x in range(12, 28124) if (abundancy(x) > x)]
abundantSet = set(abundantNumbers)






for i in range(1, 28124):
	for j in abundantNumbers:
		temp = i - j 
		if temp < 12:
			startingVal += i
			break
		elif temp in abundantSet:
			break



print startingVal, "\n", time.time()-t
