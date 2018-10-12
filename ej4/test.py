import unittest
from arbol import Arbol

class TestConstructor(unittest.TestCase):
	def test_cuando_arbol_mal_formado(self):

		with self.assertRaises(TypeError):
			arbol = Arbol(None, Arbol(2), Arbol(3))


class TestIgualdad(unittest.TestCase):
	def test_dos_arboles_iguales_es_true(self):
		arbol = Arbol(1, Arbol(2, Arbol(4), Arbol(5)), Arbol(3, Arbol(6), Arbol(7)))
		otro_arbol = Arbol(1, Arbol(2, Arbol(4), Arbol(5)), Arbol(3, Arbol(6), Arbol(7)))

		self.assertEqual(arbol, otro_arbol)

	def test_dos_arboles_distintos_es_false(self):
		arbol = Arbol(1, Arbol(2, Arbol(4), Arbol(5)), Arbol(3, Arbol(6), Arbol(7)))
		otro_arbol = Arbol(1, Arbol(8, Arbol(9), Arbol(13)), Arbol(23, Arbol(65), Arbol(337)))

		self.assertNotEqual(arbol, otro_arbol)


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

	def test_no_hay_raiz_error(self):
		arbol = Arbol()

		self.assertRaises(AttributeError, arbol.raiz)


class TestIzquierda(unittest.TestCase):
	def test_cuando_rama_izquierda_vacia_error(self):
		arbol = Arbol(1, Arbol(), Arbol(2))

		self.assertRaises(AttributeError, arbol.izquierda)

	def test_rama_izquierda_esperada(self):
		arbol = Arbol(1, Arbol(2, Arbol(4), Arbol(5)), Arbol(3, Arbol(6), Arbol(7)))

		self.assertEqual(arbol.izquierda(), Arbol(2, Arbol(4), Arbol(5)))


class TestDerecha(unittest.TestCase):
	def test_cuando_rama_derecha_vacia_error(self):
		arbol = Arbol(1, Arbol(2), Arbol())

		self.assertRaises(AttributeError, arbol.derecha)

	def test_rama_derecha_esperada(self):
		arbol = Arbol(1, Arbol(2, Arbol(4), Arbol(5)), Arbol(3, Arbol(6), Arbol(7)))

		self.assertEqual(arbol.derecha(), Arbol(3, Arbol(6), Arbol(7)))


class TestFind(unittest.TestCase):
	def test_cuando_arbol_vacio_es_false(self):
		arbol = Arbol()

		self.assertFalse(arbol.find(4))

	def test_cuando_encuentra_elemento_es_true(self):
		arbol = Arbol(2, Arbol(43, Arbol(3), Arbol(56)), Arbol(4))

		self.assertTrue(arbol.find(56))

	def test_cuando_el_elemento_no_esta_es_false(self):
		arbol = Arbol(2, Arbol(43, Arbol(3), Arbol(56)), Arbol(4))		
		
		self.assertFalse(arbol.find(1000))


class TestEspejo(unittest.TestCase):
	def test_espejo_de_arbol_vacio_es_vacio(self):
		arbol = Arbol()

		self.assertEqual(arbol.espejo(), Arbol())

	def test_espejo_no_modifica_arbol(self):
		arbol = Arbol(1, Arbol(2, Arbol(4), Arbol(5)), Arbol(3, Arbol(6), Arbol(7)))
		otro_arbol = arbol.espejo()

		self.assertNotEqual(arbol, otro_arbol)


class TestPreorder(unittest.TestCase):
	def test_preorder_de_arbol_vacio_es_vacio(self):
		arbol = Arbol()

		self.assertEqual(arbol.preorder(), [])

	def test_preorder_esperado(self):
		arbol = Arbol(1, Arbol(2, Arbol(4), Arbol(5)), Arbol(3, Arbol(6), Arbol(7)))

		self.assertEqual(arbol.preorder(), [1, 2, 4, 5, 3, 6, 7])		


class TestPosorder(unittest.TestCase):
	def test_posorder_de_arbol_vacio_es_vacio(self):
		arbol = Arbol()

		self.assertEqual(arbol.posorder(), [])

	def test_posorder_esperado(self):
		arbol = Arbol(1, Arbol(2, Arbol(4), Arbol(5)), Arbol(3, Arbol(6), Arbol(7)))

		self.assertEqual(arbol.posorder(), [7, 6, 3, 5, 4, 2, 1])		


class TestInorder(unittest.TestCase):
	def test_inorder_de_arbol_vacio_es_vacio(self):
		arbol = Arbol()

		self.assertEqual(arbol.inorder(), [])

	def test_inorder_esperado(self):
		arbol = Arbol(1, Arbol(2, Arbol(4), Arbol(5)), Arbol(3, Arbol(6), Arbol(7)))

		self.assertEqual(arbol.inorder(), [4, 2, 5, 1, 6, 3, 7])		


if __name__ == '__main__':
	unittest.main(verbosity=2)
