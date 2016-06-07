# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3

class Rompecabezas(object):
	def __init__(self, width, height, parent=None):
		self.parent = parent

		######################################
		# agregar atributos acá a continuación
		#
		######################################

		self._rompecabezas = []
		self._ancho = width
		self._alto = height
		self._espacio_vacio = (0, 0) # (alto, ancho) == (filas, columnas)

	def update(self):
		if self.parent is not None:
			self.parent.redraw()

	######################################
	# COMPLETAR LOS MÉTODOS A CONTINUACIÓN
	#
	######################################

	# TODO: Ver cómo levantar una excepción si el 
	#formato del archivo no es correcto.
	def cargar(self, fn):
		self._rompecabezas = []
		try:
			archivo = open(fn, 'r')
		except IOError:
			raise
		numero_fila = 0
		for fila in archivo.readlines():
			fila = fila.rstrip('\n')
			fila = fila.split('\t')
			for columna in range(len(fila)):
				if fila[columna] == ' ':
					self._espacio_vacio = (numero_fila, columna)
			self._rompecabezas.append(fila)
			numero_fila += 1
		archivo.close()

	# Listo
	def get(self, i, j):
		return self._rompecabezas[i][j]

	# Listo
	def ancho(self):
		return self._ancho

	# Listo
	def alto(self):
		return self._alto

	# TODO: Así como está hace n²+n operaciones.
	# Ver si se puede hacer más eficiente.
	def resuelto(self):
		lista_aux = []
		flag = True
		for fila in self._rompecabezas:
			for columna in fila:
				if columna == ' ':
					lista_aux.append(self._ancho*self._alto)
				else:
					lista_aux.append(int(columna))
		i = 0
		while i < len(lista_aux)-1 and flag:
			if lista_aux[i] > lista_aux[i+1]:
				flag = False 
			i+= 1
		return flag

	# Listo
	def mover(self, direccion):
		intercambio_realizado = False
		pos = self._espacio_vacio
		# Verifico que sea posible mover el espacio vacío en la dirección especificada previo a realizar
		# el intercambio.
		if direccion == 0 and pos[0]-1 >= 0:
			self._rompecabezas[pos[0]][pos[1]], self._rompecabezas[pos[0]-1][pos[1]] = self._rompecabezas[pos[0]-1][pos[1]], ' '
			self._espacio_vacio = (pos[0]-1, pos[1])
			intercambio_realizado = True

		elif direccion == 1 and pos[1]-1 >= 0:
			self._rompecabezas[pos[0]][pos[1]], self._rompecabezas[pos[0]][pos[1]-1] = self._rompecabezas[pos[0]][pos[1]-1], ' '
			self._espacio_vacio = (pos[0], pos[1]-1)
			intercambio_realizado = True

		elif direccion == 2 and pos[0]+1 < self._alto:
			self._rompecabezas[pos[0]][pos[1]], self._rompecabezas[pos[0]+1][pos[1]] = self._rompecabezas[pos[0]+1][pos[1]], ' '
			self._espacio_vacio = (pos[0]+1, pos[1])
			intercambio_realizado = True

		elif direccion == 3 and pos[1]+1 < self._ancho:
			self._rompecabezas[pos[0]][pos[1]], self._rompecabezas[pos[0]][pos[1]+1] = self._rompecabezas[pos[0]][pos[1]+1], ' '
			self._espacio_vacio = (pos[0], pos[1]+1)
			intercambio_realizado = True

		return intercambio_realizado		

	# Listo
	def guardar(self, fn):
		archivo = open(fn, 'w')
		for fila in range(len(self._rompecabezas)):
			archivo.write('	'.join(self._rompecabezas[fila]) + '\n')
		archivo.close()

	def resolver(self, n):
		if self.resuelto() and n >= 0:
			return True
		else:
			return False

if __name__ == '__main__':
	# acá pueden completar con algunas pruebas para usar con el intérprete interactivo
	x = Rompecabezas(4, 4)
	x.cargar('puzzle2.txt')
	print(x._rompecabezas)
	print(x.resuelto())
	x.resolver(455)