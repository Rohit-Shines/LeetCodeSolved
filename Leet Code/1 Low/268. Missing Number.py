# # n*(n+1)/2 maths formulae


class Solution:
    def missingNumber(self, nums=[3,0,1]):
        expected_sum = len(nums)*(len(nums)+1)//2 # n*(n+1)/2 maths formulae
        actual_sum = sum(nums)
        print("missing number",expected_sum - actual_sum)
        return

obj=Solution()
obj.missingNumber()