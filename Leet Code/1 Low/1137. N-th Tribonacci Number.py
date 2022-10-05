
class Solution:
    def tribonacci(self, n=4):
        dp = [0, 1, 1] + [0 for _ in range(3, n + 1)] # split the logic

        for x in range(3, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2] + dp[x - 3]
        print(dp[n])
        return



obj =Solution()
obj.tribonacci()
