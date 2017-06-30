import itertools
def prime(a):
	for x in range(2,101):
		if(a%x == 0):
			return False

	return True



def main():
	myList = [x for  x in range(1000, 10000) if prime(x)]



	newList = []
	for x in myList: 
		newList.append(str(x))

	newList = set(newList)

	counter = 0
	listx = []
	masterList = []

	for x in newList:	
		l = list(map("".join, itertools.permutations(x)))
		for y in l:
		 	if y in newList:
		 		counter += 1
			if counter > 6:
				listx = [x for x in l if (x in newList)]
				listx = list(set(listx))
				masterList.append(listx)
				
		counter = 0
	


	for x in masterList:
		for y in x:
			if (str(int(y)+3330) in x) & ((str(int(y)+6660) in x)): 
				print x , " and the number is ", y



if __name__ == "__main__":
	main()