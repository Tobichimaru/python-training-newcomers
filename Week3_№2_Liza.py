import time

class Time(object):
    def TimeOfProgramm(func):
        def wrapper(self):
            start = time.time()
            print(time.time() - start)
            return func(self)

        return wrapper


    @TimeOfProgramm
    def Function_1_sq(n):
        k1 = []
        for i in range(n + 1):
            k1.append(i * i)
        return k1

    #
    # @TimeOfProgramm
    # def Function_2_sq(n):
    #     k2 = [i * i for i in range(n + 1)]
    #     return k2


if __name__ == "__main__":
    Time.Function_1_sq(1000)
    # Time.Function_2_sq(1000)