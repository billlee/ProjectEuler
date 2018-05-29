from heapq import heappush,heappop


def traverse(i, j, mat):
	while (i != 79 & j != 79):
		#do stuff 
		pass


w, h = 80, 80
Matrix = [[0 for x in range(w)] for y in range(h)] 

file = open("matrix.txt") 
i = 0 
for line in file:
	Matrix[i] = [n for n in line.strip().split(",")]
	i += 1


w, h = 80, 80
newMatrix = [[0 for x in range(w)] for y in range(h)] 

for i in range(0,80):
	for j in range(0,80):
		newMatrix[i][j] = int(Matrix[i][j])



pq = []

for i in range(0,80):
	for j in range(0,80):
		if (i == 79 & j == 79):
			print "fin"
		elif (j == 79):
			pass
		elif (i == 79):
			pass
		else: 
			#do stuff 





