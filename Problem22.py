file = open("names.txt")
nameDict = []
with file as a:
	for line in a:
		nameDict.append([n[1:-1] for n in line.strip().split(',')])




nameDict = nameDict[0]

xList = sorted(nameDict)

string = ""




finalSum = 0
ctr = 1 
for i in xList: 
	total = 0
	for character in i:
		num = ord(character) - 64
		total += num

	finalSum += (total*ctr)
	ctr += 1


print finalSum




