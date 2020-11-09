# Napisać funkcję odwracanie(L, left, right)
# odwracającą kolejność elementów na liście
# od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place).
# Rozważyć wersję iteracyjną i rekurencyjną.



def odwracanie(L,left,right):

	for i in range(round((right-left)/2)):
		
		L[left],L[right] = L[right],L[left]
		left = left + 1
		right = right - 1
	



K = [1,2,3,4,5,6,7]

print(K)

odwracanie(K,1,5)

print(K)
	