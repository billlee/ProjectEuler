import itertools 

string =  "0123456789"
permutz =  list(map("".join, itertools.permutations(string)))

ctr = 1

for i in permutz:
	if ctr == 1000000:
		print i
		break
	ctr +=1
