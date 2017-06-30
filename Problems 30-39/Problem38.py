#Pandigital Multiples, Problem 38
#upper limit to check must be less than 9876

import itertools 

x = "123456789"
permutz = set(map("".join, itertools.permutations(x)))
solution = []

string = ""
for i in range(2,9877):
	n = 1 
	while len(string) < 6:
		string += str(i*n)
		n += 1

	print len(string)
	if string in permutz:
		solution.append(string)

	string = ""

print max(solution)