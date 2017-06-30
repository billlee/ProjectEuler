#Digit Cancelling Fractions, Problem 33

from fractions import Fraction
#we generate all the baseline fractions 

fractionSet = set()
tens = 0
for i in range(10,100):
	common =  (i%10)
	tens = common*10
	for j in range(tens+1,tens+10):
		if j == int(str(i)[::-1]):
			pass
		else:
			if i < j:
				f = Fraction(i,j)
				if f.numerator == i:
					pass
				elif((i*f.denominator) == (j*f.numerator)):
					if(((i-common)/10 < (j-tens)) & (Fraction((i-common)/10,j-tens) == f)):
						print f ,(i-common)/10,"/",(j-tens), "this is the simplified version"
						fractionSet.add(f)
			else:
				pass











