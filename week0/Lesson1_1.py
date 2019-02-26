class Solution(object):
    print('Insert the number:')

    def __judgeSquareSum__(k):
        # self.k = k
        sum1 = 0
        for i in range(1, k + 1):
            if k == sum1:
                return True
            elif k > sum1:
                sum1 += i * i
            elif k < sum1:
                return False
            else:
                pass

    if __name__ == "__main__":
        n = int(input())
    print(__judgeSquareSum__(n))




