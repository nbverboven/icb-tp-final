# -*- coding: utf-8 -*-
from __future__ import print_function

UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3

class Rompecabezas(object):
	def __init__(self, width, height, parent=None):
		self.parent = parent

		######################################
		# agregar atributos acá a continuación
		#
		######################################

		_rompecabezas = []
		_ancho = 0
		_alto = 0

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
		lista_aux = []
		try:
			archivo = open(fn, 'r')
		except IOError:
			print("No se pudo abrir el archivo")
		else:
			archivo = open(fn, 'r')
			for fila in archivo.readlines():
				fila.rstrp('\n')
				fila.split('\t')
				for i in fila:
					lista_aux.append(i)
				_rompecabezas.append(fila)
			_ancho = len(_rompecabezas)
			_alto = len(_rompecabezas[0])
			archivo.close()

	def get(self, i, j):
		return str(_rompecabezas[i][j])

	def ancho(self):
		return _ancho

	def alto(self):
		return _alto

	def resuelto(self):
		# TODO: Así como está hace n²+n operaciones.
		# Ver si se puede hacer más eficiente.
		lista_aux = []
		flag = True
		for fila in _rompecabezas:
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
		pass

	def resolver(self, n):
		if self.resuelto():
			return True
		else:
			return False

if __name__ == '__main__':
	# acá pueden completar con algunas pruebas para usar con el intérprete interactivo
	pass
