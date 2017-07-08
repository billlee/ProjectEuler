def isPalindrome(s):
    return (s == s[::-1])



counter = 0
temp = 0
temp2 = 0
for i in range(2,10001):
    temp = i
    for j in range(0,50):
        temp2 = int(str(temp)[::-1])
        temp = temp2 + temp
        if (isPalindrome(str(temp))):
            break
        elif(j == 49):
            counter += 1
    

print counter 

