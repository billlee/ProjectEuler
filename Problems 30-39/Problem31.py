#Coin Sums, Problem 31
#It's a pretty slow solution tbh
import time 

t = time.time()

pence = 1
twoPence = 2
fivePence = 5
tenPence = 10
twentyPence = 20
fiftyPence = 50
pound = 100
twoPound = 200

counter = 0
temp = 0


for i in range (0, 201):
	#pence 
	for j in range(0, (200-i)/2 + 1):
		#tP
		
		for k in range(0, (200 - i - (2*j))/5 + 1):
			#fp
		
			for l in range(0, (200 - i - (2*j)-(5*k))/10 + 1):
			
			
				for m in range(0, (200 - i - (2*j)-(5*k)-(l*10))/20 +1):
					
					for n in range(0,(200-i-(2*j)-(5*k)-(l*10)-(20*m))/50 +1):

			

						for o in range(0,(200-i-(2*j)-(5*k)-(l*10)-(20*m)-(50*n))/100 +1):
				

							for p in range(0,(200-i-(2*j)-(5*k)-(l*10)-(20*m)-(50*n)-(100*o))/200 +1):	
								temp = (pence*i) + (twoPence*j) + (fivePence*k) + (tenPence*l) + (twentyPence*m)+ (fiftyPence*n) + (pound*o) + (twoPound*p)
								
								if temp == 200:
									counter += 1


print counter, "\nTime taken :", (time.time()-t), " seconds"