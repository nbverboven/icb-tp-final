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


def distancia(punto1, punto2):
	return sqrt( ( abs(punto1[0]-punto2[0]) )**2 + ( abs(punto1[1]-punto2[1]) )**2 )

def listaDeDist(a):
	if len(a) <= 1:
		return []
	else:	
		l = []
		i = 1
		while i < len(a):
			tupla = (a[0], a[i], distancia(a[0], a[i]))
			l.append(tupla)
			i += 1
		return l + listaDeDist(a[1:])


def minima(a):
	if len(a) == 0: 
		return None
	elif len(a) == 1:
		return a[0]
	else:	
		mini = minima(a[1:])
		#asd = mini[2]
		if a[0][2] <= mini[2]:
			return (a[0][0], a[0][1])
		else:
			return mini[0], mini[1]



def distanciaMinima(a):
	return minima(listaDeDist(a))
	# if len(a)<=1:
	# 	return None
	# else:
	# 	i=1
	# 	while i<len(a) and distancia(a[0], a[i])!= minima(listaDeDist(a)):
	# 		i+=1
	# 	if i<len(a):
	# 		return a[0], a[i]
	# 	else:
	# 		return distanciaMinima(a[1:])

#div&conquer:

def partir(a):
	mitad = len(a)//2
	return a[:mitad], a[mitad:]

def divide(a):
	l1=listaDeDist(partir(a)[0])
	l2=listaDeDist(partir(a)[1])
	return l1, l2
#lista de puntos
def minimodeparticion(a):
	l1, l2=divide(a)
	if minima(l1) < minima(l2):
		return minima(l1)
	return minima(l2)

#lista de puntos
def conquer(a):
	i=len(a)//2
	x=((a[i][0] - a[i-1][0])/2)+a[i-1][0]
	j=0
	l=[]
	while j<len(a):
		if abs(a[j][0]-x)< minimodeparticion(a):
			l.append(a[j])
		j+=1
	if minimodeparticion(a)>=minima(listaDeDist(l)):
		return distanciaMinima(l)
	l1, l2=divide(a)
	if minima(l1) < minima(l2):
		return distanciaMinima(l1)
	return distanciaMinima(l2)


if __name__ == '__main__':
	#archi = sys.argv[1]
	lista_prueba = [(randint(0, 30), randint(0, 30)) for i in range(29)]
	print(distanciaMinima(lista_prueba))

