#Powerful digit sum, Problem 56

def digitsum(x):
	return sum(map(int,str(x)))

temp = 0
top = 0
large = 0


for i in range(80,100):
	for j in range(80,100):
		large = i**j
		temp = digitsum(large)
		if temp > top:
			top = temp
			


print top