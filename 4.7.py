# Mamy daną sekwencję, w której niektóre z elementów 
# mogą okazać się podsekwencjami, a takie zagnieżdżenia
# mogą się nakładać do nieograniczonej głębokości.
# Napisać funkcję flatten(sequence),
# która zwróci spłaszczoną listę wszystkich elementów sekwencji.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie
# czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).


def flatten(sequence,L):

	length = len(sequence)
	
	for i in range(length):
		if isinstance(sequence[i],(list,tuple)):
			flatten(sequence[i],L)
		else:
			L.append(sequence[i])
			
	


L = []
seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

flatten(seq,L)

print(str(L))