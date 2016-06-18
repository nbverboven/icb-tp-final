# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3

class Rompecabezas(object):

	###############################
	# Métodos públicos
	###############################

	def __init__(self, width, height, parent=None):
		self.parent = parent

		self._rompecabezas = []
		self._ancho = width
		self._alto = height
		self._espacio_vacio = (0, 0) # (alto, ancho) == (filas, columnas)


	def update(self):
		if self.parent is not None:
			self.parent.redraw()


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
					fila[columna] = self._ancho * self._alto
					self._espacio_vacio = (numero_fila, columna)
				else:
					fila[columna] = int(fila[columna])

			self._rompecabezas.append(fila)
			numero_fila += 1

		if len(self._rompecabezas) != self._alto or len(self._rompecabezas[0]) != self._ancho:
			raise IOError("Formato incorrect de archio")
		archivo.close()

	def __str__(self):
		pass

	# Listo
	def get(self, i, j):
		return self._rompecabezas[i][j]

	# Listo
	def ancho(self):
		return self._ancho

	# Listo
	def alto(self):
		return self._alto


	def resuelto(self):
		lista_aux = self._unirListas(self._rompecabezas)
		return sorted(lista_aux) == lista_aux

	# Listo
	def mover(self, direccion):
		intercambio_realizado = False
		pos = self._espacio_vacio
		# Verifico que sea posible mover el espacio vacío en la dirección especificada previo a realizar
		# el intercambio.
		if direccion == 0 and pos[0]-1 >= 0:
			self._rompecabezas[pos[0]][pos[1]], self._rompecabezas[pos[0]-1][pos[1]] = self._rompecabezas[pos[0]-1][pos[1]], self._rompecabezas[pos[0]][pos[1]]
			self._espacio_vacio = (pos[0]-1, pos[1])
			intercambio_realizado = True

		elif direccion == 1 and pos[1]-1 >= 0:
			self._rompecabezas[pos[0]][pos[1]], self._rompecabezas[pos[0]][pos[1]-1] = self._rompecabezas[pos[0]][pos[1]-1], self._rompecabezas[pos[0]][pos[1]]
			self._espacio_vacio = (pos[0], pos[1]-1)
			intercambio_realizado = True

		elif direccion == 2 and pos[0]+1 < self._alto:
			self._rompecabezas[pos[0]][pos[1]], self._rompecabezas[pos[0]+1][pos[1]] = self._rompecabezas[pos[0]+1][pos[1]], self._rompecabezas[pos[0]][pos[1]]
			self._espacio_vacio = (pos[0]+1, pos[1])
			intercambio_realizado = True

		elif direccion == 3 and pos[1]+1 < self._ancho:
			self._rompecabezas[pos[0]][pos[1]], self._rompecabezas[pos[0]][pos[1]+1] = self._rompecabezas[pos[0]][pos[1]+1], self._rompecabezas[pos[0]][pos[1]]
			self._espacio_vacio = (pos[0], pos[1]+1)
			intercambio_realizado = True

		return intercambio_realizado		


	def guardar(self, fn):
		archivo = open(fn, 'w')
		for fila in range(len(self._rompecabezas)):
			archivo.write('	'.join(self._rompecabezas[fila]) + '\n')
		archivo.close()


	def resolver(self, n):
		print(n)
		pos = self._espacio_vacio
		if self.resuelto() and n >= 0:
			return True

		elif n < 0:
			return False

		else:
			if pos[0]-1 >= 0:
				self.mover(UP)
				if self.resolver(n-1):
					return True
				self.mover(DOWN)

			if pos[1]-1 >= 0:
				self.mover(LEFT)
				if self.resolver(n-1):
					return True
				self.mover(RIGHT)

			if pos[0]+1 < self._alto:
				self.mover(DOWN)
				if self.resolver(n-1):
					return True
				self.mover(UP)

			if pos[1]+1 < self._ancho:
				self.mover(RIGHT)
				if self.resolver(n-1):
					return True
				self.mover(LEFT)

			return False

			
	###############################
	# Métodos privados
	###############################

	def _unirListas(self, lista_de_listas):
		lista_aux = []
		for fila in lista_de_listas:
			lista_aux.extend(fila)
		return lista_aux



if __name__ == '__main__':
	# acá pueden completar con algunas pruebas para usar con el intérprete interactivo
	x = Rompecabezas(4, 4)
	x.cargar('puzzle2.txt')
	print(x._rompecabezas)
	print(x._unirListas(x._rompecabezas))
	print(x.resuelto())
	x.resolver(5)
	print(x._rompecabezas)