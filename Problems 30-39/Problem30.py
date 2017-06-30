#Digital Fifth Powers, Problem 30

temp = 0
numy = 0 
total = 0


for m in range(0,10):
	for a in range(0,10):
		for b in range(0,10):
			for c in range(0,10):
				for d in range(0,10):
					for e in range(0,10):
						temp = (m**5)+(a**5) + (b**5) + (c**5) + (d**5) + (e**5)
						numy = (m*100000)+(a*10000) + (b*1000) + (c*100) + (10*d) + e
						if temp == numy:
							print temp
							total += temp



print total

