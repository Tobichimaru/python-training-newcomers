class OddNumbersGenerator:
    def __init__(self, n):
        self.n = n
    def gen(self):
        result = 1
        while result <= n:
            yield result
            result += 2

n = int(input())
r = OddNumbersGenerator(n)
for i in r.gen():
    print(i)
    if i < 0:
        break
