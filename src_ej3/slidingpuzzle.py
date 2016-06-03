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

    def update(self):
        if self.parent is not None:
            self.parent.redraw()

    ######################################
    # COMPLETAR LOS MÉTODOS A CONTINUACIÓN
    #
    ######################################

    def cargar(self, fn):
        pass

    def get(self, i, j):
        pass

    def ancho(self):
        pass

    def alto(self):
        pass

    def resuelto(self):
        return True

    def mover(self, direccion):
        pass

    def guardar(self, fn):
        pass

    def resolver(self, n):
        return False

if __name__ == '__main__':
    # acá pueden completar con algunas pruebas para usar con el intérprete interactivo
    pass
