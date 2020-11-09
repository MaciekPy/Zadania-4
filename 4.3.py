# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def iterFactorial(x):
	
	if x == 0:
		return 1
	elif x == 1:
		return 1
	else:
		sum = 1 
		for i in range(x):
			sum = sum * (i+1)
		return sum
		
		

sil1 = iterFactorial(0)
sil2 = iterFactorial(1)
sil3 = iterFactorial(2)
sil4 = iterFactorial(4)
sil5 = iterFactorial(12)

print(sil1)
print(sil2)
print(sil3)
print(sil4)
print(sil5)

