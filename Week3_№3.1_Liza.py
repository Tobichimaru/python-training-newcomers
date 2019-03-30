class MySum(object):


    def TestInt(func):

        def nn(*args):
            for arg in args:
                if isinstance(arg, int):
                    pass
                elif isinstance(arg, float):
                    pass
                elif isinstance(arg, str):
                    try:
                         not isinstance(int(arg), int)
                    except:
                        raise ValueError('{} is not int'.format(arg))
                else:
                    raise ValueError('{} is not int'.format(arg))

            return func(*args)
        return nn


    @TestInt
    def Add(*args):
        s = 0
        for arg in args:
            s += int(arg)
        return s

if __name__ == "__main__":
    print('Sum of numbers: ', MySum.Add(4, 4.7, 0, -4))
    print('Sum of numbers: ', MySum.Add(2, '5', 2.4, {6}, '7h'))
