import timeit

class TimeCode():
    def __init__(self, stmt):
        self.stmt = stmt

    def __enter__(self):
        self.t = timeit.timeit(self.stmt, number=1)
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        print(self.t)


with TimeCode('"-".join(str(n) for n in range(10))') as t:
    print("timer")

