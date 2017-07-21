from heapq import heappush,heappop

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



