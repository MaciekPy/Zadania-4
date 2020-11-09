# Napisać iteracyjną wersję funkcji fibonacci(n)
# obliczającej n-ty wyraz ciągu Fibonacciego.

def Fibonaci(Fn):
	if Fn == 0:
		return 0
	elif Fn == 1:
		return 1
	else:
		F1 = 0
		F2 = 1
		m = 0
		for i in range(Fn-1):
			m = F1 + F2
			F1 = F2
			F2 = m
		return m


Fib1 = Fibonaci(0)
Fib2 = Fibonaci(1)
Fib3 = Fibonaci(3)
Fib4 = Fibonaci(5)
Fib5 = Fibonaci(10)

print(Fib1)
print(Fib2)
print(Fib3)
print(Fib4)
print(Fib5)
