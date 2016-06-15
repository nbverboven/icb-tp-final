class Arbol(object):
	def __init__(self, elemento=None, izquierda=None, derecha=None):
		self.r = elemento
		self._vacio = True
		if elemento is not None:
			self._vacio = False
			if izquierda:
				self._izquierda = izquierda
			else:
				self._izquierda = Arbol()
			if derecha:
				self._derecha = derecha
			else:
				self._derecha = Arbol()
		else:
			if izquierda is not None or derecha is not None:
				raise TypeError("Árbol mal formado")

	def vacio(self):
		return self._vacio

	def raiz(self):
		if not self._vacio:
			return self.r
		else:
			raise AttributeError("El árbol está vacío")

	def izquierda(self):
		if not self._vacio and not self._izquierda._vacio:
			return self._izquierda
		else:
			raise AttributeError("El árbol no tiene rama izquierda")

	def derecha(self):
		if not self._vacio and not self._derecha._vacio:
			return self._derecha
		else:
			raise AttributeError("El árbol no tiene rama derecha")

	def __eq__(self, otro_arbol):
		if self._vacio and otro_arbol.vacio():
			return True
		elif (self._vacio and not otro_arbol._vacio) or (not self._vacio and otro_arbol._vacio):
			return False
		else:
			return self.r == otro_arbol.r and self._izquierda.__eq__(otro_arbol._izquierda) and self._derecha.__eq__(otro_arbol._derecha)

	def find(self, a):
		if self._vacio:
			return False
		else:
			return self.r == a or self._izquierda.find(a) or self._derecha.find(a)

	def espejo(self):
		if self._vacio:
			return Arbol()
		else:
			return Arbol(self.r, self._derecha.espejo(), self._izquierda.espejo())

	def preorder(self):
		if self._vacio:
			return []
		else:
			return [self.r] + self._izquierda.preorder() + self._derecha.preorder()

	def posorder(self):
		if self._vacio:
			return []
		else:
			return self._derecha.posorder() + self._izquierda.posorder() + [self.r]
	
	def inorder(self):
		if self._vacio:
			return []
		else:
			return self._izquierda.inorder() + [self.r] + self._derecha.inorder()
