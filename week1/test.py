import unittest
from fraction import Fraction

class FractionTestCase(unittest.TestCase):

    def test_eq(self):
        f1 = Fraction(1,2)
        f2 = Fraction(2,4)
        self.assertEqual(f1, f2)

    def test_ne(self):
        f1 = Fraction(3,4)
        f2 = Fraction(2,7)
        self.assertNotEqual(f1, f2)

    def test_lt(self):
        f1 = Fraction(-2,3)
        f2 = Fraction(-1,2)
        self.assertLess(f1, f2)

    def test_gt(self):
        f1 = Fraction(4,5)
        f2 = Fraction(1,3)
        self.assertGreater(f1, f2)

    def test_le(self):
        f1 = Fraction(1,2)
        f2 = Fraction(1,2)
        self.assertLessEqual(f1, f2)

    def test_ge(self):
        f1 = Fraction(2,5)
        f2 = Fraction(2,5)
        self.assertGreaterEqual(f1, f2)


if __name__ == '__main__':
    unittest.main()
