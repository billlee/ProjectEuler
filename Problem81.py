#!/usr/bin/env python

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


class Node():
    def __init__(self,value,visited=False):
        self.value = value
        self.visited = visited

class Neighbors():
    def __init__(self, x = None, y = None, curr = None):
        self.curr = Node(curr)
        self.x = Node(x)
        self.y = Node(y)

packet = []

def run():
	for i in range(0,80):
	    for j in range(0,80):
	        if (j == 79 & i == 79):
	            print "Done"
	            return 0
	        elif(j == 79):
	            temp = Neighbors(None,newMatrix[i+1][j],newMatrix[i][j])
	            packet.append(temp)
	        elif(i == 79):
	            temp = Neighbors(newMatrix[i][j+1], None, newMatrix[i][j])
	            packet.append(temp)
	        else:
	        	temp = Neighbors(newMatrix[i][j+1],newMatrix[i+1][j],newMatrix[i][j])
	        	packet.append(temp)

run()
total = 0
for every in packet:
    temp = every
    while (temp.curr.visited == False):
        if(temp.x == None & temp.y == None):
            print "Shortest path is ", total
            break
        elif(temp.x == None | (temp.x.value > temp.y.value)):
            temp = temp.y
            total += temp.y.value
        elif(temp.y == None | (temp.y.value > temp.x.value)):
            temp = temp.x
            total += temp.x.value
        

       
