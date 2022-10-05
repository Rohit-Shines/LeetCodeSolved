# need simple logic

class Solution:
    def moveZeroes(self, nums=[0,1,0,3,12]):
        l, r, n = 0, 0, len(nums) # n=5
        while r < n: # 0 < 5
            if nums[r] != 0: # 0 !=0 / 1!=0
                nums[l] = nums[r] #
                l += 1 # 1
            r += 1 # 1/2
        while l < n:
            nums[l] = 0
            l += 1
        print(nums)

obj=Solution()
obj.moveZeroes()