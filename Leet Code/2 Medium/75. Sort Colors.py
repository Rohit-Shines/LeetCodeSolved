class Solution:
    def sort1(self, nums=[2,0,2,1,1,0]):
        t=0;
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                t=nums[i]
                nums[i]=nums[i+1]
                nums[i+1] =t
                print(nums)
        print(nums)`

obj = Solution()
obj.sort1()s