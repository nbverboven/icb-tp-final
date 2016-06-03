import sys
from math import sqrt

archi = sys.argv[1]

def listaDePuntos(archi):
	f = open(archi,'r')
	lista = []
	for fila in f.readlines():
		fila = fila.rstrip('\n')
		fila = fila.split()
		for i in range(len(fila)):
			fila[i] = float(fila[i])
		lista.append(tuple(fila))
	f.close()
	return lista

# print(lista)

def distancia(punto1, punto2):
	return sqrt( ( abs(punto1[0]-punto2[0]) )**2 + ( abs(punto1[1]-punto2[1]) )**2 )

def listaDeDist(a):
	if len(a) == 1:
		return [0.0]
	else:	
		l = []
		i = 1
		while i < len(a):
			l.append(distancia(a[0], a[i]))
			i += 1
		return l + listaDeDist(a[1:])

# print(listaDeDist(lista))

def distanciaMinima(a):
	if len(a) == 1:
		return a[0]
	else:	
		mini = distanciaMinima(a[1:])
		if a[0] <= mini:
			return a[0]
		else:
			return mini

print(distanciaMinima(listaDeDist(listaDePuntos(archi))))

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
		if lista[i] >= lista[posicion_del_maximo]:
			posicion_del_maximo = i
	return posicion_del_maximo

# def maxpos(a,pos):
# 	return maxx(a[:pos+1])

# def maxx(a):
# 	i = 0 
# 	maxi = None 
# 	maxposi = None
# 	while i<len(a):
# 		if not(maxi) or maxi[0]<a[i][0]:
# 			maxposi = i
# 			maxi = a[i]
# 		i += 1
# 	return maxposi

def bubbleSort(lista):
	intercambiado = True
	n = len(lista)-1
	while n > 0 and intercambiado:
		intercambiado = False
		for j in range(n):
			if lista[j] > lista[j+1]:
				lista[j], lista[j+1] = lista[j+1], lista[j]
				intercambiado = True
		n -= 1
	return lista


# print(maxx(lista))
# print(upSort(lista))





