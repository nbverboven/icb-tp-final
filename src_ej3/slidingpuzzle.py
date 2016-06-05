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

	def update(self):
		if self.parent is not None:
			self.parent.redraw()

	######################################
	# COMPLETAR LOS MÉTODOS A CONTINUACIÓN
	#
	######################################

	def cargar(self, fn):
		# TODO: Ver cómo levantar una excepción si el 
		#formato del archivo no es correcto.
		
		# try:
		# 	archivo = open(fn, 'r')
		# 	self._ancho == self._alto
		# except IOError:
		# 	print("No se pudo abrir el archivo")
		# else:
		self._rompecabezas = []
		archivo = open(fn, 'r')
		for fila in archivo.readlines():
			# lista_aux = fila
			lista_aux = []
			fila = fila.rstrip('\n')
			fila = fila.split('\t')
			for i in fila:
				lista_aux.append(i)
			self._rompecabezas.append(lista_aux)
		archivo.close()

	def get(self, i, j):
		return str(self._rompecabezas[i][j])

	def ancho(self):
		return self._ancho

	def alto(self):
		return self._alto

	def resuelto(self):
		# TODO: Así como está hace n²+n operaciones.
		# Ver si se puede hacer más eficiente.
		lista_aux = []
		flag = True
		for fila in self._rompecabezas:
			for columna in fila:
				lista_aux.append(columna)
		if lista_aux[0] == ' ':
			flag = False
		i = 0
		while i < len(lista_aux)-1 and flag:
			if lista_aux[i] > lista_aux[i+1]:
				flag = False 
			i+= 1
		return flag

	def mover(self, direccion):
		pass

	def guardar(self, fn):
		archivo = open(fn, 'w')
		for fila in range(len(self._rompecabezas)):
			archivo.write('	'.join(self._rompecabezas[fila]) + '\n')
		archivo.close()

	def resolver(self, n):
		if self.resuelto():
			return True
		else:
			return False

if __name__ == '__main__':
	# acá pueden completar con algunas pruebas para usar con el intérprete interactivo
	x = Rompecabezas(4, 4)
	x.cargar('puzzle4.txt')
	print(x._rompecabezas)
	x.guardar('puzzle4_pruebita.txt')
