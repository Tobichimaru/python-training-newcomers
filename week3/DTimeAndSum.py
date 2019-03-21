import time

def timeit(func):
    def tm(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print ("Время выполнения функции: %f" % (time.clock()-t))
        return res
    return tm

@timeit
def num_arg(*args, **kwargs):
    def sum_arg(func):
        s = 0
        for i in args:
                s += func(i)
        for v in kwargs:
                s += func(kwargs[v])
        print("Sum: ", s)

    @sum_arg
    def test(h):
        try:
            h = int(h)
            return h
        except ValueError:
            raise ValueError("At least one variable type cannot be converted to int")


k = num_arg(1, 2, 3, 4, 2, 1, 2, "23", 2, a = 2)
g = num_arg(1, 2, 3, 4, 2, 1, 2, "23", "abd")

print(k, g)
