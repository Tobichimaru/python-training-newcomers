import unittest

class Fraction(object):
    def __init__(self, num, den):
        self._num = num
        self._den = den

    # @property
    # def num(self):
    #     return self._num
    #
    # @property
    # def den(self):
    #     return self._den
# str
    def __str__(self):
        return str(self._num) + "/" + str(self._den)

# '<'
    def __lt__(self, otherfrac):
        if self._num * otherfrac._den < otherfrac._num * self._den:
            return True
        else:
            return False

# '<='
    def __le__(self, otherfrac):
        if self._num * otherfrac._den <= otherfrac._num * self._den:
            return True
        else:
            return False

# '>'
    def __gt__(self, otherfrac):
        if self._num * otherfrac._den > otherfrac._num * self._den:
            return True
        else:
            return False

# '>='
    def __ge__(self, otherfrac):
        if self._num * otherfrac._den >= otherfrac._num * self._den:
            return True
        else:
            return False

# '!='
    def __ne__(self, otherfrac):
        if self._num * otherfrac._den != otherfrac._num * self._den:
            return True
        else:
            return False

# '=='
    def __eq__(self, otherfrac):
        return self._num * otherfrac._den == self._den * otherfrac._num

# hash
    def __hash__(self):
        return hash(self._num, self._def)


n1 = int(input('Input numerator of fraction №1: '))
d1 = int(input('Input denominat of fraction №1: '))
frac1 = Fraction(n1, d1)
n2 = int(input('Input numerator of fraction №2: '))
d2 = int(input('Input denominat of fraction №2: '))
frac2 = Fraction(n2, d2)


# test denominator != 0
class SimpleTest(unittest.TestCase):
    def test0(self):
        self.assertNotEqual(d1, 0)
        self.assertNotEqual(d2, 0)

print('Fraction №1:', frac1)
print('Fraction №2:', frac2)
print('Fraction №1 less fraction №2:', frac1.__lt__(frac2))
print('Fraction №1 less or equal fraction №2:', frac1.__le__(frac2))
print('Fraction №1 not equal fraction №2:', frac1.__ne__(frac2))
print('Fraction №1 more fraction №2:', frac1.__gt__(frac2))
print('Fraction №1 more or equal fraction №2:', frac1.__ge__(frac2))
print('Fraction №1 equal fraction №2:', frac1.__eq__(frac2))

if __name__ == '__main__':
    unittest.main()


