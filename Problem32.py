#Problem 32, Pandigital Products 

import itertools 
import time 


t = time.time()

def stripper(s):
	temp = sorted(s)
	father = set(['1','2','3','4','5','6','7','8','9'])	
	for i in temp:
		if i in father:
			father.remove(i)
	return "".join(father)



oneLen =  set(['2','3','4','5','6','7','8','9'])
twoLen =  set(map("".join, itertools.permutations("123456789",2)))
fourLen = set(map("".join, itertools.permutations("123456789",4)))


temp2 = 0
temp3 = 0 
res = ""
total = set()


# all possible combinations are (1,4,4)(2,3,4)

for i in twoLen:

	x = stripper(i)
	miniList = set(map("".join, itertools.permutations(x,3)))
	for j in miniList:
		y = stripper(i+j)
		nextList = set(map("".join, itertools.permutations(y,4)))
		if str(int(i)*int(j)) in nextList:
			total.add(int(i)*int(j))




for i in oneLen:
	x = stripper(i)
	miniList = set(map("".join, itertools.permutations(x,4)))
	for j in miniList:
		y=  stripper(i+j)
		nextList = set(map("".join, itertools.permutations(y,4)))
		if str(int(i)*int(j)) in nextList:
			total.add(int(i)*int(j))


totality = 0 
for i in total:
	totality += i

print totality, "\nTime taken : ", time.time()-t, " seconds"

