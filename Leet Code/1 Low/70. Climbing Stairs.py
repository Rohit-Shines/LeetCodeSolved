###

class Solution:
    def climbStairs(self, n=4) -> int: # n= 4
        if n<= 2: return n # breaking statement
        dp = [0] * (n + 1) # = [0, 0, 0, 0] // creating hash wiht N+1 columns
        dp[1] = 1 # = n[0, 1, 0, 0]
        dp[2] = 2 # = [0, 1, 2, 0]
        for i in range(3, n + 1): # start from 3 bcs of 2 types
            dp[i] = dp[i - 1] + dp[i - 2] # 2 + 1 -> dp[3] = 3 // [0, 1, 2, 3, 0]
            print(dp)
        print("stairs to climb", dp[n])
        return

obj = Solution()
obj.climbStairs()