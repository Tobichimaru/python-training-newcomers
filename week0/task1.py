import math

class Solution(object):
    def judgeSquareSum(self, c):
        if c < 0:
            raise ValueError("math domain error")
        i = 0
        max = math.sqrt(c)
        while i <= max:
            if math.sqrt(c - i ** 2) % 1 == 0:
                return(True)
            else:
                i+=1
        return(False)
    
if __name__ == "__main__":
n = int(input())
print(Solution().judgeSquareSum(n))
