import itertools


possibleVals = set()

#below performs 9 choose 4 calculations, all possible number configs 
def numberMix(oneThroughNine):
    return itertools.combinations(oneThroughNine,4) 



#below performs 4! calculations, for all possible permutations from numbermix
def permMix(fourLen):
    return itertools.permutations(fourLen)

#here performs the 4^3 = 64 calculations
def operationMix(megaList,y):
    maximal = 0
    maximalList = list()
    for i in y:
        global possibleVals
        possibleVals = set() 
        for j in range(0,24): 
            recursiveOps(megaList[i][j],float(megaList[i][j][0]),1)
        
        
        k = 1;
        chain = 0;
        while(float(k) in possibleVals):
            k+=1;
            chain+=1;
        if (chain > maximal):
            maximal = chain
            maximalList = i;
            print(maximalList, 'ha', chain); 

        if (i == (1,2,5,8)):
            print(chain, "why the hell not");
    return maximalList; 


def recursiveOps(charString,curr,part):
    if len(charString) == 0:
        if (curr >= 0):
            possibleVals.add(curr)
    elif part == 1:
         #addition
        recursiveOps(charString[1:],curr,0)
        #subtraction
        recursiveOps(charString[1:],curr,0)
        #mutliplication

        recursiveOps(charString[1:],curr,0)

        #divison
        recursiveOps(charString[1:],curr,0)

    else:
        #addition
        recursiveOps(charString[1:],curr+float(charString[0]),0)
        #subtraction
        recursiveOps(charString[1:],curr-float(charString[0]),0)
        #mutliplication

        recursiveOps(charString[1:],curr*float(charString[0]),0)

        #divison
        if charString[0] != 0:
            recursiveOps(charString[1:],curr/float(charString[0]),0)


def nonExpressibles():
    pass
# here I should try out combinations that cannot be expressed in natural order


def main():
    x = numberMix([0,1,2,3,4,5,6,7,8,9]);
    y = list(x);
    megaList = dict()
    for i in y:
        megaList[i] = list(permMix(i))
    print(operationMix(megaList,y))
 
if __name__ == "__main__":
    main()
