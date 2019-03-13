class Fraction(object):
    def __init__(self, num, den):
        if den == 0:
            raise ValueError('Denominator can not be equal 0')
        self._num = num
        self._den = den

# str
    def __str__(self):
        return str(self._num) + "/" + str(self._den)

# '<'
    def __lt__(self, otherfrac):
        return self._num * otherfrac._den < otherfrac._num * self._den

# '<='
    def __le__(self, otherfrac):
        return self._num * otherfrac._den <= otherfrac._num * self._den

# '>'
    def __gt__(self, otherfrac):
        return not self.__le__(otherfrac)
            # self._num * otherfrac._den > otherfrac._num * self._den

# '>='
    def __ge__(self, otherfrac):
        return not self.__lt__(otherfrac)

# '=='
    def __eq__(self, otherfrac):
        return self._num * otherfrac._den == self._den * otherfrac._num

# '!='
    def __ne__(self, otherfrac):
        return not self.__eq__(otherfrac)

# hash
    def __hash__(self):
        return hash(self._num, self._def)


frac1 = Fraction(int(input('Input numerator of fraction №1: ')), int(input('Input denominat of fraction №1: ')))
frac2 = Fraction(int(input('Input numerator of fraction №2: ')), int(input('Input denominat of fraction №2: ')))

if __name__ == '__main__':

    print('Fraction №1:', frac1)
    print('Fraction №2:', frac2)
    print('Fraction №1 less fraction №2:', frac1.__lt__(frac2))
    print('Fraction №1 less or equal fraction №2:', frac1.__le__(frac2))
    print('Fraction №1 not equal fraction №2:', frac1.__ne__(frac2))
    print('Fraction №1 more fraction №2:', frac1.__gt__(frac2))
    print('Fraction №1 more or equal fraction №2:', frac1.__ge__(frac2))
    print('Fraction №1 equal fraction №2:', frac1.__eq__(frac2))
