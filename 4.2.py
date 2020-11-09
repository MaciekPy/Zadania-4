# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
# które zwracają pełny string przez return.

def FLinijka(length):
	#length = input("Podaj długośc linijki : ")
	linijka = []
	for i in range(int(length)):
		linijka.append("|")
		for j in range(4):
			linijka.append(".")

	linijka.append("|")	
	linijka.append("\n")

	for i in range(int(length)+1):
	
		linijka.append(str(i))
		x = 4
		if i > 8:
			x = 3
		for j in range(x):	
			linijka.append(" ")
		
	str1 = "".join(linijka)
	return str1

def FKwadrat():
	kwadrat = []
	for k in range(3):
		for i in range(5):
			kwadrat.append("+")
			for j in range(3):
				kwadrat.append("-")
		kwadrat.append("+")
		kwadrat.append("\n")

		for i in range(5):
			kwadrat.append("|")
			for j in range(3):
				kwadrat.append(" ")
		kwadrat.append("|") 
		kwadrat.append("\n")
	
	for i in range(5):
		kwadrat.append("+")
		for j in range(3):
			kwadrat.append("-")
	kwadrat.append("+")
	kwadrat.append("\n")
		
	str1 = "".join(kwadrat)
	return str1
	

str1 = FLinijka(12)
str2 = FKwadrat()

print(str1 + "\n" + str2 )
