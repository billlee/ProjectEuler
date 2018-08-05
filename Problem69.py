import time

totientDict = dict()

def primeMaker(x):
    "all primes under x" 
    directory = [2]
    isPrime = True
    for i in range(2,x):
        y = int(i**0.5)+1
        isPrime = True
        if i%2 == 0:
            pass
        else:
            for j in range(3, y, 2):
                if i%j == 0:
                    isPrime = False
                    break
            if(isPrime):
                directory.append(i)

    return directory

def totient(number, pVals, pValsChecker):
    global totientDict
    isPrime = True
    if number in pVals:
        totientDict[number] *= (1 - (1/number))
        return 0
    # for i in pValsChecker:
        # if number%i == 0:
            # isPrime = False
            # break
    # if isPrime:
        # totientDict[number] *= (1-(1/number))
        # return 0
    
    nummy = number
    while nummy != 1:
        if number == 2018:
            print(nummy)
        for i in pValsChecker:
           if nummy%i == 0:
               nummy /= i
               totientDict[number] *= (1 - (1/i))
               while(nummy%i == 0):
                   nummy /= i
               break
    return 0 

def main():
    global totientDict
    t0 = time.time()
    print("hello")
    # Hashing Procedure
    keys = range(1000000)
    totientDict = dict(zip(keys,keys))
    pValsChecker = primeMaker(1000000)
    pVals = set(pValsChecker)
    desiredval = 0 
    n = 0
    for number in range(2,1000000):
        totient(number, pVals, pValsChecker)
        print(number, totientDict[number])
        if(number/totientDict[number] > desiredval):
            n = number
            desiredval = number/totientDict[number]
    print("total time: ", time.time()-t0)
    print("answer is ", n, desiredval)


if __name__ == "__main__":
    main()
