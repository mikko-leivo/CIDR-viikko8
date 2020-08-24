import unittest
from src.calculator import summa as plus

class TestSumma(unittest.TestCase):
    def test_summa(self):
        result = plus(2,3)
        self.assertEqual(result, 5)

    def test_summa_neg(self):
        result = plus(-2,-3)
        self.assertEqual(result, -5)

    def test_floats(self):
        result =plus(3.4, 3.5)
        self.assertAlmostEqual(result, 6.9)

    def test_with_letters(self):
        with self.assertRaises(TypeError):
            plus("a", 0)