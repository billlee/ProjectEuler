import time
t = time.time()
x = 7830457
y = 2 
total = 1
maximum = 10**10
for i in range(1,x+1):
    total *= 2
    if (total > 10**10):
        total = total%(10**10)



total = total%(10**10)
total = (total*28433)%(10**10)

total += 1


print total, "The total time it has taken: ", time.time()-t , " seconds" 
