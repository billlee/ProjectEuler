#Problem 34, Digital Factorials
import math
import time

t = time.time()

global m 
m = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def facDigSum(x):
	x  = list(x)
	total = 0 
	for i in x:
		total += m[int(i)]

	return total

temp = 0
totality = 0 
for i in range(3, 1000000):
	temp = facDigSum(str(i))
	if temp == i:
		totality += temp



print totality, "\nTime taken: ", time.time()-t, " seconds " 
