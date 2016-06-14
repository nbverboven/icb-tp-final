import sys
import algos 
import ej1_Fuerza_Bruta as fb
from random import randint
from random import random

# Ordena la lista recibida según el algoritmo descripto por el parámetro
#homónomo.
def listaOrdenadaEnX(lista, algoritmo):
	if algoritmo == "up":
		lista = algos.upSort(lista)
	elif algoritmo == "bubble":
		lista = algos.bubbleSort(lista)
	elif algoritmo == "merge":
		lista = algos.mergeSort(lista)
	elif algoritmo == "quick":
		lista = algos.quickSort(lista)
	else:
		print("Ingrese un algoritmo válido")
	return lista

# Divide la lista en mitades y busca recursivamente la mínima distancia
#dentro de cada una. Luego combina todas las soluciones parciales 
#para encontrar en mínimo global.
def obtenerMinimo(lista):
	if len(lista) <= 4:
		return fb.distanciaMinima(fb.listaDeDist(lista))
	else:
		medio = len(lista) // 2
		izq = lista[:medio]
		der = lista[medio:]
		min_izq = obtenerMinimo(izq)
		min_der = obtenerMinimo(der)
		return combinar(min_izq, min_der, izq, der, min(min_izq, min_der))

# Utiliza la cota para determinar un subconjunto de puntos que se encuentren
#como mucho a esa distancia de la mitad de la lista (entendiendo como lista a
#la union de lista1 y lista2).
# Luego, encuentra la mínima distancia entre dos puntos dentro de ese intervalo
#utilizando fuerza bruta.
# min1: mínima distancia de la mitad izquierda.
# min2: mínima distancia de la mitad derecha.
# lista1: mitad izquierda.
# lista2: mitad derecha.
# cota: mínimo entre min1 y min2.
def combinar(min1, min2, lista1, lista2, cota):
	i = 0
	j = len(lista1)-1
	while i < len(lista2) and (fb.distancia(lista2[i], lista1[j])) <= cota:
		i += 1
	while j >= 0 and (fb.distancia(lista2[0], lista1[j])) <= cota:
		j -= 1
	lista_combinada = lista1[j:] + lista2[:i+1]
	min_lista_combinada = fb.distanciaMinima(fb.listaDeDist(lista_combinada))
	return min(min_lista_combinada, cota)

def distanciaMinimaDyC(a, algoritmo):
	a = listaOrdenadaEnX(a, algoritmo)
	return obtenerMinimo(a)



if __name__ == '__main__':
	lista_prueba = [(random(), random()) for i in range(500)]
	# dist_fub = fb.distanciaMinima(fb.listaDeDist(lista_prueba))
	dist_dyc = distanciaMinimaDyC(lista_prueba, "quick")
	# print("Fuerza Bruta: " + str(dist_fub))
	print("Divide & Conquer: " + str(dist_dyc))
	# print("Mismas distancias: " + str(dist_fub == dist_dyc))