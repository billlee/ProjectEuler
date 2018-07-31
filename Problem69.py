# primeList generates a list of prime factors
# for x
def primeList(x): 
    maxima = (x**0.5)
    # finalList = [0]*x
    checkList = [2]
    #this loop generates all the primes factors to test 
    isPrime = True
    for i in range(3, int(maxima) + 1):
        isPrime= True
        if i%2 == 0:
            pass
        else:
            for j in range(2,i):
                if i%j == 0:
                    isPrime = False
            if isPrime:  
                checkList.append(i)

    return checkList 
    #now we have checkList we can iterate over the bigger list 

    # for i in range(2,x+1):
        # if i in checkList:
            # pass
        # else:
            # for j in checkList:
                # if i%j == 0:
                    # isPrime = False
            # if isPrime:
                # finalList.append(i)
    # return checkList


# def recursiveBonanza(primeFactors, x, currentTotient):
    # for i in primeFactors:
        # if i > x:
            # break
        # elif x%i == 0:
            # print(currentTotient)
            # recursiveBonanza(primeFactors, x/i, currentTotient*(i-1))

    # return currentTotient

def totient(x, primeFactors):
    toeShunt = 1
    while x != 1:
        for prime in primeFactors:
            if x%prime == 0:
                x = x/prime
                toeShunt *= prime-1
    return toeShunt



def main():
    primeFactors = primeList(1000000)
    sameThingButSet = set(primeFactors)
    largeTotientRatio = 0
    desiredRatio = 0
    for i in range(2, 1000001):
        if i in sameThingButSet:
            if i/(i-1) > largeTotientRatio:
                largeTotientRatio = i/(i-1)
                desiredRatio = i
        else:
            reduced = i  
            tempList = [x for x in primeFactors if x < int(0.5**i)]
            # need to redo recursiveBonanza
            currentTotient = totient(i,tempList)
            if (i/currentTotient) > largeTotientRatio:
                largeTotientRatio = i/currentTotient
                desiredRatio = i


if __name__=="__main__":
    main()
