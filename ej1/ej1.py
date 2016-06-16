import sys
from math import sqrt
import algos
from random import randint
import random
import time


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
 
 
def minimoposta(a):
	if len(a) == 0: 
		return None
	elif len(a) == 1:
		return a[0]
	else:
		i = 0
		j = 0
		while i < len(a) and j < len(a):
			if a[i][2] < a[j][2]:
				j += 1
			else:
				i += 1
		if i < len(a):
			return a[i]
		return a[j]


# Otra implementación de minimoposta.
def minimoPostaaaaa(a):
	if len(a) < 0:
		raise ValueError("La lista debe tener por lo menos un elemento")
	else:
		i = 1
		par_a_min_dist = a[0]
		while i < len(a)-1:
			if par_a_min_dist[2] > a[i][2]:
				par_a_min_dist = a[i]
			i += 1
		return par_a_min_dist[0], par_a_min_dist[1]



def distanciaMinima(a):
	l=listaDeDist(a)
	return minimoposta(l)[0], minimoposta(l)[1]


#div&conquer:

def minimodivconquer(lista, algoritmo):
	string = str(algoritmo)
	if string == "up":
		return conquer(algos.upSort(lista))
	elif string == "bubble":
		return conquer(algos.bubbleSort(lista))
	elif string == "merge":
		return conquer(algos.mergeSort(lista))
	elif string == "quick":
		return conquer(algos.quickSort(lista))
	else:
		raise NameError("Ingrese un algoritmo válido")


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
	if minimoposta(l1) [2] < minimoposta(l2) [2]:
		return minimoposta(l1)
	return minimoposta(l2)

#lista de puntos
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
	
print(time.clock())

if __name__ == '__main__':
	archi = sys.argv[1]
	# lista_prueba = [(randint(0, 30), randint(0, 30)) for i in range(29)]
	# print(distanciaMinima(lista_prueba))
	# lista_prueba1 = [(randint(50, 70), randint(5, 70)) for i in range(69)]
	# print(distanciaMinima(lista_prueba1))

	l=[]
	for i in range(10):
	 	for j in range(2):
	 		l.append((random.random()+i,random.random()+j))
	print(minimodivconquer(l, 'up'))
	print(time.clock())

	l=[]
	for i in range(10):
		for j in range(10):
			l.append((random.random()+i,random.random()+j))
	distanciaMinima(l)
	print(time.clock())

	
def tuplalenytime(f,r):
	l=[]
	for i in range(f):
	 	for j in range(r):
	 		l.append((random.random()+i,random.random()+j))
	minimodivconquer(l, 'up')
	return str(len(l)), str(time.clock())

def listadetuplas(a):
	i=2
	j=2
	l=[]
	while i<a:
		l.append(tuplalenytime(i,j))
		i+=10
		j+=1
	return l



with open(sys.argv[2], 'w') as salida: 
	for i in listadetuplas(100):
		salida.write(','.join(i)+'\n')
