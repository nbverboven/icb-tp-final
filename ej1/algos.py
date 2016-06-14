
#up:

def upSort(a):
	actual = len(a) - 1
	i = 0
	while actual > 0:
		i = maxPos(a, 0, actual)
		a[i], a[actual] = a[actual], a[i]
		actual -= 1
	return a

def maxPos(lista, desde, hasta):
	posicion_del_maximo = desde
	i = desde
	while i < hasta:
		i += 1
		if lista[i][0] >= lista[posicion_del_maximo][0]:
			posicion_del_maximo = i
	return posicion_del_maximo


#bubble:

def bubbleSort(lista):
	intercambiado = True
	n = len(lista)-1
	while n > 0 and intercambiado:
		intercambiado = False
		for j in range(n):
			if lista[j][0] > lista[j+1][0]:
				lista[j], lista[j+1] = lista[j+1], lista[j]
				intercambiado = True
		n -= 1
	return lista


#merge:

def mergeSort(a):
	if len(a) <= 1: 
		return a
	elif len(a) ==2 :
		if a[0][0]>a[1][0]: 
			a[0], a[1] = a[1], a[0]
		return a
	else:
		l1, l2 = partir(a)
		m1 = mergeSort(l1)
		m2 = mergeSort(l2)
		return combinar(m1, m2)

def partir(a):
	mitad = len(a)//2
	return a[:mitad], a[mitad:]

#combinar recibe listas ya ordenadas
def combinar(l1, l2):
	l = []
	i = 0
	j = 0
	while i<len(l1) and j<len(l2):
		if l1[i][0] < l2[j][0]:
			l.append(l1[i])
			i += 1
		else:
			l.append(l2[j])
			j += 1
	if i < len(l1):
		return l + l1[i:]
	else:
		return l + l2[j:]	


#quick:

def quickSort(a):
	if len(a) == 0:
		return []
	else:
		j = 0
		i = 0
		while i < len(a):
			if a[0][0] > a[i][0]:
				j += 1
				a[j], a[i] = a[i], a[j]
			i += 1
		a[0], a[j] = a[j], a[0]
		return quickSort(a[:j]) + [a[j]] + quickSort(a[j+1:])