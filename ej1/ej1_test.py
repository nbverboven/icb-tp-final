import unittest
from ej1 import combinar

class CombinarTest(unittest.TestCase):
	def test_dos_listas_misma_longitud_una_menor_que_la_otra(self):
		l1 = [1, 2]
		l2 = [3, 4]

		self.assertEqual(combinar(l1, l2), [1, 2, 3, 4])

class MergeSortTest(unittest.TestCase):
	pass


if __name__ == '__main__':
	unittest.main()