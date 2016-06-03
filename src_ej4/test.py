import unittest
from arbol import Arbol

class TestConstructor(unittest.TestCase):
    def test_cuando_arbol_mal_formado(self):
        pass


class TestVacio(unittest.TestCase):
    def test_cuando_arbol_vacio_es_true(self):
        arbol = Arbol()

        self.assertTrue(arbol.vacio())

    def test_cuando_arbol_no_vacio_es_false(self):
        arbol = Arbol(2)

        self.assertFalse(arbol.vacio())

class TestRaiz(unittest.TestCase):
    def test_devuelve_la_raiz(self):
        arbol = Arbol(2)

        self.assertEqual(arbol.raiz(), 2)


if __name__ == '__main__':
    unittest.main()
