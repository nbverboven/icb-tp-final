import sys
from math import sqrt
import algos
from random import randint

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

#print(listaDePuntos(archi))

def distancia(punto1, punto2):
	return sqrt( ( abs(punto1[0]-punto2[0]) )**2 + ( abs(punto1[1]-punto2[1]) )**2 )

def listaDeDist(a):
	if len(a) == 0:
		return []
	else:	
		l = []
		i = 1
		while i < len(a):
			l.append(distancia(a[0], a[i]))
			i += 1
		return l + listaDeDist(a[1:])

# print(listaDeDist(lista))

def distanciaMinima(a):
	if len(a) == 0: 
		return None
	elif len(a) == 1:
		return a[0]
	else:	
		mini = distanciaMinima(a[1:])
		if a[0] <= mini:
			return a[0]
		else:
			return mini


if __name__ == '__main__':
	archi = sys.argv[1]
	print(distanciaMinima(listaDeDist(listaDePuntos(archi))))


