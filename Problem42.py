#Coded Triangle Numbers 
def compute(string):
	identity = 0
	for i in range(0,len(string)):

		identity += ord(string[i]) - 64

	return identity



file = open("words.txt")
wordDirectory = []
for line in file:
	wordDirectory = [x[1:-1] for x in line.strip().split(",")]


triangleNumbers = [(x*(x+1))/2 for x in range(1,1000)]

counter = 0 

temp = 0
for x in wordDirectory:
	temp = compute(x)
	if temp in triangleNumbers:
		counter+=1


print "done ", counter
	
