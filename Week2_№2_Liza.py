class Numbers():
    def __init__(self, n):
        self.n = n

    def OddNumbers(self):
        k = 1
        while k <= self:
            yield k
            k += 2


if __name__ == "__main__":
    n = int(input('Input number: '))
    print('Odd numbers from 1 to {}:'.format(int(n)) )
    for i in Numbers.OddNumbers(n):
        print(i)


