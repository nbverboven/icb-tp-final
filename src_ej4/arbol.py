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
                raise TypeError("arbol mal formado")

    def vacio(self):
        return self._vacio

    def raiz(self):
        try:
            return self.r
        except AttributeError:
            raise AttributeError("El árbol está vacío")

    def izquierda(self):
        if self._izquierda is not None:
            return self._izquierda
        else:
            raise AttributeError("El árbol no tiene rama izquierda")

    def derecha(self):
        try:
            return self._derecha
        except AttributeError:
            raise AttributeError("El árbol no tiene rama derecha")

    def __eq__(self, otro_arbol):
        if self._vacio and otro_arbol.vacio():
            return True
        elif (self._vacio and not otro_arbol.vacio()) or (not self._vacio and otro_arbol.vacio()):
            return False
        else:
            return self.r == otro_arbol.raiz() and self._izquierda.__eq__(otro_arbol.izquierda()) and self._derecha.__eq__(otro_arbol.derecha())

    def find(self, a):
        return (not self._vacio) and (self.r == a or (self._izquierda.find(a)) or (self._derecha.find(a)))

    def inorder(self):
        if self._vacio:
            return []
        else:
            return self._izquierda.inorder() + [self.r] + self._derecha.inorder()