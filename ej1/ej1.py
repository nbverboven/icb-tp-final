import sys
from math import sqrt
import algos
from random import randint
import random
import time
# import tiempodeup

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


def generar_puntos(n):
	l = []
	for i in range(n):
		l.append((random.random()*10,random.random()*10))
	return l

def generar_lista_tuplas(n):
	ln=list(range(10,n,10))
	ls=[]
	i=0
	while i<len(ln):
		x=generar_puntos(ln[i])
		ls.append(generar_tupla(x))
		i+=1
	return ls

def generar_tupla(l):
	x=time.clock()
	distanciaMinima(l)
	y=time.clock()
	minimodivconquer(l, 'up')
	z=time.clock()
	minimodivconquer(l, 'bubble')
	u=time.clock()
	minimodivconquer(l, 'merge')
	g=time.clock()
	minimodivconquer(l, 'quick')
	h=time.clock()
	return str(len(l)), str(y-x), str(z-y), str(u-z), str(g-u), str(h-g)


with open(sys.argv[2], 'w') as salida: 
	for i in generar_lista_tuplas(700):
		salida.write(','.join(i)+'\n')


