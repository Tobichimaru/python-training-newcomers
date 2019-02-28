class Solution(object):
    def judgeSquareSum(self, c):
     a = 0
     b = 0
     g = 0
     while a <= c:
        for b in range(1, c):
            if a ** 2 + b ** 2 == c:
                g += 1
                break
            else:
                b = b + 1
        if g == 1:
            break
        a += 1
     return g != 0
if __name__ == "__main__":
    n = int(input())
    print(Solution().judgeSquareSum(n))
