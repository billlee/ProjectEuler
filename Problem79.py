f = open('keylog.txt','r')

direct = []
for line in f:
    direct.append(line.strip())


result = [list(direct[0])]
temp = 0
mini = []
for x in direct:
    mini = list(x)
    temp = len(result)
    for y in range(0,temp)):
        if mini[0] in result:
            if mini[1] in result:
                pass
            else:
                if mini[1] > result[y+1]:
                    



print result






























