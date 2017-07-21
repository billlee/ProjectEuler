global wrong
wrong = set()
wrong.add(1)
global y
y = set()
y.add(89)
def eightynine(x):
    global y
    global wrong
    p = set()
    while(x != 89):
        total = 0
        if x == 1: 
            wrong = p|wrong
            return 1
        if x in y:
            return 89
        elif x in wrong:
            return 1
        while(x > 0):
            total += (x%10)*(x%10)
            x /= 10
        
        
        p.add(total)
        x = total
    y = y | p
    return 89

    
counter = 0
for i in range(1, 1000000+1):
    if i in wrong:
        pass
    elif i in y:
        counter += 1 
    elif eightynine(i) == 89:
        counter += 1
    else:
        pass

print counter
