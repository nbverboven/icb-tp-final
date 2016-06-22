import sys
from math import sqrt
import algos
import random
import time

#lee una archivo de texto y devuelve la lista de puntos:
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


# es una lista cuyos elementos son tuplas donde se guardan pares de puntos y la distancia entre ambos:
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
 
# devuelve el elemento de listadedist cuya distancia sea minima:
def minimoposta(a):
	if len(a)==0: 
		return None
	elif len(a)==1:
		return a[0]
	else:
		i=0
		j=0
		while i<len(a) and j<len(a):
			if a[i][2]<a[j][2]:
				j+=1
			else:
				i+=1
		if i<len(a):
			return a[i]
		return a[j]

#devuelve los puntos que tiene la distancia minima entre ellos:
def distanciaMinima(a):
	l=listaDeDist(a)
	return minimoposta(l)[0], minimoposta(l)[1]


#div&conquer:


def minimodivconquer(lista, algoritmo):
	if len(lista)<=4:
		return distanciaMinima(lista)
	elif algoritmo == "up":
		return conquer(algos.upSort(lista))
	elif algoritmo == "bubble":
		return conquer(algos.bubbleSort(lista))
	elif algoritmo == "merge":
		return conquer(algos.mergeSort(lista))
	elif algoritmo == "quick":
		return conquer(algos.quickSort(lista))
	else:
		raise NameError


def partir(a):
	mitad = len(a)//2
	return a[:mitad], a[mitad:]

def divide(a):
	l1=listaDeDist(partir(a)[0])
	l2=listaDeDist(partir(a)[1])
	return l1, l2

#devuelve el elemento (dos puntos y su distancia) cuya distancia es minima si partimos la lista d epuntos en 2:
def minimodeparticion(a):
	l1, l2=divide(a)
	if minimoposta(l1) [2] < minimoposta(l2) [2]:
		return minimoposta(l1)
	return minimoposta(l2)

#toma la distancia de minimodeparticion y lo usa como cota en el eje x, los puntos cuya distancia es menor van a una lista de puntos y se calcula su distancia, devuelve la distancia minima de la lista: 
def conquer(a):
	i=len(a)//2
	x=((a[i][0] - a[i-1][0])/2)+a[i-1][0]
	j=0
	l=[]
	mini= minimodeparticion(a)
	while j<len(a):
		if abs(a[j][0]-x)< mini[2]:
			l.append(a[j])
		j+=1
	if len(l)>0:
		mi=minimoposta(listaDeDist(l))
		if mini[2] >= mi[2]:
			return mi[0], mi[1]
	return mini[0],mini[1]
	


if __name__ == '__main__':
	archi = sys.argv[1]


