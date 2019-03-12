class Solution(object):

    def judgeSquareSum(k):
        # self.k = k
        for i in range(0, k):
            for j in range(0, k):
                if k == i * i + j * j:
                    return True
                else:
                    pass
        return False

    if __name__ == "__main__":
        n = int(input('Insert the number: '))
    print(judgeSquareSum(n))




