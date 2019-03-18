import time
class DTimeAndSum():
    def __init__(self):
        def time_function(func):
            def tm(*args, **kwargs):
                t = time.clock()
                res = func(*args,**kwargs)
                print ("Время выполнения функции: %f" % (time.clock()-t))
                return res
            return tm

        @time_function
        def function(*nums):
            sum = 0
            for i in nums:
                if isinstance(i, int):
                    sum += i
                else:
                    try:
                        i = int(i)
                        sum += i
                    except ValueError:
                        print(str(i) + " не является числом")
                        return
            print("Sum: ", sum)

        function(1, 2, 3, 4, 2, 1, 2, "23")
        function(1, 2, 3, 4, 2, 1, 2, "23", "abd")


if __name__ == "__main__":
    DTimeAndSum()
