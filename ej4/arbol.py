##
# Clase que implementa un árbol binario.
# Sus atributos consisten en una raíz, un subárbol derecho,
# un subárbol izquierdo y un booleano que indica si está 
# vacío o no.
##
class Arbol(object):

	##
	# Constructor
	##
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

	##
	# Devuelve true si el árbol está vacío
	##
	def vacio(self):
		return self._vacio

	##
	# Devuelve la raíz del árbol si este no es vacío
	##
	def raiz(self):
		if not self._vacio:
			return self.r
		else:
			raise AttributeError("El árbol está vacío")

	##
	# Devuelve el subárbol izquierdo si este existe
	##
	def izquierda(self):
		if not self._vacio and not self._izquierda._vacio:
			return self._izquierda
		else:
			raise AttributeError("El árbol no tiene rama izquierda")

	##
	# Devuelve el subárbol derecho si este existe
	##
	def derecha(self):
		if not self._vacio and not self._derecha._vacio:
			return self._derecha
		else:
			raise AttributeError("El árbol no tiene rama derecha")

	##
	# Método que define la igualdad entre dos árboles
	##
	def __eq__(self, otro_arbol):
		if self._vacio and otro_arbol.vacio():
			return True
		elif (self._vacio and not otro_arbol._vacio) or (not self._vacio and otro_arbol._vacio):
			return False
		else:
			return self.r == otro_arbol.r and self._izquierda.__eq__(otro_arbol._izquierda) and self._derecha.__eq__(otro_arbol._derecha)

	##
	# Devuelve True si el elemento a se encuentra en el árbol y False en caso contrario
	##
	def find(self, a):
		if self._vacio:
			return False
		else:
			return self.r == a or self._izquierda.find(a) or self._derecha.find(a)

	##
	# Devuelve un nuevo árbol con los elementos espejados con respecto a self
	##
	def espejo(self):
		if self._vacio:
			return Arbol()
		else:
			return Arbol(self.r, self._derecha.espejo(), self._izquierda.espejo())

	##
	# Devuelve el preorder del árbol
	##
	def preorder(self):
		if self._vacio:
			return []
		else:
			return [self.r] + self._izquierda.preorder() + self._derecha.preorder()

	##
	# Devuelve el posorder del árbol
	##
	def posorder(self):
		if self._vacio:
			return []
		else:
			return self._derecha.posorder() + self._izquierda.posorder() + [self.r]
	
	##
	# Devuelve el inorder del árbol
	##
	def inorder(self):
		if self._vacio:
			return []
		else:
			return self._izquierda.inorder() + [self.r] + self._derecha.inorder()
