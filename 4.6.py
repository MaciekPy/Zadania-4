# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb
# zawartych w sekwencji, która może zawierać zagnieżdżone
# podsekwencje. Wskazówka: rozważyć wersję rekurencyjną,
# a sprawdzanie, czy element jest sekwencją,
# wykonać przez isinstance(item, (list, tuple)).

def sum_seq(sequence):
	length = len(sequence)
	sum = 0
	for i in range(length):
		if isinstance(sequence[i],(list,tuple)):
			sum = sum + sum_seq(sequence[i])
		else:
			sum = sum + sequence[i]	
			
	return sum


seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

sum1 = sum_seq(seq)

print(sum1)