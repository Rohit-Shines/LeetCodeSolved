class Solution:
    def runningSum(self, nums=[1,2,3,4]):
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        print(nums)
obj =Solution()
obj.runningSum()