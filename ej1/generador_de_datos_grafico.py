import sys
import random
import Fuerza_Bruta_y_DivideConquer
import time



def generar_puntos(n):
	l = []
	for i in range(n):
		l.append((random.random()*10,random.random()*10))
	return l

#genera tuplas del largo de la lista l y tiempo de ejecucion de los distintos programas:

def generar_tupla(l):
	x=time.clock()
	Fuerza_Bruta_y_DivideConquer.distanciaMinima(l)
	y=time.clock()
	Fuerza_Bruta_y_DivideConquer.minimodivconquer(l, 'up')
	z=time.clock()
	Fuerza_Bruta_y_DivideConquer.minimodivconquer(l, 'bubble')
	u=time.clock()
	Fuerza_Bruta_y_DivideConquer.minimodivconquer(l, 'merge')
	g=time.clock()
	Fuerza_Bruta_y_DivideConquer.minimodivconquer(l, 'quick')
	h=time.clock()
	return str(len(l)), str(y-x), str(z-y), str(u-z), str(g-u), str(h-g)

def generar_lista_tuplas(n):
	ln=list(range(10,n,10))
	ls=[]
	i=0
	while i<len(ln):
		x=generar_puntos(ln[i])
		ls.append(generar_tupla(x))
		i+=1
	return ls


with open(sys.argv[1], 'w') as salida: 
	for i in generar_lista_tuplas(700):
		salida.write(','.join(i)+'\n')