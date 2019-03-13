import unittest
from Week1_1_Liza import Fraction, frac1, frac2

# tests
class SimpleTest(unittest.TestCase):

    def test1(self):
        self.assertNotEqual(frac1, frac2)

    def test2(self):
        self.assertIsNotNone(frac1)
        self.assertIsNotNone(frac2)

    def test3(self):
        self.assertTrue(bool(frac1))
        self.assertTrue(bool(frac2))

    def test4(self):
        frac3 = Fraction(1,2)
        frac4 = Fraction(1,3)
        self.assertNotEqual(frac3, frac4)

    def test5(self):
        frac5 = Fraction(1,2)
        frac6 = Fraction(2,4)
        self.assertEqual(frac5, frac6)

if __name__ == '__main__':
    unittest.main()
