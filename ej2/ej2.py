def subListaAsc(a, n):
	i = 0
	while i < len(a) and not sufijoSubAscN(a, i, n):
		i += 1
	return i < len(a)

def sufijoSubAscN(a, i, n):
 	j = i
 	tamano = 1
 	while j < len(a)-1 and a[j] < a[j+1]:
 		j += 1
 		tamano += 1
 	return tamano >= n
