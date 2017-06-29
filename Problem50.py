#Problem 50, Consecutive Prime Sum

counter = 0
file = open("500500.txt", "r")

x = []

for item in file:
	if counter > 78497:
		break
	x.append(item.strip())
	counter += 1


file.close()


maximum = 6
temp = 0
j = 0
y = set(x)




while j < len(y):
	temp = 0
	tempLen = 0
	for each in range(0, len(x)):
		if temp > 1000000:
			del x[0]
			j += 1
			break
		elif ((tempLen > maximum) & (str(temp) in y)):
			print tempLen, " whose prime is ", temp, "starting with ", j
			maximum = tempLen
			
		temp += int(x[each])
		tempLen += 1

