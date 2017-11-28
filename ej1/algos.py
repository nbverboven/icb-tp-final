from random import randint

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
def partition(array, begin, end):
	pivot = randint(begin, end)
	array[pivot], array[end] = array[end], array[pivot]
	i = begin -1
	for j in range(begin, end):
		if array[j] <= array[end]:
			i += 1
			array[i], array[j] = array[j], array[i]
	array[i+1], array[end] = array[end], array[i+1]
	return i + 1

def quickSort(array, begin=0, end=None):
	if end is None:
		end = len(array) - 1
	def _quickSort(array, begin, end):
		if begin >= end:
			return
		pivot = partition(array, begin, end)
		_quickSort(array, begin, pivot-1)
		_quickSort(array, pivot+1, end)
	_quickSort(array, begin, end)
	return array
