
x = ""
total = 0
for i in range(1,1000000):
	x = str(i)
	y = str(bin(i))
	y = y[2::]
	if(x == x[::-1]) & (y == y[::-1]):
		total += i

print total

