### Flash#####
# Remember the logic blindly x1 = (x0 + x / x0) / 2

class Solution:
    def mySqrt(self, x=49 ):
        if x < 2: return x # # Base statement to return before tryig to execute
        x0 = x
        x1 = (x0 + x / x0) / 2 # = (4+4/4)/2 = (4+1)/2 = 2.5
        while abs(x0 - x1) >= 1: # 4 -2.5  >=1 // 1.5>1   // # abs(-9) would return 9, while abs(2) would return 2
            x0 = x1 # X0 = 2.5
            x1 = (x0 + x / x0) / 2
        print(int(x1))
        return
obj = Solution()
obj.mySqrt()