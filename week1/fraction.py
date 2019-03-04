class Fraction:
    def __init__(self, top, bottom):
       if bottom == 0:
           raise ValueError("denominator can not be 0")
       else:

        self.num = top
        self.den = bottom

    def __hash__(self):
        return hash(self.num/self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum >= secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum != secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum <= secondnum

if __name__ == "__main__":

    x = Fraction(1,2)
    y = Fraction(2,3)
    print(x >= y)
    print(x == y)
    print(str(x))

    z = Fraction(2,4)
    print(hash(x))
    print(hash(z))

