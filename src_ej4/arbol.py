class Arbol(object):
    def __init__(self, elemento=None, izquierda=None, derecha=None):
        self.r = elemento
        if elemento is not None:
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
